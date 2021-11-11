"""Mode management view callables."""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..lib.i18n import _
from ..lib.menu import Menu
from ..lib.modes import Modes


# =============================================================================
@view_config(route_name='mode')
def mode_view(request, uid='modes', menu_uid='menu'):
    """Mode redirection.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str uid: (default='modes')
        Unique ID of the modes management.
    :param str menu_uid: (default='menu')
        Unique ID of the menu management.
    """
    if uid not in request.registry or uid not in request.session:
        raise HTTPNotFound(comment=_('Modes are not activated.'))
    Menu.invalidate(request, menu_uid)
    modes = Modes(request, uid, request.registry.get(uid, ()))
    return HTTPFound(modes.select(request.matchdict['mode_id']))
