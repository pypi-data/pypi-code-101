"""
Manages Exceptions
"""


class WrongQueryError(Exception):
    pass


class NotSuchStatusError(Exception):
    pass


class WrongExpressionError(Exception):
    pass


class InvalidSyntaxError(Exception):
    pass


class NotSupportedError(Exception):
    pass
