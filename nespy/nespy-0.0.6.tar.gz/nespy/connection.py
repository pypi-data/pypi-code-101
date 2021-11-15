import requests
import ast
from nespy.datastream import *
from nespy.exceptions import *


class Connection:
    """
    Connection manages the overall connection to NebulaStream. It offers all the functions to communicate with
    NebulaStream.

    Examples
    -------
    First, we need to establish the connection with NebulaStream. For this we have to create a Connection object.
    The constructor takes two parameters: the host and port wherever NebulaStream is currently running.

    >>> import nespy as nes
    >>> c = nes.Connection("127.0.0.1", 8081)

    Now, we have to select a logical stream. However, if we do not know the name of the logical stream we should call
    the following function first. This function returns all registered logical streams in NebulaStream.

    >>> c.get_all_logical_streams()
    {
    'default_logical': 'id:INTEGER
                         value:INTEGER ',
     'exdra': 'id:INTEGER
               metadata_generated:INTEGER
               metadata_title:Char
               metadata_id:Char
               features_type:Char
               features_properties_capacity:INTEGER
               features_properties_efficiency:(Float)
               features_properties_mag:(Float)
               features_properties_time:INTEGER
               features_properties_updated:INTEGER
               features_properties_type:Char
               features_geometry_type:Char
               features_geometry_coordinates_longitude:(Float)
               features_geometry_coordinates_latitude:(Float)
               features_eventId :Char '
   }

    To select a specfic logical stream we then call the following function. This function returns an object of the type
    DataStream.

    >>> c.get_logical_stream("exdra")
    """
    def __init__(self, host, port):
        """
        Initialization of the connection to NebulaStream.

        Parameters
        ----------
        host : str
               Host where NebulaStream is running.
        port : int
               REST port of NebulaStream.
        """
        self.host = host
        self.port = port
        self.logical_stream = None

    def execute_query(self, query, strategy):
        """
        Submits a query to NebulaStream.

        Parameters
        ----------
        query : str
                The query itself as a string. The query has to follow the syntax of NebulaStream's Query API.
        strategy : str
                   Query translation strategy in NebulaStream: either bottom-up or top-down.

        Returns
        -------
        dict
        """
        url = 'http://{}:{}/v1/nes/query/execute-query'.format(self.host, self.port)
        request_body = {"userQuery": query, "strategyName": strategy}
        execute_query_response = requests.post(url, json=request_body)
        if execute_query_response.status_code == 200:
            return execute_query_response.json()  # response body
        else:
            raise WrongQueryError

    def get_query_execution_plan(self, query_id):
        """
        Asks NebulaStream for the execution plan without executing the query.

        Parameters
        ----------
        query_id : int

        Returns
        -------
        dict

        Notes
        ----------
        Exemplary response from NebulaStream's Wiki:

        {"nodes": [{
                    "id": "node_id",
                    "title": "node_title",
                    "nodeType": "node_type",
                    "capacity": "node_capacity",
                    "remainingCapacity": "remaining_capacity",
                    "physicalStreamName": "physical_stream_name"
                  }],
        "edges": [{
                    "source":"source_node",
                    "target":"target_node",
                    "linkCapacity":"link_capacity",
                    "linkLatency":"link_latency",
                }]
        }
        """
        url = 'http://{}:{}/v1/nes/query/execution-plan?queryId={}'.format(self.host, self.port, query_id)
        execution_plan_response = requests.get(url)
        if execution_plan_response.status_code == 200:
            return execution_plan_response.json()
        else:
            return "Something went wrong with NES..."

    def get_query_plan(self, query_id):
        """
        Retrieves the query plan from NebulaStream.
        Parameters
        ----------
        query_id : int

        Returns
        -------
        dict

        Notes
        -------
        Exemplary response from NebulaStream's Wiki:

        {"nodes": [{
                    "id": "node_id",
                    "title": "node_title",
                    "nodeType": "node_type"
                 }],
        "edges": [{
                    "source":"source_operator",
                    "target":"target_operator"
                 }]
        }
        """
        url = 'http://{}:{}/v1/nes/query/query-plan?queryId={}'.format(self.host, self.port, query_id)
        query_plan_response = requests.get(url)
        if query_plan_response.status_code == 200:
            return query_plan_response.json()
        else:
            return "Something went wrong with NES..."

    def stop_query(self, query_id):
        """
        Stops a query in NebulaStream.

        Parameters
        ----------
        query_id : int
                   Every registered query has an id in NebulaStream.
                   This id is required to identify which query NebulaStream should delete.

        Returns
        -------
        dict
        """
        url = 'http://{}:{}/v1/nes/query/stop-query?queryId={}'.format(self.host, self.port, query_id)
        delete_query = requests.delete(url)
        if delete_query.status_code == 200:
            return delete_query.json()
        else:
            return "Something went wrong with NES..."

    def get_nes_topology(self):
        """
        Requests the Topology graph of NebulaStream as a JSON.

        Parameters
        ----------

        Returns
        -------
        dict

        Notes
        -------
        Exemplary response from NebulaStream's Wiki:

        {"nodes": [{
            "id": "node_id",
            "title": "node_title",
            "nodeType": "node_type",
            "capacity": "node_capacity",
            "remainingCapacity": "remaining_capacity",
            "physicalStreamName": "physical_stream_name"
         }],
        "edges": [{
                "source":"source_node",
                "target":"target_node",
                "linkCapacity":"link_capacity",
                "linkLatency":"link_latency",
                }]
        }
        """
        url = 'http://{}:{}/v1/nes/topology'.format(self.host, self.port)
        nes_topology = requests.get(url)

        if nes_topology.status_code == 200:
            return nes_topology.json()
        else:
            return "Something went wrong with NES..."

    def get_all_queries(self):
        """
        Get all queries that are registered in NebulaStream.
        The user receives the query ids and the corresponding queries.

        Parameters
        ----------

        Returns
        -------
        dict

        """
        url = 'http://{}:{}/v1/nes/queryCatalog/allRegisteredQueries'.format(self.host, self.port)
        all_queries = requests.get(url)
        if all_queries.status_code == 200:
            return all_queries.json()
        elif all_queries.status_code == 204:
            return "There are no registered queries in NES"
        else:
            return "Something went wrong with NES..."

    def get_queries_with_status(self, status):
        """
        This function returns all queries with the corresponding status.

        Parameters
        ----------
        status :str
                Status of queries.
                Status can be "Registered", "Scheduling", "Running", "Marked_For_Stop"/"MarkedForStop", "Stopped" or
                "Failed".
                They are not case sensitive.

        Returns
        -------
        list

        Notes
        -------
        Registered: Query is registered to be scheduled to the worker nodes (added to the queue).

        Scheduling: Coordinator node is processing the Query and will transmit the execution pipelines to worker nodes.

        Running: Query is now running successfully.

        MarkedForStop: A request arrived into the system for stopping a query and system marks the query for stopping
        (added to the queue).

        Stopped: Query was explicitly stopped either by system or by user.

        Failed: Query failed because of some reason.
        """
        status_list = ["registered", "scheduling", "running", "marked_for_stop", "markedforstop", "stopped", "failed"]

        if status.casefold() in status_list:
            if (status.casefold() == "markedforstop") or (status.casefold() == "marked_for_stop"):
                status = "MarkedForStop"
            else:
                status = status.casefold().capitalize()
            url = 'http://{}:{}/v1/nes/queryCatalog/queries?status={}'.format(self.host, self.port, status)
            status_response = requests.get(url)
            if status_response.status_code == 200:
                if isinstance(status_response.json(), list):
                    return status_response.json()
                elif isinstance(status_response.json(), None):
                    return []
            elif status_response.status_code == 204:
                return []
        else:
            raise NotSuchStatusError

    def get_queries_with_status_at_pos(self, status, pos):
        """
        This function extends get_status_of_all_queries by saying which query the user wants exactly.

        Parameters
        ----------
        status : str
                 Status of queries.
                 Status can be "Registered", "Scheduling", "Running", "Marked_For_Stop"/"MarkedForStop", "Stopped" or
                 "Failed".
                 They are not case sensitive.
        pos : int
              Position of response of get_status_of_all_queries.

        Returns
        -------
        str
        """
        try:
            status_response = self.get_queries_with_status(status)
            if len(status_response) > 0:
                return status_response[pos]
            else:
                return ""
        except NotSuchStatusError:
            print("There is no such status \"{}\".".format(status))

    def get_all_logical_streams(self):
        """
        Lists all registered logial streams and their schema in NebulaStream.

        Parameters
        ----------

        Returns
        -------
        str
        """
        url = 'http://{}:{}/v1/nes/streamCatalog/allLogicalStream'.format(self.host, self.port)
        logical_streams = requests.get(url)

        if logical_streams.status_code == 200:
            return logical_streams.json()
        else:
            return "Something went wrong with NES..."

    def get_all_physical_streams(self, logical_stream_name):
        """
        Lists all physical streams for a specific logical stream.

        Parameters
        ----------
        logical_stream_name : str
                              Name of logical stream. Has to be registered in NebulaStream.

        Returns
        -------
        dict
        """
        url = 'http://{}:{}/v1/nes/streamCatalog/allPhysicalStream?logicalStreamName={}'.format(self.host, self.port, logical_stream_name)
        physical_streams = requests.get(url)

        if physical_streams.status_code == 200:
            physical_streams_dict = ast.literal_eval(physical_streams.content.decode("utf-8"))
            return physical_streams_dict
        else:
            return "Something went wrong with NES..."

    def get_logical_stream(self, position_or_name):
        """
        Selects a specific logical stream.

        Parameters
        ----------
        position_or_name : str or int
                           Position in dictionary or name of logical stream.
                           Name has to be written correctly or else it does not work.

        Returns
        -------
        DataStream
        """
        if isinstance(position_or_name, int):
            logical_streams = self.get_all_logical_streams()
            self.logical_stream = DataStream(list(logical_streams.keys())[position_or_name], self)
        elif isinstance(position_or_name, str):
            self.logical_stream = DataStream(position_or_name, self)

        return self.logical_stream

    def add_logical_stream(self, logical_stream_name, schema):
        """
        Adds a logical stream to NebulaStream. Currently the schema has to be written in the C++ syntax.

        Parameters
        ----------
        logical_stream_name : str
                              The name of the new logical stream.
        schema : str
                 The schema of the logical stream. Has to be in C++ syntax at the moment.

        Returns
        -------
        dict

        """
        url = 'http://{}:{}/v1/nes/streamCatalog/addLogicalStream'.format(self.host, self.port)
        request_body = {"streamName": logical_stream_name, "schema": schema}
        add_logical_stream_response = requests.post(url, json=request_body)
        if add_logical_stream_response.status_code == 200:
            return add_logical_stream_response.json()  # response body
        else:
            return "Adding Logical Stream did not work out"

    def update_logical_stream(self, logical_stream_name, schema):
        """
        Adds a logical stream to nes. Currently the schema has to be written in the C++ syntax.

        Parameters
        ----------
        logical_stream_name : str
                              The name of the new logical stream.
        schema : str
                 The schema of the logical stream. Has to be in C++ syntax at the moment.

        Returns
        -------
        str
        """
        url = 'http://{}:{}/v1/nes/streamCatalog/updateLogicalStream'.format(self.host, self.port)
        request_body = {"streamName": logical_stream_name, "schema": schema}
        update_logical_stream_response = requests.post(url, json=request_body)
        if update_logical_stream_response.status_code == 200:
            return update_logical_stream_response.json()  # response body
        else:
            return "Updating Logical Stream did not work out"

    def delete_logical_stream(self, logical_stream_name):
        """
        Deletes a registered logical stream.

        Parameters
        ----------
        logical_stream_name : str
                              Name of logical stream. Has to be registered in NebulaStream.

        Returns
        -------
        str

        """
        url = 'http://{}:{}/v1/nes/streamCatalog/deleteLogicalStream'.format(self.host, self.port)
        request_body = {"streamName": logical_stream_name}
        delete_logical_stream = requests.delete(url, json=request_body)
        if delete_logical_stream.status_code == 200:
            return delete_logical_stream.text
        else:
            return "Something went wrong with NES..."

    def submit_pattern(self, pattern, strategy):
        """
        Submits a pattern.

        Parameters
        ----------
        pattern : str
        strategy : str

        Returns
        -------
        dict

        """
        url = 'http://{}:{}/v1/nes/pattern/execute-pattern'.format(self.host, self.port)
        request_body = {"pattern": pattern, "strategy": strategy}
        submit_pattern_response = requests.post(url, json=request_body)
        if submit_pattern_response.status_code == 200:
            return submit_pattern_response.json()  # response body
        else:
            return "Submitting Pattern did not work out"


