from dataclasses import fields
from urllib.parse import urlparse
from abc import ABC, abstractmethod, abstractproperty
import logging

from airflow.models.dag import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor

from gcp_airflow_foundations.base_class.salesforce_ingestion_config import SalesforceIngestionConfig

from gcp_airflow_foundations.operators.api.operators.sf_to_gcs_query_operator import SalesforceToGcsQueryOperator
from gcp_airflow_foundations.operators.api.sensors.gcs_sensor import GCSObjectListExistenceSensor
from gcp_airflow_foundations.source_class.ftp_source import FTPtoBQDagBuilder
from gcp_airflow_foundations.base_class.data_source_table_config import DataSourceTablesConfig
from gcp_airflow_foundations.source_class.source import DagBuilder
from gcp_airflow_foundations.common.gcp.load_builder import load_builder


class GCSFiletoBQDagBuilder(FTPtoBQDagBuilder):
    """
    Builds DAGs to load files from GCS to a BigQuery Table.
    """

    def set_schema_method_type(self):
        self.schema_source_type = self.config.source.schema_options.schema_source_type     

    def get_bq_ingestion_task(self, table_config):

        taskgroup = TaskGroup(group_id="ftp_taskgroup")

        metadata_file_sensor = self.metadata_file_sensor(table_config)
        metadata_file_sensor.task_group

        sensor_task = self.get_file_sensor(table_config)
        sensor_task.task_group = taskgroup

        file_ingestion_task = self.file_ingestion_task(table_config)
        file_ingestion_task.task_group = taskgroup

        load_to_landing_task = self.load_to_landing_task(table_config)
        load_to_landing_task.task_group = taskgroup

        sensor_task >> file_ingestion_task >> load_to_landing_task

        return taskgroup

    def metadata_file_tasks(self, table_config):
        metadata_file = table_config.extra_options.get("gcs_table_config")["metadata_file"]
        bucket = self.config.source.extra_options["ftp_gcs_config"]["gcs_bucket"]

        file_sensor = GCSObjectExistenceSensor(
            task_id="wait_for_metadata_file",
            bucket=bucket,
            object=metadata_file
        )

    def file_ingestion_task(self, table_config):
        """
        No ingestion is needed - data is already in GCS, so return a dummy operator.
        """
        return DummyOperator(
            task_id="dummy_operator"
        )

    def file_sensor(self, table_config, files_to_wait_for):
        """
        Returns an Airflow sensor that waits for the list of files specified by either
        (1) the metadata file provided, or
        (2) the files provided in the config
        """
        bucket = self.config.source.extra_options["ftp_gcs_config"]["gcs_bucket"]

        return GCSObjectListExistenceSensor(
            task_id="wait_for_files",
            bucket=bucket,
            objects=files_to_wait_for
        )

    def load_to_landing_task(self, table_config, files_to_load):
        data_source = self.config.source

        # Parameters
        bucket = self.config.source.extra_options["gcs_bucket"]
        source_format = table_config.extra_options.get("gcs_config")["source_format"]
        gcp_project = data_source.gcp_project
        landing_dataset = data_source.landing_zone_options.landing_zone_dataset 
        destination_table = f"{gcp_project}:{landing_dataset}.{table_config.landing_zone_table_name_override}"

        return GCSToBigQueryOperator(
            task_id='import_csv_to_bq_landing',
            bucket=bucket,
            source_objects=files_to_load,
            source_format=source_format,
            destination_project_dataset_table=destination_table,
            write_disposition='WRITE_TRUNCATE',
            create_disposition='CREATE_IF_NEEDED',
            skip_leading_rows=1,
        )

    def validate_extra_options(self):
        tables = self.config.tables