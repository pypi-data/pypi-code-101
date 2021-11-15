#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

class MySQLPool(object):
    """
    create a pool when connect mysql, which will decrease the time spent in 
    request connection, create connection and close connection.
    """
    def __init__(self, host='127.0.0.1', user='root', port='3306',
                 password='', database='test', pool_name='mailhunt_pool',
                 pool_size=3):
        
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.pool_size = pool_size
        self.connection_string = f"mysql://{user}:{password}@{host}:{port}/{database}"

        self.pool = self.create_pool()

    def create_pool(self):
        """
        Create a connection pool, after created, the request of connecting 
        MySQL could get a connection from this pool instead of request to 
        create a connection.
        :return: connection pool
        """
        pool = create_engine(self.connection_string, pool_size=self.pool_size, max_overflow=0, poolclass=QueuePool, pool_pre_ping=True, pool_timeout=60)

        return pool

    def execute(self, sql, args=None, commit=False):
        """
        Execute a sql, it could be with args and with out args. The usage is 
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        connection = self.pool.raw_connection()
        try:
            result = None

            cursor = connection.cursor()
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)

            if commit is True:
                connection.commit()
            else:
                result = cursor.fetchall()
            return result
        finally:
            cursor.close()
            connection.close()

    def executemany(self, sql, args, commit=False):
        """
        Execute with many args. Similar with executemany() function in pymysql.
        args should be a sequence.
        :param sql: sql clause
        :param args: args
        :param commit: commit or not.
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        connection = self.pool.raw_connection()
        try:
            result = None

            cursor = connection.cursor()
            cursor.executemany(sql, args)
            if commit is True:
                connection.commit()
            else:
                result = cursor.fetchall()
            return result
        finally:
            cursor.close()
            connection.close()