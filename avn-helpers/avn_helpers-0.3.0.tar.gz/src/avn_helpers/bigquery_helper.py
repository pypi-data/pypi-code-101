from google.cloud import bigquery, bigquery_datatransfer
from google.oauth2 import service_account
import datetime
import json


def get_bq_schema_from_record_config(record_config):
    fields = record_config.get("fields", [])
    sub_xml = record_config.get("sub_xml", None)
    schema = []
    for field in fields:
        field_config = fields[field]
        type = field_config.get("type", "string").upper()
        mode = field_config.get("mode", "nullable").upper()
        new_schema = {
            "name": field,
            "type": type,
            "mode": mode
        }
        if "description" in field_config:
            new_schema["description"] = field_config["description"]
        if type == "RECORD":
            new_schema["fields"] = get_bq_schema_from_record_config(field_config)
        schema.append(new_schema)
    if sub_xml:
        schema += get_bq_schema_from_record_config(sub_xml)
    return schema


class BigqueryHandler:

    def __init__(
            self,
            logger,
            project_id: str,
            service_account_file_path: str = '/defaultserviceaccount.json',
            bigquery_datetime_format: str = '%Y-%m-%d %H:%M:%S UTC',
            bigquery_date_format: str = '%Y-%m-%d',
    ):
        self.project_id = project_id
        self.bigquery_datetime_format = bigquery_datetime_format
        self.bigquery_date_format = bigquery_date_format

        cred = service_account.Credentials.from_service_account_file(service_account_file_path)
        self.client = bigquery.Client(project=self.project_id, credentials=cred)
        self.transfer_client = bigquery_datatransfer.DataTransferServiceClient(credentials=cred)
        self.logger = logger


    def create_table_from_gcs_as_CSV(self, dataset_id, table_id, source_uri, overwrite=False, append=False,
                                     field_delimiter=None, schema=None, skip_leading_rows=None, errors_allowed=None,
                                     quote_character=None):
        full_table_id = self.project_id + "." + dataset_id + "." + table_id
        job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV)
        # write disposition
        if overwrite:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        elif append:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        # field delimiter
        if field_delimiter:
            job_config.field_delimiter = field_delimiter
        # errors allowed
        if errors_allowed:
            job_config.max_bad_records = errors_allowed
        # quote character (usually, to avoid double quoted errors)
        if quote_character:
            job_config.quote_character = quote_character
        # schema spec
        if schema:
            if isinstance(schema, str):
                with open(schema,) as f:
                    schema = json.load(f)
            job_config.schema = schema
        else:
            job_config.autodetect = True
        # skip header
        if skip_leading_rows:
            job_config.skip_leading_rows = skip_leading_rows
        load_job = self.client.load_table_from_uri(source_uri, full_table_id, job_config=job_config)
        try:
            load_job.result()
        except Exception as ex:
            print(ex)
            raise ex
        final_table = self.client.get_table(full_table_id)
        self.logger.info("Uploaded {} rows to table {}".format(str(final_table.num_rows), full_table_id))

    def get_list_from_query(self, querystr, params=None, job_config=None):
        if params is None:
            params = {}
        if any(params):
            for param in params:
                if type(params[param]) == datetime.datetime:
                    params[param] = params[param].strftime(self.bigquery_datetime_format)
                elif type(params[param]) == datetime.date:
                    params[param] = params[param].strftime(self.bigquery_date_format)
                else:
                    params[param] = str(params[param])
            query = querystr.format(**params)
        else:
            query = querystr
        if job_config:
            query_job = self.client.query(query, job_config=job_config)
        else:
            query_job = self.client.query(query)
        return list(query_job.result())

    def get_table_rows(self, table_name):
        return self.get_list_from_query(querystr=f'select * from {table_name}')

    def get_column_names(self, dataset_name, table_name):
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        table = self.client.get_table(table_ref)
        cols = [f.name for f in table.schema]
        return cols

    def write_from_query(self, querystr, dataset_id, table_id, overwrite=True, append=False):
        full_table_id = self.project_id + "." + dataset_id + "." + table_id
        job_config = bigquery.QueryJobConfig(destination=full_table_id)

        """ 
            note that you can use schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION] 
            in QueryJobConfig
        """

        # write disposition
        if overwrite:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        elif append:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        query_job = self.client.query(querystr, job_config=job_config)
        res = query_job.result()
        self.logger.info(f"wrote on table {full_table_id}")

    def get_table(self, dataset_name, table_name):
        table_ref = bigquery.dataset.DatasetReference(self.project_id,dataset_name).table(table_name)
        try:
            table = self.client.get_table(table_ref)
        except:
            table = None
        return table

    def create_table(self, dataset_name, table_name, schema, day_partition_field=None):
        table_ref = bigquery.dataset.DatasetReference(self.project_id, dataset_name).table(table_name)
        table = bigquery.Table(table_ref, schema=schema)
        if day_partition_field is not None:
            table.time_partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY,
                field=day_partition_field
            )
        table = self.client.create_table(table)
        return table

    def get_or_create_table(self, dataset_name, table_name, schema, day_partition_field=None):
        table = self.get_table(dataset_name, table_name)
        if table is None:
            table = self.create_table(dataset_name, table_name, schema, day_partition_field)
        return table

    def execute_query(self, querystr):
        query_job = self.client.query(querystr)
        res = query_job.result()

    def export_table_to_gcs(self, dataset_name, table_name, destination_uri, location, schema=None):
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = dataset_ref.table(table_name)

        extract_job = self.client.extract_table(
            table_ref,
            destination_uri,
            location=location,
        )
        if schema:
            if isinstance(schema, str):
                with open(schema, ) as f:
                    schema = json.load(f)
            extract_job.schema = schema

        extract_job.result()
        self.logger.info(f"exported table {self.project_id}:{dataset_name}.{table_name} to {destination_uri}")

    def update_views_query(self, view_dataset, view_name, query):
        view_id = self.project_id + "." + view_dataset + "."+ view_name
        view = bigquery.Table(view_id)
        view.view_query = query
        view = self.client.update_table(view, ["view_query"])
        self.logger.info(f"updated {view.table_type}: {str(view.reference)}")

    def schedule_query(
            self, query, dataset_name, display_name, table_name_template, schedule , write_disposition="WRITE_APPEND",
            partitioning_field=""
    ):
        parent = self.transfer_client.common_project_path(self.project_id)
        transfer_config = bigquery_datatransfer.TransferConfig(
            destination_dataset_id=dataset_name,
            display_name=display_name,
            data_source_id="scheduled_query",
            params={
                "query":query,
                "destination_table_name_template":table_name_template,
                "write_disposition": write_disposition,
                "partitioning_field": partitioning_field
            },
            schedule=schedule
        )
        transfer_config = self.transfer_client.create_transfer_config(
            bigquery_datatransfer.CreateTransferConfigRequest(
                transfer_config=transfer_config, parent=parent,
            )
        )
        self.logger.info(f"Created scheduled query {transfer_config.name}")

    def insert_rows(self, row_list, dataset_name, table_name, schema=None, day_partition_field=None):
        if schema:
            table = self.get_or_create_table(dataset_name, table_name, schema, day_partition_field)
        else:
            table = self.get_table(dataset_name, table_name)
        self.insert_rows_from_table(row_list, table)

    def insert_rows_from_table(self, row_list, table, batch_size=50):
        i = 0
        all_errors = []
        while i < len(row_list):
            rows = row_list[i:i + batch_size]
            i += batch_size
            all_errors.append(self.client.insert_rows(table, rows))
            if any(all_errors):
                self.logger.info(
                    "errors while writing row {} into bigquery with errors {}".format(str(rows[0]), str(all_errors)))

    def create_view(self, view):
        view_creation_query = f"""
        CREATE OR REPLACE VIEW {view['project']}.{view['dataset_name']}.{view['display_name']}_source
        AS
        {view['view_query']} 
        """
        self.execute_query(view_creation_query)

    def schedule_view_query(self, view):
        view = view.copy()
        view['table_name_template'] = view['display_name']
        if view['write_disposition'] == 'WRITE_EMPTY':
            view['table_name_template'] += '_{run_date}'
        view['query'] = f"SELECT * FROM {view['project']}.{view['dataset_name']}.{view['display_name']}_source"
        # non necessary arguments
        view.pop('view_query', None)
        self.schedule_query(
            **view
        )

    def create_functions(self, function):
        function_creation_query = f"""
                CREATE OR REPLACE FUNCTION `{function['project']}.{function['dataset_name']}.{function['display_name']}`({function['args']})
                AS(
                {function['function_query'].strip()}
                ) 
                """
        self.execute_query(function_creation_query)

    def delete_table(self, dataset_id, table_id, yes_i_am_sure=False):
        assert yes_i_am_sure, "you have to be sure before you delete a BQ table."
        full_table_id = self.project_id + "." + dataset_id + "." + table_id
        self.client.delete_table(full_table_id, not_found_ok=True)
        self.logger.info(f"deleted table {full_table_id}")
