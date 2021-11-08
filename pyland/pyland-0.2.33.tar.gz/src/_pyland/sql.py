#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from .log import logger
from .config import Config
from .utils.error import Sqlerror


class Sql(object):
    def __init__(self, sql_server="discover_services_id_test", db=None, charset="utf8"):
        if isinstance(sql_server, str):
            sql_server = Config().get(sql_server)

        self.sql_server = sql_server.get('sql_server')
        self.sql_port = sql_server.get('sql_port')
        self.sql_user = sql_server.get('sql_user')
        self.sql_password = sql_server.get('sql_password')
        self.db_name = sql_server.get('db_name') if not db else db
        self.charset = charset
        # self.connect()
        #
        # # 使用cursor()方法获取操作游标
        # self.cursor = self.db.cursor()
        # self.cursor.execute("SET NAMES utf8mb4")

    def connect(self, db_name=None):
        if db_name is None:
            db_name = self.db_name
        logger.debug('连接到mysql服务器{}'.format(self.sql_server))
        self.db = mysql.connector.connect(host=self.sql_server, port=self.sql_port,
                                          user=self.sql_user, passwd=self.sql_password,
                                          database=db_name, use_unicode=True, buffered=True, charset=self.charset)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        self.cursor.execute("SET NAMES utf8mb4")
        return self.db

    def exec(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.db.commit()
            logger.info('sql执行成功')
            self.close()
        except:
            err = 'sql执行失败，回滚数据库'
            logger.error(err)
            self.db.rollback()
            raise Sqlerror(err)

    def query(self, sql):
        try:
            self.connect()
            logger.debug(sql)
            self.cursor.execute(sql)

            results = []
            row = self.cursor.fetchone()
            while row is not None:
                # logger.debug(row)
                results.append(row)
                row = self.cursor.fetchone()

            # results = self.cursor.fetchall()
            logger.debug('查询结果为：{}'.format(results))
            self.close()
            return results
        except:
            err = "Error: unable to fecth data"
            logger.error(err)
            raise Sqlerror(err)

    def load_sql(self, abs_sql_file):
        """
        Load sql file to mysql server.
        Sql file must only contains sql cmd (not support comment), every cmd should end with ';' and a line break.
        注意：这里埋了一个坑，sql文件如果结尾处没有空行，执行不成功且不会报错
        """
        self.connect()
        logger.debug("load {} ".format(abs_sql_file))
        with open(abs_sql_file, 'r', encoding='utf-8') as file_sql:
            file_sql_video = file_sql.read().split(';\n')[:-1]
            # logger.debug(sql_video)
            sql_list = [x.replace('\n', '') if '\n' in x else x for x in file_sql_video]
            # logger.debug(sql_list)

        for sql_item in sql_list:
            self.exec(sql_item)

        self.close()

    def batch_single_query(self, query_state, batch_size=1):
        try:
            self.connect()
            self.cursor.execute(query_state)
            i = 0
            query_batch_list = []

            while True:
                row = self.cursor.fetchmany(batch_size)
                if not row:
                    break
                single_list = []
                for single_element in row:
                    single_list.append(single_element[0])
                query_batch_list.append(single_list)
            self.close()
            return query_batch_list
        except:
            err = "Error: unable to fecth data"
            logger.error(err)
            raise Sqlerror(err)

    def pre_data(self, data, strip=True):
        """
        strip data
        replace [' " \\] to [\' \" \\\\]
        """
        if strip:
            data = data.strip()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()


if __name__ == '__main__':
    query_camera_count = ""
    mysql = Sql()
    count = mysql.query(query_camera_count)[0][0]
    logger.info(count)
    mysql.close()
