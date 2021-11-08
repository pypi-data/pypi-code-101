# -*- coding: utf-8 -*-
import time
import threading
import os

import numpy
from qpython.qconnection import QConnection

from pyconn import logger
from pyconn.db.advancedqreader import AdvancedQReader


class Server:
    def __init__(self, **kwargs):
        self.name = ""
        self.host = ""
        self.port = 0
        self.username = ""
        self.password = ""
        self.timeout = 30.0  # seconds
        self.pandas = False
        self.callback = None
        self.encoding = "utf-8"
        self.__dict__.update(kwargs)


class MonitorThread(threading.Thread):
    def __init__(self):
        super(MonitorThread, self).__init__()
        self.pool = ConnectionPool()

    def run(self):
        while True:
            if self.pool is not None:
                for server_name, handle in self.pool.handle_dict.items():
                    if handle.is_connected:
                        try:
                            with handle.lock:
                                handle.sendSync('til 1')
                                logger.debug(server_name + ' heartbeat success')
                        except Exception as e:
                            logger.warning(server_name + ' heartbeat failed')
                            handle.is_connected = False
                    else:
                        handle = self.pool.create_connection(handle.server)
                        if handle is not None and handle.is_connected:
                            logger.info('Reconnected to {}'.format(handle.server.name))
                            callback = handle.server.callback
                            if callable(callback):
                                callback()
                time.sleep(30)


class QHandle(QConnection):
    def __init__(self, server):
        super(QHandle, self).__init__(host=server.host, port=server.port, username=server.username,
                                      encoding=server.encoding, timeout=server.timeout, password=server.password,
                                      pandas=server.pandas, reader_class=AdvancedQReader)
        self.is_connected = False
        self.server = server
        self.lock = threading.Lock()


class ConnectionPool:
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, server_list=None):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = super(ConnectionPool, cls).__new__(cls)
                    cls._instance.handle_dict = {}
        return cls._instance

    def __init__(self, server_list=None):
        if server_list is None:
            return
        for server in server_list:
            if server.name not in self._instance.handle_dict.keys():
                self.create_connection(server)
        self.start_monitor_thread()

    @staticmethod
    def start_monitor_thread():
        thread = MonitorThread()
        thread.start()

    def create_connection(self, server):
        conn = QHandle(server)
        self.handle_dict[server.name] = conn
        try:
            logger.debug('Try connect to ' + server.name)
            with conn.lock:
                conn.open()
        except Exception as e:
            logger.error('Connect to {} failed: '.format(server.name, e.args))
            conn.is_connected = False
        else:
            conn.is_connected = True
        return conn

    def get_connection(self, server):
        return self.handle_dict.get(server.name)


class Query:

    def __init__(self, server):
        self.pool = ConnectionPool()
        self.server = server
        self.conn = None

    def query_sync(self, query, *parameters, **options):
        result = None
        self.conn = self.pool.get_connection(self.server)
        if self.conn is not None and self.conn.is_connected:
            try:
                with self.conn.lock:
                    result = self.conn.sendSync(query, *parameters, **options)
            except Exception as e:
                log_str = "DB[{}] error: {}, query: {}, params: {}, options: {}"
                logger.error(log_str.format(self.server.name, e.args, query, parameters, options))
        else:
            log_str = "DB[{}] error: Invalid handle"
            logger.error(log_str.format(self.server.name))
        return result

    @staticmethod
    def to_sym(s):
        return numpy.string_(s, encoding='utf-8')

    @staticmethod
    def to_sym_list(arr):
        """
        convert numpy.array[object] to numpy.array[numpy.string_ with utf-8]
        :param arr: df['col'].values
        :return: numpy.string_ with utf-8
        """
        if isinstance(arr, list):
            arr = numpy.array(arr)
        return numpy.char.encode(arr.astype(numpy.unicode_), encoding='utf-8')

    @staticmethod
    def to_date(dt):
        return dt.astype('M8[D]')
