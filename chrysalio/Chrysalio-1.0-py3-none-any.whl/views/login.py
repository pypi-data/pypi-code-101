"""Manager login view callables."""

from time import time
from datetime import date
from hashlib import sha1

from colander import Mapping, SchemaNode, String, Boolean

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import forget, remember

from ..lib.form import Form
from ..lib.log import log_info
from ..models.dbuser import DBUser


# =============================================================================
def login(request, dbuser_class=DBUser):
    """This view renders a login form and processes the post checking
    credentials.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :type  dbuser_class: .models.dbuser.DBuser
    :param dbuser_class: (default=DBUser)
        Class to manage user.
    """
    # Next step
    next_path = request.params.get('next') \
        or (request.url != request.route_url('login') and request.url) \
        or request.route_url('home')

    # Create form
    schema = SchemaNode(Mapping())
    schema.add(SchemaNode(String(), name='login'))
    schema.add(SchemaNode(String(), name='password'))
    schema.add(SchemaNode(Boolean(), name='remember', missing=False))
    form = Form(request, schema=schema, defaults={'next': next_path})

    # Validate form
    if form.validate():
        dbuser, error = dbuser_class.get(request)
        if dbuser is not None and dbuser.password_mustchange:
            token = '{0}{1}'.format(dbuser.login, date.today().isoformat())
            token = sha1(token.encode('utf8')).hexdigest()
            return HTTPFound(request.route_path(
                'user_password_reset', user_id=dbuser.user_id, token=token))
        if dbuser is not None:
            dbuser.set_session(request)
            log_info(request, 'login')
            max_age = request.registry['settings']['remember-me'] \
                if form.values['remember'] else None
            return HTTPFound(location=next_path, headers=remember(
                request, request.session['user']['login'], max_age=max_age))
        request.session.flash(error, 'alert')

    return {'form': form, 'next': next_path}


# =============================================================================
@view_config(route_name='logout')
def logout(request):
    """This view will clear the credentials of the logged in user and redirect
    back to the login page.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    if 'user' in request.session:
        log_info(request, 'logout')
    request.session.clear()
    request.session['_creation_time'] = time()
    request.session['_accessed_time'] = time()
    return HTTPFound(
        location=request.route_path('login'), headers=forget(request))
