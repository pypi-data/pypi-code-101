BUILTIN_NAMES = {
    '打印': 'builtin_print',
    '绝对值': 'builtin_abs',
    '最大值': 'builtin_max',
    '最小值': 'builtin_min',
    '类型': 'builtin_type'
}


# -----------------------------------------------------------------------------
# Build-in types
# -----------------------------------------------------------------------------
class BooleanType(int):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '对' if self.value else '错'

    def __str__(self):
        return '对' if self.value else '错'

    def get_type(self):
        return '<类型 \'布林\'>'


class IntegerType(int):

    def __init__(self, value):
        self.value = value

    def get_type(self):
        return '<类型 \'整数\'>'


class FloatType(float):

    def __init__(self, value):
        self.value = value

    def get_type(self):
        return '<类型 \'浮点数\'>'


class ComplexType(complex):

    def __init__(self, value):
        self.value = value

    def get_type(self):
        return '<类型 \'复数\'>'


class StringType(str):

    def __init__(self, value):
        self.value = value

    def get_type(self):
        return '<类型 \'字符串\'>'


class ListType(list):

    def __init__(self, iterable):
        self.extend(iterable)

    def get_type(self):
        return '<类型 \'列表\'>'


# -----------------------------------------------------------------------------
# Built-in functions
# -----------------------------------------------------------------------------
def builtin_print(value):
    print(value)
    return None

def builtin_abs(value):
    return abs(value)

def builtin_max(iterable):
    return max(iterable)

def builtin_min(iterable):
    return min(iterable)

def builtin_type(value):
    return value.get_type()
