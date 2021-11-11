# pylint: disable = import-outside-toplevel
"""Tests of ``lib.modes`` class methods."""

from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden

from . import ConfiguratorTestCase


MENU_ADMIN = (
    '{theme}/images/menu_admin.png', 'Administration', None, None,
    ((None, 'Profile Management', 'profile-create', 'profile_index', None),
     (None, 'User Management', None, 'user_index', None)))
MODE_HOME = ('home', (
    '{theme}/images/menu_home.png', 'Home', None, 'home', None))
MODE_TEST = ('test', (
    '{theme}/images/menu_test1.png', 'Test', None, 'home', None))
MODE_ADMIN = ('admin', (
    '{theme}/images/menu_admin.png', ('Administration'), 'mode-admin',
    'settings_view', MENU_ADMIN))


# =============================================================================
class ULibModesModes(ConfiguratorTestCase):
    """Unit test class for :class:`lib.modes.Modes`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pyramid.testing import DummyRequest
        from ..models.dbsettings import DBSettings

        super(ULibModesModes, self).setUp()
        self.configurator.add_route('home', '/')
        self.configurator.add_route('mode', '/mode/{mode_id}')
        self.configurator.include('..security')

        self.request = DummyRequest()
        self.request.registry['settings'] = DBSettings.settings_defaults.copy()

    # -------------------------------------------------------------------------
    def test_label(self):
        """[u:lib.modes.Modes.label]"""
        from ..lib.modes import Modes

        modes = Modes(self.request, 'modes', [MODE_HOME, MODE_ADMIN])
        self.assertEqual(modes.label(), 'Home')
        self.assertIn(modes.uid, self.request.session)
        self.assertEqual(self.request.session[modes.uid][0], 'home')

    # -------------------------------------------------------------------------
    def test_menu_framework(self):
        """[u:lib.modes.Modes.menu_framework]"""
        from ..lib.modes import Modes

        # New activation
        modes = Modes(self.request, 'modes', [MODE_ADMIN, MODE_TEST])
        framework = modes.menu_framework()
        self.assertIsInstance(framework, tuple)
        self.assertEqual(len(framework), 2)
        self.assertEqual(framework[0], MENU_ADMIN[4][0])

        # Unknown activated mode
        modes = Modes(self.request, 'modes', [MODE_HOME, MODE_ADMIN])
        self.request.session[modes.uid] = [
            'foo', 'Foo', [MODE_HOME, MODE_ADMIN]]
        framework = modes.menu_framework()
        self.assertIsInstance(framework, tuple)
        self.assertEqual(len(framework), 0)

        # Kwown activated mode
        self.request.session[modes.uid] = [
            'admin', 'Administration', [MODE_HOME, MODE_ADMIN]]
        framework = modes.menu_framework()
        self.assertIsInstance(framework, tuple)
        self.assertEqual(len(framework), 2)

    # -------------------------------------------------------------------------
    def test_select(self):
        """[u:lib.modes.Modes.select]"""
        from ..lib.modes import Modes

        # Unknown mode
        modes = Modes(self.request, 'modes', [MODE_HOME, MODE_ADMIN])
        self.assertRaises(HTTPNotFound, modes.select, 'foo')

        # Forbidden mode
        self.assertRaises(HTTPForbidden, modes.select, 'admin')

        # Authorized mode
        route = modes.select('home')
        self.assertEqual(route, '/')

    # -------------------------------------------------------------------------
    def test_xhtml(self):
        """[u:lib.modes.Modes.xhtml]"""
        from ..lib.modes import Modes

        # 1 authorized mode
        modes = Modes(self.request, 'modes', [MODE_HOME, MODE_ADMIN])
        html = modes.xhtml()
        self.assertFalse(html)
        self.assertIn(modes.uid, self.request.session)
        self.assertEqual(self.request.session[modes.uid][0], 'home')
        self.assertEqual(self.request.session[modes.uid][1], 'Home')
        self.assertFalse(self.request.session[modes.uid][2])

        # 2 authorized modes
        modes = Modes(
            self.request, 'modes', [MODE_HOME, MODE_TEST, MODE_ADMIN])
        self.request.session[modes.uid] = ['home', 'Home', None]
        html = modes.xhtml()
        self.assertIn('cioModes-{0}'.format(modes.uid), html)

        # Cache
        html = modes.xhtml()
        self.assertIn('cioModes-{0}'.format(modes.uid), html)

        # 0 authorized mode
        modes = Modes(self.request, 'modes', [MODE_ADMIN])
        self.request.session[modes.uid] = ['home', 'Home', None]
        html = modes.xhtml()
        self.assertFalse(html)

    # -------------------------------------------------------------------------
    def test_invalidate(self):
        """[u:lib.modes.Modes.invalidate]"""
        from ..lib.modes import Modes

        self.request.session['modes'] = ['home', 'Home', '']
        Modes.invalidate(self.request, 'modes')
        self.assertIn('modes', self.request.session)
        self.assertEqual(self.request.session['modes'][0], 'home')
        self.assertEqual(self.request.session['modes'][1], 'Home')
        self.assertIsNone(self.request.session['modes'][2])
