import os
import re

from typing import AnyStr
from math import log10

from .exception import ConversionError

###############################################################################
# Getter
###############################################################################


def get_program_file_x86_location():
    """
    :return:  The location of the 'Program Files' folder. (require windows platform).
    """
    if os.environ.get("PROGRAMFILES(X86)") is None:  # this case is 32bit
        folder_path = os.environ.get("PROGRAMFILES")
    else:
        folder_path = os.environ.get("PROGRAMFILES(X86)")
    return folder_path


def is_empty_str(str_: str):
    """
    :return:  True is the string is only space or empty
    """
    return str_.isspace() or len(str_) == 0


def get_digit_number(number: int):
    """
    :param  number:  Any natural numbers
    :return:  The number of digit of the number. If the number is negative we count the minus sign
    """
    if number == 0:
        return 1
    elif number > 0:
        return int(log10(number)) + 1
    elif number < 0:
        return get_digit_number(number * -1) + 1

# End of getter
###############################################################################
# Utility functions
###############################################################################


def noop(*_, **__):
    """
    An no operation function which accept any number of argument.
    """
    pass


def convert_str_to_type(value: str, type_: type):
    """
    Will convert the value to the right type
    :raise ConversionError: in case the value can't be converted
    """
    value = value.strip()
    if type_ == int:
        return convert_str_to_int(value)
    elif type_ == bool:
        return convert_str_to_bool(value)
    elif type_ == float:
        return convert_str_to_float(value)
    elif type_ == str:
        return value


_STR_TO_INT_REGEX_BASE10 = re.compile("^\\d+$")
_STR_TO_INT_REGEX_BASE16 = re.compile("^0x[0-9a-f]+$")
_STR_TO_INT_REGEX_BASE8 = re.compile("^0o[0-7]+$")
_STR_TO_INT_REGEX_BASE2 = re.compile("^0b[0-1]+$")
def convert_str_to_int(value: str):
    if _STR_TO_INT_REGEX_BASE10.match(value):
        return int(value)
    elif _STR_TO_INT_REGEX_BASE16.match(value.lower()):
        return int(value, 16)
    elif _STR_TO_INT_REGEX_BASE8.match(value):
        return int(value, 8)
    elif _STR_TO_INT_REGEX_BASE2.match(value):
        return int(value, 2)
    else:
        raise ConversionError("The value given isn't a number")


_STR_TO_FLOAT_REGEX = re.compile("^(\\d+\\.)|(\\d*\\.?\\d+)$")
def convert_str_to_float(value: str):
    if _STR_TO_FLOAT_REGEX.match(value):
        return float(value)
    else:
        raise ConversionError("The value given isn't a decimal number")


_STR_TO_BOOL_VALUES = {
    'on': True,
    'y': True,
    'ye': True,
    'yes': True,

    'off': False,
    'n': False,
    'no': False
}
def convert_str_to_bool(value: str):
    try:
        return _STR_TO_BOOL_VALUES[value.lower()]
    except KeyError:
        raise ConversionError("The value given isn't a boolean")


def str_is_integer(value: str):
    if _STR_TO_INT_REGEX_BASE10.match(value):
        return True
    else:
        return False


def str_is_float(value: str):
    if _STR_TO_FLOAT_REGEX.match(value):
        return True
    else:
        return False


def read_file_content(file_path: str) -> str:
    """
    Read the content of a file and return it.

    :param  file_path:  The path of file that we have to read.
    :return:  The file content
    """

    with open(file_path, 'r') as f:
        content = f.read()
    return content


def write_file_content(file_content: AnyStr, file_path: str):
    if not os.path.isdir(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    f = open(file_path, 'x')
    f.write(file_content)
    f.close()


def replace_forbidden_file_name_char(file_name: str) -> str:
    file_name = file_name.replace('/', "-")
    file_name = file_name.replace('\\', "-")
    file_name = file_name.replace(':', "-")
    file_name = file_name.replace('*', "-")
    file_name = file_name.replace('?', ".")
    file_name = file_name.replace('"', "''")
    file_name = file_name.replace('<', "(")
    file_name = file_name.replace('>', ")")
    return file_name.replace('|', ", ")

# End of utility functions
