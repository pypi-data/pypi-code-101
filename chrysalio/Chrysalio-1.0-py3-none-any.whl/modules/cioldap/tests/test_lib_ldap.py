# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioldap.lib.ldap.LDAP`` class."""

from ....tests import DBUnitTestCase

from ..models.dbldap import DBLdap


# =============================================================================
class UViews(DBUnitTestCase):
    """Unit test class for testing
    :class:`modules.cioldap.lib.LDAP`."""

    # -------------------------------------------------------------------------
    def _add_ldap_settings(self):
        """Add LDAP settings."""
        from ..models.dbldap import DBLdapProfile

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbldap = DBLdap(
            host='ipa.demo1.freeipa.org',
            base='dc=demo1,dc=freeipa,dc=org',
            check_interval=0,
            user_dn='uid=_UID_,cn=users,cn=accounts,dc=demo1,'
            'dc=freeipa,dc=org',
            user_filter='(&(objectclass=person)(uid=_UID_))',
            field_first_name='givenName')
        dbsession.add(dbldap)
        dbsession.flush()
        dbldap.user_profiles.append(DBLdapProfile(profile_id='profile_viewer'))
        return dbldap

    # -------------------------------------------------------------------------
    def test_get(self):
        """[u:modules.cioldap.lib.ldap.LDAP.get]"""
        from json import dumps
        from webob.acceptparse import AcceptLanguageValidHeader
        from ....models.dbuser import DBUser
        from ....models.dbprofile import DBProfile
        from ..lib.ldap import LDAP

        self.request.accept_language = AcceptLanguageValidHeader(
            'fr-FR, fr;q=0.8, en-US;q=0.5, en;q=0.3')

        # Without password
        error = LDAP().get(self.request, 'user100', None, DBUser)[1]
        self.assertEqual('Password is mandatory.', error)

        # Without base
        error = LDAP().get(self.request, 'user100', 'user100pwd', DBUser)[1]
        self.assertEqual('LDAP configuration is missing.', error)

        # With an unknown user
        self._add_ldap_settings()
        ldap = LDAP()
        error = ldap.get(self.request, 'foo', 'Secret123', DBUser)[1]
        self.assertEqual('ID or password is incorrect.', error)

        # With a known user and unknown profile
        dbuser, error = ldap.get(self.request, 'admin', 'Secret123', DBUser)
        if error == 'ID or password is incorrect.':
            return
        self.assertIsNotNone(error)
        self.assertIn('without email', error)

        # With a known user and unknown profile
        dbuser, error = ldap.get(
            self.request, 'employee', 'Secret123', DBUser)
        if error != 'ID or password is incorrect.':
            self.assertIsInstance(dbuser, DBUser)
            self.assertEqual(dbuser.first_name, 'Test')
            self.assertEqual(dbuser.last_name, 'Employee')
            self.assertEqual(dbuser.email, 'employee@demo1.freeipa.org')
            self.assertFalse(dbuser.profiles)

        # With a known user and known profile
        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbsession.add(DBProfile(
            profile_id='profile_viewer',
            i18n_label=dumps({'en': 'User profile viewer'})))
        dbuser, error = ldap.get(self.request, 'helpdesk', 'Secret123', DBUser)
        if error != 'ID or password is incorrect.':
            self.assertTrue(dbuser.profiles)

    # -------------------------------------------------------------------------
    def test_check(self):
        """[u:modules.cioldap.lib.ldap.LDAP.check]"""
        from ....lib.utils import encrypt
        from ....models.dbuser import DBUser
        from ..lib.ldap import LDAP

        dbuser = DBUser(
            login='test2', status='active', first_name='Guy',
            last_name='LIGUILI', honorific='Mr', email='test2@chrysal.io',
            authority='ldap')
        dbuser.set_password('test2pwd')

        # Without base
        error = LDAP().check(self.request, 'test2', 'employeepwd', dbuser)
        self.assertEqual('LDAP configuration is missing.', error)

        # With an unknown user
        dbldap = self._add_ldap_settings()
        ldap = LDAP()
        error = ldap.check(self.request, 'test2', 'test2pwd', dbuser)
        self.assertEqual('ID or password is incorrect.', error)

        # With a known user and an invalid password
        dbuser = DBUser(
            login='employee', status='active', first_name='Guy',
            last_name='LIGUILI', honorific='Mr', email='employee@chrysal.io',
            authority='ldap')
        dbuser.set_password('employeepwd')
        error = ldap.check(self.request, 'employee', 'employeepwd', dbuser)
        self.assertEqual('ID or password is incorrect.', error)

        # With a known user and a valid password
        error = ldap.check(self.request, 'employee', 'Secret123', dbuser)
        if error == 'ID or password is incorrect.':
            return
        self.assertIsNone(error)

        # Without password and an anonymous connection
        error = ldap.check(self.request, 'employee', None, dbuser)
        self.assertIsNone(error)

        # With cache
        dbldap.check_interval = 500
        ldap = LDAP()
        error = ldap.check(self.request, 'employee', None, dbuser)
        self.assertIsNone(error)
        error = ldap.check(self.request, 'employee', None, dbuser)
        self.assertIsNone(error)

        # Without password and with root_dn/root_password
        dbldap.check_interval = 0
        dbldap.root_dn = \
            'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org'
        dbldap.root_password = encrypt('Secret123', 'ldap')
        error = LDAP().check(self.request, 'employee', None, dbuser)
        if error == 'ID or password is incorrect.':
            return
        self.assertIsNone(error)

        # With an invalid filter
        dbldap.base = 'dc=demo1,dc=freeipa2,dc=org'
        error = LDAP().check(self.request, 'employee', 'Secret123', dbuser)
        self.assertEqual(
            error, 'LDAP: unable to retrieve user information.')

        # With an invalid filter
        dbldap.user_filter = '(&(objectclass=group)(uid=_UID_))'
        error = LDAP().check(self.request, 'employee', 'Secret123', dbuser)
        self.assertIn('incorrect filter', error)
