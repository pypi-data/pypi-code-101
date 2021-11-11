# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioldap.models.dbldap`` classes."""

from ....tests import DBUnitTestCase
from ..models.dbldap import DBLdap


# =============================================================================
class UModelsDBLdapDBLdap(DBUnitTestCase):
    """Unit test class for :class:`modules.cioldap.models.dbldap.DBLdap`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _make_one(cls):
        """Make an `DBLdap`` object."""
        from ..models.dbldap import DBLdapProfile

        dbldap = DBLdap(
            ssl=True,
            base='dc=iinov,dc=com',
            root_dn='cn=admin,dc=iinov,dc=com',
            root_password='/ZSHiyU30mLjsr20KSXUoAD3tcragNnsQY+YxS2cIiA=',
            user_dn='uid=_UID_,ou=people,dc=iinov,dc=com',
            user_filter='(&(objectclass=inetOrgPerson)(uid=_UID_))',
            field_first_name='givenName',
            field_last_name='sn',
            field_email='mail')
        dbldap.user_profiles.append(DBLdapProfile(profile_id='profile_viewer'))

        return dbldap

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:.modules.cioldap.models.dbldap.DBLdap.xml2db]"""
        from lxml import etree

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbsession.add(DBLdap(
            base='dc=iinov,dc=fr',
            user_dn='uid=_UID_,ou=people,dc=iinov,dc=com',
            user_filter='(&(objectclass=inetOrgPerson)(uid=_UID_))',
            field_first_name='givenName'))

        # Without element
        self.assertIsNone(DBLdap.xml2db(dbsession, None))
        self.assertTrue(dbsession.query(DBLdap).first())

        # With an incorrect configuration
        ldap_elt = etree.XML(
            '<ldap xmlns="http://ns.chrysal.io/cioldap">'
            '  <user>'
            '    <dn>uid=_UID_,ou=people,dc=iinov,dc=com</dn>'
            '  </user>'
            '</ldap>')
        self.assertIsNotNone(DBLdap.xml2db(dbsession, ldap_elt))
        self.assertFalse(dbsession.query(DBLdap).first())

        # With a correct configuration
        ldap_elt = etree.XML(
            '<ldap xmlns="http://ns.chrysal.io/cioldap">'
            '  <base>dc=iinov,dc=com</base>'
            '  <user>'
            '    <dn>uid=_UID_,ou=people,dc=iinov,dc=com</dn>'
            '    <profiles>'
            '      <profile>profile_viewer</profile>'
            '      <profile>user_viewer</profile>'
            '    </profiles>'
            '  </user>'
            '</ldap>')
        self.assertIsNone(DBLdap.xml2db(dbsession, ldap_elt))
        dbldap = dbsession.query(DBLdap).first()
        self.assertIsInstance(dbldap, DBLdap)
        self.assertEqual(dbldap.host, 'localhost')
        self.assertEqual(dbldap.base, 'dc=iinov,dc=com')
        self.assertEqual(dbldap.user_dn, 'uid=_UID_,ou=people,dc=iinov,dc=com')
        user_profiles = [k.profile_id for k in dbldap.user_profiles]
        self.assertIn('profile_viewer', user_profiles)
        self.assertIn('user_viewer', user_profiles)

    # -------------------------------------------------------------------------
    def test_record_from_xml(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.record_from_xml]"""
        from lxml import etree
        from ..models.dbldap import LDAP_CHECK_INTERVAL

        ldap_elt = etree.XML(
            '<ldap xmlns="http://ns.chrysal.io/cioldap">'
            '  <ssl>true</ssl>'
            '  <dn>cn=admin,dc=iinov,dc=com</dn>'
            '  <password>sesame</password>'
            '  <base>dc=iinov,dc=com</base>'
            '  <user>'
            '    <dn>uid=_UID_,ou=people,dc=iinov,dc=com</dn>'
            '    <last-name>sn</last-name>'
            '    <profiles>'
            '      <profile>profile_viewer</profile>'
            '    </profiles>'
            '  </user>'
            '</ldap>')
        record = DBLdap.record_from_xml(ldap_elt)
        self.assertIn('host', record)
        self.assertIn('port', record)
        self.assertEqual(record['port'], 389)
        self.assertIn('ssl', record)
        self.assertTrue(record['ssl'])
        self.assertIn('check_interval', record)
        self.assertEqual(record['check_interval'], LDAP_CHECK_INTERVAL)

    # -------------------------------------------------------------------------
    def test_record_format(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.record_format]"""

        # ldap_id, root_password without root_dn, no base
        record = {'host': None, 'root_password': 'sesame'}
        error = DBLdap.record_format(record)
        self.assertNotIn('host', record)
        self.assertNotIn('root_password', record)
        self.assertIsNotNone(error)
        self.assertIn('No base', error)

        # root_password with root_dn, without user_dn
        record = {
            'root_dn': 'cn=admin,dc=iinov,dc=com', 'root_password': 'sesame',
            'base': 'dc=iinov,dc=com'}
        error = DBLdap.record_format(record)
        self.assertIn('root_password', record)
        self.assertTrue(record['root_password'].endswith('='))
        self.assertIsNotNone(error)
        self.assertIn('No DN', error)

        # user_dn without _UID_
        record['user_dn'] = 'uid=_FOO_,ou=people,dc=iinov,dc=com'
        error = DBLdap.record_format(record)
        self.assertIsNotNone(error)
        self.assertIn('_UID_', error)

        # Ok
        record['user_dn'] = 'uid=_UID_,ou=people,dc=iinov,dc=com'
        self.assertIsNone(DBLdap.record_format(record))

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.db2xml]"""
        dbldap = self._make_one()
        ldap_elt = dbldap.db2xml()
        self.assertEqual(ldap_elt.findtext('base'), 'dc=iinov,dc=com')
        self.assertEqual(
            ldap_elt.findtext('user/profiles/profile'), 'profile_viewer')

    # -------------------------------------------------------------------------
    def test_attachments2directory(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.attachments2directory]"""
        from os.path import exists
        from ....tests import ATTACHMENTS_DIR, TEST_DIR

        DBLdap.attachments2directory(ATTACHMENTS_DIR, TEST_DIR)
        self.assertFalse(exists(TEST_DIR))

    # -------------------------------------------------------------------------
    def test_sheet4view(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.sheet4view]"""
        from ....lib.form import Form

        profile_labels = {'profile_viewer': 'Profile viewer'}
        dbldap = self._make_one()
        html = dbldap.sheet4view(
            self.request, Form(self.request), profile_labels)
        self.assertIn('Profile viewer', html)

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.settings_schema]"""
        from colander import SchemaNode
        from ..models.dbldap import LDAP_CHECK_INTERVAL

        profiles = {
            'profile_viewer': 'Profile viewer', 'user_viewer': 'User viewer'}

        # Creation mode
        schema, defaults = DBLdap.settings_schema(profiles)
        self.assertIsInstance(schema, SchemaNode)
        serialized = schema.serialize()
        self.assertIn('host', serialized)
        self.assertIn('user_dn', serialized)
        self.assertIn('pfl:profile_viewer', serialized)
        self.assertIsInstance(defaults, dict)
        self.assertIn('host', defaults)
        self.assertIn('port', defaults)
        self.assertIn('check_interval', defaults)
        self.assertEqual(defaults['check_interval'], LDAP_CHECK_INTERVAL)

        # Edition mode
        schema, defaults = DBLdap.settings_schema(profiles, self._make_one())
        self.assertIsInstance(defaults, dict)
        self.assertIn('pfl:profile_viewer', defaults)
        self.assertNotIn('pfl:user_viewer', defaults)

    # -------------------------------------------------------------------------
    def test_sheet4edit(self):
        """[u:modules.cioldap.models.dbldap.DBLdap.sheet4edit]"""
        from ....lib.form import Form

        profiles = {
            'profile_viewer': 'Profile viewer', 'user_viewer': 'User viewer'}
        dbldap = self._make_one()
        html = dbldap.sheet4edit(self.request, Form(self.request), profiles)
        self.assertIn('Attributed Profiles:', html)
