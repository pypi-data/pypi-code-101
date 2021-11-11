'''
Provides monitoring functionality to the db_util module
'''
import pymongo
from packaging import version

if version.parse(pymongo.__version__) >= version.parse('3.1'):
    from pymongo.monitoring import CommandListener                              #pylint:disable=no-name-in-module, ungrouped-imports
else:
    CommandListener = None                                                      #pylint:disable=invalid-name

if version.parse(pymongo.__version__) >= version.parse('3.3'):
    from pymongo.monitoring import ServerListener, ServerHeartbeatListener, TopologyListener   #pylint:disable=no-name-in-module, ungrouped-imports
else:
    ServerListener = ServerHeartbeatListener = TopologyListener = None          #pylint:disable=invalid-name

if version.parse(pymongo.__version__) >= version.parse('3.9'):
    from pymongo.monitoring import ConnectionPoolListener                       #pylint:disable=no-name-in-module, ungrouped-imports
else:
    ConnectionPoolListener = None                                               #pylint:disable=invalid-name

if CommandListener:
    class CommandLogger(CommandListener):
        """
        Monitors the commands executed over the client
        """
        def __init__(self, logger):
            self.logger = logger

        def started(self, event):
            """
            Issuing of a command
            """
            self.logger.info("Command %s, query %s with request id %s started on server %s",
                             event.command_name,
                             event.command.get('query'),
                             event.request_id,
                             event.connection_id)

        def succeeded(self, event):
            """
            Command successful
            """
            self.logger.info(
                "Command %s with request id %s on server %s succeeded in %s microsecond",
                event.command_name,
                event.request_id,
                event.connection_id,
                event.duration_micros)

        def failed(self, event):
            """
            Command failed
            """
            self.logger.warning(
                "Command %s with request id %s on server %s failed in %s microsecond",
                event.command_name,
                event.request_id,
                event.connection_id,
                event.duration_micros)

if ServerListener:
    class ServerLogger(ServerListener):
        """
        Monitors metrics related to the Server discovery
        """
        def __init__(self, logger):
            self.logger = logger

        def opened(self, event):
            """
            Addition of new server to the topology
            """
            self.logger.info("Server %s added to topology %s",
                             event.server_address,
                             event.topology_id)

        def description_changed(self, event):
            """
            Change in the description of the server
            """
            previous_server_type = event.previous_description.server_type
            new_server_type = event.new_description.server_type
            if new_server_type != previous_server_type:
                try:
                    self.logger.info("Server %s changed type from %s to %s",
                                     event.server_address,
                                     event.previous_description.server_type_name,
                                     event.new_description.server_type_name)
                except AttributeError:
                    #server_type_name unavailable in current version
                    self.logger.info("Server %s changed type from %s to %s",
                                     event.server_address,
                                     event.previous_description.server_type,
                                     event.new_description.server_type)

        def closed(self, event):
            """
            Removal of server from the topology
            """
            self.logger.warning("Server %s removed from topology %s",
                                event.server_address,
                                event.topology_id)

if ServerHeartbeatListener:
    class HeartbeatLogger(ServerHeartbeatListener):
        """
        Monitor Heartbeat from the server
        """
        def __init__(self, logger):
            self.logger = logger

        def started(self, event):
            """
            Sending Heartbeat
            """
            self.logger.info("Heartbeat sent to server %s",
                             event.connection_id)

        def succeeded(self, event):
            """
            Heartbeat received successful
            """
            try:
                self.logger.info("Heartbeat to server %s succeeded with reply %s",
                                 event.connection_id,
                                 event.reply.document)
            except AttributeError:
                #reply.document unavailable in current version
                self.logger.info("Heartbeat to server %s succeeded",
                                 event.connection_id)

        def failed(self, event):
            """
            Heartbeat failed
            """
            self.logger.warning("Heartbeat to server %s failed with error %s",
                                event.connection_id,
                                event.reply)

if TopologyListener:
    class TopologyLogger(TopologyListener):
        """
        Monitor metrics related to topology
        """
        def __init__(self, logger):
            self.logger = logger

        def opened(self, event):
            """
            Opening of a topology
            """
            self.logger.info("Topology with id %s opened",
                             event.topology_id)

        def description_changed(self, event):
            """
            Change in the topology
            """
            self.logger.info("Topology description updated for topology id %s",
                             event.topology_id)
            previous_topology_type = event.previous_description.topology_type
            new_topology_type = event.new_description.topology_type
            if new_topology_type != previous_topology_type:
                try:
                    self.logger.info("Topology %s changed type from %s to %s",
                                     event.topology_id,
                                     event.previous_description.topology_type_name,
                                     event.new_description.topology_type_name)
                except AttributeError:
                    #topology_type_name is unavailable in current version
                    self.logger.info("Topology %s changed type from %s to %s",
                                     event.topology_id,
                                     event.previous_description.topology_type,
                                     event.new_description.topology_type)
            try:
                if not event.new_description.has_writable_server():
                    self.logger.warning("No writable servers available.")
                if not event.new_description.has_readable_server():
                    self.logger.warning("No readable servers available.")
            except AttributeError:
                #has_writeable_server and has_readable_server is unavailable in current version
                pass

        def closed(self, event):
            """
            Closing a topology
            """
            self.logger.info("Topology with id %s closed",
                             event.topology_id)

if ConnectionPoolListener:
    class ConnectionPoolLogger(ConnectionPoolListener):
        """
        Every MongoClient instance has a built-in connection pool per server
        in your MongoDB topology. These pools open sockets on demand to support
        the number of concurrent MongoDB operations that your multi-threaded
        application requires. There is no thread-affinity for sockets.
        """
        def __init__(self, logger):
            self.logger = logger

        def pool_created(self, event):
            """
            logs Pool creation
            """
            self.logger.info("[pool %s] pool created",
                             event.address)

        def pool_cleared(self, event):
            """
            logs Pool cleared
            """
            self.logger.info("[pool %s] pool cleared",
                             event.address)

        def pool_closed(self, event):
            """
            logs pool closure
            """
            self.logger.info("[pool %s] pool closed",
                             event.address)

        def connection_created(self, event):
            """
            logs connection creation to the pool
            """
            self.logger.info("[pool %s][conn #%s] connection created",
                             event.address,
                             event.connection_id)

        def connection_ready(self, event):
            """
            Logs connection ready
            """
            self.logger.info("[pool %s][conn #%s] connection setup succeeded",
                             event.address,
                             event.connection_id)

        def connection_closed(self, event):
            """
            Logs connection closure
            """
            self.logger.info("[pool %s][conn #%s] connection closed, reason: %s",
                             event.address,
                             event.connection_id,
                             event.reason)

        def connection_check_out_started(self, event):
            """
            Logs connection checkout
            """
            self.logger.info("[pool %s] connection check out started", event.address)

        def connection_check_out_failed(self, event):
            """
            Logs failed connection checkout
            """
            self.logger.warning("[pool %s] connection check out failed, reason: %s",
                                event.address,
                                event.reason)

        def connection_checked_out(self, event):
            """
            Logs successful connection checkout
            """
            self.logger.info("[pool %s][conn #%s] connection checked out of pool",
                             event.address,
                             event.connection_id)

        def connection_checked_in(self, event):
            """
            Logs connection checkin
            """
            self.logger.info("[pool %s][conn #%s] connection checked into pool",
                             event.address,
                             event.connection_id)
