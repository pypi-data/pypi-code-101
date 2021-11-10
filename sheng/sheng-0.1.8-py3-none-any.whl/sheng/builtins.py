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

class BaseType(object):

    def __init__(self, type_name):
        self.type_name = type_name

    def get_type(self):
        return f'<类型 \'{self.type_name}\'>'


class NullType(BaseType):

    def __init__(self, value):
        super().__init__('空类型')
        self.value = value

    def __repr__(self):
        return '空'

    def __str__(self):
        return '空'

    def __bool__(self):
        return bool(None)

    def __eq__(self, other):
        return other == None

    def __ne__(self, other):
        return other != None


class BooleanType(BaseType, int):

    def __init__(self, value):
        super().__init__('布林')
        self.value = value

    def __repr__(self):
        return '对' if self.value else '错'

    def __str__(self):
        return '对' if self.value else '错'

    def __bool__(self):
        return self.value


class IntegerType(BaseType, int):

    def __init__(self, value):
        super().__init__('整数')
        self.value = value


class FloatType(BaseType, float):

    def __init__(self, value):
        super().__init__('浮点数')
        self.value = value


class ComplexType(BaseType, complex):

    def __init__(self, value):
        super().__init__('复数')
        self.value = value


class StringType(BaseType, str):

    def __init__(self, value):
        super().__init__('字符串')
        self.value = value


class TupleType(BaseType, tuple):

    def __init__(self, value):
        super().__init__('元组')
        self.value = value
    
    def __new__(self, value):
        return tuple.__new__(self, value)


class ListType(BaseType, list):

    def __init__(self, value):
        super().__init__('列表')
        self.extend(value)


class DictType(BaseType, dict):

    def __init__(self, value):
        super().__init__('字典')
        self.update(value)


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
