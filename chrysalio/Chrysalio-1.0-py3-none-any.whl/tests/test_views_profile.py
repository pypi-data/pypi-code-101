# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``views.profile`` class."""

# pylint: disable = unused-import
from ..models.dbgroup import DBGroup  # noqa
# pylint: enable = unused-import
from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsProfileProfileView(DBUnitTestCase):
    """Unit test class for testing :class:`views.profile.ProfileView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from json import dumps
        from ..models.dbprofile import DBProfile, DBProfilePrincipal

        super(UViewsProfileProfileView, self).setUp()

        dbsession = self.request.dbsession

        record = {
            'profile_id': 'user_creator',
            'i18n_label': dumps({'en': 'User account manager'})}
        DBProfile.record_format(record)
        dbprofile = DBProfile(**record)
        dbprofile.principals.append(
            DBProfilePrincipal(principal='user.creator'))
        dbsession.add(dbprofile)

        record = {
            'profile_id': 'user_editor',
            'i18n_label': dumps({'en': 'User account editor'})}
        DBProfile.record_format(record)
        dbprofile = DBProfile(**record)
        dbprofile.principals.append(
            DBProfilePrincipal(principal='user.editor'))
        dbsession.add(dbprofile)

        self.configurator.add_route('home', '/')
        self.configurator.add_route('profile_index', '/profile/index')
        self.configurator.add_route('profile_create', '/profile/create')
        self.configurator.add_route(
            'profile_view', '/profile/view/{profile_id}')
        self.configurator.add_route(
            'profile_edit', '/profile/edit/{profile_id}')

    # -------------------------------------------------------------------------
    def test_index(self):
        """[u:views.profile.ProfileView.index]"""
        from collections import namedtuple
        from ..lib.filter import Filter
        from ..views.profile import ProfileView
        from . import DummyPOST

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_index')

        response = ProfileView(self.request).index()
        self.assertIn('pfilter', response)
        self.assertIsInstance(response['pfilter'], Filter)
        self.assertTrue(response['pfilter'].is_empty())
        self.assertIn('paging', response)
        self.assertIn('i_creator', response)
        self.assertIn('i_editor', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Profiles')

        self.request.is_xhr = True
        self.request.POST = DummyPOST()
        response = ProfileView(self.request).index()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_index_delete(self):
        """[u:views.profile.ProfileView.index] delete profile"""
        from ..models.dbprofile import DBProfile
        from ..views.profile import ProfileView

        dbsession = self.request.dbsession
        self.assertEqual(dbsession.query(DBProfile).count(), 2)

        self.request.POST = {'del!user_creator.x': True}
        ProfileView(self.request).index()
        self.assertEqual(dbsession.query(DBProfile).count(), 1)

    # -------------------------------------------------------------------------
    def test_index_import(self):
        """[u:views.profile.ProfileView.index] import profile"""
        from cgi import FieldStorage
        from . import TEST1_PFL_XML, DummyPOST
        from ..views.profile import ProfileView

        self.request.POST = DummyPOST({'imp!.x': True})
        response = ProfileView(self.request).index()
        self.assertIn('paging', response)
        self.assertNotIn(
            'user_viewer', [k.profile_id for k in response['paging']])

        with open(TEST1_PFL_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_PFL_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = ProfileView(self.request).index()
        self.assertIn('paging', response)
        self.assertIn(
            'user_viewer', [k.profile_id for k in response['paging']])

    # -------------------------------------------------------------------------
    def test_index_export(self):
        """[u:views.profile.ProfileView.index] export profile"""
        from pyramid.response import Response
        from ..views.profile import ProfileView

        self.request.POST = {'exp!foo.x': True}
        response = ProfileView(self.request).index()
        self.assertIsInstance(response, dict)

        self.request.POST = {'exp!user_creator.x': True}
        response = ProfileView(self.request).index()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'user_creator', response.body)

    # -------------------------------------------------------------------------
    def test_index_filter(self):
        """[u:views.profile.ProfileView.index_filter]"""
        from ..views.profile import ProfileView

        self.request.is_xhr = True
        self.request.params = {'field': 'i18n_label', 'value': 'user'}
        data = ProfileView(self.request).index_filter()
        self.assertIsInstance(data, list)
        self.assertIn('User account manager', data)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:views.profile.ProfileView.view]"""
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPNotFound
        from ..views.profile import ProfileView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_view')

        self.request.matchdict = {'profile_id': 'foo'}
        self.assertRaises(HTTPNotFound, ProfileView(self.request).view)

        self.request.matchdict = {'profile_id': 'user_creator'}
        response = ProfileView(self.request).view()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(),
            'Profile "User account manager"')

    # -------------------------------------------------------------------------
    def test_view_export(self):
        """[u:views.profile.ProfileView.view] export profiles"""
        from pyramid.response import Response
        from ..views.profile import ProfileView

        self.request.POST = {'exp!.x': True}
        self.request.matchdict = {'profile_id': 'user_creator'}

        response = ProfileView(self.request).view()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'user_creator', response.body)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[u:views.profile.ProfileView.edit] creation"""
        from collections import namedtuple
        from ..views.profile import ProfileView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_create')

        response = ProfileView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('label', response)
        self.assertIsNone(response['label'])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Profile Creation')

    # -------------------------------------------------------------------------
    def test_create_save(self):
        """[u:views.profile.ProfileView.edit] save creation"""
        from collections import namedtuple
        from ..views.profile import ProfileView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_create')
        self.request.POST = {
            'profile_id': 'user_editor',
            'label_en': 'User account observer',
            'description_en': 'These users can view user accounts.',
            'sav!.x': True}

        # Existing profile
        response = ProfileView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('exists', errors[0])
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Profile Creation')

        # New profile, missing label
        self.request.POST['profile_id'] = 'user_viewer'
        self.request.POST['label_en'] = ''
        ProfileView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])
        # pylint: disable = no-member
        self.request.dbsession.rollback()
        # pylint: enable = no-member

        # New profile OK
        self.request.POST['label_en'] = 'User account observer'
        ProfileView(self.request).edit()
        self.assertFalse(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:views.profile.ProfileView.edit]"""
        from collections import namedtuple
        from ..models.dbprofile import DBProfile
        from ..views.profile import ProfileView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_edit')
        self.request.matchdict = {'profile_id': 'user_editor'}

        response = ProfileView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('label', response)
        self.assertEqual(response['label'], 'User account editor')
        self.assertIn('dbprofile', response)
        self.assertIsInstance(response['dbprofile'], DBProfile)
        self.assertEqual(
            self.request.breadcrumbs.current_title(),
            'Profile "User account editor" Edition')

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:views.profile.ProfileView.edit] save"""
        from pyramid.httpexceptions import HTTPFound
        from ..security import PRINCIPALS
        from ..views.profile import ProfileView

        self.request.matchdict = {'profile_id': 'user_editor'}
        self.request.registry['principals'] = list(PRINCIPALS)
        self.request.POST = {
            'description_en': 'These users can edit and view user accounts.',
            'pcpl:user.viewer': True, 'sav!.x': True}

        ProfileView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])

        self.request.POST['label_en'] = 'User account editor'
        self.assertIsInstance(ProfileView(self.request).edit(), HTTPFound)


# =============================================================================
class FViewsProfileProfileView(FunctionalTestCase):
    """Functional test class for testing :class:`views.profile.ProfileView`."""

    # -------------------------------------------------------------------------
    def test_index(self):
        """[f:views.profile.ProfileView.index]"""
        self.login('test1')
        self.testapp.get('/profile/index', status=403)

        self.login('admin')
        response = self.testapp.get('/profile/index', status=200)
        self.assertIn(b'Profiles', response.body)
        self.assertIn(b'Create', response.body)
        self.assertIn(b'Import', response.body)
        self.assertIn(b'Export profile', response.body)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[f:views.profile.ProfileView.view]"""
        self.login('test1')
        self.testapp.get('/profile/view/user_editor', status=403)

        self.login('admin')
        response = self.testapp.get('/profile/view/user_editor', status=200)
        self.assertIn(b'Edit', response.body)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[f:views.profile.ProfileView.create]"""
        self.login('test1')
        self.testapp.get('/profile/create', status=403)

        self.login('admin')
        response = self.testapp.get('/profile/create', status=200)
        self.assertIn(b'Create', response.body)

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[f:views.profile.ProfileView.edit]"""
        self.login('test1')
        self.testapp.get('/profile/edit/user_editor', status=403)

        self.login('admin')
        response = self.testapp.get('/profile/edit/user_editor', status=200)
        self.assertIn(b'Save', response.body)
