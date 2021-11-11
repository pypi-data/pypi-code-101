#!/usr/bin/python3
#pylint: disable=protected-access
"""
Unit test case for Database module

NOTE - This testcase requires pymongo version >= 3.1
"""
import unittest
from unittest.mock import patch, Mock
import sys
import os
import pymongo
from packaging import version
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"/src/")
import mongodb_util                                  #pylint:disable=wrong-import-position, import-error

class Admin():                                 #pylint:disable=too-few-public-methods
    '''
    Mocked admin class
    Pylint disable - Too few public methods
    '''
    @staticmethod
    def command(msg):
        '''
        Mocked command function
        Pylint disable - Mothod could be a function
        '''
        return msg

class Mockedmongo():                            #pylint:disable=too-few-public-methods
    '''
    Mocked MongoClient
    Pylint disable - Too few public methods
    '''
    def __init__(self, _url, event_listeners):
        _dummy = event_listeners
        self.admin = Admin()

class DbmodTest(unittest.TestCase):
    """
    Testing database module
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = mongodb_util.Database("test_uri")

    def test_enable_logging(self):
        """
        Test enable_logging module
        """
        self.assertEqual(str(type(self.obj._enable_logging()[0])),
                         "<class 'mongodb_monitoring.CommandLogger'>",
                         msg="test_enable_logging-1-failed")
        del self.obj

        self.obj = mongodb_util.Database("test_uri", log={'commandlogger':True,
                                                          'serverlogger':False,
                                                          'heartbeatlogger':False,
                                                          'topologylogger':False,
                                                          'connectionpoollogger':False})
        list_eventlisteners = [str(type(item)) for item in self.obj._enable_logging()]
        self.assertEqual(list_eventlisteners,
                         ["<class 'mongodb_monitoring.CommandLogger'>"],
                         msg="test_enable_logging-2-failed")
        del self.obj

        if version.parse(pymongo.__version__) >= version.parse('3.3'):
            self.obj = mongodb_util.Database("test_uri", log={'commandlogger':False,
                                                              'serverlogger':True,
                                                              'heartbeatlogger':True,
                                                              'topologylogger':True})
            list_eventlisteners = [str(type(item)) for item in self.obj._enable_logging()]
            self.assertEqual(list_eventlisteners,
                             ["<class 'mongodb_monitoring.ServerLogger'>",
                              "<class 'mongodb_monitoring.HeartbeatLogger'>",
                              "<class 'mongodb_monitoring.TopologyLogger'>"],
                             msg="test_enable_logging-3-failed")
            del self.obj

        if version.parse(pymongo.__version__) >= version.parse('3.9'):
            self.obj = mongodb_util.Database("test_uri", log={'commandlogger':False,
                                                              'serverlogger':True,
                                                              'heartbeatlogger':True,
                                                              'topologylogger':True,
                                                              'connectionpoollogger':True})
            list_eventlisteners = [str(type(item)) for item in self.obj._enable_logging()]
            self.assertEqual(list_eventlisteners,
                             ["<class 'mongodb_monitoring.ServerLogger'>",
                              "<class 'mongodb_monitoring.HeartbeatLogger'>",
                              "<class 'mongodb_monitoring.TopologyLogger'>",
                              "<class 'mongodb_monitoring.ConnectionPoolLogger'>"],
                             msg="test_enable_logging-4-failed")
            del self.obj

    def test_failed_connect(self):
        """
        Testing connect module
        """
        mock_log = Mock()
        with patch('mongodb_util.pymongo.MongoClient', autospec=True) as mock_mongoclient,\
            self.assertRaises(pymongo.errors.ServerSelectionTimeoutError):
            self.obj = mongodb_util.Database("test_uri", mock_log)
            mock_mongoclient.side_effect = Mock(
                side_effect=pymongo.errors.ServerSelectionTimeoutError)
            self.obj.connect()
        del self.obj
        self.obj = mongodb_util.Database("test_uri", mock_log)
        with patch('mongodb_util.pymongo.MongoClient', autospec=True) as mock_mongoclient,\
            self.assertRaises(pymongo.errors.ConnectionFailure):
            mock_mongoclient.side_effect = Mock(side_effect=pymongo.errors.ConnectionFailure)
            self.obj.connect()
        del self.obj

    @patch('mongodb_util.pymongo.MongoClient', Mockedmongo)
    def test_success_connect(self):
        """
        Tests successful connection
        """
        self.obj = mongodb_util.Database("test_uri", logger=Mock())
        client = self.obj.connect()
        self.assertEqual("<class '__main__.Mockedmongo'>", str(type(client)))
        del self.obj

if __name__ == '__main__':
    unittest.main()
