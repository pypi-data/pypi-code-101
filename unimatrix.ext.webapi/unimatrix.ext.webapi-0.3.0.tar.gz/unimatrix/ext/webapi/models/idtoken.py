"""Declares :class:`IDToken`."""
import time
import uuid

from pydantic import BaseModel
from unimatrix.ext import crypto
from unimatrix.ext import jose


class IDToken(BaseModel):
    iss: str = ""
    aud: str = ""
    sub: str

    async def sign(self, signer=None, ttl=60*10, **extra):
        now = int(time.time())
        signer = signer or crypto.get_signer()
        claims = {
            **{k: v for k, v in dict.items(dict(self)) if v is not None},
            **extra,
            'exp': now + ttl,
            'iat': now,
            'jti': str(uuid.uuid4())
        }
        return {
            'access_token': str(await jose.jwt(claims, signer=signer)),
            'claims': claims
        }
