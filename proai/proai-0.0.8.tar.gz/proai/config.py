""" config file parsing and environment var loading for configuration of your app """
from pathlib import Path


def load_env(filepath='.env'):
    filepath = Path(filepath)
    with filepath.open() as fin:
        lines = fin.readlines()
    var_values = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            name, value = line.split('=')
            name, value = name.strip().upper(), value.strip()
            if len(value) > 1:
                value = value[1:-1] if value[0] in '"\'' and value[-1] == value[0] else value
        except (ValueError, IndexError):
            name, value = None, None
        if name and value:
            var_values[name.upper().strip()] = value
    return var_values
