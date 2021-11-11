"""Provide the Requestor class."""
import logging
from collections import defaultdict

import requests
from requests import codes

from .const import __version__
from .exceptions import (
    Conflict,
    Forbidden,
    InvalidJSON,
    InvalidRequest,
    NotFound,
    ServerError,
    Unauthorized,
    UnknownStatusCode,
)

log = logging.getLogger(__package__)


def _urljoin(base, path):
    if base.endswith("/"):  # pragma: no cover
        base = base[:-1]
    if not path.startswith("/"):  # pragma: no cover
        path = f"/{path}"
    return f"{base}{path}"


class Requestor(object):
    """Requestor provides an interface to HTTP requests."""

    _exceptionMapping = defaultdict(
        lambda: UnknownStatusCode,
        {
            400: InvalidRequest,
            401: Unauthorized,
            403: Forbidden,
            404: NotFound,
            409: Conflict,
            422: ServerError,
            500: ServerError,
            502: ServerError,
            503: ServerError,
            504: ServerError,
            520: ServerError,
            522: ServerError,
        },
    )
    _retry_error = (InvalidRequest, ServerError, UnknownStatusCode)
    _successCodes = [200, 201, 202, 204]

    def __init__(self, credmgrUrl, auth, sessionClass, **sessionKwargs):
        """Create an instance of the Requestor class.

        :param str credmgrUrl: Url used to make API requests
        :param auth: An auth tuple or a class that subclasses requests.auth
        :param Session sessionClass: (Optional) A custom session class to handle
            requests, compatible with requests.Session(). (Default: None)

        """
        self._baseUrl = credmgrUrl
        self._session = (sessionClass or requests.Session)()
        self._session.auth = auth
        for key, value in sessionKwargs.items():  # pragma: no cover
            setattr(self._session, key, value)
        self._session.headers["User-Agent"] = f"credmgr/{__version__}"

    def __getattr__(self, attribute):  # pragma: no cover
        """Pass all undefined attributes to the _session attribute."""
        if attribute.startswith("__"):
            raise AttributeError
        return getattr(self._session, attribute)

    @staticmethod
    def _logRequest(data, method, params, url):
        log.debug(f"Data: {data}")
        log.debug(f"Request: {method} {url}")
        log.debug(f"Query Parameters: {params}")

    def request(self, path, method, data=None, params=None, **kwargs):
        """Issue the HTTP request capturing any errors that may occur."""
        url = _urljoin(self._baseUrl, path)
        retry_limit = 4
        retry_count = 0
        while retry_count < retry_limit:
            try:
                self._logRequest(data, method, params, url)
                response = self._session.request(
                    method, url, params, data=data, timeout=15, **kwargs
                )
                log.debug(
                    f'Response: {response.status_code} ({response.headers.get("content-length")} bytes)'
                )
                if response.status_code in self._exceptionMapping:
                    raise self._exceptionMapping[response.status_code](response)
                elif response.status_code == codes["no_content"]:
                    return
                if response.headers.get("content-length") == "0":  # pragma: no cover
                    return ""
                try:
                    response.json()
                except ValueError:  # pragma: no cover
                    raise InvalidJSON(response)
                return response
            except self._retry_error as error:
                retry_count += 1
                if retry_count < retry_limit:
                    log.debug(
                        f"Error occurred: {error}. Retrying...attempt {retry_count}/3"
                    )
                else:
                    log.error(f"Error occurred: {error}. Max attempts reached")
                    raise error
