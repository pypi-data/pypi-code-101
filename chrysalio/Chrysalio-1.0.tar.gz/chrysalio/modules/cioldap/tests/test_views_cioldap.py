# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioldap.views.cioldap.`` class."""

from json import dumps
from collections import namedtuple
from cgi import FieldStorage

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from ....tests import DBUnitTestCase


# =============================================================================
class UViewsCioLDAPCioLDAPView(DBUnitTestCase):
    """Unit test class for testing
    :class:`modules.cioldap.views.cioldap.CioLDAPView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..models.dbldap import DBLdap, DBLdapProfile
        from ....models.dbprofile import DBProfile
        from ..lib.ldap import LDAP

        super(UViewsCioLDAPCioLDAPView, self).setUp()

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbldap = DBLdap(
            base='dc=iinov,dc=com',
            root_password='/ZSHiyU30mLjsr20KSXUoAD3tcragNnsQY+YxS2cIiA=',
            root_dn='cn=admin,dc=iinov,dc=com',
            user_dn='uid=_UID_,ou=people,dc=iinov,dc=com',
            user_filter='(&(objectclass=inetOrgPerson)(uid=_UID_))',
            field_first_name='givenName')
        dbldap.user_profiles.append(DBLdapProfile(profile_id='profile_viewer'))
        dbsession.add(dbldap)

        dbsession.add(DBProfile(
            profile_id='profile_creator',
            i18n_label=dumps({'en': 'Profile manager'})))
        dbsession.add(DBProfile(
            profile_id='profile_viewer',
            i18n_label=dumps({'en': 'Profile observer'})))
        dbsession.add(DBProfile(
            profile_id='user_viewer',
            i18n_label=dumps({'en': 'User account observer'})))

        self.configurator.add_route('home', '/')
        self.configurator.add_route('cioldap_edit', '/cioldap/edit')
        self.configurator.add_route('cioldap_view', '/cioldap/view')
        self.request.registry['authorities'] = {'ldap': LDAP()}

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.view]"""
        from ..views.cioldap import CioLDAPView
        from ..models.dbldap import DBLdap
        from ....tests import DummyPOST

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        self.request.matched_route = namedtuple('Route', 'name')(
            name='cioldap_view')

        # With a LDAP configuration
        response = CioLDAPView(self.request).view()
        self.assertIn('form', response)
        self.assertIn('profile_labels', response)
        self.assertIn('dbldap', response)
        self.assertIsInstance(response['dbldap'], DBLdap)
        self.assertEqual(
            self.request.breadcrumbs.current_title(),
            'CioLDAP Module Configuration')

        # Without a LDAP configuration
        for dbldap in dbsession.query(DBLdap):
            dbsession.delete(dbldap)
        response = CioLDAPView(self.request).view()
        self.assertIsInstance(response, HTTPFound)

        # Ajax call
        self.request.is_xhr = True
        self.request.POST = DummyPOST()
        response = CioLDAPView(self.request).view()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_view_export(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.view] export config"""
        from ..views.cioldap import CioLDAPView

        self.request.POST = {'exp!.x': True}

        response = CioLDAPView(self.request).view()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')

    # -------------------------------------------------------------------------
    def test_view_import(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.view] import config"""
        from ....tests import DummyPOST
        from . import TEST1_LDAP_XML
        from ..views.cioldap import CioLDAPView
        from ..models.dbldap import LDAP_CHECK_INTERVAL, DBLdap

        self.request.POST = DummyPOST({'imp!.x': True})
        response = CioLDAPView(self.request).view()
        self.assertIn('dbldap', response)
        self.assertIsInstance(response['dbldap'], DBLdap)
        self.assertEqual(
            response['dbldap'].check_interval, LDAP_CHECK_INTERVAL)

        with open(TEST1_LDAP_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_LDAP_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = CioLDAPView(self.request).view()
        self.assertEqual(response['dbldap'].check_interval, 0)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.edit] creation"""
        from ..views.cioldap import CioLDAPView
        from ..models.dbldap import DBLdap

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        self.request.matched_route = namedtuple('Route', 'name')(
            name='ldap_edit')
        for dbldap in dbsession.query(DBLdap):
            dbsession.delete(dbldap)

        response = CioLDAPView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('profile_labels', response)
        self.assertEqual(len(response['profile_labels']), 3)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'CioLDAP Module Edition')

    # -------------------------------------------------------------------------
    def test_edit_import(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.edit] import config"""
        from ....tests import DummyPOST
        from . import TEST1_LDAP_XML, TEST2_LDAP_XML
        from ..views.cioldap import CioLDAPView

        # A correct import
        self.request.POST = DummyPOST({'imp!.x': True})
        with open(TEST1_LDAP_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_LDAP_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = CioLDAPView(self.request).edit()
        self.assertIsInstance(response, HTTPFound)

        # With missing base
        with open(TEST2_LDAP_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST2_LDAP_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = CioLDAPView(self.request).edit()
        self.assertNotIsInstance(response, HTTPFound)

    # -------------------------------------------------------------------------
    def test_create_save(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.edit] save creation"""
        from ..views.cioldap import CioLDAPView
        from ..models.dbldap import DBLdap

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        self.request.matched_route = namedtuple('Route', 'name')(
            name='ldap_edit')
        self.request.POST = {
            'host': 'localhost', 'port': '389', 'check_interval': '60',
            'user_dn': 'uid=_UID_,ou=people,dc=iinov,dc=com',
            'user_filter': '(&(objectclass=inetOrgPerson)(uid=_UID_))',
            'field_name': 'sn', 'pfl:profile_viewer': True,
            'sav!.x': True}
        for dbldap in dbsession.query(DBLdap):
            dbsession.delete(dbldap)

        # Missing base
        response = CioLDAPView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('errors', errors[0])
        self.assertIn('form', response)

        # Correct form
        self.request.POST['base'] = 'cn=admin,dc=iinov,dc=com'
        CioLDAPView(self.request).edit()
        self.assertFalse(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.edit]"""
        from ..views.cioldap import CioLDAPView
        from ..models.dbldap import DBLdap

        self.request.matched_route = namedtuple('Route', 'name')(
            name='ldap_edit')

        response = CioLDAPView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('profile_labels', response)
        self.assertIn('dbldap', response)
        self.assertIsInstance(response['dbldap'], DBLdap)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'CioLDAP Module Edition')

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:modules.cioldap.views.cioldap.CioLDAPView.edit] save"""
        from ..views.cioldap import CioLDAPView

        self.request.POST = {
            'host': 'localhost', 'port': '389', 'check_interval': '60',
            'base': 'cn=admin,dc=iinov,dc=com',
            'user_dn': 'uid=_UID_,ou=people,dc=iinov,dc=com',
            'user_filter': '(&(objectclass=inetOrgPerson)(uid=_UID_))',
            'field_name': 'sn', 'pfl:profile_viewer': False,
            'pfl:user_viewer': True, 'sav!.x': True}

        CioLDAPView(self.request).edit()
        self.assertIsInstance(CioLDAPView(self.request).edit(), HTTPFound)
