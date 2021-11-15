from nespy.wrapper import *
from nespy.exceptions import *


class Operators:
    """
    This class manages all the operators and translates the query into NebulaStream's Query API syntax.
    """

    def __init__(self):
        self.operator_list = list()
        self.strategy = "BottomUp"

        self.current_window = None

    def from_stream(self, logical_stream_name):
        """
        Identifies on which data stream the user wants to work on.
        This function just adds "Query::from(stream)" to the operator_list.

        Parameters
        ----------
        logical_stream_name : str
                              Name of the logical stream we are working on.

        Returns
        -------
        Operators

        """
        self.operator_list.append("Query::from(\"{}\")".format(logical_stream_name))
        return self

    def filter(self, predicate):
        """
        Filters according to a filter predicate.
        This function adds ".filter(Attribute(a)" to the operator_list. "a" is the filter predicate.

        Parameters
        ----------
        predicate : str
                    Is then added to the fitting string to send a filter query. This string is then added to the list of
                    operators.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".filter({})".format(predicate))
        return self

    def map(self, arg):
        """
        Maps a certain value of the data stream to a new defined value.
        This function adds ".map(a)" whereas a is the mapping expression.
        For example "Attribute("a") = Attribute("a") + 1".

        Parameters
        ----------
        arg : str
              Python map operator already translated into the NebulaStream syntax.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".map({})".format(arg))
        return self

    def select(self, arg):
        """
        Selects an attribute. Like SELECT in SQl or projection in relational algebra.
        This function adds ".project(a)" to the operator_list. The value a is the attribute to project on.

        Parameters
        ----------
        arg : str or list
              List of attributes or Wrapper (if it's just one attribute we want to filter).

        Returns
        -------
        Operators

        """
        if isinstance(arg, Wrapper):
            self.operator_list.append(".project(Attribute(\"{}\"))".format(arg.key[0]))
        elif isinstance(arg, list) & (len(arg) > 0):
            attributes = ""
            for a in arg:
                attributes += "Attribute(\"{}\"), ".format(a)
            attributes = attributes[:-2]  # remove comma and whitespace at the end
            self.operator_list.append(".project({})".format(attributes))

        return self

    def rename(self, arg):
        """
        Renames the columns after a projection.
        This function adds ".rename(a)" to the operator_list after a projection. This a is the new name for the
        projected attribute.

        Parameters
        ----------
        arg : dict
              Keys are the old names of the data stream and the value the new names for this column.

        Returns
        -------
        Operators

        """
        if self.operator_list[-1].startswith(".project"):
            current_project = self.operator_list[-1]
            self.operator_list = self.operator_list[:-1]
            if isinstance(arg, dict):
                for key in arg:
                    new_name = ".as(\"{}\")".format(arg[key])
                    key_start_index = current_project.index(key)
                    key_end_index = key_start_index + len(key) + 2
                    insert_rename_into_string = current_project[:key_end_index]
                    insert_rename_into_string += new_name
                    insert_rename_into_string += current_project[key_end_index:]
                    current_project = insert_rename_into_string
                self.operator_list.append(current_project)
        else:
            raise WrongQueryError("You can only use rename right after the projection.")
        return self

    def zmq_sink(self, host, port):
        """
        ZMQ Sink for NES.
        This function adds the zmq sink to the operator_list.

        Parameters
        ----------
        host : str
               Destination host (probably localhost for now).
        port : int
               Destination port.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".sink(ZmqSinkDescriptor::create(\"{}\", {}))".format(host, port))
        return self

    def print_sink(self):
        """
        This function adds the a print sink into the operator_list of this class.
        A print sink prints data in terminal.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".sink(PrintSinkDescriptor::create())")
        return self

    def file_sink(self, path):
        """
        This function adds the a file sink into the operator_list of this class.
        A file sink prints data in a file found in the given path.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".sink(FileSinkDescriptor::create(\"{}\"))".format(path))
        return self

    def kafka_sink(self, topic, brokers, timeout):
        """
        This function adds the a print sink into the operator_list of this class.
        A print sink prints data in terminal.

        Returns
        -------
        Operators

        """
        self.operator_list.append(".sink(KAFKASinkDescriptor::create(\"{}\", \"{}\", {}))".format(topic, brokers,
                                                                                                  timeout))
        return self

    def compact_window(self, window):
        self.operator_list.append(window.create_window_query())
        return self

    def window(self, window):
        """
        Adds query to create any window.

        Parameters
        ----------
        window :  WindowsTransformer
                  Window object that manages window type, parameters of window, aggregation function and create query
                  for the window.

        Returns
        -------
        Operators

        """
        self.current_window = window
        # self.operator_list.append(self.current_window.create_window_query())
        return self

    def aggr_func(self, aggr_type, on, name=""):
        """
        Adds aggregation functions to operators.
        Only works if a window has been selected or the window was the last one.

        Parameters
        ----------
        aggr_type : str
                    Type of aggregation function.
        on : str
             On which attribute to aggregate.
        name : str, optional
               Name of the new column.

        Returns
        -------
        Operators

        """
        if self.current_window is not None:
            self.current_window.aggr_func(aggr_type, on=on, name=name)
            # self.operator_list = self.operator_list[:-1]
            self.operator_list.append(self.current_window.create_window_query())
        else:
            raise InvalidSyntaxError("The syntax is incorrect")
        return self

    def union(self, left_stream_name, right_stream):
        """
        This function adds the union operator into the operator_list of this class.

        Parameters
        ----------
        left_stream_name : str
        right_stream : DataStream

        Returns
        -------
        Operators

        """
        complete_query = ""
        left_query = ''.join(self.operator_list)
        # auto cars = Query::from("cars").project(Attribute("f1"));
        complete_query += "auto " + left_stream_name + " = " + left_query + ";\n"
        right_query = ''.join(right_stream.operator.operator_list)
        # auto bikes = Query::from("bikes").project(Attribute("f1"));
        complete_query += "auto " + right_stream.name + " = " + right_query + ";\n"
        # cars.unionWith(bikes)
        complete_query += left_stream_name + ".unionWith(" + right_stream.name + ")"
        self.operator_list = []
        self.operator_list.append(complete_query)
        return self

    def join(self, left_stream_name, right_stream, on=None, left_on=None, right_on=None):
        """
        This function adds the join operator into the operator_list of this class.
        Join works just like JOIN in SQL or the theta join in relational algebra.
        If both of the data streams have an attribute with the same name, we can set the parameter "on".
        Otherwise, we have to set the parameter "left_on" and "right_on".

        Parameters
        ----------
        left_stream_name : str
                           Name of the left stream.
        right_stream : DataStream
                Stream on the right side of the join.
        on : str, optional
             Parameter to join on if they are both the same.
        left_on : str, optional
                  Parameter on the left side to join on in case the parameters to join on are named differently.
        right_on : str, optional
                   Parameter on the right side to join on in case the parameters to join on are named differently.
        Returns
        -------
        Operators

        """
        complete_query = ""
        left_query = ''.join(self.operator_list)
        # auto purchases = Query::from("purchases");
        complete_query += "auto " + left_stream_name + " = " + left_query + ";\n"
        right_query = ''.join(right_stream.operator.operator_list)
        # auto tweets = Query::from("tweets");
        complete_query += "auto " + right_stream.name + " = " + right_query + ";\n"
        # purchases.joinWith(tweets)
        complete_query += left_stream_name + ".joinWith(" + right_stream.name + ")"

        if on is not None:
            complete_query += ".where(Attribute(\"{}${}\")).equalsTo(Attribute(\"{}${}\"))".format(left_stream_name,
                                                                                                   on,
                                                                                                   right_stream.name,
                                                                                                   on)
        elif (left_on is not None) and (right_on is not None):
            complete_query += ".where(Attribute(\"{}${}\")).equalsTo(Attribute(\"{}${}\"))".format(left_stream_name,
                                                                                                   left_on,
                                                                                                   right_stream.name,
                                                                                                   right_on)
        else:
            raise InvalidSyntaxError("No attribute to join on")
        self.operator_list = []
        self.operator_list.append(complete_query)
        return self

    def window_join(self, window):
        if "joinWith" in self.operator_list[-1]:
            if isinstance(window.window, WindowsTransformer):
                self.operator_list.append(window.create_window_query())
        return self

    def create_query(self):
        """
        Creates query by joining all operators and finishing the string with the zmq sink.

        Parameters
        ----------
        host : str
        port : int

        Returns
        -------
        query : str

        """
        query = ''.join(self.operator_list)
        query += ";"
        return query

    def remove_last_operator(self):
        self.operator_list.pop()


class WindowsTransformer:
    """
    manages the strings we create in DataStream.
    """

    def __init__(self, name, on=None, event='timestamp', event_unit='sec', size=0, size_unit='sec', slide=0,
                 slide_unit='sec', lateness=0,
                 lateness_unit='sec'):
        self.name = name
        self.on = on
        self.event = event
        self.event_unit = event_unit
        self.size = size
        self.size_unit = size_unit
        self.slide = slide
        self.slide_unit = slide_unit
        self.lateness = lateness
        self.lateness_unit = lateness_unit
        self.aggregation = list()

    def aggr_func(self, agg_type, on, name=""):
        """
        Creates the string for any aggregation function.

        Parameters
        ----------
        agg_type : str
                   Name of aggregation.
        on : str
             On which attribute to aggregate.
        name : str
               How to call the aggregation column.

        Returns
        -------
        self

        """
        agg_query = ".apply({}())".format(agg_type)
        if len(on) > 0:
            agg_query = ".apply({}(Attribute(\"{}\")))".format(agg_type, on)
        if len(name) != 0:
            agg_query = agg_query[:-1] # remove last ")"
            agg_query += "->as(Attribute(\"{}\")))".format(name)
            # raise NotSupportedError("NebulaStream does not support renaming columns when aggregating at the moment.")
        self.aggregation.append(agg_query)
        return self

    def create_window_query(self):
        """
        Creates all different string representation of windows.

        Returns
        -------
        query : str
                This is the window operator as a string.

        Notes
        -------
        From the NebulaStream documentation:

        Global Window
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .apply(Sum(Attribute("f2")));

        Tumbling window
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Sum(Attribute("f2")));

        Sliding window with window size of 10 ms and slide size 5 ms
        stream.window(SlidingWindow::of(EventTime(Attribute("timestamp")), Milliseconds(10), Milliseconds(5)))
                        .byKey(Attribute("f2"))
                        .apply(Sum(Attribute("f2")));

        Aggregation field naming
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Sum(Attribute("f2")))
                        .as(Attribute("sum_f2"));
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Max(Attribute("f2")))
                        .as(Attribute("max_f2"));
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Min(Attribute("f2")))
                        .as(Attribute("min_f2"));
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Count())
                        .as(Attribute("count_f2"));

        Keyed window
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp")), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Sum(Attribute("f2")));

        Specify timestamp unit
        stream.window(TumblingWindow::of(EventTime(Attribute("timestamp"), Seconds()), Seconds(10)))
                        .byKey(Attribute("f2"))
                        .apply(Sum(Attribute("f2")));

        """
        size_units_options = {
            "count": "Count",
            "Count": "Count",
            "ms": "Milliseconds",
            "millis": "Milliseconds",
            "milliseconds": "Milliseconds",
            "sec": "Seconds",
            "s": "Seconds",
            "second": "Seconds",
            "seconds": "Seconds",
            "min": "Minutes",
            "minute": "Minutes",
            "minutes": "Minutes",
            "m": "Minutes",
            "hours": "Hours",
            "hour": "Hours",
            "hr": "Hours",
            "h": "Hours",
        }
        transformed_event_unit = ""
        if self.event_unit is not None:
            transformed_event_unit = ', ' + size_units_options[self.event_unit] + '()'

        # window.(TumblingWindow::of(
        query = '.window({}::of(EventTime(Attribute(\"{}\"){}), '.format(self.name, self.event, transformed_event_unit)
        if self.size >= 0:
            # Seconds(10)
            query += '{}({})'.format(size_units_options[self.size_unit], self.size)
        if self.name == "SlidingWindow" and self.slide > 0:
            # , Milliseconds(5)
            query += ', {}({})'.format(size_units_options[self.slide_unit], self.slide)
        if self.lateness > 0:
            # Lateness(Seconds(10))
            query += ', Lateness({}({}))'.format(size_units_options[self.lateness_unit], self.lateness)
        query += '))'  # end ) of "WindowType::of()

        if (self.on is not None) and isinstance(self.on, str):
            # .windowByKey(Attribute("f2"), TumblingWindow::of(EventTime(Attribute("timestamp")),
            query += '.byKey(Attribute(\"{}\"))'.format(self.on)

        if len(self.aggregation) > 0:
            query += ' '.join(self.aggregation)
        return query
