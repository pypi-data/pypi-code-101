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

import inspect
import traceback
from .lex import *
from .parse import *
from .ast import *
from .context import *
from .builtins import *


def execute(data):
    try:
        # Lex
        lexer.input(data)

        if (Global().is_debug):
            Global().log('[DEBUG] Lex tokens:')
            while (True):
                tok = lexer.token()
                if (not tok): break
                Global().log(f'[DEBUG] {tok}')
        
        # Initialise context with symbol table
        symtable = SymbolTable()
        context = Context(symtable)

        # Add builtin functions to the symbol table
        def get_default_args(func):
            signature = inspect.signature(func)
            return {
                k: v.default
                for k, v in signature.parameters.items()
                if v.default is not inspect.Parameter.empty
            }
        for identifier, function_pointer in BUILTIN_FUNCTIONS.items():
            name = Name(identifier)
            parameters = [
                Name(arg)
                for arg in inspect.getfullargspec(function_pointer)[0]
            ]
            default_args = get_default_args(function_pointer)
            functiondef = FunctionDef(
                name, parameters, function_pointer, default_args
            )
            context.symtable.insert(identifier, functiondef)

        # Parse
        ast = parser.parse(data)
        return ast.evaluate(context)
        
    except BaseException as e:
        Global().log(f'{type(e).__name__}: {e}')
        if (Global().is_debug):
            Global().log(f'[DEBUG] {traceback.format_exc()}')

    finally:
        return None


# -----------------------------------------------------------------------------
# ENG compile.py
# -----------------------------------------------------------------------------
