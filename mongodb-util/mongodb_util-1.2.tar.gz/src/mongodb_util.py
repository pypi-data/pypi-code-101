"""
A custom module that provides Database access
"""
import pymongo

class Database(object):
    """
    Connect to MongoDB
    Driver = PyMongo

    logger: Pass a logger handle
    log: Pass a dictionary with various event listeners
    """
    def __init__(self, uri, logger=None, log=None):
        self._uri = uri
        self.should_reconnect = True
        self.logger = logger
        self.log_dict = log if log is not None else {}

    def connect(self):
        """
        This method creates the event listeners list,
        tries to connect to the MongoDB,
        if the connection fails, it retries. In case the connection
        fails again, the exception is thrown
        """
        event_listeners = self.get_event_listeners()
        try:
            return self.obtain_database_handle(event_listeners)
        except (pymongo.errors.ConnectionFailure,
                pymongo.errors.ServerSelectionTimeoutError) as exception:
            if self.logger:
                self.logger.exception("Connection failed")
            self.handle_connection_exception(exception)

    def obtain_database_handle(self, listeners_list):
        """
        Try obtaining a database handle and run a basic
        command to validate the connection
        """
        client = pymongo.MongoClient(self._uri, event_listeners=listeners_list)
        client.admin.command('ismaster')
        return client

    def get_event_listeners(self):
        """
        Creates a list of event listeners based on various conditions
        """
        if self.logger:
            return_list = self._enable_logging()
        else:
            return_list = []
        return return_list

    def handle_connection_exception(self, exception):
        """
        Performs a retry if the connection fails in the first try.
        If a seconds failure is encountered, an exception is thrown
        """
        if self.should_reconnect:
            if self.logger:
                self.logger.info("Exception while trying to connect, retrying")
            self.should_reconnect = False
            return self.connect()
        else:
            raise exception

    def _enable_logging(self):                                                  #pylint:disable=too-many-branches
        """
        Generate a list of event listeners based on user input
        CommandLogger is enabled by default
        """
        return_list = []

        if 'commandlogger' not in self.log_dict.keys() or \
            ('commandlogger' in self.log_dict.keys() and \
            self.log_dict['commandlogger'] is True):
            try:
                from mongodb_monitoring import CommandLogger
                return_list.append(CommandLogger(self.logger))
            except ImportError:
                pass

        if 'serverlogger' in self.log_dict.keys() and \
            self.log_dict['serverlogger'] is True:
            try:
                from mongodb_monitoring import ServerLogger
                return_list.append(ServerLogger(self.logger))
            except ImportError:
                pass

        if 'heartbeatlogger' in self.log_dict.keys() and \
            self.log_dict['heartbeatlogger'] is True:
            try:
                from mongodb_monitoring import HeartbeatLogger
                return_list.append(HeartbeatLogger(self.logger))
            except ImportError:
                pass

        if 'topologylogger' in self.log_dict.keys() and \
            self.log_dict['topologylogger'] is True:
            try:
                from mongodb_monitoring import TopologyLogger
                return_list.append(TopologyLogger(self.logger))
            except ImportError:
                pass

        if 'connectionpoollogger' in self.log_dict.keys() and \
            self.log_dict['connectionpoollogger'] is True:
            try:
                from mongodb_monitoring import ConnectionPoolLogger
                return_list.append(ConnectionPoolLogger(self.logger))
            except ImportError:
                pass

        return return_list
