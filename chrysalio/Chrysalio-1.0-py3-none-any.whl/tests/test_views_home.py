# pylint: disable = import-outside-toplevel
"""Tests of ``views.home`` functions."""

from pyramid.httpexceptions import HTTPFound
from pyramid.testing import DummySession

from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsHomeHomeView(DBUnitTestCase):
    """Unit test class for testing :func:`views.home.home_view`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.home.home_view]"""
        from collections import namedtuple
        from ..views.home import home_view
        from ..modes import MODE_HOME, MODE_ADMIN

        self.configurator.registry['modes'] = [MODE_HOME, MODE_ADMIN]
        self.configurator.add_route('home', '/')
        self.configurator.add_route('mode', '/mode/{mode_id}')
        self.configurator.add_route('settings_view', '/settings/view')
        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        self.request.session = DummySession({'modes': ['home', 'Home', None]})

        # Display home
        response = home_view(self.request)
        self.assertIn('button', response)
        self.assertEqual(self.request.breadcrumbs.current_title(), 'Home')

        # With a mode and a page change
        self.request.params = {'route': 'settings_view', 'mode': 'admin'}
        response = home_view(self.request)
        self.assertIsInstance(response, HTTPFound)


# =============================================================================
class FViewsHomeHomeView(FunctionalTestCase):
    """Functional test class for testing :func:`views.home.home_view`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[f:views.home.home_view]"""
        self.testapp.get('/', status=302)
        self.login('test1')
        self.testapp.get('/', status=200)
