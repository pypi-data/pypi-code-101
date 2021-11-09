from json import JSONEncoder as _JSONEncoder

import jwt
from flask import request

from flask_mysso.context import User, SecurityContext
from flask_mysso.errors import InvalidTokenError


class JsonEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return super().default(o)


class JwtHelper:
    @staticmethod
    def decode_jwt(token, key, algorithms=None, **kwargs):
        if algorithms is None:
            header = jwt.get_unverified_header(token)
            algorithms = [header['alg']]

        return jwt.decode(token, key=key, algorithms=algorithms, **kwargs)


class BearerTokenExtractor:
    def extract(self) -> str:
        token = self._extract_token_from_header()
        if token is None:
            token = self._extract_token_from_query()
        return token

    @staticmethod
    def _extract_token_from_header():
        auth = request.headers.get('Authorization')
        if auth is not None and auth.lower().startswith('bearer'):
            return auth.split(' ', 1)[1]

    @staticmethod
    def _extract_token_from_query():
        token = request.args.get('access_token')
        if token is not None:
            return token


class JwtManager:
    AUTHORITIES = 'authorities'
    USERNAME = 'username'
    USERINFO = 'userinfo'

    def __init__(self, public_key=None):
        self.public_key = public_key
        self.token_extractor = BearerTokenExtractor()

    def authenticate(self):
        access_token_value = self.token_extractor.extract()

        if access_token_value is not None:
            payload = self._decode(access_token_value)
            authorities = payload.get(self.AUTHORITIES)
            username = payload.get(self.USERNAME)
            userinfo = payload.get(self.USERINFO)
            user = User(username=username, authorities=authorities)
            if userinfo and isinstance(userinfo, dict):
                for k, v in userinfo.items():
                    setattr(user, k, v)

            SecurityContext.set_user(user)

    def _decode(self, access_token_value):
        try:
            payload = JwtHelper.decode_jwt(
                access_token_value,
                self.public_key,
            )
        except Exception as e:
            raise InvalidTokenError(e)
        return payload
