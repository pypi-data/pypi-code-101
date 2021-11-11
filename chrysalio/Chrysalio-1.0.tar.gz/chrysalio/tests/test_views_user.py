# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``views.user`` methods."""

from ..models.dbgroup import DBGroup
from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsUserUserView(DBUnitTestCase):
    """Unit test class for testing :class:`views.user.UserView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""

        super(UViewsUserUserView, self).setUp()

        self.add_user({
            'login': 'admin', 'status': 'administrator', 'last_name': 'ADMIN',
            'password': 'adminpwd', 'email': 'admin@chrysal.io'})
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        self.add_user({
            'login': 'test2', 'first_name': 'Sophie', 'last_name': 'FONFEC',
            'password': 'test2pwd', 'email': 'test2@chrysal.io',
            'attachments_key': 'User2'})
        self.add_user({
            'login': 'test3', 'first_name': 'Guy', 'last_name': 'LIGUILI',
            'password': 'test3pwd', 'email': 'test3@chrysal.io',
            'attachments_key': 'User3'})

        self.configurator.add_route('home', '/')
        self.configurator.add_route('user_index', '/user/index')
        self.configurator.add_route('user_create', '/user/create')
        self.configurator.add_route('user_edit', '/user/edit/{user_id}')
        self.configurator.add_route('user_view', '/user/view/{user_id}')
        self.configurator.add_route(
            'user_password_reset', '/user/password/reset/{user_id}/{token}')

    # -------------------------------------------------------------------------
    def test_index(self):
        """[u:views.user.UserView.index]"""
        from collections import namedtuple
        from ..lib.filter import Filter
        from ..lib.paging import Paging
        from ..views.user import UserView
        from . import DummyPOST

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')

        # Normal HTTP
        response = UserView(self.request).index()
        self.assertIn('pfilter', response)
        self.assertIn('paging', response)
        self.assertIn('i_creator', response)
        self.assertIn('i_editor', response)
        self.assertIsInstance(response['pfilter'], Filter)
        self.assertFalse(response['pfilter'].is_empty())
        self.assertIsInstance(response['paging'], Paging)
        self.assertTrue(response['i_creator'])
        self.assertTrue(response['i_editor'])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Users')

        # Ajax
        self.request.is_xhr = True
        self.request.POST = DummyPOST()
        response = UserView(self.request).index()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_index_send_invitation(self):
        """[u:views.user.UserView.index] send invitation"""
        from ..views.user import UserView

        self.request.registry['settings']['title'] = 'Chrysalio'
        self.request.registry.settings['smtp.host'] = 'foo'
        self.request.session['user'] = {
            'user_id': 1, 'login': 'test1', 'email': 'test1@chrysal.io'}
        self.request.POST = {'mel!1.x': True}

        UserView(self.request).index()
        self.assertTrue(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_index_delete(self):
        """[u:views.user.UserView.index] delete user"""
        from os import makedirs
        from os.path import join, exists
        from . import TEST_DIR
        from ..views.user import UserView
        from ..models.dbuser import DBUser

        dbsession = self.request.dbsession
        self.assertEqual(dbsession.query(DBUser).count(), 4)
        self.request.session['user'] = {'user_id': 1}
        attachments = join(TEST_DIR, 'Attachments')
        self.request.registry.settings['attachments'] = attachments

        self.request.POST = {'del!1.x': True}
        UserView(self.request).index()
        self.assertEqual(dbsession.query(DBUser).count(), 4)

        self.request.session['user'] = {'user_id': 2}
        UserView(self.request).index()
        self.assertEqual(dbsession.query(DBUser).count(), 4)

        makedirs(join(attachments, 'Users', 'User2'))
        self.request.POST = {'del!3.x': True}
        UserView(self.request).index()
        self.assertEqual(dbsession.query(DBUser).count(), 3)
        self.assertFalse(exists(join(attachments, 'Users', 'User2')))

    # -------------------------------------------------------------------------
    def test_index_import(self):
        """[u:views.user.UserView.index] import users"""
        from os.path import join, exists
        from cgi import FieldStorage
        from . import TEST_DIR, TEST1_USR_ZIP, TEST3_USR_XML, DummyPOST
        from ..models.dbuser import DBUser
        from ..views.user import UserView

        self.request.POST = DummyPOST({'imp!.x': True})
        response = UserView(self.request).index()
        self.assertIn('paging', response)
        self.assertNotIn('user1', [k.login for k in response['paging']])

        self.request.registry.settings['attachments'] = TEST_DIR
        with open(TEST1_USR_ZIP, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_USR_ZIP
            input_file.file = hdl
            self.request.POST.multikeys = {'file': (input_file,)}
            response = UserView(self.request).index()
        self.assertIn('paging', response)
        self.assertIn('user3', [k.login for k in response['paging']])
        self.assertTrue(exists(join(
            TEST_DIR, DBUser.attachments_dir, 'User3', 'user3.svg')))

        with open(TEST3_USR_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST3_USR_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = UserView(self.request).index()
        self.assertIn('paging', response)
        self.assertIn('user1', [k.login for k in response['paging']])

    # -------------------------------------------------------------------------
    def test_index_export(self):
        """[u:views.user.UserView.index] export users"""
        from pyramid.response import Response
        from ..views.user import UserView

        self.request.POST = {'exp!1.x': True}
        UserView(self.request).index()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('cannot export', errors[0])

        self.request.POST = {'exp!2.x': True}
        response = UserView(self.request).index()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'test1', response.body)

    # -------------------------------------------------------------------------
    def test_index_filter(self):
        """[u:views.user.UserView.index_filter]"""
        from ..views.user import UserView

        self.request.is_xhr = True
        self.request.params = {'field': 'login', 'value': 'test'}
        data = UserView(self.request).index_filter()
        self.assertIsInstance(data, list)
        self.assertIn('test1', data)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:views.user.UserView.view]"""
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden
        from ..views.user import UserView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_view')
        self.request.session['user'] = {'user_id': 1}

        self.request.matchdict = {'user_id': 'foo'}
        self.assertRaises(HTTPNotFound, UserView(self.request).view)

        self.request.matchdict = {'user_id': '11'}
        self.assertRaises(HTTPNotFound, UserView(self.request).view)

        self.request.matchdict = {'user_id': '2'}
        self.request.referrer = '/user/view/1'
        response = UserView(self.request).view()
        self.assertIn('form', response)
        self.assertIn('user_name', response)
        self.assertEqual(response['user_name'], 'Édith AVULEUR')
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Édith AVULEUR Account')
        self.assertEqual(
            self.request.breadcrumbs.current_path(), '/user/view/2')

        self.request.has_permission = lambda x: False
        self.request.session['user'] = {'user_id': 3}
        self.assertRaises(HTTPForbidden, UserView(self.request).view)

    # -------------------------------------------------------------------------
    def test_view_export(self):
        """[u:views.user.UserView.view] export users"""
        from collections import namedtuple
        from pyramid.response import Response
        from ..views.user import UserView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_view')
        self.request.POST = {'exp!.x': True}
        self.request.matchdict = {'user_id': '2'}
        self.request.session['user'] = {'user_id': 1}

        response = UserView(self.request).view()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'test1', response.body)

    # -------------------------------------------------------------------------
    def test_view_send_invitation(self):
        """[u:views.user.UserView.view] send invitation"""
        from collections import namedtuple
        from ..views.user import UserView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_view')
        self.request.registry['settings']['title'] = 'Chrysalio'
        self.request.registry.settings['smtp.host'] = 'foo'
        self.request.session['user'] = {
            'user_id': 2, 'login': 'test2', 'email': 'test2@chrysal.io'}
        self.request.matchdict = {'user_id': '2'}
        self.request.POST = {'mel!.x': True}

        UserView(self.request).view()
        self.assertTrue(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_create(self):
        """[u:views.user.UserView.edit] creation"""
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPForbidden
        from ..views.user import UserView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_create')

        response = UserView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('user_name', response)
        self.assertIsNone(response['user_name'])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'User Creation')

        self.request.has_permission = lambda x: False
        self.assertRaises(HTTPForbidden, UserView(self.request).edit)

    # -------------------------------------------------------------------------
    def test_create_save(self):
        """[u:views.user.UserView.edit] save creation"""
        from collections import namedtuple
        from json import dumps
        from ..models.dbprofile import DBProfile
        from ..views.user import UserView

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_viewer', i18n_label=dumps({'en': 'User Viewer'})))
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_create')
        self.request.POST = {
            'login': 'test1', 'status': 'active',
            'first_name': 'Sébastienne', 'last_name': 'TOUSSEUL',
            'email': 'test11@chrysal.io',
            'password1': 'test11pwd', 'password2': 'test11pwd',
            'email_hidden': True, 'pfl:user_viewer': True, 'sav!.x': True}

        # Existing user
        response = UserView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertIn('form', response)
        self.assertEqual(len(errors), 1)
        self.assertIn('exists', errors[0])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'User Creation')
        dbsession.rollback()

        # New user, missing status
        del self.request.POST['status']
        UserView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])

        # New user
        self.request.POST['login'] = 'test11'
        self.request.POST['status'] = 'active'
        UserView(self.request).edit()
        self.assertFalse(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:views.user.UserView.edit]"""
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPForbidden
        from ..models.dbuser import DBUser
        from ..views.user import UserView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_edit')
        self.request.matchdict = {'user_id': '2'}
        self.request.session['user'] = {'user_id': 2}

        # As an administrator
        self.request.referrer = '/user/account'
        response = UserView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('user_name', response)
        self.assertEqual(response['user_name'], 'Édith AVULEUR')
        self.assertIn('dbuser', response)
        self.assertIsInstance(response['dbuser'], DBUser)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'My Account Edition')

        # As a normal user
        self.request.has_permission = lambda x: False
        self.request.session['user'] = {'user_id': 3}
        self.assertRaises(HTTPForbidden, UserView(self.request).edit)

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:views.user.UserView.edit] save"""
        from json import dumps
        from pyramid.httpexceptions import HTTPFound
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUser, DBUserProfile
        from ..models.dbgroup import DBGroupUser
        from ..views.user import UserView

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_editor', i18n_label=dumps({'en': 'User Editor'})))
        dbprofile = DBProfile(
            profile_id='user_viewer', i18n_label=dumps({'en': 'User Viewer'}))
        dbsession.add(dbprofile)
        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()
        dbuser.profiles.append(dbprofile)
        dbuser.groups.append(DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'})))
        dbsession.add(DBGroup(
            group_id='editors', i18n_label=dumps({'en': 'Editors'})))
        self.request.matchdict = {'user_id': str(dbuser.user_id)}
        self.request.session['user'] = {'user_id': dbuser.user_id}

        self.request.POST = {
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password1': 'test1pwd2', 'password2': 'test1pwd2',
            'email': 'test1chrysal.io', 'pfl:user_editor': True,
            'grp:editors': True, 'sav!.x': True}
        UserView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])

        self.request.POST['email'] = 'test1@chrysal.io'
        self.assertIsInstance(UserView(self.request).edit(), HTTPFound)
        self.assertIsNone(dbsession.query(DBUserProfile).filter_by(
            user_id=dbuser.user_id, profile_id='user_viewer').first())
        self.assertIsNotNone(dbsession.query(DBUserProfile).filter_by(
            user_id=dbuser.user_id, profile_id='user_editor').first())
        self.assertIsNone(dbsession.query(DBGroupUser).filter_by(
            group_id='managers', user_id=dbuser.user_id).first())
        self.assertIsNotNone(dbsession.query(DBGroupUser).filter_by(
            group_id='editors', user_id=dbuser.user_id).first())

        self.request.has_permission = lambda x: False
        self.request.POST['grp:managers'] = True
        UserView(self.request).edit()
        self.assertIsNone(dbsession.query(DBGroupUser).filter_by(
            group_id='managers', user_id=dbuser.user_id).first())

    # -------------------------------------------------------------------------
    def test_edit_picture(self):
        """[u:views.user.UserView.edit] change picture"""
        from ..views.user import UserView

        self.request.matchdict = {'user_id': '2'}
        self.request.session['user'] = {'user_id': 2}
        self.request.POST = {
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'email': 'test1@chrysal.io', 'picture': None, 'pct!.x': True}

        # Normal HTTP
        UserView(self.request).edit()

        # AJAX
        self.request.is_xhr = True
        response = UserView(self.request).edit()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_password_forgot(self):
        """[u:views.user.UserView.password_forgot]"""
        from collections import namedtuple
        from ..views.user import UserView

        self.request.registry['settings']['title'] = 'Chrysalio'
        self.request.registry['settings']['email'] = 'admin@chrysal.io'
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_password_forgot')

        response = UserView(self.request).password_forgot()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Forgot Password')

        self.request.POST = {'email': 'testX@chrysal.io'}
        UserView(self.request).password_forgot()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('email associated', errors[0])

        self.request.registry.settings['smtp.host'] = 'foo'
        self.request.POST['email'] = 'test1@chrysal.io'
        UserView(self.request).password_forgot()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertTrue(
            ('Connection refused' in errors[0]) or
            ('No address associated with hostname' in errors[0]) or
            ('Name or service not known' in errors[0]) or
            ('Temporary failure in name resolution') in errors[0] or
            ('Connection timed out' in errors[0]))

    # -------------------------------------------------------------------------
    def test_password_reset(self):
        """[u:views.user.UserView.password_reset]"""
        from hashlib import sha1
        from datetime import date
        from collections import namedtuple
        from pyramid.httpexceptions import HTTPNotFound
        from ..views.user import UserView

        self.request.registry['settings']['title'] = 'Chrysalio'
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_password_reset')
        self.request.matchdict['user_id'] = '2'
        self.request.matchdict['token'] = 'foo'

        self.assertRaises(HTTPNotFound, UserView(self.request).password_reset)

        token = 'test1{0}'.format(date.today().isoformat())
        token = sha1(token.encode('utf8')).hexdigest()
        self.request.matchdict['token'] = token
        response = UserView(self.request).password_reset()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Password Reset')

        self.request.POST = {
            'password1': 'test1pwd', 'password2': 'test1pwd'}
        UserView(self.request).password_reset()
        messages = self.request.session.pop_flash()
        self.assertEqual(len(messages), 1)
        self.assertIn('changed', messages[0])

    # -------------------------------------------------------------------------
    def test_can_view(self):
        """[u:views.user.UserView.can_view]"""
        from ..views.user import UserView

        self.assertTrue(UserView(self.request).can_view())

        self.request.has_permission = lambda x: False
        self.request.session['user'] = {'user_id': 1}
        self.request.matchdict['user_id'] = '1'
        self.assertTrue(UserView(self.request).can_view())

        self.request.matchdict['user_id'] = '2'
        self.assertFalse(UserView(self.request).can_view())

    # -------------------------------------------------------------------------
    def test_can_create(self):
        """[u:views.user.UserView.can_create]"""
        from ..views.user import UserView

        self.assertTrue(UserView(self.request).can_create())

        self.request.has_permission = lambda x: False
        self.assertFalse(UserView(self.request).can_create())

    # -------------------------------------------------------------------------
    def test_can_edit(self):
        """[u:views.user.UserView.can_edit]"""
        from ..views.user import UserView

        self.assertTrue(UserView(self.request).can_edit())

        self.request.has_permission = lambda x: False
        self.request.session['user'] = {'user_id': 1}
        self.request.matchdict['user_id'] = '1'
        self.assertTrue(UserView(self.request).can_edit())

        self.request.matchdict['user_id'] = '2'
        self.assertFalse(UserView(self.request).can_edit())


# =============================================================================
class FViewsUserUserView(FunctionalTestCase):
    """Functional test class for testing :class:`views.user.UserView`."""

    # -------------------------------------------------------------------------
    def test_index(self):
        """[f:views.user.UserView.index]"""
        self.login('test1')
        self.testapp.get('/user/index', status=403)

        self.login('admin')
        response = self.testapp.get('/user/index?display=list', status=200)
        self.assertIn(b'Users', response.body)
        self.assertIn(b'Create', response.body)
        self.assertIn(b'Import', response.body)
        self.assertIn(b'Send an invitation', response.body)
        self.assertIn(b'Export user', response.body)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[f:views.user.UserView.view]"""
        self.login('test1')
        self.testapp.get('/user/view/3', status=403)

        response = self.testapp.get('/user/view/2', status=200)
        self.assertIn(b'Edit', response.body)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[f:views.user.UserView.create]"""
        self.login('test1')
        self.testapp.get('/user/create', status=403)

        self.login('admin')
        response = self.testapp.get('/user/create', status=200)
        self.assertIn(b'Create', response.body)

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[f:views.user.UserView.edit]"""
        self.login('test1')
        self.testapp.get('/user/edit/3', status=403)

        response = self.testapp.get('/user/edit/2', status=200)
        self.assertIn(b'Save', response.body)

    # -------------------------------------------------------------------------
    # def test_password_forgot(self):
    #     """[f:views.user.UserView.password_forgot]"""
    #     csrf = self.testapp.get('/login').form.get('csrf_token').value
    #     self.testapp.post(
    #         '/user/password/forgot',
    #         {'email': 'test1@chrysal.io', 'csrf_token': csrf}, status=302)

    # -------------------------------------------------------------------------
    def test_password_reset(self):
        """[f:views.user.UserView.password_reset]"""
        from hashlib import sha1
        from datetime import date

        csrf = self.testapp.get('/login').form.get('csrf_token').value
        token = 'test1{0}'.format(date.today().isoformat())
        token = sha1(token.encode('utf8')).hexdigest()
        self.testapp.post(
            '/user/password/reset/2/{0}'.format(token), {
                'password1': 'test1pwd2', 'password2': 'test1pwd2',
                'csrf_token': csrf},
            status=302)
