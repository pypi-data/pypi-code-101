import io
import time
import pandas as pd
import zmq
from IPython.core.display import display, HTML, clear_output
import holoviews as hv
from holoviews.streams import Buffer
import re

from nespy.format import _write_header, _how_many_bytes_per_row, _byte_row_to_string, _write_data, _types_details
from nespy.operators import *
from nespy.exceptions import *
from nespy.wrapper import *
from nespy.sinktypes import *
import nespy.grpc.SerializableOperator_pb2 as pb


class DataStream():
    """
    DataStream manages the communication with the user and data processing functions.

    Examples
    -------
    Chosing a logical stream. Here we chose the data stream "sensor".
    This data stream measures, e.g., the temperature, the humidity, and the air quality.

    >>> import nespy as nes
    >>> c = nes.Connection("127.0.0.1", 8081)
    >>> sensor = c.get_logical_stream("sensor")

    Now, we can filter specific records according to a filter predicate.

    >>> # Filter
    >>> sensor[sensor["temperature"] > 3]
    >>> sensor[sensor["temperature"] < 3]
    >>> sensor[sensor["temperature"] <= 3]
    >>> sensor[sensor["temperature"] >= 3]
    >>> sensor[sensor["temperature"] == 3]
    >>> sensor[sensor["temperature"] != 3]
    >>> sensor[sensor["temperature"] > sensor["humidity"]
    >>> sensor[(sensor["temperature"] > 3) & (sensor["temperature"] < 15)]
    >>> sensor[(sensor["temperature"] < 3) | (sensor["temperature"] == 10)]

    But we can also select only specific attributes of our data stream.

    >>> # Select
    >>> sensor[sensor["sensor_id"]]
    >>> # or
    >>> sensor[["sensor_id"]]
    >>> sensor[["sensor_id", "temperature", "humidity", "air_pressure"]]

    Here, we manipulate the data stream. We can map different values to specific attributes.

    >>> sensor["temperature"] = sensor["temperature"] + 0.01
    >>> sensor["temperature"] = sensor["temperature"] - 0.01
    >>> sensor["temperature"] = sensor["temperature"] * 0.01
    >>> sensor["temperature"] = sensor["temperature"] / 0.01
    >>> sensor["temperature"] = (sensor["sensor_a"] + sensor["sensor_b"]) / 2
    >>> sensor["temperature"] = 0.01 * sensor["temperature"]
    """

    def __init__(self, name, connection):
        self.connection = connection
        self.name = name
        self.operator = Operators()
        self.operator.from_stream(name)
        self.key = list()
        self.executed = False
        self.query_id = None

        self.window = None
        self.window_key = None

        self.running = False

        self.function = None
        self.process_again = False

        self.batch_mode = False
        self.timeframe = 0
        self.timeframe_unit = "sec"
        self.on_time_over = False

        # tail
        self.n = None

        # configs
        self.timeout = 30000
        self.zmq_host = '127.0.0.1'
        self.zmq_port = 5555
        self.topic = ""
        self.brokers = ""
        self.timeout = 10000
        self.path = ""
        self.sink_type = Sink.ZMQSINK

    def set_timeout(self, timeout=30000):
        """
        Sets a max time for how long the user wants to wait for a tuple to arrive in the python pipeline.
        If the defined timeout is reached the NebulaStream Python Client stops the current query.

        Parameters
        ----------
        timeout : int

        Returns
        -------

        """
        self.timeout = timeout

    def set_zmq_configs(self, host='127.0.0.1', port=5555):
        """
        This function sets the ZMQ host and port if the default values are different from what the user needs.

        Parameters
        ----------
        host : str
        port : int

        Returns
        -------

        """
        self.zmq_host = host
        self.zmq_port = port

    def set_sink(self,
                 sink,
                 host='127.0.0.1',
                 port=5555,
                 topic="nespy",
                 brokers="",
                 timeout=10000,
                 path=""):
        if sink == Sink.ZMQSINK.value:
            self.sink_type = Sink.ZMQSINK
            self.zmq_host = host
            self.zmq_port = port
        elif sink == Sink.KAFKA.value:
            self.sink_type = Sink.KAFKA
            self.topic = topic
            self.brokers = brokers
            self.timeout = timeout
        elif sink == Sink.FILESINK.value:
            self.sink_type = Sink.FILESINK
            self.path = path
        elif sink == Sink.PRINT.value:
            self.sink_type = Sink.PRINT
        else:
            raise NotSupportedError("Your selected sink is not supported.")

    def __getitem__(self, *args):
        """
        Filter and select in one function.

        Parameters
        ----------
        args :
               If args a list or just one string it will result in select.
               Otherwise when we enter a predicate the filter operator gets called.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> # Filter
        >>> sensor[sensor["temperature"] > 3]
        >>> sensor[sensor["temperature"] < 3]
        >>> sensor[sensor["temperature"] <= 3]
        >>> sensor[sensor["temperature"] >= 3]
        >>> sensor[sensor["temperature"] == 3]
        >>> sensor[sensor["temperature"] != 3]
        >>> sensor[sensor["temperature"] > sensor["humidity"]
        >>> sensor[(sensor["temperature"] > 3) & (sensor["temperature"] < 15)]
        >>> sensor[(sensor["temperature"] < 3) | (sensor["temperature"] == 10)]

        >>> # Select
        >>> cars["car_id"]
        >>> # or
        >>> cars[["cars_id"]]
        >>> cars[["car_id", "speed", "lat", "lon"]]

        """
        for arg in args:
            if isinstance(arg, tuple) and len(arg) > 1:
                arg = list(arg)
                for a in arg:
                    self.key.append(a)
            elif isinstance(arg, LogicalOperator):
                self.operator.filter(arg)
                return self
            elif isinstance(arg, Wrapper) or isinstance(arg, list):
                self.operator.select(arg)
                return self
            else:
                key = list()
                key.append(arg)
                return Wrapper(key, self)

        return self

    def __setitem__(self, index, value):
        """
        Map function for the user.

        Parameters
        ----------
        index : str
                Attribute name.
        value : str or int or float
                New value that we want to set the attribute to.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor["temperature"] = sensor["temperature"] + 0.01
        >>> sensor["temperature"] = sensor["temperature"] - 0.01
        >>> sensor["temperature"] = sensor["temperature"] * 0.01
        >>> sensor["temperature"] = sensor["temperature"] / 0.01
        >>> sensor["temperature"] = (sensor["sensor_a"] + sensor["sensor_b"]) / 2
        >>> sensor["temperature"] = 0.01 * sensor["temperature"]

        """
        if isinstance(value, int) or isinstance(value, float):
            self.operator.map('Attribute(\"{}\") = {}'.format(index, value))
        elif isinstance(value, str) and value.startswith('Attribute'):
            self.operator.map('Attribute(\"{}\") = {}'.format(index, value))
        elif isinstance(value, str):
            self.operator.map('Attribute(\"{}\") = \"{}\"'.format(index, value))
        return self

    def rename(self, columns):
        """
        Renames the attribute name temporarily for the projection.

        Parameters
        ----------
        columns : dict
                  Columns that are renamed.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> cars = c.get_logical_stream("cars")
        >>>
        >>> cars["car_id"]
        >>> cars.rename(columns={"car_id":"id"})
        """
        self.operator.rename(columns)
        return self
        # raise NotSupportedError("This operator is currently not supported in NebulaStream.")

    # WINDOWS
    def groupby(self, by):
        self.window = Window(data_stream=self, on=by)
        return self.window


    def tumbling(self, on=None, event='timestamp', event_unit=None, size=0, lateness=0):
        """
        Tumbling window. The tumbling window has a length that is determined by the user. The length can
        either be a specific amount of time or a number of tuples. The tumbling window first fills itself up
        until the time or the number of tuples is reached. Then the window omit every tuple and starts filling up
        again. This technique allows to compute aggregation functions continuously on a small section of a
        data stream and in a disjoint fashion.

        Parameters
        ----------
        on : str
             Key for keyed window.
        event : str
                Declares event time (default value is 'timestamp').
        event_unit : str
                     Unit of size, can be min, sec, ms, and count.
        size : int
               Size of the window.
        size_unit : str
                    Unit of size, can be min, sec, ms, and count.
        lateness : int
                   Lateness of window.
        lateness_unit : str
                        Unit of lateness, can be min, sec, ms, and count.

        Returns
        -------
        DataStream

        Example
        ----------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> shop = c.get_logical_stream("shop")
        >>>
        >>> # keyed window
        >>> shop.tumbling(on="value", size=10, size_unit="sec").sum(on="sales")

        >>> # global window
        >>> shop.tumbling(size=10, size_unit="sec").sum(on="sales")
        """
        if on is not None:
            if len(on) == 1:
                self.window_key = on[0]
            else:
                InvalidSyntaxError("We do not support aggregations on multiple attributes.")
        self.window = Window(data_stream=self)
        self.window.tumbling(size, event, event_unit, lateness)
        # checks whether last operator was a join. If so, we append it
        self.operator.window_join(self.window)
        return self

    def sliding(self, on=None, event='timestamp', event_unit=None, size=0, slide=0, lateness=0):
        """
        Sliding window. A sliding window has a fixed length that is determined by the user. This length can either
        be an amount of time or a number of tuples. Furthermore, the sliding window has a slide value. This slide
        value is also determined by the user and tells the window how often it should update the window, in
        particular when the sliding window slides over the data stream.

        Parameters
        ----------

        on : str
             Key for keyed window.
        event : str
                Declares event time (default value is 'timestamp').
        event_unit : str
                     Unit of event. Can be min, sec, ms, and count.
        size : int
               Size of the window.
        size_unit : str
                    Unit of size. Can be min, sec, ms, and count.
        slide : int
                Update frequency of sliding window.
        slide_unit : str
                     Unit of slide, same as size_unit.
        lateness : int
                   Lateness of window.
        lateness_unit : str
                        Unit of lateness. Can be min, sec, ms, and count.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> shop = c.get_logical_stream("shop")
        >>>
        >>> # keyed window
        >>> shop.sliding(on="sales", size=10, size_unit="sec", slide=5, slide_unit="sec").sum(on="sales")

        >>> # global window
        >>> shop.sliding(size=10, size_unit="sec", slide=5, slide_unit="sec").sum(on="sales")

        """
        if on is not None:
            if len(on) == 1:
                self.window_key = on[0]
            else:
                InvalidSyntaxError("We do not support aggregations on multiple attributes.")
        self.window = Window(data_stream=self)
        self.window.sliding(size, slide, event, event_unit, lateness)
        # checks whether last operator was a join. If so, we append it
        self.operator.window_join(self.window)
        return self

    def sum(self, name=""):
        """
        Aggregation function sum for the window.

        Parameters
        ----------
        name : str
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> shop = c.get_logical_stream("shop")
        >>>
        >>> shop.sliding(on="purchases", size=10, size_unit="sec", slide=5, slide_unit="sec")
        >>>     .sum(on="purchases", name="")


        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            if self.window_key is not None:
                self.window.aggregate_on = self.window_key
            self.window.sum(name=name)
            self.operator.compact_window(self.window)
        return self

    def count(self, name=""):
        """
        Aggregation function count for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> cars = c.get_logical_stream("cars")
        >>>
        >>> cars.sliding(on="color", size=10, size_unit="sec", slide=5, slide_unit="sec").max(name="")


        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            self.window.count(name=name)
            self.operator.compact_window(self.window)
        return self

    def avg(self, name=""):
        """
        Aggregation function avg for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").avg(on="temperature")


        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            if self.window_key is not None:
                self.window.aggregate_on = self.window_key
            self.window.avg(name=name)
            self.operator.compact_window(self.window)
        return self

    def min(self, name=""):
        """
        Aggregation function min for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").min(on="temperature")

        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            if self.window_key is not None:
                self.window.aggregate_on = self.window_key
            self.window.min(name=name)
            self.operator.compact_window(self.window)
        return self

    def max(self, name=""):
        """
        Aggregation function max for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").max(on="temperature")

        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            if self.window_key is not None:
                self.window.aggregate_on = self.window_key
            self.window.max(name=name)
            self.operator.compact_window(self.window)
        return self

    def median(self, name=""):
        """
        Aggregation function max for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.groupby("temperature")["temperature"].sliding(size="10s", slide="5s").median()

        """
        if self.window is None:
            raise InvalidSyntaxError("A window is missing.")
        else:
            if self.window_key is not None:
                self.window.aggregate_on = self.window_key
            self.window.median(name=name)
            self.operator.compact_window(self.window)
        return self

    def union(self, other_stream):
        """
        Union unites two data streams with the same schema.

        Parameters
        ----------
        other_stream : DataStream

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>>
        >>> bus = c.get_logical_stream("bus")
        >>> cars = c.get_logical_stream("car")
        >>> bus.union(car)

        """
        if isinstance(other_stream, DataStream):
            self.operator.union(self.name, other_stream)
        else:
            raise InvalidSyntaxError("The syntax is incorrect")
        return self

    def join(self, other_stream, on=None, left_on=None, right_on=None):
        """
        Join works just like JOIN in SQL or the theta join in relational algebra.
        If both of the data streams have an attribute with the same name, we can set the parameter "on".
        Otherwise, we have to set the parameter "left_on" and "right_on".

        Parameters
        ----------
        other_stream : DataStream
                       The other data stream we want to join the current data stream with.
        on : str, optional
             Common attribute to join on.
        left_on : str, optinal
                  Attribute of the left data stream to join the right attribute with.
        right_on : str, optional
                   Attribute of the right data stream to join the left attribute with.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> position = c.get_logical_stream("car_position")
        >>> details = c.get_logical_stream("car_details")
        >>> position.join(details, left_on="id", right_on="car_id")

        >>> purchases = get_logical_stream("purchases")
        >>> products = c.get_logical_stream("products")
        >>> purchases.join(products, on="product_id")


        """
        if isinstance(other_stream, DataStream):
            self.operator.join(self.name, other_stream, on, left_on, right_on)
        else:
            raise InvalidSyntaxError("The syntax is incorrect")
        return self

    def _create_query(self):
        """
        Creates query string for NebulaStream.

        Returns
        -------
        str

        """
        if self.sink_type == Sink.ZMQSINK:
            self.operator.zmq_sink(self.zmq_host, self.zmq_port)
        elif self.sink_type == Sink.KAFKA:
            self.operator.kafka_sink(self.topic, self.brokers, self.timeout)
        elif self.sink_type == Sink.PRINT:
            self.operator.print_sink()
        elif self.sink_type == Sink.FILESINK:
            self.operator.file_sink(self.path)
        return self.operator.create_query()

    def reset_operators(self):
        """
        Deletes all operators that have been called and deletes the current running query.

        Returns
        -------

        """
        self.operator = Operators()
        self.operator.from_stream(self.name)
        self.executed = False
        self.connection.stop_query(self.query_id)
        self.query_id = None

    def _execute_query(self, query):
        """
        Executes query in NebulaStream.

        Parameters
        ----------
        query : str
                Translated query for NebulaStream.

        Returns
        -------

        """
        try:
            self.executed = True
            self.query_id = self.connection.execute_query(query, self.operator.strategy)["queryId"]
        except WrongQueryError as e:
            print(e)

    def zmq_sink(self, host, port):
        """
        Zmq sink for NebulaStream.

        Parameters
        ----------
        host : str
               Host where zmq is running
        port : int
               Port of ZMQ. This is not the same as connection with NebulaStream.

        Returns
        -------
        DataStream

        """
        self.zmq_host = host
        self.zmq_port = port
        self.operator.zmq_sink(host, port)
        return self

    def print_sink(self):
        """
        Prints the data in your terminal where NebulaStream is running.

        Returns
        -------
        DataStream

        """
        self.operator.print_sink()
        return self

    def __str__(self):
        """
        Creates a string of the object DataStream.

        Returns
        -------
        str

        """
        query = self._create_query()
        return str(self._execute_query(query))

    def _repr_html_(self):
        """
        Sends query and creates the output.

        Returns
        -------
        str
            This string is a table in HTML.

        """
        stringio = self._create_stringio_and_header()
        return self._get_data_from_nes(stringio=stringio, n=self.n)

    def _get_data_from_nes(self,
                           stringio=None,
                           plot_buffer=None,
                           plot_data=False,
                           get_column="",
                           n=None):
        """
        This function requests data from NebulaStream

        Parameters
        ----------
        stringio : stringio
                   This is a stringio to write the results as an HTML table into it.
        batch_mode : bool
                     Whether this function is called in the batch mode or not.
        timeframe : int
                    Timeframe for when the batch mode is activated.
        timeframe_unit : str
                         Unit for the timeframe. Only accept 'sec', 'min', and 'h'.
        on_time_over : bool
                       When to trigger the batch function. If True then only after the timeframe is reached. Otherwise,
                       every time a tuple enters the buffer in the batch mode.
        batch_function : function
                         The user defined batch function.
        plot_buffer: Buffer
        plot_data: Boolean
        get_column: String

        Returns
        -------
        str
            Depending on what was chosen in the parameters it returns the data stream as an HTMl or the result
            of the buffer function.


        Notes
        -------
        The response of NebulaStream consists of four messages:
        1 (is when counter == 1) length of 2nd message
        2 schema of data
        3 length of 4th message
        4 data

        Then message 3 and 4 repeat until someone stops the query.

        """

        # prepare zmq
        context = zmq.Context()
        url = "tcp://{}:{}".format(self.zmq_host, self.zmq_port)
        socket = context.socket(zmq.PULL)
        socket.bind(url)

        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)

        # execute query in nes
        query = self._create_query()
        self._execute_query(query)
        self.running = True
        counter = 0

        serializable_schema = pb.SerializableSchema()
        number = 0
        rows = 0
        col = 0
        details = list()
        details_dict = dict()
        batch_buffer = pd.DataFrame()
        batch_result = pd.DataFrame()

        accepted_timeframe_unit = {
            'sec': 1,
            'min': 60,
            'h': 60 * 60
        }

        transformed_timeframe = self.timeframe * accepted_timeframe_unit[
            self.timeframe_unit]  # transforms into milliseconds
        start = time.perf_counter()  # measures time in seconds

        no_of_elements_arriving = 0

        last_n_values = list()
        while self.running:
            try:
                timeout = dict(poller.poll(self.timeout))
                if not timeout:
                    raise KeyboardInterrupt

                else:
                    message = socket.recv()

                    if len(message) > 0:
                        counter += 1
                    if counter == 1:
                        # first message
                        # read how many bytes long the schema message is
                        number = int.from_bytes(message[0:4], byteorder='little', signed=True)
                    elif counter == 2:
                        # second message
                        # schema of the result
                        message = message[0:number]
                        serializable_schema.ParseFromString(message)

                        col = len(serializable_schema.fields)  # wie viele Spalten die Tabelle haben wird

                        for i in range(col):
                            if stringio is not None:
                                _write_header(stringio, serializable_schema.fields[i].name)

                            det = _types_details(serializable_schema.fields[i].type.details.type_url,
                                                 serializable_schema.fields[i].type.details.value)
                            details.append(det)

                            details_dict[serializable_schema.fields[i].name] = det
                        if stringio is not None:
                            stringio.write('</tr>')
                            stringio.write('</table>')
                    elif counter == 3 or counter % 2 == 1:
                        # third message
                        # length of the fourth message
                        if stringio is not None:
                            current_value = stringio.getvalue()
                            current_value = current_value[:-8]  # removes </table>

                            stringio = io.StringIO()
                            stringio.write(current_value)
                        rows = int.from_bytes(message[0:4], byteorder='little', signed=True)

                    else:
                        # fourth message
                        # data
                        cols = col + 1  # 2+1
                        byte_length = cols * 4

                        bytes_per_row = _how_many_bytes_per_row(details_dict.items())
                        column_names = list(details_dict.keys())
                        # iterating through each row
                        for i in range(rows):
                            one_row_byte = message[i * bytes_per_row:(i + 1) * bytes_per_row]
                            # data is a list of just the values (for just regular displayment)
                            # dictionary is the data but as key value pairs (for batch and processing)
                            # (key = name of attribute, value= actual value)
                            data, dictionary = _byte_row_to_string(details, one_row_byte, column_names)

                            plot_result = dictionary
                            # checking which mode the user has chosen
                            if self.batch_mode and self.function is not None:
                                # adding to batch buffer and assuming order variables don't change
                                batch_buffer = batch_buffer.append(dictionary, ignore_index=True)
                                current_time = time.perf_counter()
                                if self.on_time_over:
                                    if current_time - start < transformed_timeframe:
                                        continue
                                    else:
                                        batch_result, plot_result = self._process_in_batches_with_dataframe(
                                            batch_function=self.function, data_frame=batch_buffer,
                                            batch_result=batch_result)
                                        start = time.perf_counter()
                                        batch_buffer = pd.DataFrame()
                                else:
                                    # process data buffer
                                    batch_result, plot_result = self._process_in_batches_with_dataframe(
                                        batch_function=self.function, data_frame=batch_buffer,
                                        batch_result=batch_result)
                            elif not (self.function is None) and not self.batch_mode:
                                # is user set a function in process
                                # process the function
                                result = self.function(dictionary)
                                if result is not None:
                                    if not isinstance(result, dict):
                                        raise NotSupportedError("You have to return a dictionary.")
                                    else:
                                        if counter == 4 and i == 0:
                                            # if it was the very first message and the first data
                                            stringio = self._create_stringio_and_header()
                                            for key in list(result.keys()):
                                                _write_header(stringio, key)
                                        data = list(result.values())
                                        plot_result = result

                            # if we want to plot the data in a graph
                            if plot_data:
                                temporary_df = None
                                if isinstance(plot_result, dict):
                                    temporary_df = pd.DataFrame([plot_result])
                                    temporary_df.index = [(i + no_of_elements_arriving)]
                                elif isinstance(plot_result, pd.DataFrame):
                                    temporary_df = plot_result
                                else:
                                    raise NotSupportedError("We only support dict and pd.DataFrame.")
                                # send to plot buffer to display plot
                                plot_buffer.send(temporary_df[get_column].to_frame())

                            # check whether tail has been used
                            if n is not None and not self.batch_mode and not plot_data:
                                if len(last_n_values) >= n:
                                    del last_n_values[0]  # remove first element if n is reached
                                last_n_values.append(data)  # add new data to last n values

                            # check whether user just wants to display but is not batch mode or plot mode
                            if stringio is not None and not self.batch_mode:
                                current_index = (i + no_of_elements_arriving)
                                if n is not None:
                                    # if n is set we iterate through the last n data and write it to the stringio
                                    stringio = self._create_stringio_and_header()
                                    for key in column_names:
                                        _write_header(stringio, key)
                                    if current_index >= n:
                                        for index_of_row, list_index in zip(
                                                range(current_index - n + 1, current_index + 1), range(n)):
                                            _write_data(stringio, last_n_values[list_index], index_of_row)
                                    else:
                                        for index_of_row in range(len(last_n_values)):
                                            _write_data(stringio, last_n_values[index_of_row], index_of_row)
                                else:
                                    # if n is not set just write the current data to the stringio
                                    _write_data(stringio, data, current_index)
                        no_of_elements_arriving += rows

                        # display batch result
                        if plot_data:
                            # ignore the rest of the code and go back to the beginning
                            continue
                        elif len(batch_result) > 0:
                            if n is not None:
                                # display batch tail
                                display(batch_result.tail(n))
                            else:
                                # display everything
                                display(batch_result)
                            clear_output(wait=True)

                        #  general display of a data stream but not batch
                        # I have to seperate this because the batch results are pandas data frame and the rest are just
                        # strings written into the string io
                        if stringio is not None and not self.batch_mode:
                            stringio.write('</table>')
                            display(HTML(stringio.getvalue()))
                            clear_output(wait=True)

            except KeyboardInterrupt:
                self.stop_query()
                socket.close(0)
                context.destroy(0)
                context.term()
            except Exception as e:
                self.stop_query()
                socket.close(0)
                context.destroy(0)
                context.term()
        if self.batch_mode:
            if n is not None:
                return batch_result.tail(n).to_html()
            else:
                return batch_result.to_html()
        else:
            if stringio is not None:
                return stringio.getvalue()

    def _create_stringio_and_header(self):
        stringio = io.StringIO()
        stringio.write('<table border=\"1\" class=\"dataframe\">      <tr style=\"text-align: right;\"> <th></th>')
        return stringio

    def _process_in_batches_with_dataframe(self, batch_function, data_frame, batch_result):
        """
        This function computes the batch function on the created batch.

        Parameters
        ----------
        batch_function : function
        data_frame : DataFrame
        batch_result : pandas dataframe

        Returns
        -------
        DataFrame
        """

        result_from_this_batch = batch_function(data_frame)
        result_from_this_batch.index += len(batch_result)
        batch_result = batch_result.append(result_from_this_batch, ignore_index=True)
        return batch_result, result_from_this_batch

    def stop_query(self):
        """
        This function stops a query. Once a query is stopped it cannot rerun again. The user has to run a new
        query.

        Returns
        -------

        """
        self.running = False
        self.connection.stop_query(self.query_id)

    def tail(self, n=5):
        self.n = n
        return self

    def plot(self, column, width=900, height=400, show_grid=True):
        """

        Parameters
        ----------
        column: String
                Name of the column. In the case of the plot it is the y axis label because the x axis is the index in the DataFrame.
                User has to chose the attribute that needs to be displayed.
        width: int
               Width of the plot.
        height: int
               Height of the plot.
        show_grid: Boolean
                   Whether plot should have a grid or not.

        Returns
        -------

        """
        hv.extension('bokeh')
        # create an empty df and make a buffer out of it
        # when we receive the data from nes we send the data to this buffer
        df = pd.DataFrame({column: []}, columns=[column])
        plot_buffer = Buffer(df)
        # this is the actual plot
        plot = hv.DynamicMap(hv.Curve, streams=[plot_buffer]).opts(width=width, height=height, show_grid=show_grid)
        # display plot
        hv.output(plot, fig='png')
        # receive data for the plot
        self._get_data_from_nes(plot_data=True, plot_buffer=plot_buffer, get_column=column)

    def process(self, function):
        """
        This function enables user to compute their own defined python function (one tuple at a time).

        Parameters
        ----------
        function : function
                   Function that can process one tuple at a time.

        Returns
        -------

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> data_stream = c.get_logical_stream("data_stream")
        >>>
        >>> def myfunction(data):
        >>>     #do something with a single tuple
        >>>     return data
        >>> data_stream.process(myfunction)

        """
        self.function = function
        return self

    def batch(self, function, timeframe=10, timeframe_unit='min', on_time_over=True):
        """
        This function enables user to compute their user defined function on a batch of the data stream.

        Parameters
        ----------

        function : function
                         User defined batch function. This function has to return the desired results.
        timeframe : int
                    Defines the timeframe over which the stream is buffered.
        timeframe_unit : str
                         Unit of the timeframe.
        on_time_over : bolean
                       Defines when the batch function is called.
                       If this value is True we call the batch function once the time is up.
                       Otherwise, if this value is False we call the batch function when a new record is
                       added to the buffer.

        Returns
        -------

        Examples
        -------
        >>> def calculate_mean_for_all_columns(data_frame):
        >>>     return data_frame.mean()
        >>> cars.batch(calculate_mean_for_all_columns, timeframe=10, timeframe_unit='min', on_time_over=False)

        """
        if not isinstance(on_time_over, bool):
            raise InvalidSyntaxError("This batch mode does not exists. Has to be type of Boolean.")

        all_timeframe_units = ['sec', 'min', 'h']
        if timeframe_unit in all_timeframe_units:
            self.batch_mode = True
            self.timeframe = timeframe
            self.timeframe_unit = timeframe_unit
            self.on_time_over = on_time_over
            self.function = function
            return self
        else:
            raise InvalidSyntaxError("Invalid Syntax! This unit does not exist. ")


class Window:
    def __init__(self, data_stream, on=None, aggregate_on=""):
        self.on = on
        self.data_stream = data_stream
        self.window = None
        self.aggregate_on = aggregate_on

    def __getitem__(self, item):
        if isinstance(item, str):
            self.aggregate_on = item
            return self
        elif isinstance(item, tuple) or isinstance(item, list):
            raise InvalidSyntaxError("You can only group by one attribute.")
        else:
            raise InvalidSyntaxError("The name of the attribute has to be a string.")

    def sliding(self, size, slide, event="timestamp", event_unit=None, lateness=0):
        size, *size_unit = re.findall('(\d+|[A-Za-z]+)', str(size))
        slide, *slide_unit = re.findall('(\d+|[A-Za-z]+)', str(slide))
        lateness, *lateness_unit = re.findall('(\d+|[A-Za-z]+)', str(lateness))

        if len(size_unit) == 0:
            size_unit = "count"
        else:
            size_unit = size_unit[0]

        if len(slide_unit) == 0:
            size_unit = "count"
        else:
            slide_unit = slide_unit[0]

        if len(lateness_unit) == 0:
            lateness_unit = "count"
        else:
            lateness_unit = lateness_unit[0]

        self.window = WindowsTransformer(name='SlidingWindow', on=self.on, event=event, event_unit=event_unit,
                                         size=int(size),
                                         size_unit=size_unit,
                                         slide=int(slide),
                                         slide_unit=slide_unit, lateness=int(lateness), lateness_unit=lateness_unit)
        return self.data_stream

    def tumbling(self, size, event="timestamp", event_unit=None, lateness=0):
        size, *size_unit = re.findall('(\d+|[A-Za-z]+)', str(size))
        lateness, *lateness_unit = re.findall('(\d+|[A-Za-z]+)', str(lateness))

        if len(size_unit) == 0:
            size_unit = "count"
        else:
            size_unit = size_unit[0]

        if len(lateness_unit) == 0:
            lateness_unit = "count"
        else:
            lateness_unit = lateness_unit[0]

        self.window = WindowsTransformer(name='TumblingWindow', on=self.on, event=event, event_unit=event_unit,
                                         size=int(size),
                                         size_unit=size_unit,
                                         lateness=int(lateness), lateness_unit=lateness_unit)
        return self.data_stream

    def sum(self, name=""):
        """
        Aggregation function sum for the window.

        Parameters
        ----------
        name : str
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> shop = c.get_logical_stream("shop")
        >>>
        >>> shop.sliding(on="purchases", size=10, size_unit="sec", slide=5, slide_unit="sec")
        >>>     .sum(on="purchases", name="")


        """
        if len(self.aggregate_on) == 0:
            raise InvalidSyntaxError("There is no attribute to aggregate on")
        else:
            self.window.aggr_func(agg_type='Sum', on=self.aggregate_on, name=name)
        return self.data_stream

    def count(self, name=""):
        """
        Aggregation function count for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> cars = c.get_logical_stream("cars")
        >>>
        >>> cars.sliding(on="color", size=10, size_unit="sec", slide=5, slide_unit="sec").max(name="")


        """
        self.window.aggr_func(agg_type="Count", on="", name=name)
        return self.data_stream

    def avg(self, name=""):
        """
        Aggregation function avg for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").avg(on="temperature")


        """
        if len(self.aggregate_on) == 0:
            raise InvalidSyntaxError("There is no attribute to aggregate on")
        else:
            self.window.aggr_func(agg_type="Avg", on=self.aggregate_on, name=name)
        return self.data_stream

    def min(self, name=""):
        """
        Aggregation function min for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").min(on="temperature")

        """
        if len(self.aggregate_on) == 0:
            raise InvalidSyntaxError("There is no attribute to aggregate on")
        else:
            self.window.aggr_func(agg_type="Min", on=self.aggregate_on, name=name)
        return self.data_stream

    def max(self, name=""):
        """
        Aggregation function max for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.sliding(on="temperature", size=10, size_unit="sec", slide=5, slide_unit="sec").max(on="temperature")

        """
        if len(self.aggregate_on) == 0:
            raise InvalidSyntaxError("There is no attribute to aggregate on")
        else:
            self.window.aggr_func(agg_type="Max", on=self.aggregate_on, name=name)
        return self.data_stream

    def median(self, name=""):
        """
        Aggregation function max for the window.

        Parameters
        ----------
        name : str, optional
               How to call the column.

        Returns
        -------
        DataStream

        Examples
        -------
        >>> c = nes.Connection("127.0.0.1", 8081)
        >>> sensor = c.get_logical_stream("sensor")
        >>>
        >>> sensor.groupby("temperature")["temperature"].sliding(size="10s", slide="5s").median()

        """
        if len(self.aggregate_on) == 0:
            raise InvalidSyntaxError("There is no attribute to aggregate on")
        else:
            self.window.aggr_func(agg_type="Median", on=self.aggregate_on, name=name)
        return self.data_stream

    def create_window_query(self):
        return self.window.create_window_query()
