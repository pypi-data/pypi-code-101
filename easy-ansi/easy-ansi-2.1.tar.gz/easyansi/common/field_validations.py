from typing import Any, Union, List, Tuple
import re


def _raise_error(field: str, value: str, msg: str, error_type: Any) -> None:
    """Build an error message, and use it to raise the error_type.

    Parameters:
        field: The name of the field in error.
        value: The value of the field in error.
        msg: The error message to show.
        error_type: The type of error / exception to raise.
    """
    raise error_type(f"Field: {field}, Value: {value}, Error: {msg}")


def check_if_boolean(value: bool, field: str) -> None:
    """Check if a value is a boolean.

    Parameters:
        value: The value to check for being a boolean.
        field: The name of the field being checked.
    """
    if not isinstance(value, bool):
        _raise_error(field, str(value), "Not a boolean value", TypeError)


def check_if_string(value: str, field: str) -> None:
    """Check if a value is a string.

    Parameters:
        value: The value to check for being a string.
        field: The name of the field being checked.
    """
    if not isinstance(value, str):
        _raise_error(field, str(value), "Not a string value", TypeError)


def check_if_int(value: int, field: str) -> None:
    """Check if a value is an int.

    Parameters:
        value: The value to check for being an int.
        field: The name of the field being checked.
    """
    if (not isinstance(value, int)) or (isinstance(value, bool)):
        _raise_error(field, str(value), "Not an int value", TypeError)


def check_int_minimum_value(value: int, minimum: int, field: str) -> None:
    """Check if a value is >= a minimal value.

    Parameters:
        value: The value to check.
        minimum: The minimum the value can be.
        field: The name of the field being checked.
    """
    check_if_int(value, field)
    check_if_int(minimum, f"Minimum for {field}")
    if not value >= minimum:
        _raise_error(field, str(value), f"Value is less than minimum of {minimum}", ValueError)


def check_int_in_range(value: int, minimum: int, maximum: int, field: str) -> None:
    """Check if an integer is between 2 values.

    Parameters:
        value: The value to check for being within the range.
        minimum: The minimum value the value can be.
        maximum: The maximum value the value can be.
        field: The name of the field being checked.
    """
    check_if_int(value, field)
    check_if_int(minimum, f"Minimum for {field}")
    check_if_int(maximum, f"Maximum for {field}")
    if not minimum <= value <= maximum:
        _raise_error(field, str(value), f"Value is not within range of {minimum} to {maximum}", ValueError)


def check_if_any_have_value(field: str, *args: Any, zero_int_no_value: bool = False) -> None:
    """Given an arbitrary number of arguments, raise an error if none of them have a value.

    Parameters:
        field: The name of the field(s) being checked.
        *args: values to be checked to be anything except None.
        zero_int_no_value: True/False: if an integer is zero, count this as no value.
    """
    value_found = False
    for arg in args:
        if arg is not None:
            if zero_int_no_value:
                if (isinstance(arg, int)) or (isinstance(arg, bool)):
                    if arg != 0:
                        value_found = True
                else:
                    value_found = True
            else:
                value_found = True
        if value_found:
            break
    if not value_found:
        _raise_error(field, "", "No provided arguments have a value", ValueError)


def check_if_string_matches_regex(value: str, regex: str, field: str) -> None:
    """Given a string and a regex, check if the string matches the regex.

    Parameters:
        value: The string value to check.
        regex: The regular expression to test the string against.
        field: The name of the field being checked.
    """
    check_if_string(value, field)
    check_if_string(regex, f"Regex for {field}")
    if not re.match(regex, value):
        _raise_error(field, str(value), "Value is not in a valid format", ValueError)


def check_if_sequence(value: Union[List[Any], Tuple[Any]], field: str) -> None:
    """Given a value, check if it is a supported sequence.

    Parameters:
        value: The value to check to be a supported sequence.
        field: The name of the field being checked.
    """
    if not ((isinstance(value, list)) or (isinstance(value, tuple))):
        _raise_error(field, str(value), "Value is not a supported sequence", TypeError)
