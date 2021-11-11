"""Main menu management."""

from pyramid.config import Configurator
from pyramid.events import BeforeRender
from pyramid.threadlocal import get_current_request

from .lib.i18n import _
from .lib.menu import Menu


# Menu entry = (icon, label, permission, route, (subentry, ...))
MENU_HOME = ('{theme}/images/menu_home.png', _('Home'), None, 'home', None)
MENU_TEST = (
    '{theme}/custom/menu_test1.png', _('Test'), None, None,
    (('{theme}/custom/menu_test2.png', _('Users'), None, 'user_index',
      ((None, _('Administrator'), None, ('user_view', {'user_id': 1}), None),
       (None, _('User 1'), None, ('user_view', {'user_id': 3}), None))),
     ('{theme}/custom/menu_test3.png', _('Profiles'), None, 'profile_index',
      None)))
MENU_ADMIN = (
    '{theme}/images/menu_admin.png', _('Administration'), None, None,
    [(None, _('General Settings'), 'settings-view', 'settings_view', None),
     (None, _('Groups'), 'group-view', 'group_index', None),
     (None, _('Users'), 'user-view', 'user_index', None),
     (None, _('Profiles'), 'profile-view', 'profile_index', None),
     (None, _('Backup'), 'backup-create', 'backup', None)])


# =============================================================================
def includeme(configurator):
    """Function to include menu functionality.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    if isinstance(configurator, Configurator):
        configurator.registry['menu'] = [MENU_HOME, MENU_ADMIN]
        configurator.add_subscriber(before_render, BeforeRender)


# =============================================================================
def before_render(event):
    """A subscriber for :class:`pyramid.events.BeforeRender` events to add a
    main menu.

    :type  event: pyramid.events.BeforeRender
    :param event:
        Current event.
    """
    request = event.get('request') or get_current_request()
    event['menu'] = Menu(request, 'menu', request.registry.get('menu', ''))
