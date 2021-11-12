#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import traceback
from dbpoolpy.dbhelper.postgresql import PostgresqlHelper

from contextlib import contextmanager


def with_postgresql_reconnect(func):
    def close_postgresql_conn(self):
        try:
            self._conn.close()
        except:
            print(traceback.format_exc())
            self._conn = None

    def _(self, *args, **argitems):
        trycount = 3
        while True:
            try:
                x = func(self, *args, **argitems)
            except self._engine.OperationalError as e:
                if e[0] >= 2000 and not self._transaction:  # 客户端错误
                    print(traceback.format_exc())
                    close_postgresql_conn(self)
                    self._connect()
                    trycount -= 1
                    if trycount > 0:
                        continue
                print(traceback.format_exc())
                raise
            except (self._engine.InterfaceError, self._engine.InternalError):
                print(traceback.format_exc())
                if not self._transaction:
                    close_postgresql_conn(self)
                    self._connect()
                    trycount -= 1
                    if trycount > 0:
                        continue
                raise
            else:
                return x
    return _


class DBConnection(object):
    pass

class PostgreSQLConnection(PostgresqlHelper):
    dbtype = "postgresql"

    def __init__(self, name, engine, lasttime, status, role='master', *args, **kwargs):
        self._name = name                       # 连接池名称
        self._engine = engine                   # 数据库连接引擎，满足DB API 2.0规范
        self._args, self._kwargs = args, kwargs # 数据库连接所传参数
        self._conn = None                       # 连接存储位置
        self._status = status                   # 连接状态
        self._lasttime = lasttime               # 连接创建时间
        self._server_id = None                  # PostgreSQL服务唯一id
        self._conn_id = 0                       # PostgreSQL连接唯一id
        self._transaction = False               # 是否正在执行事务
        self._role = role                       # PostgreSQL服务器在PostgreSQL集群中的角色
        self.connect()

    def __str__(self):
        return '<%s %s:%d %s@%s>' % (
            self.dbtype,
            self._kwargs.get('host', ''), 
            self._kwargs.get('port', 0),
            self._kwargs.get('user', ''), 
            self._kwargs.get('database', 0)
        )

    def connect(self):
        self._conn = self._engine.connect(*self._args, **self._kwargs)
        # self._conn.autocommit(1)
        self._transaction = False

        # cur = self._conn.cursor()
        # cur.execute("show variables like 'server_id'")
        # row = cur.fetchone()
        self._server_id = 0
        # cur.close()

        # cur = self._conn.cursor()
        # cur.execute("select connection_id()")
        # row = cur.fetchone()
        self._conn_id = 0
        # cur.close()

        print('server=%s|func=connect|id=%d|name=%s|user=%s|role=%s|addr=%s:%d|db=%s' % (
                 self.dbtype, 
                 self._conn_id % 10000,
                 self._name, 
                 self._kwargs.get('user', ''), 
                 self._role,
                 self._kwargs.get('host', ''), 
                 self._kwargs.get('port', 0),
                 self._kwargs.get('database', '')))

    def cursor(self, *args, **kwargs):
        return self._conn.cursor(*args, **kwargs)

    def close(self):
        self._conn.close()
        self._conn = None
    
    def reconnect(self):
        '''重新连接'''
        try:
            self.close()
        except:
            pass
        self.connect()

    def escape(self, s):
        # 第一种
        # return extensions.adapt(s)
        # 第二种
        with self.connect_cur() as cur:
            res = str(cur.mogrify("%s", (s,)), encoding='utf-8')
            return res

    def is_available(self):
        return self._status == 0

    def useit(self):
        self._status = 1
        self._lasttime = time.time()

    def releaseit(self):
        self._status = 0

    def alive(self):
        return True if self._conn is not None else False

    @contextmanager
    def connect_cur(self):
        cur = None
        try:
            cur = self.cursor()
            yield cur
            if not self._transaction:
                self._conn.commit()
        except Exception as e:
            if not self._transaction:
                self._conn.rollback()
            raise e
        finally:
            if cur is not None:
                cur.close()

    @contextmanager
    def transaction(self):
        if self._transaction:
            raise Exception('this connect is transaction now')
        self._transaction = True
        try:
            yield self
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            raise e
        finally:
            self._transaction = False
