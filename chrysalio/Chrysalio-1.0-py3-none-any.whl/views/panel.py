"""Panel management view callables."""

from pyramid.view import view_config


# =============================================================================
@view_config(route_name='panel_open', renderer='json', xhr=True)
@view_config(route_name='panel_close', renderer='json', xhr=True)
def panel_view(request):
    """Toggle the state of a panel.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    if 'panels' not in request.registry:
        return {}
    panel_id = request.matchdict['panel_id']
    if panel_id not in request.registry['panels']:
        return {}

    if request.matched_route.name == 'panel_open':
        request.registry['panels'][panel_id].open(request)
    else:
        request.registry['panels'][panel_id].close(request)
    return {}
