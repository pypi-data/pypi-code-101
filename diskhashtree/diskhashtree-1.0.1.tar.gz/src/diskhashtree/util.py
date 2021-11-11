import re
import os

# Regex ensures that the key is not all non-alphanumeric and does not start with a .
# Also ensures no forbidden characters are used and the file name is not all special characters
FILE_NAME_REGEX = '''^(?=.*[0-9a-zA-Z])([^.\^\/\"\'\\\:\;\|\,\?\*\[\]][^\^\/\"\'\\\:\;\|\,\?\*\[\]]{0,254})$'''


def filter_valid_files(file_list: list[str]):
    '''
    Filters out the valid files from the list provided using the FILE_NAME_REGEX.
    All file names will have their leading directory removed.
    '''
    for f in file_list:
        file_name_only = f[f.rfind('/') + 1:]
        if os.path.isfile(f):
            if bool(re.match(FILE_NAME_REGEX, file_name_only)):
                yield file_name_only


def filter_valid_directories(file_list: list[str]):
    '''
    Filters out the valid directories from the list provided.
    All directory names will have their leading directory and trailing slash
    removed.
    '''
    for f in file_list:
        file_name_only = f[f.rfind('/') + 1:].replace('/', '')
        if os.path.isdir(f):
            if bool(re.match(FILE_NAME_REGEX, file_name_only)):
                yield file_name_only


def safe_str_replace(s: str, term: str, replace_with: str):
    '''
    This function replaces the instance of `term` with `replace_with` only if
    the `term` occurs at the very start of `s`.

    We cannot use `s.replace(term, replace_with, 1)` because it is possible
    that `s` does not start with term and will damage the rest of the string.
    '''
    l_term = len(term)

    if s.startswith(term):
        return replace_with + s[l_term:]
    else:
        return s
