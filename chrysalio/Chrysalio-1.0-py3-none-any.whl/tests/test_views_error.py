# pylint: disable = import-outside-toplevel
"""Tests of ``views.error`` functions."""

from pyramid.testing import DummyRequest
from pyramid.httpexceptions import HTTPFound

from . import ConfiguratorTestCase, FunctionalTestCase


# =============================================================================
class DummyException(object):
    """Dummy exception class."""
    status_int = None
    explanation = None
    comment = None

    # -------------------------------------------------------------------------
    def __init__(self, status_int, title=None):
        """Constructor method."""
        self.status_int = status_int
        self.title = title


# =============================================================================
class UViewsErrorErrorView(ConfiguratorTestCase):
    """Unit test class for testing :func:`views.error.error_view`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        super(UViewsErrorErrorView, self).setUp()
        self.configurator.add_route('login', '/login')

    # -------------------------------------------------------------------------
    def test_not_authenticated(self):
        """[u:views.error.error_view] not authenticated."""
        from ..views.error import error_view

        request = DummyRequest()
        request.exception = DummyException(403)
        request.is_xhr = False
        response = error_view(request)
        self.assertIsInstance(response, HTTPFound)

    # -------------------------------------------------------------------------
    def test_is_xhr(self):
        """[u:views.error.error_view] is xhr."""
        from ..views.error import error_view

        request = DummyRequest()
        request.exception = DummyException(404)
        request.is_xhr = True
        response = error_view(request)
        self.assertIn('error', response)
        self.assertEqual(response['error'], 404)

    # -------------------------------------------------------------------------
    def test_forbidden(self):
        """[u:views.error.error_view] forbidden."""
        from ..views.error import error_view

        self.configurator.testing_securitypolicy('test1', permissive=True)
        request = DummyRequest()
        request.exception = DummyException(403)
        request.is_xhr = False
        response = error_view(request)
        self.assertIn('status', response)
        self.assertEqual(response['status'], 403)

    # -------------------------------------------------------------------------
    def test_not_found(self):
        """[u:views.error.error_view] not found."""
        from ..views.error import error_view

        self.configurator.testing_securitypolicy(permissive=True)
        request = DummyRequest()
        request.exception = DummyException(404)
        request.is_xhr = False
        response = error_view(request)
        self.assertIn('status', response)
        self.assertEqual(response['status'], 404)

    # -------------------------------------------------------------------------
    def test_bad_request(self):
        """[u:views.error.error_view] bad request."""
        from ..views.error import error_view

        self.configurator.testing_securitypolicy(permissive=True)
        request = DummyRequest()
        request.exception = DummyException(400, title='Bad request')
        request.is_xhr = False
        response = error_view(request)
        self.assertIn('status', response)
        self.assertEqual(response['status'], 400)


# =============================================================================
class FViewsErrorErrorView(FunctionalTestCase):
    """Functional test class for testing :func:`views.error.error_view`."""

    # -------------------------------------------------------------------------
    def test_not_authenticated(self):
        """[f:views.error.error_view] not authenticated."""
        response = self.testapp.get('/', status=302)
        self.assertEqual(response.location, 'http://localhost/login?next=%2F')

    # -------------------------------------------------------------------------
    def test_not_found(self):
        """[f:views.error.error_view] not found."""
        self.login('test1')
        self.testapp.get('/user/foo', status=404)

    # -------------------------------------------------------------------------
    def test_bad_request(self):
        """[f:views.error.error_view] bad request."""
        self.testapp.post(
            '/login', {'login': 'test1', 'password': 'test1pwd'}, status=400)

    # -------------------------------------------------------------------------
    def test_forbidden(self):
        """[f:views.error.error_view] forbidden."""
        self.login('test1')
        self.testapp.get('/user/index', status=403)
