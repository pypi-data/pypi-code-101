# pylint: skip-file
import asyncio
import unittest
import time

from fastapi.testclient import TestClient

from .. import __unimatrix__ as boot
from .. import ResourceEndpointSet
from ..asgi import Application
from ..trustedidentityproviders import TrustedIdentityProviders
from .basesigning import BaseSigningTestCase


class IdentificationTestCase(BaseSigningTestCase):

    class view_class(ResourceEndpointSet):
        trust_local = True

        async def index(self):
            pass

    def setUp(self):
        asyncio.run(boot.on_setup())
        self.providers = TrustedIdentityProviders()
        self.k1 = self.generate_key()
        self.k2 = self.generate_key()

        self.trust(self.k1)
        self.providers.register(self.k1.keyid, 'foo', 'bar')

        self.app = Application(
            allowed_hosts=['*'],
            enable_debug_endpoints=True,
            openid=self.providers
        )
        self.client = TestClient(self.app)
        self.url = '/.well-known/identify'
        self.view_class.add_to_router(self.app, '/test')

    def test_untrusted_key_returns_trust_issues(self):
        token = self.get_token(self.k2, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 403, response.text)
        dto = response.json()
        self.assertEqual(dto['code'], "TRUST_ISSUES")

    def test_trusted_key_with_valid_audience_and_issuer_is_swapped(self):
        token = self.get_token(self.k1, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 200, response.text)

    def test_subject_is_included_in_access_token(self):
        token = self.get_token(self.k1, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 200, response.text)
        dto = response.json()
        self.assertIn('access_token', dto)
        self.assertIn('claims', dto)
        self.assertIn('sub', dto['claims'])
        self.assertEqual(dto['claims']['sub'], 'baz')

    def test_invalid_audience_is_rejected(self):
        token = self.get_token(self.k1, aud='invalid', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 403, response.text)

    def test_invalid_issuer_is_rejected(self):
        token = self.get_token(self.k1, aud='foo', iss='invalid', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 403, response.text)

    def test_issued_access_token_is_valid(self):
        token = self.get_token(self.k1, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 200, response.text)

        dto = response.json()
        access_token = dto['access_token']
        response = self.client.get('/test',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        self.assertEqual(response.status_code, 200, response.text)

    def test_issued_access_token_has_exp(self):
        token = self.get_token(self.k1, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 200, response.text)
        dto = response.json()
        access_token = self.parse_token(dto['access_token'])
        self.assertIn('exp', access_token)

    def test_issued_access_token_has_iat(self):
        token = self.get_token(self.k1, aud='foo', iss='bar', sub='baz')
        response = self.client.post(self.url, json={
            'id_token': token
        })
        self.assertEqual(response.status_code, 200, response.text)
        dto = response.json()
        access_token = self.parse_token(dto['access_token'])
        self.assertIn('iat', access_token)
