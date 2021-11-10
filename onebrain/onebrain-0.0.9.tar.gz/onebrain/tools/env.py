import os


def get_env(variable_name):
    return os.environ.get(variable_name)


def put_env(variable_name, variable_value):
    os.environ[str(variable_name)] = str(variable_value)


def unset_variable(variable_name):
    if variable_name in os.environ:
        del os.environ[variable_name]
