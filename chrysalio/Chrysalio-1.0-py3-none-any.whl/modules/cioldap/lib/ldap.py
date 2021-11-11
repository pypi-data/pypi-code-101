"""Class to manage LDAP as an authority for authentication."""

from datetime import datetime

from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPBindError, LDAPSocketOpenError
from ldap3.core.exceptions import LDAPObjectClassError
from ldap3.core.exceptions import LDAPPasswordIsMandatoryError

from ....lib.i18n import _
from ....lib.utils import decrypt
from ....lib.config import settings_get_list
from ....lib.log import log_error
from ....models.dbprofile import DBProfile
from ....models.dbuser import DBUserProfile
from ..models.dbldap import DBLdap


# =============================================================================
class LDAP(object):
    """Authority class to manage LDAP authentication.

    It reads its parameters in its SQL table. The default values are:

    * host: localhost
    * port: 389
    * ssl: false
    * check_interval: 0 (no cache)
    * user_filter: (&(objectclass=inetOrgPerson)(uid=_UID_))
    * field_firstname: givenName
    * field_lastname: sn
    * field_email: mail
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        """Constructor method."""
        self._settings = {
            'host': 'localhost',
            'port': 389,
            'ssl': False,
            'check_interval': 0,
            'root_dn': None,
            'root_password': None,
            'base': None,
            'user_dn': None,
            'user_filter': '(&(objectclass=inetOrgPerson)(uid={uid}))',
            'field_first_name': 'givenName',
            'field_last_name': 'sn',
            'field_email': 'mail',
            'user_profiles': []}

    # -------------------------------------------------------------------------
    def get(self, request, login, password, dbuser_class):
        """Get user from LDAP server.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str login:
            Login of the user to authenticate.
        :param str password:
            Clear password.
        :type  dbuser_class: .models.dbuser.DBUser
        :param dbuser_class:
            The SQL class to create a user.
        :rtype: tuple
        :return:
            A tuple like ``(dbuser, error)``. It can be ``(None, None)``
        """
        if not password:
            return None, _('Password is mandatory.')
        self._load_configuration(request)
        if self._settings['base'] is None:
            return None, _('LDAP configuration is missing.')

        # Create user
        record, error = self._user_record(request, login, password)
        if error:
            return None, error
        now = datetime.now()
        language = request.accept_language.lookup(
            settings_get_list(
                request.registry.settings, 'languages', ['en']),
            default_tag=request.registry['settings']['language'])
        record.update({
            'login': login, 'password': password,
            'language': language, 'last_login': now,
            'account_creation': now, 'authority': 'ldap',
            'authority_check': now})
        error = dbuser_class.record_format(record)
        if error:  # pragma: nocover
            return None, error
        dbuser = dbuser_class(**record)
        request.dbsession.add(dbuser)
        request.dbsession.flush()

        # Add profiles
        if self._settings['user_profiles']:
            available = [k[0] for k in request.dbsession.query(
                DBProfile.profile_id).all()]
            for profile_id in self._settings['user_profiles']:
                if profile_id not in available:
                    log_error(
                        request, 'unknown profile {0}'.format(profile_id))
                else:
                    request.dbsession.add(DBUserProfile(
                        user_id=dbuser.user_id, profile_id=profile_id))

        return dbuser, None

    # -------------------------------------------------------------------------
    def check(self, request, login, password, dbuser):
        """Check user authorization according to LDAP server.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str login:
            Login of the user to authenticate.
        :param str password:
            Clear password.
        :type  dbuser: .models.dbuser.DBUser
        :param dbuser:
            The SQL object of the user to check.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        self._load_configuration(request)
        if self._settings['base'] is None:
            return _('LDAP configuration is missing.')

        if dbuser.authority_check and \
           (datetime.now() - dbuser.authority_check).total_seconds() \
           < self._settings['check_interval']:
            return None

        # Information update
        record, error = self._user_record(request, login, password)
        if error:
            return error

        # Update database
        modified = False
        for field in record:
            if getattr(dbuser, field) != record[field]:
                setattr(dbuser, field, record[field])
                modified = True
        if modified:
            dbuser.account_update = datetime.now()
        dbuser.authority_check = datetime.now()
        dbuser.last_login = datetime.now()
        return None

    # -------------------------------------------------------------------------
    def reset_configuration(self):
        """Reset the configuration."""
        self._settings['base'] = None

    # -------------------------------------------------------------------------
    def _user_record(self, request, login, password):
        """Check user authorization according to LDAP server and retrieve
        information about the user.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str login:
            User login.
        :param str password:
            Clear password.
        :rtype: tuple
        :return:
            A tuple such as ``(record, error)`` where ``record`` is a
            dictionary containing user information.
        """
        # Connection to LDAP server
        connection = self._ldap_connection(request, login, password)
        if connection is None:
            return None, _('ID or password is incorrect.')

        # Retrieve information from LDAP server
        fields = ('last_name', 'first_name', 'email')
        fields = [k for k in fields if self._settings['field_{0}'.format(k)]]
        try:
            connection.search(
                self._settings['base'],
                self._settings['user_filter'].format(uid=login),
                attributes=[
                    self._settings['field_{0}'.format(k)] for k in fields])
        except LDAPObjectClassError:
            return None, _('LDAP: incorrect filter "${f}".',
                           {'f': self._settings['user_filter']})
        if len(connection.entries) != 1:
            return None, _('LDAP: unable to retrieve user information.')

        attributes = connection.entries[0].entry_raw_attributes
        record = {
            k: attributes[
                self._settings['field_{0}'.format(k)]][0].decode('utf8')
            for k in fields
            if attributes[self._settings['field_{0}'.format(k)]]}

        return record, None

    # -------------------------------------------------------------------------
    def _ldap_connection(self, request, login, password):
        """Establish a connection with the LDAP server.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str login:
            User login.
        :param str password:
            Clear password.
        :rtype: ldap3.Connection
        """
        server = Server(
            self._settings['host'], self._settings['port'],
            use_ssl=self._settings['ssl'])
        try:
            if password is not None:
                connection = Connection(
                    server, self._settings['user_dn'].format(login),
                    password, auto_bind=True)
            elif self._settings['root_dn']:
                connection = Connection(
                    server, self._settings['root_dn'],
                    decrypt(self._settings['root_password'], 'ldap'),
                    auto_bind=True)
            else:
                connection = Connection(server, auto_bind=True)
        except (LDAPBindError, LDAPSocketOpenError,
                LDAPPasswordIsMandatoryError) as error:
            log_error(request, error)
            return None
        return connection

    # -------------------------------------------------------------------------
    def _load_configuration(self, request):
        """Possibly load configuration from database.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        if self._settings['base'] is not None:
            return

        dbldap = request.dbsession.query(DBLdap).first()
        if dbldap is None:
            return

        self._settings = {k: getattr(dbldap, k) for k in self._settings}
        self._settings['port'] = int(self._settings['port'])
        self._settings['user_dn'] = self._settings['user_dn'].replace(
            '_UID_', '{0}')
        self._settings['user_filter'] = self._settings['user_filter'].replace(
            '_UID_', '{uid}')
        # pylint: disable = no-member
        self._settings['user_profiles'] = [
            k.profile_id for k in dbldap.user_profiles]
