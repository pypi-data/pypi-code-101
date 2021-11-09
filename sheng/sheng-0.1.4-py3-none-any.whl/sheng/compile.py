import sys
import inspect
from .lex import *
from .parse import *
from .ast import *
from .symtable import *
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
    
    # Initialise symbol table
    symtable = SymbolTable()

    # Add builtin functions to the symbol table
    builtins = {
        name: obj 
        for name, obj 
        in inspect.getmembers(sys.modules['src.sheng.builtins'])
    }
    for identifier, builtin_name in BUILTIN_NAMES.items():
        name = Name(identifier)
        function_pointer = builtins[builtin_name]
        arguments = [
            Name(arg) 
            for arg in inspect.getfullargspec(function_pointer)[0]
        ]
        functiondef = FunctionDef(name, arguments, function_pointer)
        symtable.insert(identifier, functiondef)
    
    # Parse
    ast = parser.parse(data)
    ast.evaluate(symtable)
