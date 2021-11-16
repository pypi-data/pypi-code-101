"""# Utility Functions
"""
import sys
from typing_extensions import Literal

def escape_triple_quotes(string: str, single_quote: Literal["'", '"']='"') -> str:
    """Escape triple quotes inside a string

    :param string: string to escape
    :param single_quote: single-quote character
    :return: escaped string
    """
    assert len(single_quote) == 1
    quote = single_quote * 3
    escaped_single_quote = f'\\{single_quote}'
    escaped_quote = escaped_single_quote * 3
    return string.replace(quote, escaped_quote)
if sys.version_info < (3, 9, 0):
    import astunparse
    import astunparse.unparser

    class ASTUnparser(astunparse.unparser.Unparser):
        """AST unparser with additional preference for triple-quoted multi-line strings"""

        def _Constant(self, tree):
            if isinstance(tree.value, str) and '\n' in tree.value:
                self.write(f'"""{escape_triple_quotes(tree.value)}"""')
                return
            super()._Constant(tree)
    astunparse.Unparser = ASTUnparser
    astunparse.unparser.Unparser = ASTUnparser
    from astunparse import unparse as unparse_ast
else:
    from ast import unparse as unparse_ast