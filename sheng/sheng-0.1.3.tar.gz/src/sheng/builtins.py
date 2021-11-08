# TODO

def builtin_print(value):
    if (isinstance(value, str)):
        # Discard leading and trailing quotes
        value = value[1:-1]
    if (isinstance(value, bool)):
        value = '对' if value else '错'
    print(value)
    return None
