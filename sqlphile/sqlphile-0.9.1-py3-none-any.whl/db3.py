import sqlite3
import json
import zlib
import sqlphile
from . import sql
from .dbtypes import DB_SQLITE3
from .skitai_compat import dispatch
from rs4 import asyncore
from rs4.misc.cbutil import tuple_cb
import time
import threading

class AttrDict (dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Committed:
    def commit (self):
        pass

    def set_callback (self, func, *args, **kargs):
        func (self)


class open:
    dbtype = DB_SQLITE3
    def __init__ (self, path, dir = None, auto_reload = False, auto_closing = True):
        self.closed = False
        self.auto_closing = auto_closing
        self.conn = sqlite3.connect (path, check_same_thread = False)
        self._init (dir, auto_reload, self.dbtype)

    def _init (self, dir, auto_reload, engine):
        self.create_cursor ()
        self.sqlphile = sqlphile.SQLPhile (dir, auto_reload, engine = engine, conn = self)

    def create_cursor (self):
        self.cursor = self.c = self.conn.cursor ()

    def set_autocommit (self, flag = None):
       # flags: None (autocommit), DEFERRED, IMMEDIATE or EXCLUSIVE
       self.conn.isolation_level = flag

    def __enter__ (self):
        return self

    def __exit__ (self, type, value, tb):
        self.auto_closing and self.close ()

    def __del__ (self):
        self.close ()

    def __getattr__ (self, name):
        try:
            return getattr (self.c, name)
        except AttributeError:
            return getattr (self.sqlphile, name)

    def close (self):
        if self.conn and not self.closed:
            self.c.close ()
            self.conn.close ()
            self.closed = True

    def commit (self):
        self.conn.commit ()
        return Committed ()

    def rollback (self):
        self.conn.rollback ()

    def serialize (self, obj):
        return zlib.compress (json.dumps (obj).encode ("utf8"))

    def deserialize (self, data):
        return json.loads (zlib.decompress (data).decode ('utf8'))

    def blob (self, obj):
        return sqlite3.Binary (obj)

    def field_names (self):
        return [x [0] for x in self.description]

    def as_dict (self, row, field_names = None):
        return AttrDict (dict ([(f, row [i]) for i, f in enumerate (field_names or self.field_names ())]))

    def execute (self, sql, *args, **kargs):
        is_script = False
        if isinstance (sql, (list, tuple)):
            sql = ";\n".join (map (str, sql)) + ";"
            is_script = True
        if is_script and self.dbtype == DB_SQLITE3:
            self.cursor.executescript (str (sql), *args, **kargs)
        else:
            self.cursor.execute (str (sql), *args, **kargs)
        return self

    def fetchone (self, as_dict = False):
        row = self.fetchmany (1, as_dict)
        return row and row [0] or None

    def fetchmany (self, limit, as_dict = False):
        rows = limit and self.cursor.fetchmany (limit) or self.cursor.fetchall ()
        if not as_dict:
            return rows
        field_names = self.field_names ()
        return [self.as_dict (row, field_names) for row in rows]

    def fetchall (self, as_dict = False):
        return self.fetchmany (0, as_dict)

    def one (self, *args, **kargs):
        try:
            from skitai import exceptions
        except ImportError:
            expt_class = ValueError
        else:
            expt_class = exceptions.HTTPError

        rows = self.fetchall (True)
        if not rows:
            raise expt_class ("410 Partial Not Found")
        if len (rows) > 1:
            raise expt_class ("409 Conflict")
        return rows [0]

    def fetch (self, *args, **kargs):
        return self.fetchall (True)

    def fetchn (self, n):
        return self.fetchmany (n, True)

    def fetch1 (self):
        return self.fetchone (True)


class open2 (open):
    # same as open but conn must be injected
    # conn maybe one of connection pool managed by an app
    def __init__ (self, conn, dir = None, auto_reload = False, auto_closing = True):
        self.closed = False
        self.conn = conn
        self.auto_closing = auto_closing
        self._init (dir, auto_reload, self.dbtype)


class open3 (open2):
    # single connection, multiple disposable cursors
    def __init__ (self, conn, dir = None, auto_reload = False):
        self.closed = False
        self.conn = conn
        self.auto_closing = False
        self._init (dir, auto_reload, self.dbtype)

    def _init (self, dir, auto_reload, engine):
        self.sqlphile = sqlphile.SQLPhile (dir, auto_reload, engine = engine, conn = self)
        self.cursor = self.c = None
        self.results = []

    def __del__ (self):
        self._close ()

    def _close (self):
        if not self.closed:
            for result in self.results:
                result.conn = None
                try: result._close ()
                except: pass
            try: self.conn.close ()
            except: pass
            self.closed = True

    def execute (self, *args, **kargs):
        cursor = self.conn.cursor ()
        # IMP: SHOUD give self for auto closing
        result = Result (self, cursor)._execute (*args, **kargs)
        self.results.append (result)
        return result

    def close (self):
        # remove explicit close
        raise AttributeError

    def rollback (self):
        raise AttributeError

    def commit (self):
        raise AttributeError


class Result (open2):
    # emulating corequest result object but this has
    # commit, rollback, fetch1, fetchone, fetchmay and fetchn

    def __init__ (self, conn, cursor):
        self.conn = conn
        self.cursor = self.c = cursor
        self.expt = None
        self.meta = {}

    def close (self):
        # remove explicit close
        raise AttributeError

    def _execute (self, sql, *args, **kargs):
        try:
            super ().execute (sql, *args, **kargs)
        except:
            self.expt = asyncore.compact_traceback () [2]
            self._close ()
        return self

    def __del__ (self):
        self._close ()

    def close_all (self):
        # CHEAT KEY: close connection and its own cursors forcely
        self.conn and self.conn._close ()

    def _close (self):
        # close cursor only
        if self.cursor:
            try:
                self.cursor.close ()
            except:
                pass
            self.conn = None
            self.cursor = self.c = None

    def set_callback (self, callback, reqid = None, timeout = 10):
        if reqid is not None:
            self.meta ["__reqid"] = reqid
        tuple_cb (self, callback)

    def maybe_reraise (self):
        if self.expt:
            raise self.expt

    def rollback (self):
        if not self.expt:
            self.conn.conn.rollback ()
            self._close ()
        self.maybe_reraise ()

    def commit (self, *args, **kargs):
        if not self.expt:
            self.conn.conn.commit ()
            self._close ()
        self.maybe_reraise ()

    def dispatch (self, *args, **kargs):
        r = dispatch (self.fetchall (True), self.expt)
        self._close ()
        return r

    def fetchmany (self, limit, as_dict = False):
        self.maybe_reraise ()
        r = super ().fetchmany (limit, as_dict)
        # auto closing
        if not limit or not r:
            self._close ()
        # # maybe this is main usage of this class
        # if limit and not r:
        #     self.close ()
        return r

    def fetch (self, *args, **kargs):
        self.maybe_reraise ()
        return super ().fetch (*args, **kargs)

    def one (self, *args, **kargs):
        self.maybe_reraise ()
        return super ().one (*args, **kargs)

    # lower version compatable --------------------
    def wait (self, timeout = 10, *args, **karg):
        pass
    getswait = getwait = dispatch
    wait_or_throw = commit
