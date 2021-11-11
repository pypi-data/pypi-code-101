"""Security functionalities."""

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated, Everyone, Allow, ALL_PERMISSIONS

from .lib.i18n import _
from .lib.log import log_info
from .models.dbuser import DBUser


PRINCIPALS = (
    ('mode', _('Mode management'), [
        ('admin', _('Access to administration mode'), ('mode-admin',)),
        ('job', _('Access to job mode'), ('mode-job',))
    ]),
    ('group', _('Group management'), (
        ('viewer', _('View all groups'), (
            'group-view',)),
        ('editor', _('Edit or view any group'), (
            'group-edit', 'group-view')),
        ('creator', _('Create a new one or edit or view any group'), (
            'group-create', 'group-edit', 'group-view'))
    )),
    ('user', _('User management'), (
        ('viewer', _('View all users'), (
            'user-view',)),
        ('editor', _('Edit or view any user'), (
            'user-edit', 'user-view')),
        ('creator', _('Create a new one or edit or view any user'), (
            'user-create', 'user-edit', 'user-view'))
    )),
    ('profile', _('Profile management'), (
        ('viewer', _('View any profile'), (
            'profile-view',)),
        ('editor', _('Edit or view any profile'), (
            'profile-edit', 'profile-view')),
        ('creator', _('Create a new one or edit or view any profile'), (
            'profile-create', 'profile-edit', 'profile-view'))
    )),
    ('settings', _('General settings management'), (
        ('viewer', _('View general settings'), (
            'settings-view',)),
        ('editor', _('Edit or view general settings'), (
            'settings-edit', 'settings-view'))
    )),
    ('backup', _('Backup management'), (
        ('creator', _('Backup and restore'), (
            'backup-create',)),
    ))
)


# =============================================================================
def includeme(configurator):
    """Function to include authentication mechanism.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    settings = configurator.get_settings()
    configurator.set_authorization_policy(ACLAuthorizationPolicy())
    configurator.set_authentication_policy(SessionAuthenticationPolicy(
        secret=settings.get('auth.secret', '-'), hashalg='sha512',
        cookie_name=settings.get('auth.cookie', 'CIO_AUTH'),
        secure=settings.get('auth.secure') == 'true',
        http_only=True, samesite=settings.get('auth.samesite', 'Strict')))
    configurator.set_root_factory(RootFactory)
    configurator.registry['principals'] = list(PRINCIPALS)


# =============================================================================
class SessionAuthenticationPolicy(AuthTktAuthenticationPolicy):
    """Authentication policy class based on session."""

    _DBUser = DBUser

    # -------------------------------------------------------------------------
    def authenticated_userid(self, request):
        """Return the authenticated :term:`userid` or ``None`` if
        no authenticated user ID can be found.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: :class:`str` or ``None``
        """
        user = self._user(request)
        if user is not None:
            return user['user_id']
        return None

    # -------------------------------------------------------------------------
    def effective_principals(self, request):
        """Return a list of principals including, at least,
        :class:`pyramid.security.Everyone`.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :return: (list)
        """
        principals = [Everyone]
        user = self._user(request)
        if user is not None:
            principals.append(Authenticated)
            principals += user['principals']
        return principals

    # -------------------------------------------------------------------------
    @classmethod
    def _user(cls, request):
        """Get user from session.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: dict
        """
        # Already authenticated
        login = request.unauthenticated_userid
        if login and 'user' in request.session and \
           request.session['user']['login'] == login:
            return request.session['user']

        # Auto login
        dbuser = cls._DBUser.get(request, login)[0]
        if dbuser is not None and not dbuser.password_mustchange:
            # pylint: disable = no-member
            dbuser.set_session(request)
            log_info(request, 'autologin')
            return request.session['user']
        if dbuser is not None and dbuser.password_mustchange:
            request.session['user'] = {'login': ''}

        return None


# =============================================================================
class RootFactory(object):
    """Access Control List (ACL) definition.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    # pylint: disable = too-few-public-methods
    __acl__ = [
        (Allow, Authenticated, 'authenticated'),
        (Allow, 'system.administrator', ALL_PERMISSIONS)] + [
            (Allow, '{0}.{1}'.format(group[0], principal[0]), principal[2])
            for group in PRINCIPALS for principal in group[2]]

    # -------------------------------------------------------------------------
    def __init__(self, request):
        """Constructor method."""
