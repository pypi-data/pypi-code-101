class APIError(Exception):
    pass


class APIRateLimitError(Exception):
    """Wrapper for a JSONDecode error which means Mining Pool Hub has sent an HTML response
    meaning they likely have rate limited you
    """

    pass


class InvalidCoinError(Exception):
    """Thrown when an invalid coin name is given"""

    pass


class JsonFormatError(Exception):
    pass


class UnauthorizedError(Exception):
    """Wrapper for an HTTP 401 Unauthorized error"""

    pass
