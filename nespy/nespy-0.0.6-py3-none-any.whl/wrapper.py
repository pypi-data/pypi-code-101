import nespy.datastream as ds
from nespy.logicaloperators import *
from nespy.exceptions import *


class Wrapper:
    """
    Wrapper has all the necessary functions to perform mathematical and logical operators
    it therefore wraps the values into LogicalOperator, which creates the correct string.
    This class is mainly needed to distinguish between filter and select.
    """

    def __init__(self, key, data_stream):
        self.key = key
        self.data_stream = data_stream

    def tumbling(self, event='timestamp', event_unit=None, size=0, lateness=0):
        return self.data_stream.tumbling(on=self.key, event=event, event_unit=event_unit, size=size, lateness=lateness)

    def sliding(self, event='timestamp', event_unit=None, size=0, slide=0, lateness=0):
        return self.data_stream.sliding(on=self.key, event=event, event_unit=event_unit, size=size, slide=slide, lateness=lateness)

    def __lt__(self, other):
        """
        Manages '<' of DataStream.

        Parameters
        ----------
        other : int or float or DataStream
                If we have, e.g., DataStream["attribute"] < 1 then other is the 1. It is just the data type that is not
                DataStream.

        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) < LogicalOperator(str(other))
            elif isinstance(other, float):
                return LogicalOperator(self.key[0]) < LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) < LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) < LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __le__(self, other):
        """
        Manages '<=' of DataStream.

        Parameters
        ----------
        other : int or float or DataStream
                If we have, e.g., DataStream["attribute"] <= 1 then other is the 1. Itis just the data type that is not
                DataStream.

        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) <= LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) <= LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) <= LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __eq__(self, other):
        """
        Manages '==' of DataStream.

        Parameters
        ----------
        other : int or float or DataStream
                If we have, e.g., DataStream["attribute"] == 1 then other is the 1. It is just the data type that is not
                DataStream.

        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) == LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) == LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) == LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __ne__(self, other):
        """
        Manages '!=' of DataStream.

        Parameters
        ----------
        other : int or float or DataStream
                If we have, e.g., DataStream["attribute"] != 1 then other is the 1. It is just the data type that is not
                DataStream.

        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) != LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) != LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) != LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __ge__(self, other):
        """
        Manages '>=' of DataStream.

        Parameters
        ----------
        other: int or float or DataStream
               If we have, e.g., DataStream["attribute"] >= 1 then other is the 1. It is just the data type that is not
               DataStream.


        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) >= LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) >= LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) >= LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __gt__(self, other):
        """
        Manages '>' of DataStream.

        Parameters
        ----------
        other : int or float or DataStream
                If we have, e.g., DataStream["attribute"] > 1 then other is the 1. It is just the data type that is not
                DataStream.


        Returns
        -------
        str

        """
        if len(self.key) == 1 and isinstance(self.key[0], str):
            if isinstance(other, int):
                return LogicalOperator(self.key[0]) > LogicalOperator(str(other))
            elif isinstance(other, str):
                return LogicalOperator(self.key[0]) > LogicalOperator("\"" + other + "\"")
            elif isinstance(other, ds.DataStream):
                return LogicalOperator(self.key[0]) > LogicalOperator(other.key[0])
            else:
                raise InvalidSyntaxError("The syntax is incorrect")

    def __add__(self, other):
        """
        Manages '+' of DataStream.

        Parameters
        ----------
        other :
                If we have, e.g., DataStream["attribute"] + 1 then other is the 1. It is just the data type that is not
                DataStream other is always on the right hand side.

        Returns
        -------
        str

        """
        if isinstance(other, Wrapper) and (isinstance(other.key, list)) and len(other.key) == 1:
            other = "Attribute(\"" + other.key[0] + "\")"
        return self._map_to_string() + " + " + str(other)

    def __radd__(self, other):
        """
        Opposite of __add__.
        Whenever other is on the left hand side.

        Parameters
        ----------
        other

        Returns
        -------
        Wrapper

        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Manages '-' of DataStream.

        Parameters
        ----------
        other :
                If we have, e.g., DataStream["attribute"] - 1 then other is the 1. Iis just the data type that is not
                DataStream other is always on the right hand side.

        Returns
        -------
        str

        """
        if isinstance(other, Wrapper) and (isinstance(other.key, list)) and len(other.key) == 1:
            other = "Attribute(\"" + other.key[0] + "\")"
        return self._map_to_string() + " - " + str(other)

    def __rsub__(self, other):
        """
        Opposite of __sub__.
        Whenever other is on the left hand side.

        Parameters
        ----------
        other

        Returns
        -------
        Wrapper

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """
        Manages '*' of DataStream.

        Parameters
        ----------
        other :
                If we have, e.g., DataStream["attribute"] * 1 then other is the 1. It is just the data type that is not
                DataStream other is always on the right hand side.

        Returns
        -------
        str

        """
        if isinstance(other, Wrapper) and (isinstance(other.key, list)) and len(other.key) == 1:
            other = "Attribute(\"" + other.key[0] + "\")"
        return self._map_to_string() + " * " + str(other)

    def __rmul__(self, other):
        """
        Opposite of __mul__.
        Whenever other is on the left hand side.

        Parameters
        ----------
        other

        Returns
        -------
        Wrapper

        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Manages '/' of DataStream.

        Parameters
        ----------
        other :
                If we have, e.g., DataStream["attribute"] / 1 then other is the 1. It is just the data type that is not
                DataStream other is always on the right hand side.

        Returns
        -------
        str

        """
        if isinstance(other, Wrapper) and (isinstance(other.key, list)) and len(other.key) == 1:
            other = "Attribute(\"" + other.key[0] + "\")"
        return self._map_to_string() + " / " + str(other)

    def __rtruediv__(self, other):
        """
        Opposite of __truediv__.
        Whenever other is on the left hand side.

        Parameters
        ----------
        other

        Returns
        -------
        Wrapper

        """
        return self.__truediv__(other)

    def __mod__(self, other):
        """
        Manages '%' of DataStream.

        Parameters
        ----------
        other :
                If we have, e.g., DataStream["attribute"] % 10 then other is the 10. It is just the data type that is
                not DataStream other is always on the right hand side.

        Returns
        -------
        str

        """
        if isinstance(other, Wrapper) and (isinstance(other.key, list)) and len(other.key) == 1:
            other = "Attribute(\"" + other.key[0] + "\")"
        return self._map_to_string() + " % " + str(other)

    def __rmod__(self, other):
        """
        Opposite of __mod__.
        Whenever other is on the left hand side.

        Parameters
        ----------
        other

        Returns
        -------
        Wrapper

        """
        return self.__mod__(other)

    def _map_to_string(self):
        """
        This function just creates "Attribute("attribute") && Attribute("attribute2")" string.

        Returns
        -------
        s : str

        """
        s = ""
        for k in self.key:
            s += "Attribute(\"" + k + "\") && "
        s = s[:-4]
        return s
