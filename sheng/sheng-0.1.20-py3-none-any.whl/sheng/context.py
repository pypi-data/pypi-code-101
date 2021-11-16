# -----------------------------------------------------------------------------
# sheng: context.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/luojiahai/sheng
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
# BEGIN context.py
# -----------------------------------------------------------------------------

from .exception import *


class Context(object):

    def __init__(self, symtable):
        self._symtable = symtable

    @property
    def symtable(self):
        return self._symtable


class SymbolTable(object):

    def __init__(self, parent=None):
        self._symbols = dict()
        if (parent):
            for _, symbol in parent.symbols.items():
                self.insert(symbol.identifier, symbol.node)

    @property
    def symbols(self):
        return self._symbols
    
    def insert(self, identifier, node):
        symbol = Symbol(identifier, node)
        self.symbols[identifier] = symbol

    def lookup(self, identifier):
        if (identifier not in self.symbols):
            return None
        return self.symbols[identifier]


class Symbol(object):

    def __init__(self, identifier, node):
        self._identifier = identifier
        self._node = node

    @property
    def identifier(self):
        return self._identifier

    @property
    def node(self):
        return self._node


# -----------------------------------------------------------------------------
# END context.py
# -----------------------------------------------------------------------------
