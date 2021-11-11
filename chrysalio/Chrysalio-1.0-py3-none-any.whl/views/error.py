"""Error view callables."""

from pyramid.view import view_config
from pyramid.view import notfound_view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED

from ..lib.i18n import _
from ..lib.form import button


# =============================================================================
@forbidden_view_config(renderer='chrysalio:Templates/error.pt')
@notfound_view_config(renderer='chrysalio:Templates/error.pt')
@view_config(context=HTTPBadRequest, renderer='chrysalio:Templates/error.pt',
             permission=NO_PERMISSION_REQUIRED)
@forbidden_view_config(renderer='json', xhr=True)
@notfound_view_config(renderer='json', xhr=True)
@view_config(context=HTTPBadRequest, renderer='json', xhr=True)
def error_view(request):
    """This view outputs an error message or redirects to login page.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    status = request.exception.status_int

    # AJAX
    if request.is_xhr:
        return {'error': status}

    # Not authenticated and 401 (unauthorized) or 403 (forbidden)
    if status in (401, 403) and request.authenticated_userid is None:
        return HTTPFound(
            request.route_path('login', _query=(('next', request.path),)))

    # Comment adjustment
    if status == 400 and \
       request.exception.title in ('Bad CSRF Token', 'Bad CSRF Origin'):
        request.exception.comment = _(
            'Access is denied: the server can not verify that your protection '
            'against cross-site request forgery (CSRF) is correct.')

    # 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found)
    request.response.status = status
    return {
        'title': _('Error ${status}', {'status': status}),
        'status': status,
        'message': request.exception.comment or {
            400: _('The server could not comply with the request since'
                   ' it is either malformed or otherwise incorrect.'),
            401: _('This server could not verify that you are authorized to'
                   ' access the document you requested.'),
            403: _('Access was denied to this resource.'),
            404: _('The resource could not be found.'),
            500: _('Internal Server Error.')}.get(
                status, request.exception.explanation),
        'button': button}
