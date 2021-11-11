# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioldap.models.populate`` functions."""

from ....tests import DBUnitTestCase
from ..models.dbldap import DBLdap


# =============================================================================
class UModelsPopulateXml2Db(DBUnitTestCase):
    """Unit test class for :func:`modules.cioldap.models.populate.xml2db`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modules.cioldap.models.populate.xml2db]"""
        from lxml import etree
        from ..models.populate import xml2db

        root_elt = etree.XML(
            '<cioldap xmlns="http://ns.chrysal.io/cioldap" version="1.0">'
            '  <ldap>'
            '    <base>dc=iinov,dc=com</base>'
            '    <user>'
            '      <dn>uid=_UID_,ou=people,dc=iinov,dc=com</dn>'
            '    </user>'
            '  </ldap>'
            '</cioldap>')
        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member

        self.assertFalse(xml2db(dbsession, root_elt, 'foo', True))
        self.assertEqual(len(xml2db(dbsession, root_elt, None, True)), 0)

        root_elt = etree.XML(
            '<cioldap xmlns="http://ns.chrysal.io/cioldap" version="1.0">'
            '</cioldap>')
        self.assertFalse(xml2db(dbsession, root_elt, 'ldap'))


# =============================================================================
class UModelsPopulateDb2Xml(DBUnitTestCase):
    """Unit test class for :func:`modules.cioldap.models.populate.db2xml`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modules.cioldap.models.populate.db2xml]"""
        from lxml import etree
        from ..models.populate import db2xml

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbsession.add(DBLdap(
            base='dc=iinov,dc=fr',
            user_dn='uid=_UID_,ou=people,dc=iinov,dc=com',
            user_filter='(&amp;(objectclass=inetOrgPerson)(uid=_UID_))',
            field_first_name='givenName',
            field_last_name='sn',
            field_email='mail'))
        namespace = 'http://ns.chrysal.io/cioldap'
        root_elt = etree.Element(
            '{{{0}}}cioldap'.format(namespace),
            nsmap={None: namespace}, version='1.0')

        db2xml(dbsession, root_elt)
        self.assertEqual(len(root_elt), 1)
