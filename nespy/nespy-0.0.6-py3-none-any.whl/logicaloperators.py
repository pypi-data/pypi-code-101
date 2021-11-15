
class LogicalOperator:
    """
    Creates the strings of the logical operators.
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        """
        Creates a string that looks the following: current_value < other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, "<")

    def __gt__(self, other):
        """
        Creates a string that looks the following: current_value > other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, ">")

    def __le__(self, other):
        """
        Creates a string that looks the following: current_value <= other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, "<=")

    def __eq__(self, other):
        """
        Creates a string that looks the following: current_value == other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, "==")

    def __ne__(self, other):
        """
        Creates a string that looks the following: current_value != other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, "!=")

    def __ge__(self, other):
        """
        Creates a string that looks the following: current_value >= other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        str

        """
        return self._create_string(self.value, other, ">=")

    def __and__(self, other):
        """
        Creates a string that looks the following: current_value && other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        lo : LogicalOperator

        """
        # both are Logical operators
        value = self.value + " && " + other.value
        lo = LogicalOperator(value)
        return lo

    def __or__(self, other):
        """
        Creates a string that looks the following: current_value || other_value.

        Parameters
        ----------
        other : LogicalOperator

        Returns
        -------
        lo : LogicalOperator

        """
        # both are Logical operators
        value = self.value + " || " + other.value
        lo = LogicalOperator(value)
        return lo

    def __str__(self):
        """
        String representation of Logical_Operator.

        Returns
        -------
        self.value : str

        """
        return self.value

    def _create_string(self, value, other, operator):
        """
        Creates a string that looks the following: current_value operator other_value.
        Operator can be any logical operator.

        Parameters
        ----------
        value : str
        other : LogicalOperator
        operator : str

        Returns
        -------
        logical_operator : LogicalOperator

        """
        if isinstance(other, LogicalOperator):
            value = "(Attribute(\"" + value + "\") " + operator + " " + other.value + ")"
            logical_operator = LogicalOperator(value)
            return logical_operator
        elif isinstance(other, int):
            value = "(Attribute(\"" + value + "\") " + operator + " " + str(other) + ")"
            logical_operator = LogicalOperator(value)
            return logical_operator
