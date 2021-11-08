#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from typing import Union

ConvertibleIntoBool = Union[str, int, float, bool]


def filter_bool(value: ConvertibleIntoBool) -> bool:
    """
    Converts input into boolean. Expects string representing boolean or number.
    In case of string the true will be generated for strings "true", "yes", "1"
    and false for any other string.
    For number input true will be generated for any value but 0.
    For boolean input the input will be returned back as it is
    :param value: value to be converted
    :raises: ValueError in case of any other input type given
    :return: boolean representation of the input
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ["true", "yes", "1"]
    if isinstance(value, (int, float)):
        return value != 0
    raise ValueError("Value {} can't be converted into boolean".format(value))


def filter_not(value: ConvertibleIntoBool) -> bool:
    """
    Returns the value opposite to the input.
    If input is not of the boolean type it will try to convert it first (see filter_bool)
    :param value:
    :raises: ValueError if input can't be converted into boolean
    :return: value opposite to the given input
    """
    return not filter_bool(value)
