# coding=utf8
from re import findall, sub
from ..sql import Sql


class TableCount(object):
    def __init__(self, sql_server):
        self.sql_server = sql_server

    def get_table_list(self, table_name):
        # 根据数据库配置，获取指定名称开头的表集合，组成列表
        query_table_list = "show tables;"
        sqler = Sql(self.sql_server)
        res = sqler.query(query_table_list)
        sqler.close()

        _list = findall('(\'{}.*?\')'.format(table_name),str(res))
        if _list:
            table_list = [sub("'",'',each) for each in _list]
            # logger.info(table_list)
        else:
            table_list = []
        return table_list


    def query_table_count(self, table_list, condition=""):
        # 根据数据库配置，以及表集合，循环查询每个表的数据条数
        table_info = []
        table_count = 0
        if table_list:
            for i in table_list:
                query_count = "SELECT COUNT(ID) FROM {} {};".format(i, condition)

                sqler = Sql(self.sql_server)
                res = int(sqler.query(query_count)[0][0])
                sqler.close()

                table_info.append((i, res))
                table_count += res
        return table_info, table_count