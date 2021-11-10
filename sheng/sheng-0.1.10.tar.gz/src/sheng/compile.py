# -----------------------------------------------------------------------------
# sheng: compile.py
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
# BEGIN compile.py
# -----------------------------------------------------------------------------

import sys
import inspect
from .lex import *
from .parse import *
from .ast import *
from .context import *
from .builtins import *


def exec(data, debug=False):
    if (debug):
        print('[DEBUG] input data as raw string:')
        print(repr(data))
        print('[DEBUG] input data as string:')
        print(data)

    # Lex
    lexer.input(data)

    if (debug):
        print('[DEBUG] tokens:')
        while (True):
            tok = lexer.token()
            if (not tok): break
            print(tok)
    
    if (debug):
        print('[DEBUG] program output:')
    
    # Initialise context with symbol table
    symtable = SymbolTable()
    context = Context(symtable)

    # Add builtin functions to the symbol table
    builtins = {
        name: obj 
        for name, obj 
        in inspect.getmembers(sys.modules['src.sheng.builtins'])
    }
    for identifier, builtin_name in BUILTIN_NAMES.items():
        name = Name(identifier)
        function_pointer = builtins[builtin_name]
        parameters = [
            Name(arg) 
            for arg in inspect.getfullargspec(function_pointer)[0]
        ]
        functiondef = FunctionDef(name, parameters, function_pointer)
        context.symtable.insert(identifier, functiondef)
    
    # Parse
    ast = parser.parse(data)
    ast.evaluate(context)


# -----------------------------------------------------------------------------
# ENG compile.py
# -----------------------------------------------------------------------------
