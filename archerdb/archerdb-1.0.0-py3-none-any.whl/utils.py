"""Define utility methods shared by different files."""

from .constants import get_log_file_path, get_db_dir
from functools import wraps

def log_transaction(func):
    """
    Log a function call and parameters.

    :param func: function called
    :return: function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = list(args)
        with open('{}/{}'.format(get_db_dir(),
                                 get_log_file_path()), 'a') as f:
            f.write('{} : {}\n'.format(func.__name__, args[1:]))
        return func(*args, **kwargs)
    return wrapper
