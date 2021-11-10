"""Declares :class:`HTTPAuthenticationService`."""
from unimatrix.ext import jose

from ..ihttpauthenticationservice import IHTTPAuthenticationService


class HTTPAuthenticationService(IHTTPAuthenticationService):

    async def resolve(self,
        bearer: bytes,
        audience: set = None,
        issuers: set = None,
        scope: set = None
    ):
        """Decode JWT `bearer` and return the principal described by the
        claimset.

        Args:
            bearer (str): the bearer token as received by the ``Authorization``
                header.
            audience (set): a list of string indicating the audiences that
                are valid for this bearer token. If `audience` is ``None`` or
                empty, then no validation of the ``aud`` claim is performed.
            issuers (set): the list of issuers that should be trusted.
            scope (set): the required scope.
        """
        jws = await jose.payload(bearer)
        jws.verify(
            audience=audience or None,
            issuers=issuers or None,
            scope=scope or None
        )
        return jws.claims

