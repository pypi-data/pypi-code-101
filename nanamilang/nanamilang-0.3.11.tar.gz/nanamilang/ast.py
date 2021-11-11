"""NanamiLang AST CLass"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

from typing import List
from nanamilang import datatypes
from nanamilang.token import Token
from nanamilang.shortcuts import ASSERT_IS_INSTANCE_OF
from nanamilang.shortcuts import ASSERT_COLLECTION_IS_NOT_EMPTY
from nanamilang.shortcuts import ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF


class AST:
    """
    NanamiLang AST (abstract syntax tree) Generator

    Usage:
    ```
    from nanamilang import AST, Tokenizer, datatypes
    t: Tokenizer = Tokenizer('(+ 2 2 (* 2 2))')
    tokenized = t.tokenize() # => tokenize input string
    ast: AST = AST(tokenized) # => create new AST instance
    result: datatypes.Base = ast.evaluate() # => <IntegerNumber>: 8
    ```
    """

    _wood: list
    _tokenized: List[Token]

    def __init__(self, tokenized: List[Token]) -> None:
        """Initialize a new NanamiLang AST instance"""

        ASSERT_IS_INSTANCE_OF(tokenized, list)
        ASSERT_COLLECTION_IS_NOT_EMPTY(tokenized)
        ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF(tokenized, Token)

        self._tokenized = tokenized
        self._wood = self._make_wood()

    def wood(self) -> list:
        """NanamiLang AST, self._wood getter"""

        return self._wood

    def _make_wood(self) -> list:
        """NanamiLang AST, make an actual wood of trees"""

        # Written by @buzzer13 (https://gitlab.com/buzzer13)

        # TODO: I need to better understand how it works O.O, thank you Michael

        items = []
        stack = [items]

        for token in self._tokenized:

            if token.type() == Token.ListBegin:

                wired = []
                stack[-1].append(wired)
                stack.append(wired)

            elif token.type() == Token.ListEnd:

                stack.pop()

            else:
                stack[-1].append(token)

        return [i
                if isinstance(i, list)
                else [Token(Token.Identifier, 'identity'), i] for i in items]

    def evaluate(self) -> datatypes.Base:
        """NanamiLang AST, recursively evaluate tree"""

        def recursive_evaluate(tree: list) -> datatypes.Base:
            identifier: (list or Token)
            rest: list
            identifier, *rest = tree
            arguments: list = []
            argument: (Token or list)
            if isinstance(identifier, Token):
                if identifier.dt().name == datatypes.Macro.name:
                    return recursive_evaluate(
                        identifier.dt().reference()(
                            # we need this because we can not import
                            # nanamilang.token module in
                            # nanamilang.builtin module which is
                            # responsible to handle macro
                            rest, recursive_evaluate, Token
                        ))
            for part in rest:
                if isinstance(part, Token):
                    arguments.append(part.dt())
                elif isinstance(part, list):
                    arguments.append(recursive_evaluate(part))
            if isinstance(identifier, Token):
                return identifier.dt().reference()(arguments)
            elif isinstance(identifier, list):
                return recursive_evaluate(identifier).reference()(arguments)

        return list(recursive_evaluate(expression) for expression in self.wood())[-1]
