# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``views.group`` class."""

from json import dumps
from collections import namedtuple
from cgi import FieldStorage

from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.testing import DummySession

from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsGroupGroupView(DBUnitTestCase):
    """Unit test class for testing :class:`views.group.GroupView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUser
        from ..models.dbgroup import DBGroup, DBGroupUser
        from . import TEST_DIR

        super(UViewsGroupGroupView, self).setUp()

        dbsession = self.request.dbsession
        self.request.registry.settings['site.uid'] = 'test'
        self.request.registry.settings['attachments'] = TEST_DIR

        dbsession.add(DBProfile(
            profile_id='profile_manager',
            i18n_label=dumps({'en': 'Profile manager'})))
        self.add_user({
            'login': 'member1', 'first_name': 'Cécile',
            'last_name': 'OURKESSA', 'password': 'member1pwd',
            'email': 'member1@chrysal.io'})
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        user_id = dbsession.query(DBUser.user_id).filter_by(
            login='member1').first()[0]
        dbgroup = DBGroup(
            group_id='managers',
            i18n_label=dumps({'en': 'Managers'}),
            i18n_description={'en': 'Permission to view, edit and create.'},
            attachments_key='Managers', picture='managers.png')
        dbgroup.users.append(DBGroupUser(user_id=user_id))
        dbgroup.profiles.append(DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User account manager'})))
        dbsession.add(dbgroup)
        dbsession.add(DBGroup(
            group_id='editors', i18n_label=dumps({'en': 'Editors'})))
        self.request.session['user'] = {
            'login': 'member1', 'user_id': user_id}

        self.configurator.add_route('home', '/')
        self.configurator.add_route('group_index', '/group/index')
        self.configurator.add_route('group_create', '/group/create')
        self.configurator.add_route('group_view', '/group/view/{group_id}')
        self.configurator.add_route('group_edit', '/group/edit/{group_id}')
        self.configurator.add_route('attachment', '/attachment/*path')

    # -------------------------------------------------------------------------
    def test_index(self):
        """[u:views.group.GroupView.index]"""
        from ..lib.filter import Filter
        from ..views.group import GroupView
        from . import DummyPOST

        self.request.matched_route = namedtuple('Route', 'name')(
            name='group_index')
        self.request.session = DummySession({'user': {'user_id': 1}})

        # As creator
        response = GroupView(self.request).index()
        self.assertIn('pfilter', response)
        self.assertIsInstance(response['pfilter'], Filter)
        self.assertTrue(response['pfilter'].is_empty())
        self.assertIn('paging', response)
        self.assertIn('PAGE_SIZES', response)
        self.assertIn('i_creator', response)
        self.assertTrue(response['i_creator'])
        self.assertTrue(response['i_editor'])
        self.assertEqual(self.request.breadcrumbs.current_title(), 'Groups')

        # Not as creator
        self.request.has_permission = lambda k: False
        response = GroupView(self.request).index()
        self.assertFalse(response['i_creator'])
        self.assertFalse(response['i_editor'])

        # AJAX mode
        self.request.has_permission = lambda k: True
        self.request.is_xhr = True
        self.request.POST = DummyPOST()
        response = GroupView(self.request).index()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_index_delete(self):
        """[u:views.group.GroupView.index] delete group"""
        from ..models.dbgroup import DBGroup
        from ..views.group import GroupView

        dbsession = self.request.dbsession
        self.assertEqual(dbsession.query(DBGroup).count(), 2)

        self.request.POST = {'del!editors.x': True}
        GroupView(self.request).index()
        self.assertEqual(dbsession.query(DBGroup).count(), 1)

    # -------------------------------------------------------------------------
    def test_index_import(self):
        """[u:views.group.GroupView.index] import group"""
        from . import TEST1_GROUP_XML, DummyPOST
        from ..views.group import GroupView

        self.request.POST = DummyPOST({'imp!.x': True})
        response = GroupView(self.request).index()
        self.assertIn('paging', response)
        self.assertNotIn('team1', [k.group_id for k in response['paging']])

        with open(TEST1_GROUP_XML, 'r', encoding='utf8') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_GROUP_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = GroupView(self.request).index()
        self.assertIn('paging', response)
        self.assertIn('team1', [k.group_id for k in response['paging']])

    # -------------------------------------------------------------------------
    def test_index_export(self):
        """[u:views.group.GroupView.index] export group"""
        from ..views.group import GroupView

        self.request.POST = {'exp!foo.x': True}
        response = GroupView(self.request).index()
        self.assertIsInstance(response, dict)

        self.request.POST = {'exp!managers.x': True}
        response = GroupView(self.request).index()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'managers', response.body)

    # -------------------------------------------------------------------------
    def test_index_filter(self):
        """[u:views.group.GroupView.index_filter]"""
        from ..views.group import GroupView

        self.request.is_xhr = True
        self.request.params = {'field': 'i18n_label', 'value': 'Managers'}
        data = GroupView(self.request).index_filter()
        self.assertIsInstance(data, list)
        self.assertIn('Managers', data)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:views.group.GroupView.view]"""
        from ..views.group import GroupView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='group_view')

        self.request.matchdict = {'group_id': 'foo'}
        self.assertRaises(HTTPNotFound, GroupView(self.request).view)

        self.request.matchdict = {'group_id': 'managers'}
        response = GroupView(self.request).view()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Group "Managers"')

    # -------------------------------------------------------------------------
    def test_view_export(self):
        """[u:views.group.GroupView.view] export groups"""
        from ..views.group import GroupView

        self.request.POST = {'exp!.x': True}
        self.request.matchdict = {'group_id': 'managers'}

        response = GroupView(self.request).view()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'managers', response.body)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[u:views.group.GroupView.edit] creation"""
        from ..views.group import GroupView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='group_create')

        response = GroupView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('dbgroup', response)
        self.assertIn('user_filter', response)
        self.assertIn('user_paging', response)
        self.assertIn('picture', response)
        self.assertIn('label', response)
        self.assertIsNone(response['label'])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Group Creation')

    # -------------------------------------------------------------------------
    def test_create_save(self):
        """[u:views.group.GroupView.edit] save creation"""
        from ..views.group import GroupView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='group_create')
        self.request.POST = {
            'group_id': 'managers', 'label_en': 'Managers', 'sav!.x': True}

        # Existing group
        response = GroupView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('form', response)
        self.assertIn('exists', errors[0])
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Group Creation')
        # pylint: disable = no-member
        self.request.dbsession.rollback()
        # pylint: enable = no-member

        # New group, missing label
        self.request.POST = {'group_id': 'team1', 'sav!.x': True}
        GroupView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])
        # pylint: disable = no-member
        self.request.dbsession.rollback()
        # pylint: enable = no-member

        # New group OK
        self.add_user({
            'login': 'member1', 'first_name': 'Cécile',
            'last_name': 'OURKESSA', 'password': 'member1pwd',
            'email': 'member1@chrysal.io'})
        self.request.POST['label_en'] = 'Team 1'
        GroupView(self.request).edit()
        self.assertFalse(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:views.group.GroupView.edit]"""
        from ..models.dbgroup import DBGroup
        from ..views.group import GroupView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='group_edit')
        self.request.matchdict = {'group_id': 'managers'}

        response = GroupView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('label', response)
        self.assertEqual(response['label'], 'Managers')
        self.assertIn('dbgroup', response)
        self.assertIsInstance(response['dbgroup'], DBGroup)
        self.assertEqual(
            self.request.breadcrumbs.current_title(),
            'Group "Managers" Edition')

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:views.group.GroupView.edit] save"""
        from ..models.dbuser import DBUser
        from ..views.group import GroupView

        dbsession = self.request.dbsession
        self.request.matchdict = {'group_id': 'managers'}
        self.request.POST = {
            'description_en': 'Managers can create, destroy and modify.',
            'sav!.x': True}

        # Missing label
        GroupView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])

        # Correct group
        user1_id = dbsession.query(DBUser.user_id).filter_by(
            login='member1').first()[0]
        user2_id = dbsession.query(DBUser.user_id).filter_by(
            login='test1').first()[0]
        self.request.POST['label_en'] = 'Managers'
        self.request.POST['shw:{0}'.format(user1_id)] = True
        self.request.POST['shw:{0}'.format(user2_id)] = True
        self.request.POST['mbr:{0}'.format(user2_id)] = True
        self.request.POST['pfl:profile_manager'] = True
        self.assertIsInstance(GroupView(self.request).edit(), HTTPFound)

        # Whitout permission
        self.request.has_permission = lambda k: False
        self.assertIsInstance(GroupView(self.request).edit(), HTTPFound)

    # -------------------------------------------------------------------------
    def test_edit_picture(self):
        """[u:views.group.GroupView.edit] change picture"""
        from ..views.group import GroupView
        from . import TEST1_SVG

        self.request.matchdict = {'group_id': 'managers'}
        self.request.POST = {'pct!.x': True}

        # Normal HTTP
        with open(TEST1_SVG, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_SVG
            input_file.file = hdl
            self.request.POST['picture'] = input_file
            GroupView(self.request).edit()

        # AJAX
        with open(TEST1_SVG, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_SVG
            input_file.file = hdl
            self.request.is_xhr = True
            self.request.POST['picture'] = input_file
            response = GroupView(self.request).edit()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)


# =============================================================================
class FViewsGroupGroupView(FunctionalTestCase):
    """Functional test class for testing :class:`views.group.GroupView`."""

    # -------------------------------------------------------------------------
    def test_index(self):
        """[f:views.group.GroupView.index]"""
        self.login('test1')
        self.testapp.get('/group/index', status=403)

        self.login('admin')
        response = self.testapp.get('/group/index', status=200)
        self.assertIn(b'Groups', response.body)
        self.assertIn(b'Create', response.body)
        self.assertIn(b'Import', response.body)
        self.assertIn(b'Export selected group', response.body)
        self.assertIn(b'Delete selected group', response.body)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[f:views.group.GroupView.view]"""
        self.login('test1')
        self.testapp.get('/group/view/team1', status=403)

        self.login('admin')
        response = self.testapp.get('/group/view/team1', status=200)
        self.assertIn(b'Edit', response.body)

    # -------------------------------------------------------------------------
    def test_create(self):
        """[f:views.group.GroupView.create]"""
        self.login('test1')
        self.testapp.get('/group/create', status=403)

        self.login('admin')
        response = self.testapp.get('/group/create', status=200)
        self.assertIn(b'Create', response.body)

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[f:views.group.GroupView.edit]"""
        self.login('test1')
        self.testapp.get('/group/edit/team1', status=403)

        self.login('admin')
        response = self.testapp.get('/group/edit/team1', status=200)
        self.assertIn(b'Save', response.body)
