# pylint: disable = import-outside-toplevel
"""Tests of ``views.mode`` functions."""

from . import DBUnitTestCase

MODE_TEST = ('test', (
    '{theme}/images/menu_test1.png', 'Test', None,
    ('user_view', {'user_id': 3}), None))


# =============================================================================
class UViewsModeModeView(DBUnitTestCase):
    """Unit test class for testing :func:`views.mode.mode_view`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.home.home_view]"""
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPFound, HTTPNotFound
        from pyramid.httpexceptions import HTTPForbidden
        from ..modes import MODE_HOME, MODE_ADMIN
        from ..views.mode import mode_view

        self.configurator.add_route('home', '/')
        self.configurator.add_route('mode', '/mode/{mode_id}')
        self.configurator.add_route('settings_view', '/settings/view')
        self.configurator.add_route('user_view', '/user/view/{user_id}')
        self.request.matched_route = namedtuple('Route', 'name')(name='home')

        self.assertRaises(HTTPNotFound, mode_view, self.request)

        self.request.registry['modes'] = [MODE_HOME, MODE_TEST, MODE_ADMIN]
        self.request.session['modes'] = ['home', 'Home', None]
        self.request.matchdict = {'mode_id': 'foo'}
        self.assertRaises(HTTPNotFound, mode_view, self.request)

        self.request.matchdict = {'mode_id': 'test'}
        response = mode_view(self.request)
        self.assertIsInstance(response, HTTPFound)

        self.request.matchdict = {'mode_id': 'admin'}
        response = mode_view(self.request)
        self.assertIsInstance(response, HTTPFound)

        self.request.has_permission = lambda x: False
        self.assertRaises(HTTPForbidden, mode_view, self.request)
