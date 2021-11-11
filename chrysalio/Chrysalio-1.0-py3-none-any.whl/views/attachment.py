"""Attachment view callables."""

from os import sep
from os.path import join, dirname

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import FileResponse
from pyramid.asset import abspath_from_asset_spec
from pyramid.security import NO_PERMISSION_REQUIRED


# =============================================================================
@view_config(route_name='attachment')
def attachment(request):
    """Output an attachment file.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    attachments = request.registry.settings.get('attachments')
    if not attachments:
        raise HTTPNotFound()

    try:
        return FileResponse(
            join(attachments, sep.join(request.matchdict['path'])),
            request=request, cache_max_age=3600)
    except OSError:
        raise HTTPNotFound()


# =============================================================================
@view_config(route_name='favicon', permission=NO_PERMISSION_REQUIRED)
def favicon(request):
    """Output the `favicon.ico` file.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    settings = request.registry.settings
    if settings.get('site.favicon'):
        icon = abspath_from_asset_spec(settings['site.favicon'])
    else:
        icon = join(dirname(__file__), '..', 'Static', 'favicon.ico')
    return FileResponse(icon, request=request, cache_max_age=3600)


# =============================================================================
@view_config(route_name='robots', permission=NO_PERMISSION_REQUIRED)
def robots(request):
    """Output the `robots.txt` file.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    settings = request.registry.settings
    if settings.get('site.robots'):
        robots_file = abspath_from_asset_spec(settings['site.robots'])
    else:
        robots_file = join(dirname(__file__), '..', 'Static', 'robots.txt')
    return FileResponse(robots_file, request=request, cache_max_age=3600)
