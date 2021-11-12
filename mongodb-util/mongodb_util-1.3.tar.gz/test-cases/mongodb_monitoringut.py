#!/usr/bin/python3
'''
Unit test cases for mongodb_monitoring
'''

import unittest
from unittest.mock import Mock
import os
import sys
import pymongo
from packaging import version
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"/src/")
import mongodb_monitoring                             #pylint: disable=wrong-import-position, import-error


class Previousdescription():                          #pylint:disable=too-few-public-methods
    '''
    Mocked previous description class
    Pylint disable - Too few public methods
    '''
    def __init__(self):
        self.server_type = 'test_server'
        self.server_type_name = 'test'
        self.topology_type = 'type1'
        self.topology_type_name = 'type1_name'

class Newdescription():
    '''
    Mocked New description
    '''
    def __init__(self):
        self.server_type = 'new_test_server'
        self.server_type_name = 'new_test'
        self.topology_type = 'type2'
        self.topology_type_name = 'type2_name'
        self.flag_read = True
        self.flag_write = True

    def has_readable_server(self):
        '''
        Mocked has_readable_server
        '''
        return_val = None
        if self.flag_read:
            self.flag_read = False
            return_val = True
        else:
            return_val = False
        return return_val

    def has_writable_server(self):
        '''
        Mocked has_writable_server
        '''
        return_val = None
        if self.flag_write:
            self.flag_write = False
            return_val = True
        else:
            return_val = False
        return return_val

class Event():                           #pylint:disable=too-many-instance-attributes,too-few-public-methods
    '''
    Mocked event
    Pylint disable - Too many instance attributes, Too few public methods
    '''
    def __init__(self):
        self.command_name = 'test'
        self.command = {'query':'test_query'}
        self.request_id = 'test123'
        self.connection_id = '123'
        self.duration_micros = 0000
        self.server_address = 'test_address'
        self.topology_id = '123'
        self.previous_description = Previousdescription()
        self.new_description = Newdescription()
        self.reply = Reply()
        self.address = 'address'
        self.reason = 'test_reason'

class Reply():                           #pylint:disable=too-few-public-methods
    '''
    Mocked Reply
    Pylint disable - Too few public methods
    '''
    def __init__(self):
        self.document = 'doc'

class MonitoringUT(unittest.TestCase):
    '''
    Testing mongo monitoring module
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @unittest.skipUnless(version.parse(pymongo.__version__) >= version.parse('3.1'),
                         "CommandListener is supported in pymongo >= 3.1")
    def test_monitoring_commandlogger(self):                                    #pylint:disable=no-self-use
        '''
        Testing monitoring - commandlogger
        pylint disabled - Too many statements
        '''
        event_obj = Event()
        mock_log = Mock()
        obj = mongodb_monitoring.CommandLogger(mock_log)
        obj.started(event_obj)
        mock_log.info.assert_called_with(
            'Command %s, query %s with request id %s started on server %s',
            'test',
            'test_query',
            'test123',
            '123')
        obj.succeeded(event_obj)
        mock_log.info.assert_called_with(
            'Command %s with request id %s on server %s succeeded in %s microsecond',
            'test',
            'test123',
            '123',
            0)
        obj.failed(event_obj)
        mock_log.warning.assert_called_with(
            'Command %s with request id %s on server %s failed in %s microsecond',
            'test',
            'test123',
            '123',
            0)
        del obj

    @unittest.skipUnless(version.parse(pymongo.__version__) >= version.parse('3.3'),
                         "ServerListener is supported in pymongo >= 3.3")
    def test_monitoring_serverlogger(self):                                     #pylint:disable=no-self-use
        '''
        Testing monitoring - serverlogger
        pylint disabled - Too many statements
        '''
        event_obj = Event()
        mock_log = Mock()
        obj = mongodb_monitoring.ServerLogger(mock_log)
        obj.opened(event_obj)
        mock_log.info.assert_called_with('Server %s added to topology %s',
                                         'test_address',
                                         '123')
        obj.description_changed(event_obj)
        mock_log.info.assert_called_with('Server %s changed type from %s to %s',
                                         'test_address',
                                         'test',
                                         'new_test')
        event_obj.new_description.server_type = 'test_server'
        obj.description_changed(event_obj)
        mock_log.info.assert_called_with('Server %s changed type from %s to %s',
                                         'test_address',
                                         'test',
                                         'new_test')
        obj.closed(event_obj)
        mock_log.warning.assert_called_with('Server %s removed from topology %s',
                                            'test_address',
                                            '123')
        del obj

    @unittest.skipUnless(version.parse(pymongo.__version__) >= version.parse('3.3'),
                         "ServerHeartbeatListener is supported in pymongo >= 3.3")
    def test_monitoring_heartbeatlogger(self):                                  #pylint:disable=no-self-use
        '''
        Testing monitoring - heartbeatlogger
        pylint disabled - Too many statements
        '''
        event_obj = Event()
        mock_log = Mock()
        obj = mongodb_monitoring.HeartbeatLogger(mock_log)
        obj.started(event_obj)
        mock_log.info.assert_called_with('Heartbeat sent to server %s',
                                         '123')
        obj.succeeded(event_obj)
        mock_log.info.assert_called_with('Heartbeat to server %s succeeded with reply %s',
                                         '123',
                                         'doc')
        event_obj.reply = "Error"
        obj.failed(event_obj)
        mock_log.warning.assert_called_with('Heartbeat to server %s failed with error %s',
                                            '123',
                                            'Error')
        del obj

    @unittest.skipUnless(version.parse(pymongo.__version__) >= version.parse('3.3'),
                         "TopologyListener is supported in pymongo >= 3.3")
    def test_monitoring_topologylogger(self):                                   #pylint:disable=no-self-use
        '''
        Testing monitoring - topologylogger
        pylint disabled - Too many statements
        '''
        event_obj = Event()
        mock_log = Mock()
        obj = mongodb_monitoring.TopologyLogger(mock_log)
        obj.opened(event_obj)
        mock_log.info.assert_called_with('Topology with id %s opened',
                                         '123')
        obj.description_changed(event_obj)
        mock_log.info.assert_called_with('Topology %s changed type from %s to %s', '123',
                                         'type1_name',
                                         'type2_name')
        event_obj.new_description.topology_type = 'type1'
        obj.description_changed(event_obj)
        mock_log.info.assert_called_with('Topology description updated for topology id %s',
                                         '123')
        obj.closed(event_obj)
        mock_log.info.assert_called_with('Topology with id %s closed',
                                         '123')
        del obj

    @unittest.skipUnless(version.parse(pymongo.__version__) >= version.parse('3.9'),
                         "ConnectionPoolListener is supported in pymongo >= 3.9")
    def test_monitoring_connpoollogger(self):                                   #pylint:disable=no-self-use
        '''
        Testing monitoring - connectionpoollogger
        pylint disabled - Too many statements
        '''
        event_obj = Event()
        mock_log = Mock()
        obj = mongodb_monitoring.ConnectionPoolLogger(mock_log)
        obj.pool_created(event_obj)
        mock_log.info.assert_called_with('[pool %s] pool created', 'address')
        obj.pool_cleared(event_obj)
        mock_log.info.assert_called_with('[pool %s] pool cleared', 'address')
        obj.pool_closed(event_obj)
        mock_log.info.assert_called_with('[pool %s] pool closed', 'address')
        obj.connection_created(event_obj)
        mock_log.info.assert_called_with('[pool %s][conn #%s] connection created',
                                         'address',
                                         '123')
        obj.connection_ready(event_obj)
        mock_log.info.assert_called_with('[pool %s][conn #%s] connection setup succeeded',
                                         'address',
                                         '123')
        obj.connection_closed(event_obj)
        mock_log.info.assert_called_with('[pool %s][conn #%s] connection closed, reason: %s',
                                         'address',
                                         '123',
                                         'test_reason')
        obj.connection_check_out_started(event_obj)
        mock_log.info.assert_called_with('[pool %s] connection check out started',
                                         'address')
        obj.connection_check_out_failed(event_obj)
        mock_log.warning.assert_called_with('[pool %s] connection check out failed, reason: %s',
                                            'address',
                                            'test_reason')
        obj.connection_checked_out(event_obj)
        mock_log.info.assert_called_with('[pool %s][conn #%s] connection checked out of pool',
                                         'address',
                                         '123')
        obj.connection_checked_in(event_obj)
        mock_log.info.assert_called_with('[pool %s][conn #%s] connection checked into pool',
                                         'address',
                                         '123')
        del obj

if __name__ == '__main__':
    unittest.main()
