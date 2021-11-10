import pandas as pd
import pymssql
from pandas import read_sql_query

# to config
columns2targets = {
    'FPT': ['FPT'],
    'FVS': ['FVS'],
    'FOYD': ['FOYD'],
    'FOS': ['FOS'],
    'FPTP': ['FPTP'],
    'FVSP': ['FVSP'],
    'FOYDP': ['FOYDP'],
    'FYDR': ['FYDR'],
    'FUV_1': ['FUV'],
    'FUV_2': ['FUV'],
    'FUV_3': ['FUV'],
    'FDV_1': ['FDV'],
    'FDV_2': ['FDV'],
    'FDV_3': ['FDV'],
    'DWTT1': ['DWTT'],
    'DWTT2': ['DWTT'],
    'DVC1': ['DVC'],
    'DVC2': ['DVC'],
    'DVC3': ['DVC'],
    'NB1': ['NB_'],
    'NB2': ['NB_'],
    'FPT05': ['FPT05'],
    'FPTP05': ['FPTP05']
}

metrics2ids = {
    'R2': 1,
    'MAE': 2,
    'MAE train': 3,
    'MAE test': 4,
    'P95': 5,
    'Samples': 6
}

targets2db = {
    'FPT': 'FPT',
    'FVS': 'FVS',
    'FOYD': 'FOYD',
    'FOS': 'FOS',
    'FPTP': 'FPTP',
    'FVSP': 'FVSP',
    'FOYDP': 'FOYDP',
    'FYDR': 'FYDR',
    'FUV': 'FUV_1',
    'FDV': 'FDV_1',
    'DWTT': 'DWTT1',
    'DVC': 'DVC1',
    'NB_': 'NB1',
    'FPT05': 'FPT05',
    'FPTP05': 'FPTP05'
}


class DB_Connector:
    def __init__(self,
                 server: str = '',
                 user: str = '',
                 password: str = '',
                 db: str = ''):
        self.conn = pymssql.connect(server, user, password, db)
        self.cursor = self.conn.cursor(as_dict=True)

    def get_columns_id(self, columns_names: list[str]) -> pd.DataFrame:
        query = '''select column_id, name from Columns where '''
        for name in columns_names:
            if name in targets2db:
                query += f'(Columns.name = \'{targets2db[name]}\') or '
            else:
                query += f'(Columns.name = \'{name}\') or '
        # erase extra ' or '
        query = query[:-4]

        df = read_sql_query(query, self.conn)

        return df

    def update_status(self, model_id: int):
        query = '''update Models set status = 1
                   where model_id = %s'''
        self.cursor.execute(query, (model_id))
        self.conn.commit()

    def insert_features(self, model_id: int,
                        features: list[str]):
        df = self.get_columns_id(features)

        for column_id in df['column_id']:
            query = '''insert into ColumnsToModels(model_id, column_id)
                       values (%s, %s)'''
            self.cursor.execute(query, (model_id, column_id))
        self.conn.commit()

    def insert_metrics(self, model_id,
                       metrics: dict[str, dict[str, str]]):
        targets = list(metrics.keys())
        df = self.get_columns_id(targets)

        for index, row in df.iterrows():
            column_name, column_id = row['name'], row['column_id']
            for metric_name, metric_value in metrics[columns2targets[column_name][0]].items():

                query = '''insert into
                           MetricToModels(model_id, target_id,
                           metric_id, value)
                           values (%s, %s, %s, %s)'''
                self.cursor.execute(query, (model_id, column_id,
                                            metrics2ids[metric_name],
                                            metric_value))
        self.conn.commit()

    def get_columns(self, model_id: int) -> tuple[list, list]:
        def flatten(array: list[list[str]]) -> list[str]:
            return [item for sublist in array for item in sublist]

        model_id = (model_id, )

        query = """select name, type
                        from ColumnsToModels as T1
                        inner join Columns as T2
                        on T1.column_id = T2.column_id
                        where T1.model_id=%s"""
        self.cursor.execute(query, (model_id))

        rows = self.cursor.fetchall()

        target_columns = [i['name'] for i in rows if i['type'] is True]
        feature_columns = [i['name'] for i in rows if i['type'] is False]

        if not target_columns:
            raise Exception('''No targets have been selected,
                            fitting is impossible.\n''')
        # ex: ['FPT', 'FUV_1'] -> ['FPT', 'FUV']
        else:
            target_columns = [columns2targets[i] for i in target_columns]
            target_columns = flatten(target_columns)

        return target_columns, feature_columns

    def _create_where(self, filters, flag=True) -> str:
        def create_or(column_name: str, values: list[str], flag: bool = True):
            # for categorical filters
            if flag:
                return '(' + ' or '.join(f"{column_name}=\'%s\'" % str(x) if x else f"{column_name} is Null" for x in values ) + ')'
            else:
                return '(' + ' or '.join(f"{column_name} between %s and %s" % (str(x[0]), str(x[1])) for x in values) + ')'

        def create_and(values: str):
            return '(' + ' and '.join('%s' % str(x) for x in values) + ')'

        where_sql = create_and([create_or(i, filters[i], flag) for i in filters])

        return where_sql

    def _create_where_for_num_filters(self, model_id: int) -> str:

        query = """select "begin", "end", name from Filters_num as a1
                   inner join Columns as a2
                   on a1.column_id=a2.column_id
                   where model_id = %s """

        self.cursor.execute(query, (model_id))
        data = self.cursor.fetchall()
        df = pd.DataFrame(data)

        # works fine?
        if df.empty:
            return ''

        filters = df.groupby('name')[['begin', 'end']].apply(
            lambda x: x.values.tolist()
        ).to_dict()

        return self._create_where(filters, flag=False)

    def _create_where_for_cat_filters(self, model_id: int) -> str:

        query = """select name, value from Filters_cat as a1
                   inner join Columns as a2
                   on a1.column_id=a2.column_id
                   where model_id = %s """

        self.cursor.execute(query, (model_id))
        data = self.cursor.fetchall()
        df = pd.DataFrame(data)

        # works fine?
        if df.empty:
            return ''

        filters = df.groupby('name')['value'].apply(
            lambda x: x.values.tolist()
        ).to_dict()

        return self._create_where(filters)

    def _create_where_query(self, model_id: int) -> str:
        where_for_num_query = self._create_where_for_num_filters(model_id)
        where_for_cat_query = self._create_where_for_cat_filters(model_id)

        query = 'select * from Data_Model'
        if where_for_cat_query != '' and where_for_num_query == '':
            query = query + ' where ' + where_for_cat_query
        elif where_for_num_query != '' and where_for_cat_query == '':
            query = query + ' where ' + where_for_num_query
        elif where_for_num_query != '' and where_for_cat_query != '':
            query = (query + ' where ' + where_for_num_query
                           + ' and ' + where_for_cat_query)

        return query

    def get_filtered_data(self, model_id: int) -> pd.DataFrame:

        query = self._create_where_query(model_id)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        df = pd.DataFrame(data)

        return df

    def get_reliability(self, model_id: int, data_id: int) -> bool:
        query = self._create_where_query(model_id)
        query += ' and ID=%s'

        self.cursor.execute(query, (data_id))
        data = self.cursor.fetchall()
        df = pd.DataFrame(data)

        return bool(df.shape[0])
