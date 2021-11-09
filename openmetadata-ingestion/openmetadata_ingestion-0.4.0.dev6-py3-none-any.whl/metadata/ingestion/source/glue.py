import json
import os
import uuid
import logging
from typing import Iterable, Optional

import boto3

from ...generated.schema.entity.data.table import Table
from ...generated.schema.entity.services.databaseService import DatabaseServiceType
from ...utils.column_helpers import _handle_complex_data_types, check_column_complex_type, get_column_type
from .sql_source import SQLConnectionConfig, SQLSourceStatus
from ..api.common import IncludeFilterPattern, Record, ConfigModel
from ..api.source import Source, SourceStatus
from ..models.ometa_table_db import OMetaDatabaseAndTable
from ..ometa.ometa_api import OpenMetadata
from ..ometa.openmetadata_rest import MetadataServerConfig
from ...generated.schema.entity.data.database import Database
from ...generated.schema.entity.data.pipeline import Pipeline, Task
from ...generated.schema.type.entityReference import EntityReference
from ...utils.helpers import get_database_service_or_create

logger: logging.Logger = logging.getLogger(__name__)

class GlueSourceConfig(ConfigModel):
    service_type = "MySQL"
    aws_access_key_id: str
    aws_secret_access_key: str
    endpoint_url: str
    region_name: str
    database: str
    service_name: str
    host_port: str = ''
    filter_pattern: IncludeFilterPattern = IncludeFilterPattern.allow_all()



    def get_service_type(self) -> DatabaseServiceType:
        return DatabaseServiceType[self.service_type]

class GlueSource(Source):
    def __init__(
            self, config: GlueSourceConfig, metadata_config: MetadataServerConfig, ctx
    ):
        super().__init__(ctx)
        self.status = SQLSourceStatus()
        self.config = config
        self.metadata_config = metadata_config
        self.metadata = OpenMetadata(metadata_config)
        self.service = get_database_service_or_create(config, metadata_config)
        os.environ["AWS_ACCESS_KEY_ID"] = self.config.aws_access_key_id
        os.environ["AWS_SECRET_ACCESS_KEY"] = self.config.aws_secret_access_key
        self.glue = boto3.client(service_name='glue', region_name=self.config.region_name,
                                 endpoint_url=self.config.endpoint_url)

    @classmethod
    def create(cls, config_dict, metadata_config_dict, ctx):
        config = GlueSourceConfig.parse_obj(config_dict)
        metadata_config = MetadataServerConfig.parse_obj(metadata_config_dict)
        return cls(config, metadata_config, ctx)

    def prepare(self):
        pass

    def next_record(self) -> Iterable[Record]:
        yield from self.ingest_tables()
        yield from self.ingest_pipelines()

    def get_columns(self, columnData):
        for column in columnData['Columns']:
            if column['Type'].startswith('union <'):
                column['Type'] = column['Type'].replace(' ','')
            col_type, data_type_display, arr_data_type, col_obj = check_column_complex_type(self.status, self.dataset_name, column['Type'].lower(), column['Name'])
            print(column['Type'])
            print(col_type, data_type_display, arr_data_type, col_obj)


            

    def ingest_tables(self) -> Iterable[OMetaDatabaseAndTable]:
        try:
            for tables in self.glue.get_tables(DatabaseName=self.config.database)['TableList']:
                if not self.config.filter_pattern.included(tables['Name']):
                    self.status.filter(
                        "{}.{}".format(self.config.get_service_name(), tables['Name']),
                        "Table pattern not allowed",
                    )
                    continue
                database_entity = Database(
                    name=tables['DatabaseName'],
                    service=EntityReference(id=self.service.id, type=self.config.service_type),
                )
                logger.info(json.dumps(tables,indent=4,default=str))
                fqn = f"{self.config.service_name}.{self.config.database}.{tables['Name']}"
                self.dataset_name = fqn
                table_columns = self.get_columns(tables['StorageDescriptor'])
                table_entity = Table(
                    id=uuid.uuid4(),
                    name=tables['Name'],
                    description=tables['Description'],
                    fullyQualifiedName=fqn,
                    columns=table_columns,
                )
                table_and_db = OMetaDatabaseAndTable(
                    table=table_entity, database=database_entity
                )
                yield table_and_db
        except Exception as err:
            logger.error(err)
    def get_downstream_tasks(self, task_unique_id, tasks):
        downstreamTasks = []
        for edges in tasks:
            if edges['SourceId'] == task_unique_id:
                downstreamTasks.append(edges['DestinationId'])



    def get_tasks(self, tasks):
        for task in tasks['Graph']['Nodes']:
            downstreamTasks = self.get_downstream_tasks(task['UniqueId'], tasks['Graph']['Edges'])
            Task(
                Name=task['Name'],
                taskType=task['Type'],
                downstreamTasks=downstreamTasks
            )
        pass

    def ingest_pipelines(self) -> Iterable[OMetaDatabaseAndTable]:
        try:
            for workflow in self.glue.list_workflows()['Workflows']:
                for job in self.glue.get_workflow(Name=workflow)['Workflow']:
                    tasks = self.get_tasks(job)
                    pipeline_ev = Pipeline(
                        id=uuid.uuid4(),
                        name=job["Name"],
                        description='',
                        tasks=tasks,
                        service=EntityReference(
                            id=self.pipeline_service.id, type="pipelineService"
                        ),
                    )
                    yield pipeline_ev
        except Exception as err:
            logger.error(err)

    def close(self):
        pass

    def get_status(self) -> SourceStatus:
        return self.status
