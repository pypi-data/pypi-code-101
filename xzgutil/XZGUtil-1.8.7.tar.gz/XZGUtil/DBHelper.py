#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-10-18 17:25
# @Site    :
# @File    : DBHelper.py
# @Software: PyCharm


def create_in_sql(table_name: str, data: dict, conversion=False, update=False):
    """
    传入字典和表名，返回组装好的sql
    sql中的插入字段为传入字典的key
    conversion:是否全部转换成字符串类型
    update:是否启动更新语句
    data = {'w':'d1','ew':'d2','wr':'d3','wa':'d4'}
    """
    sql = 'insert into ' + table_name + ' ('
    data_keys = [key for key in data.keys()]
    for key in data_keys:
        sql += key
        if data_keys.index(key) != len(data_keys) - 1:
            sql += ','
        else:
            sql += ')  values ('
            for key in data_keys:
                value = data.get(key)
                if isinstance(value, str) or conversion:
                    sql += f'"{value}",'
                elif value == None:
                    sql += f'null,'
                else:
                    sql += f'{value},'
            sql = sql.rstrip(',')
    if update:
        sql += ")  ON DUPLICATE KEY UPDATE "
        for key in data_keys:
            sql += key + '=' + f'values({key}),'
        sql = sql.rstrip(',')
        sql += ";"
    else:
        sql += ");"
    return sql
