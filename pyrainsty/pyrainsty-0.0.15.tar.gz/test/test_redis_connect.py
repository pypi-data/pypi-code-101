#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test.py
@time:   2019-12-29 11:00:29
@description:
"""

from pyrainsty import redis_connect


def main():
    config = dict(
        host='114.116.246.174',
        port='6379',
        password='foobared',
        db='0'
    )

    rc = redis_connect.RedisConnect(config, decode_responses=True)
    rc.create_connect()
    result = rc.connect.get('aaa')
    print(result)


if __name__ == '__main__':
    main()
