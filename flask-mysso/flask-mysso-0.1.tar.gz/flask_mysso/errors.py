class AuthenticationError(Exception):
    """
    Authentication exception
    """


class InvalidTokenError(AuthenticationError):
    """
    Invalid token exception
    """
