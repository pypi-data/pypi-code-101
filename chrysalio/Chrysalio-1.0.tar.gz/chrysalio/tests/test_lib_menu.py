# pylint: disable = import-outside-toplevel
"""Tests of ``lib.menu`` class."""

from . import ConfiguratorTestCase

# Menu entry = (icon, label, permission, route, (subentry, ...))
MENU_HOME = ('{theme}/images/menu_home.png', 'Home', None, 'home', None)
MENU_ADMIN = (
    '{theme}/images/menu_admin.png', 'Administration', None, None,
    ((None, 'Profile Management', 'profile-create', 'profile_index', None),
     (None, 'User Management', None, 'user_index',
      ((None, 'Administrator', None, ('user_view', {'user_id': 1}), None),
       (None, 'User 1', None, ('user_view', {'user_id': 3}), None),
       (None, 'Nobody', None, None, None)))))


# =============================================================================
class ULibMenuMenu(ConfiguratorTestCase):
    """Unit test class for :class:`lib.menu.Menu`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from collections import namedtuple
        from pyramid.testing import DummyRequest
        from ..lib.breadcrumbs import Breadcrumbs

        super(ULibMenuMenu, self).setUp()
        self.configurator.add_route('home', '/')
        self.configurator.add_route('user_index', '/user/index')
        self.configurator.add_route('user_view', '/user/view/{user_id}')
        self.configurator.add_route('profile_index', '/profile/index')
        self.configurator.include('..security')

        self.request = DummyRequest(
            matched_route=namedtuple('Route', 'name')(name='home'))
        self.request.breadcrumbs = Breadcrumbs(self.request)
        self.request.registry['themes'] = {'': {'path': None, 'name': ''}}
        self.request.registry['settings'] = {'theme': ''}

        self.request.breadcrumbs('Home', forced_route=('home', {}))
        self.request.breadcrumbs(
            'User Management', forced_route=('user_index', {}))

    # -------------------------------------------------------------------------
    def test_is_empty(self):
        """[u:lib.menu.Menu.is_empty]"""
        from ..lib.menu import Menu

        self.assertTrue(Menu(self.request, 'foo', '').is_empty())
        self.assertFalse(
            Menu(self.request, 'menu', [MENU_HOME, MENU_ADMIN]).is_empty())

    # -------------------------------------------------------------------------
    def test_xhtml(self):
        """[u:lib.menu.Menu.xhtml]"""
        from ..lib.menu import Menu

        menu = Menu(self.request, 'menu', [MENU_HOME, MENU_ADMIN])
        html = menu.xhtml()
        self.assertIn('cioCurrent', html)
        self.assertNotIn('/profile/index', html)
        self.assertIn('/user/index', html)

        # Cache
        html = menu.xhtml()
        self.assertIn('/user/index', html)

    # -------------------------------------------------------------------------
    def test_xhtml_whitout_breadcrumbs(self):
        """[u:lib.menu.Menu.xhtml] without breadcrumbs"""
        from ..lib.menu import Menu

        del self.request.session['breadcrumbs']
        self.request.matched_route = None
        html = Menu(self.request, 'menu', [MENU_HOME, MENU_ADMIN]).xhtml()
        self.assertNotIn('cioCurrent', html)

    # -------------------------------------------------------------------------
    def test_invalidate(self):
        """[u:lib.menu.Menu.invalidate]"""
        from ..lib.menu import Menu

        self.request.session['menu'] = ()
        Menu.invalidate(self.request, 'menu')
        self.assertNotIn('menu', self.request.session)
