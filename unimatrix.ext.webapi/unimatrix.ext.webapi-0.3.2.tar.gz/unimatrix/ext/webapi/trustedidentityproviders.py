"""Declares :class:`TrustedIdentityProviders`."""
from unimatrix.ext import crypto
from unimatrix.ext import jose
from .exceptions import TrustIssues


class TrustedIdentityProviders:
    """Maintains the registry of trusted identity providers."""
    trusted_claims = ["sub"]

    def __init__(self):
        self.__providers = {}
        self.__keys = {}

    def add(self, url: str, audience: str, issuer: str, tags: list) -> None: # pragma: no cover
        """Adds a new provider to the registry."""
        self.__providers[url] = {
            'audience': audience,
            'issuer': issuer,
            'tags': tags
        }

    async def on_setup(self):
        """Retrieve the public keys for the registered identity provider
        and create a mapping between the provider and the key.
        """
        for url, opts in dict.items(self.__providers): # pragma: no cover
            keys = await crypto.trust.jwks(url, opts['tags'], {})
            for key in keys:
                self.register(
                    key.keyid,
                    audience=opts['audience'],
                    issuer=opts['issuer']
                )

    def register(self, keyid, audience, issuer):
        self.__keys[keyid] = self.Provider(
            audience=audience,
            issuer=issuer
        )

    async def verify(self, token: str) -> dict:
        """Verify the signature of the OpenID identity token `token`
        and return a :class:`~unimatrix.ext.webapi.models.IDToken`
        instance.
        """
        jws = jose.parse(str.encode(token))
        try:
            await jws.verify(jws.key)
        except LookupError:
            raise TrustIssues
        provider = self.__keys[jws.kid]
        provider.verify(jws.payload)
        return {k: jws.payload.claims[k] for k in self.trusted_claims}

    class Provider:

        def __init__(self, audience: str, issuer: str):
            self.audience = audience
            self.issuer = issuer

        def verify(self, jwt):
            return jwt.verify(audience=self.audience, issuers=self.issuer)
