import abc
import datetime
from dbpoolpy.utils import DBFunc
from dbpoolpy.utils import timesql
from dbpoolpy import pager
from contextlib import contextmanager
from . import SelectHelper, UpdateHelper, InsertHelper, DeleteHelper
from dbpoolpy.config import settings
from dbpoolpy.constants import DBTYPE

class PostgresqlHelper:
    def __init__(self):
        self._conn = None

    def format_timestamp(self, ret, cur):
        '''将字段以_time结尾的格式化成datetime'''
        if not ret:
            return ret
        index = []
        for d in cur.description:
            if d[0].endswith('_time'):
                index.append(cur.description.index(d))

        res = []
        for i, t in enumerate(ret):
            if i in index and isinstance(t, int):
                res.append(datetime.datetime.fromtimestamp(t))
            else:
                res.append(t)
        return res

    #执行命令
    @timesql
    def execute(self, sql, args=None):
        '''执行单个sql命令'''
        with self.connect_cur() as cur:
            if args:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                ret = cur.execute(sql, args)
            else:
                ret = cur.execute(sql)
            return ret

    # 执行插入命令
    @timesql
    def execute_insert(self, sql, args=None, isdict=True):
        '''执行单个sql命令'''
        with self.connect_cur() as cur:
            if settings.DB_TYPE == DBTYPE.POSTGRESQL:
                lower_sql = str(sql).lower()
                if lower_sql.find('returning') == -1:
                    sql = '%s returning *' % sql
            if args:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                ret = cur.execute(sql, args)
            else:
                ret = cur.execute(sql)
            if settings.DB_TYPE == DBTYPE.POSTGRESQL:
                res = cur.fetchone()
                res = self.format_timestamp(res, cur)
                if res and isdict:
                    xkeys = [i[0] for i in cur.description]
                    return dict(zip(xkeys, res))
                else:
                    return res
            else:
                if cur.lastrowid:
                    return cur.lastrowid
                return ret

    @timesql
    def executemany(self, sql, args=None):
        '''调用executemany执行多条命令'''
        with self.connect_cur() as cur:
            if args:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                ret = cur.executemany(sql, args)
            else:
                ret = cur.executemany(sql)
            return ret

    @timesql
    def query(self, sql, args=None, isdict=True, hashead=False):
        '''sql查询，返回查询结果
        sql: 要执行的sql语句
        args: 要传入的参数
        isdict: 返回值格式是否为dict, 默认True
        hashead: 如果isdict为Fasle, 返回的列表中是否包含列标题
        '''
        with self.connect_cur() as cur:
            if not args:
                cur.execute(sql)
            else:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                cur.execute(sql, args)
            res = cur.fetchall()
            res = [self.format_timestamp(r, cur) for r in res]
            if res and isdict:
                ret = []
                xkeys = [i[0] for i in cur.description]
                for item in res:
                    ret.append(dict(zip(xkeys, item)))
            else:
                ret = res
                if hashead:
                    xkeys = [i[0] for i in cur.description]
                    ret.insert(0, xkeys)
            return ret

    @timesql
    def get(self, sql, args=None, isdict=True):
        '''sql查询，只返回一条
        sql: sql语句
        args: 传参
        isdict: 返回值是否是dict
        '''
        with self.connect_cur() as cur:
            if args:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                cur.execute(sql, args)
            else:
                cur.execute(sql)
            res = cur.fetchone()
            res = self.format_timestamp(res, cur)
            if res and isdict:
                xkeys = [i[0] for i in cur.description]
                return dict(zip(xkeys, res))
            else:
                return res

    def mogrify(self, sql, args=None):
        '''返回填充args后的sql语句
        sql: sql语句
        args: 传参
        '''
        with self.connect_cur() as cur:
            if args:
                if not isinstance(args, (dict, tuple, list)):
                    args = tuple([args])
                sql = cur.mogrify(sql, args)
                if isinstance(sql, str):
                    return sql
                else:
                    return str(sql, encoding='utf-8')
            else:
                return sql

    def escape(self, s):
        return s

    def select(self, tables, **kwargs):
        return SelectHelper(self, tables, **kwargs)

    def insert(self, table, **kwargs):
        return InsertHelper(self, table, **kwargs)

    def update(self, table, **kwargs):
        return UpdateHelper(self, table, **kwargs)

    def delete(self, table, **kwargs):
        return DeleteHelper(self, table, **kwargs)

    @abc.abstractmethod
    @contextmanager
    def connect_cur(self):
        cur = None
        try:
            yield cur
        except:
            pass
        finally:
            pass

    def select_page(self, sql, pagecur=1, pagesize=20, count_sql=None, maxid=-1, isdict=True):
        page = pager.db_pager(self, sql, pagecur, pagesize, count_sql, maxid)
        if isdict:
            page.todict()
        else:
            page.tolist()
        return page

class TestPool():
    def __init__(self):
        self._idle_cache = []
        self._idle_using = []
        self._maxconnections = 10

class SimplePostgresqlConnection(PostgresqlHelper):

    type='simple_mysql'

    def __init__(self, engine, *args, **kwargs):
        self._conn = None
        self._name = 'simple'
        self.pool = TestPool()
        self._args, self._kwargs = args, kwargs
        try:
            self._engine = engine.connect
        except Exception as e:
            raise Exception('数据库连接器不可用')
        self._conn = self._engine(*self._args, **self._kwargs)
        # 记录连接的数据库信息
        self._server_id = None
        self._conn_id = 0
        self.conn_info()
        self._transaction = 0

    def __enter__(self):
        """Enter the runtime context for the connection object."""
        return self

    def __exit__(self, *exc):
        """Exit the runtime context for the connection object.
        This does not close the connection, but it ends a transaction.
        """
        if exc[0] is None and exc[1] is None and exc[2] is None:
            self.commit()
        else:
            self.rollback()

    def conn_info(self):
        """获取数据库连接信息，便于问题追踪"""
        cur = self._conn.cursor()
        cur.execute("show variables like 'server_id'")
        row = cur.fetchone()
        self._server_id = int(row[1])
        cur.close()

        cur = self._conn.cursor()
        cur.execute("select connection_id()")
        row = cur.fetchone()
        self._conn_id = row[0]
        cur.close()


    def cursor(self, *args, **kwargs):
        return self._conn.cursor(*args, **kwargs)

    def close(self):
        self._conn.close()

    def begin(self, *args, **kwargs):
        begin = self._conn.begin
        begin(*args, **kwargs)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def cancel(self):
        cancel = self._conn.cancel
        cancel()

    def ping(self, *args, **kwargs):
        return self._conn.ping(*args, **kwargs)
    
    def escape(self, s):
        return self._conn.escape_string(s)

    @contextmanager
    def connect_cur(self):
        cur = None
        try:
            cur = self.cursor()
            yield cur
            self.commit()
        except Exception as e:
            self.rollback()
            raise e
        finally:
            if cur is not None:
                cur.close()
