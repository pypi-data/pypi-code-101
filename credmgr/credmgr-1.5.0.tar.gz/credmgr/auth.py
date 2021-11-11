"""Auth base."""

from requests.auth import AuthBase


class ApiTokenAuth(AuthBase):
    """Class for generating API Token request headers."""

    def __init__(self, apiToken):
        """Initialize the :class:`ApiTokenAuth` class."""
        self.apiToken = apiToken

    def __call__(self, request):
        """Generate the request headers."""
        request.headers["X-API-TOKEN"] = self.apiToken
        return request
