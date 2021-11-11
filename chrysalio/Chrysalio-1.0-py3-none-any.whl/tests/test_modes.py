# pylint: disable = import-outside-toplevel
"""Tests of ``modes`` functions."""

from . import ConfiguratorTestCase


# =============================================================================
class UModesIncludeme(ConfiguratorTestCase):
    """Unit test class for :func:`modes.includeme`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modes.includeme]"""
        from ..modes import MODE_HOME, MODE_ADMIN, includeme

        includeme(self.configurator)
        self.assertIn(MODE_HOME, self.configurator.registry['modes'])
        self.assertIn(MODE_ADMIN, self.configurator.registry['modes'])


# =============================================================================
class UModesBeforeRender(ConfiguratorTestCase):
    """Unit test class for :func:`menu.before_render`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modes.before_render]"""
        from pyramid.testing import DummyRequest
        from ..lib.modes import Modes
        from ..lib.menu import Menu
        from ..modes import MODE_ADMIN, before_render

        self.configurator.add_route('home', '/')
        self.configurator.add_route('backup', '/backup')
        self.configurator.add_route('settings_view', '/settings/view')
        self.configurator.add_route('profile_index', '/profile/index')
        self.configurator.add_route('user_index', '/user/index')
        self.configurator.add_route('group_index', '/group/index')
        self.configurator.add_route('modules_view', '/modules/view')
        request = DummyRequest()
        request.registry['modes'] = [MODE_ADMIN]
        event = {'request': request}
        before_render(event)
        self.assertIn('modes', event)
        self.assertIn('menu', event)
        self.assertIsInstance(event['modes'], Modes)
        self.assertIsInstance(event['menu'], Menu)
