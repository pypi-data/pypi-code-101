# pylint: disable = import-outside-toplevel
"""Tests of ``lib.restful`` functions."""

from datetime import datetime, timedelta
from unittest import TestCase

from . import DBUnitTestCase


# =============================================================================
class ULibRestfullRestfulCall(TestCase):
    """Unit test class for :func:`lib.restful.restful_call`."""

    # -------------------------------------------------------------------------
    def test_it_ko(self):
        """[u:lib.restful.restful_call] Ko"""
        from ..lib.utils import decrypt
        from ..lib.restful import restful_call
        from . import RESTFUL_HOST, RESTFUL_LOGIN, RESTFUL_KEY

        # Incorrect URL
        url = 'http://localhost:6543/user/index'
        response, error = restful_call(url, RESTFUL_LOGIN, 'foo')
        self.assertIsNone(response)
        self.assertTrue(
            ('Connection refused' in error) or
            ('Connection timed out' in error) or
            ('No route to host') in error or
            ('Could not resolve host') in error or
            ('HTTP Error 400: Bad Request') in error)

        # Incorrect action
        url = '{0}warehouse/fullrefresh/Buggy'.format(RESTFUL_HOST)
        response, error = restful_call(
            url, RESTFUL_LOGIN, decrypt(RESTFUL_KEY, 'test'))
        self.assertIsNone(response)
        self.assertIsNotNone(error)

    # -------------------------------------------------------------------------
    def test_it_ok(self):
        """[u:lib.restful.restful_call] Ok"""
        from ..lib.utils import decrypt
        from ..lib.restful import restful_call
        from . import RESTFUL_HOST, RESTFUL_LOGIN, RESTFUL_KEY

        # Without data
        url = '{0}warehouse/fullrefresh/Sandbox'.format(RESTFUL_HOST)
        response, error = restful_call(
            url, RESTFUL_LOGIN, decrypt(RESTFUL_KEY, 'test'))
        if response is None:
            return
        self.assertIsNotNone(response)
        self.assertIsNone(error)

        # With data
        url = '{0}warehouse/refresh/Sandbox'.format(RESTFUL_HOST)
        data = {
            'files': ['file_00001.txt', 'file_00002.txt'],
            'recursive': True, 'ignored': {'foo': 1}}
        response, error = restful_call(
            url, RESTFUL_LOGIN, decrypt(RESTFUL_KEY, 'test'), data)
        self.assertIsNotNone(response)
        self.assertIsNone(error)


# =============================================================================
class ULibRestfullRestfulLogin(DBUnitTestCase):
    """Unit test class for :func:`lib.restful.restful_login`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.restful.restful_login]"""
        from ..lib.utils import decrypt
        from ..lib.restful import restful_login
        from ..lib.utils import encrypt
        from . import RESTFUL_KEY

        # User not in session, incorrect login
        key = decrypt(RESTFUL_KEY, 'test')
        self.assertIsNotNone(restful_login(self.request, key))

        # User not in session, correct login, no token
        self.add_user({
            'login': 'admin', 'status': 'administrator',
            'last_name': 'Administrator', 'password': 'adminpwd',
            'email': 'admin@chrysal.io'})
        self.request.params = {'login': 'admin'}
        self.assertIsNotNone(restful_login(self.request, key))

        # User not in session, correct login, bad token
        self.request.params['token'] = 'bad-token'
        self.assertIsNotNone(restful_login(self.request, key))

        # User not in session, correct login, expired token
        self.request.params['token'] = encrypt(
            (datetime.utcnow() + timedelta(hours=1)).isoformat(), key)
        self.assertIsNotNone(restful_login(self.request, key))

        # User not in session, correct login, correct token, incorrect user
        self.request.params['login'] = 'foo'
        self.request.params['token'] = encrypt(
            datetime.utcnow().isoformat(), key)
        self.assertIsNotNone(restful_login(self.request, key))

        # User not in session, correct login, correct token, correct user
        self.request.params['login'] = 'admin'
        self.request.params['token'] = encrypt(
            datetime.utcnow().isoformat(), key)
        self.assertIsNone(restful_login(self.request, key))

        # User in session
        self.assertIsNone(restful_login(self.request, key))
