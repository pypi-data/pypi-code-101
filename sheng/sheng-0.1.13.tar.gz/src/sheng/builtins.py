# -----------------------------------------------------------------------------
# sheng: builtins.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/sheng-lang/sheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# BEGIN builtins.py
# -----------------------------------------------------------------------------

from .utils import *
from .context import *


# -----------------------------------------------------------------------------
# Build-in types
# -----------------------------------------------------------------------------

class BaseType(object):

    def __init__(self, type_name):
        self._type = type_name

    @property
    def type(self):
        return f'<类型 \'{self._type}\'>'


class NullType(BaseType):

    def __init__(self, value):
        BaseType.__init__(self, '空类型')
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
        BaseType.__init__(self, '布林')
        self.value = value

    def __repr__(self):
        return '对' if self.value else '错'

    def __str__(self):
        return '对' if self.value else '错'

    def __bool__(self):
        return self.value


class IntegerType(BaseType, int):

    def __init__(self, value):
        BaseType.__init__(self, '整数')
        self.value = value


class FloatType(BaseType, float):

    def __init__(self, value):
        BaseType.__init__(self, '浮点数')
        self.value = value


class ComplexType(BaseType, complex):

    def __init__(self, value):
        BaseType.__init__(self, '复数')
        self.value = value


class StringType(BaseType, str):

    def __init__(self, value):
        BaseType.__init__(self, '字符串')
        self.value = value


class TupleType(BaseType, tuple):

    def __init__(self, value):
        BaseType.__init__(self, '元组')
        self.value = value
    
    def __new__(self, value):
        return tuple.__new__(self, value)


class ListType(BaseType, list):

    def __init__(self, value):
        BaseType.__init__(self, '列表')
        self.extend(value)


class DictType(BaseType, dict):

    def __init__(self, value):
        BaseType.__init__(self, '字典')
        self.update(value)


class ClassType(BaseType):

    def __init__(self, class_name):
        BaseType.__init__(self, class_name)
        symtable = SymbolTable()
        self._context = Context(symtable)
    
    @property
    def context(self):
        return self._context


BUILTIN_TYPES = {
    'NoneType': NullType,
    'bool': BooleanType,
    'int': IntegerType,
    'float': FloatType,
    'complex': ComplexType,
    'str': StringType,
    'tuple': TupleType,
    'list': ListType,
    'dict': DictType,
}


# -----------------------------------------------------------------------------
# Built-in functions
# -----------------------------------------------------------------------------

def builtin_print(value=''):
    print(value, file=Global().output_stream)
    if (Global().is_debug):
        Global().log(f'[DEBUG] [{Global().output_stream.name}] {value}')
    return None

def builtin_input(prompt=''):
    value = input(prompt)
    if (Global().is_debug):
        Global().log(f'[DEBUG] [<stdin>] {prompt}{value}')
    return value

def builtin_abs(value):
    return abs(value)

def builtin_max(iterable):
    return max(iterable)

def builtin_min(iterable):
    return min(iterable)

def builtin_type(value):
    return value.type


BUILTIN_FUNCTIONS = {
    '打印': builtin_print,
    '输入': builtin_input,
    '绝对值': builtin_abs,
    '最大值': builtin_max,
    '最小值': builtin_min,
    '类型': builtin_type,
}


# -----------------------------------------------------------------------------
# END builtins.py
# -----------------------------------------------------------------------------
