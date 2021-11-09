import json
from typing import Optional

import jwt
import requests

from flask_mysso.context import SecurityContext
from flask_mysso.jwt import JwtManager


class MySSO:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        self._jwt_manager: Optional[JwtManager] = None

    def init_app(self, app):
        app.config.setdefault('MYSSO_CERT', 'http://sso.app.kdsec.org/api/cert')
        resp = requests.get(app.config['MYSSO_CERT'])
        resp.raise_for_status()
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(resp.json()))
        self._jwt_manager = JwtManager(public_key=public_key)

        role_prefix = app.config.get('MYSSO_ROLE_PREFIX')
        if role_prefix is not None:
            SecurityContext.DEFAULT_ROLE_PREFIX = role_prefix

        app.before_request(self._handle_token)

    def _handle_token(self):
        self._jwt_manager.authenticate()
