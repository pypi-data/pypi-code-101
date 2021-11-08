#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test.py
@time:   2019-12-29 11:00:29
@description:
"""

from pyrainsty import connect


def main():
    config = dict(
        host='121.36.85.248',
        port=9024,
        user='root',
        password='123456',
        database='storm_monitor',
        charset='utf8'
    )

    mc = connect.MysqlConnect(config)
    mc.create_connect()
    mc.close_connect()
    mc.check_connect()
    result = mc.get_data('select * from check_time limit %(limit)s', dict(limit=10))
    print(result)

    cursor = mc.get_cursor
    cursor.execute('select * from check_time limit 1')
    data = cursor.fetchall()
    for d in data:
        print(d)

    result = mc.exec_cmd('select * from check_time limit 1')
    print(result)


if __name__ == '__main__':
    main()
