"""Mode management."""

from pyramid.config import Configurator
from pyramid.events import BeforeRender
from pyramid.threadlocal import get_current_request

from .menu import MENU_TEST, MENU_ADMIN, Menu
from .lib.i18n import _
from .lib.modes import Modes

# Mode = (mode_id, (icon, label, permission, route, menu))
MODE_HOME = ('home', (
    '{theme}/images/menu_home.png', _('Home'), None, 'home', None))
MODE_TEST = ('test', (
    '{theme}/images/menu_test1.png', _('Test'), None,
    ('user_view', {'user_id': 3}), MENU_TEST))
MODE_ADMIN = ('admin', (
    '{theme}/images/menu_admin.png', _('Administration'), 'mode-admin',
    'settings_view', MENU_ADMIN))


# =============================================================================
def includeme(configurator):
    """Function to manage modes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Mode = (mode_id, (label, permission, value_or_function_menu))
    if isinstance(configurator, Configurator):
        configurator.registry['modes'] = [MODE_HOME, MODE_ADMIN]
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
    event['modes'] = Modes(request, 'modes', request.registry.get('modes', ()))
    menu = Menu(request, 'menu', event['modes'].menu_framework())
    if not menu.is_empty():
        event['menu'] = menu
