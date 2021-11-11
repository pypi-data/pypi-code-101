"""Home view callables."""

from pyramid.httpexceptions import HTTPFound

from ..lib.i18n import _
from ..lib.form import button
from ..lib.panel import Panel
from ..lib.menu import Menu
from ..lib.modes import Modes


# =============================================================================
def home_view(request, title=None, modes_uid='modes', menu_uid='menu'):
    """Home view.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str title: (optional)
        Alternative title of the home page.
    :param str modes_uid: (default='modes')
        Unique ID of the modes management.
    :param str menu_uid: (default='menu')
        Unique ID of the menu management.
    """
    # Mode
    mode_id = request.params.get('mode')
    if mode_id and modes_uid in request.registry \
       and modes_uid in request.session:
        Menu.invalidate(request, menu_uid)
        Modes(request, modes_uid, request.registry[modes_uid]).select(mode_id)

    # Route
    route_id = request.params.get('route')
    if route_id:
        return HTTPFound(request.route_path(route_id, **request.params))

    # Panel
    Panel.manage_panels(request)

    request.breadcrumbs(title or _('Home'), 1)
    return {'button': button}
