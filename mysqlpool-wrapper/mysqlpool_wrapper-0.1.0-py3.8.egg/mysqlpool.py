#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
from sqlalchemy.pool import QueuePool

class MySQLPool(object):
    """
    create a pool when connect mysql, which will decrease the time spent in 
    request connection, create connection and close connection.
    """
    def __init__(self, host='127.0.0.1', user='root', port='3306',
                 password='', database='test', pool_name='mailhunt_pool',
                 pool_size=3):
        
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        self._pool_size = pool_size
        self.dbconfig = {
            'host': self._host,
            'user': self._user,
            'port': self._port,
            'password': self._password,
            'database': self._database,
            'pool_size': pool_size
        }

        self.pool = self.create_pool()

    def create_pool(self):
        """
        Create a connection pool, after created, the request of connecting 
        MySQL could get a connection from this pool instead of request to 
        create a connection.
        :return: connection pool
        """
        pool = QueuePool(
            lambda: mysql.connector.connect(host=self._host, user=self._user, password=self._password, database=self._database),
            pool_size=self._pool_size 
        )

        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn: 
        :param cursor: 
        :return: 
        """
        cursor.close()
        conn.close()

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
        conn = self.pool.connect()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

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
        conn = self.pool.connect()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res    