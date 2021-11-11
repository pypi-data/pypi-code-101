# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models.dbgroup`` classes."""

from json import dumps, loads
from collections import namedtuple

from lxml import etree
from colander import SchemaNode

from pyramid.i18n import TranslationString

from ..models.dbgroup import DBGroup
from . import DBUnitTestCase


# =============================================================================
class UModelsDBGroupDBGroup(DBUnitTestCase):
    """Unit test class for :class:`models.dbgroup.DBGroup`."""

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:.models.dbgroup.DBGroup.xml2db]"""
        from ..models.dbuser import DBUser
        from ..models.dbgroup import DBGroupProfile

        dbsession = self.request.dbsession
        self.add_user({
            'login': 'member1', 'first_name': 'John', 'last_name': 'DEUF',
            'password': 'member1pwd', 'email': 'member1@chrysal.io'})
        dbsession.add(DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'})))

        # error_if_exists
        group_elt = etree.XML(
            '<group id="managers">'
            '  <label xml:lang="en">Managers</label>'
            '</group>')
        error = DBGroup.xml2db(dbsession, group_elt)
        self.assertIsNotNone(error)
        error = DBGroup.xml2db(dbsession, group_elt, error_if_exists=False)
        self.assertIsNone(error)

        # Without content
        group_elt = etree.XML(
            '<group id="Foo">'
            '</group>')
        error = DBGroup.xml2db(dbsession, group_elt)
        self.assertIsNotNone(error)

        # A valid group
        group_elt = etree.XML(
            '<group id="editors">'
            '  <label xml:lang="en">Editors</label>'
            '  <description xml:lang="en">Éditeurs</description>'
            '  <attachments key="Editors">'
            '    <picture>editors.png</picture>'
            '  </attachments>'
            '  <users>'
            '    <user>member1</user>'
            '  </users>'
            '  <profiles>'
            '    <profile>profile_editor</profile>'
            '    <profile>user_editor</profile>'
            '  </profiles>'
            '</group>')
        user_id = dbsession.query(DBUser.user_id).filter_by(
            login='member1').first()
        error = DBGroup.xml2db(dbsession, group_elt, kwargs={
            'users': {'member1': user_id[0]},
            'profiles': ('profile_editor', 'user_editor')})
        self.assertIsNone(error)
        dbgroup = dbsession.query(DBGroup).filter_by(
            group_id='editors').first()
        self.assertIsInstance(dbgroup, DBGroup)
        self.assertNotIsInstance(dbgroup.i18n_label, dict)
        self.assertIsInstance(dbgroup.i18n_description, dict)
        self.assertIn('en', dbgroup.i18n_description)
        self.assertEqual(len(dbgroup.users), 1)
        self.assertEqual(len(dbsession.query(DBGroupProfile).all()), 2)

    # -------------------------------------------------------------------------
    def test_record_from_xml(self):
        """[u:models.dbgroup.DBGroup.record_from_xml]"""
        group_elt = etree.XML(
            '<group id="editors">'
            '  <label xml:lang="en">Editors</label>'
            '  <attachments key="Editors">'
            '    <picture>editors.png</picture>'
            '  </attachments>'
            '  <users>'
            '    <user>member1</user>'
            '  </users>'
            '  <profiles>'
            '    <profile>profile_editor</profile>'
            '    <profile>group_editor</profile>'
            '  </profiles>'
            '</group>')
        record = DBGroup.record_from_xml('editors', group_elt)
        self.assertEqual(record['group_id'], 'editors')
        self.assertIn('i18n_label', record)
        labels = loads(record['i18n_label'])
        self.assertIn('en', labels)
        self.assertEqual(labels['en'], 'Editors')

    # -------------------------------------------------------------------------
    def test_record_format(self):
        """[u:models.dbgroup.DBGroup.record_format]"""
        record = {'group_id': None}
        error = DBGroup.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without ID', error)

        record = {'group_id': 'team1'}
        error = DBGroup.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without label', error)

        record = {
            'group_id': 'team1', 'label_en': 'Team 1',
            'label_fr': 'Équipe 1', 'description_en': 'Team of users n° 1.'}
        error = DBGroup.record_format(record)
        self.assertIsNone(error)
        self.assertIn('i18n_label', record)
        labels = loads(record['i18n_label'])
        self.assertEqual(len(labels), 2)
        self.assertIn('fr', labels)
        self.assertEqual(labels['fr'], 'Équipe 1')
        self.assertIn('i18n_description', record)
        self.assertEqual(len(record['i18n_description']), 1)

        record = {
            'group_id': 'team1', 'label_en': 'Team 1', 'label_fr': 'Équipe 1'}
        error = DBGroup.record_format(record)
        self.assertIsNone(error)
        self.assertIn('i18n_description', record)

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:models.dbgroup.DBGroup.db2xml]"""
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUser
        from ..models.dbgroup import DBGroupUser

        dbsession = self.request.dbsession
        self.add_user({
            'login': 'member1', 'first_name': 'John', 'last_name': 'DEUF',
            'password': 'member1pwd', 'email': 'member1@chrysal.io'})
        user_id = dbsession.query(DBUser.user_id).filter_by(
            login='member1').first()[0]
        dbgroup = DBGroup(
            group_id='managers',
            i18n_label=dumps({'en': 'Managers'}),
            i18n_description={'en': 'Permission to view, edit and create.'},
            attachments_key='Managers', picture='managers.png')
        dbgroup.users.append(DBGroupUser(user_id=user_id))
        dbgroup.profiles.append(DBProfile(profile_id='user_manager'))

        group_elt = dbgroup.db2xml(dbsession)
        self.assertEqual(group_elt.get('id'), 'managers')
        self.assertEqual(group_elt.findtext('label'), 'Managers')
        self.assertEqual(
            group_elt.findtext('description').strip(),
            'Permission to view, edit and create.')
        self.assertIsNotNone(group_elt.find('users'))
        self.assertEqual(group_elt.findtext('users/user'), 'member1')
        self.assertIsNotNone(group_elt.find('profiles'))
        self.assertEqual(
            group_elt.findtext('profiles/profile'), 'user_manager')

    # -------------------------------------------------------------------------
    def test_tab4view(self):
        """[u:models.dbgroup.DBGroup.tab4view]"""
        from ..lib.form import Form
        from ..lib.paging import Paging
        from ..lib.filter import Filter
        from ..models.dbuser import DBUser
        from ..models.dbprofile import DBProfile

        dbsession = self.request.dbsession
        form = Form(self.request)
        paging_id = 'group_users'
        user_filter = Filter(
            self.request, paging_id, (('login', 'Login', False, None),))
        user_paging = Paging(self.request, paging_id, [
            DBUser(user_id=1, login='user1', last_name='Mr TEST')])
        dbgroup = DBGroup(
            group_id='viewers',
            i18n_label=dumps({'en': 'Observers', 'fr': 'Observateurs'}),
            i18n_description={'en': 'These users do not touch.'},
            attachments_key='Viewers', picture='viewers.png')
        dbsession.add(dbgroup)
        self.configurator.add_route('home', '/')
        self.configurator.add_route(
            'profile_view', '/profile/view/{profile_id}')
        self.configurator.add_route('user_view', '/user/view/{user_id}')
        self.request.matched_route = namedtuple('Route', 'name')(name='home')

        # Information
        html = dbgroup.tab4view(
            self.request, 0, form, user_filter, user_paging)
        self.assertIn('viewers', html)
        self.assertIn('These users do not touch.', html)

        # Users
        html = dbgroup.tab4view(
            self.request, 1, form, user_filter, user_paging)
        self.assertIn('Mr TEST', html)

        # Profiles
        html = dbgroup.tab4view(
            self.request, 2, form, user_filter, user_paging)
        self.assertIn('No attributed profile.', html)
        dbgroup.profiles.append(DBProfile(
            profile_id='user_viewer', i18n_label=dumps({'en': 'User Viewer'})))
        html = dbgroup.tab4view(
            self.request, 2, form, user_filter, user_paging)
        self.assertIn('User Viewer', html)

        # Other
        self.assertEqual(
            dbgroup.tab4view(self.request, 3, form, user_filter, user_paging),
            '')

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:models.dbgroup.DBGroup.settings_schema]"""
        from ..models.dbprofile import DBProfile
        from ..models.dbgroup import DBGroupUser

        self.request.registry.settings['languages'] = 'en, fr'
        self.add_user({
            'login': 'member1', 'first_name': 'John', 'last_name': 'DEUF',
            'password': 'member1pwd', 'email': 'member1@chrysal.io'})

        # Creation
        schema, defaults = DBGroup.settings_schema(
            self.request, {}, ('profile_manager', 'user_manager'))
        self.assertIsInstance(schema, SchemaNode)
        serialized = schema.serialize()
        self.assertIn('group_id', serialized)
        self.assertIn('label_en', serialized)
        self.assertIn('label_fr', serialized)
        self.assertIn('description_en', serialized)
        self.assertIn('description_fr', serialized)
        self.assertIn('pfl:user_manager', serialized)
        self.assertIsInstance(defaults, dict)
        self.assertFalse(defaults)

        # Update
        dbgroup = DBGroup(
            group_id='managers',
            i18n_label=dumps({'en': 'Managers', 'fr': 'Gestionnaires'}),
            i18n_description={'en': 'These users manage.'},
            attachments_key='Managers', picture='managers.png')
        dbgroup.users.append(DBGroupUser(user_id='member1'))
        dbgroup.profiles.append(DBProfile(profile_id='user_manager'))
        schema, defaults = DBGroup.settings_schema(
            self.request, {}, ('profile_manager', 'user_manager'), dbgroup)
        self.assertNotIn('group_id', schema.serialize())
        self.assertIn('label_en', defaults)
        self.assertIn('description_en', defaults)
        self.assertIn('pfl:user_manager', defaults)

    # -------------------------------------------------------------------------
    def test_tab4edit(self):
        """[u:models.dbgroup.DBGroup.tab4edit]"""
        from ..lib.form import Form
        from ..lib.paging import Paging
        from ..lib.filter import Filter
        from ..models.dbuser import DBUser

        paging_id = 'group_users'
        self.request.registry.settings['languages'] = 'en, fr'
        user_filter = Filter(
            self.request, paging_id, (('login', 'Login', False, None),))
        user_paging = Paging(self.request, paging_id, [
            DBUser(user_id=1, login='test1', last_name='Mr TEST')])
        form = Form(self.request)
        dbgroup = DBGroup(
            group_id='managers',
            i18n_label=dumps({'en': 'Managers', 'fr': 'Gestionnaires'}),
            i18n_description={'en': 'These users manage.'},
            attachments_key='Managers', picture='managers.png')
        profiles = {
            'user_creator': ('User Creator', 'Authorized to create users.'),
            'user_editor': ('User Editor', None)}
        self.configurator.add_route('home', '/')
        self.request.matched_route = namedtuple('Route', 'name')(name='home')

        # Information, creation
        html = DBGroup.tab4edit(
            self.request, 0, form, user_filter, user_paging, {})
        self.assertIn('Identifier:', html)
        self.assertIn('group_id', html)
        self.assertIn('label_en', html)
        self.assertIn('label_fr', html)
        self.assertIn('description_en', html)
        self.assertIn('description_fr', html)

        # Information, update
        html = DBGroup.tab4edit(
            self.request, 0, form, user_filter, user_paging, profiles, dbgroup)
        self.assertNotIn('group_id', html)

        # Users
        html = DBGroup.tab4edit(
            self.request, 1, form, user_filter, user_paging, {}, dbgroup)
        self.assertIn('test1', html)

        # Profiles
        html = DBGroup.tab4edit(
            self.request, 2, form, user_filter, user_paging, {})
        self.assertEqual(html, 'No available profile.')
        html = DBGroup.tab4edit(
            self.request, 2, form, user_filter, user_paging, profiles, dbgroup)
        self.assertIn('User Creator', html)
        self.request.has_permission = lambda x: False
        html = DBGroup.tab4edit(
            self.request, 2, form, user_filter, user_paging, profiles, dbgroup)
        self.assertEqual(html, 'You do not have the rigths to edit profiles.')

        # Other
        html = DBGroup.tab4edit(
            self.request, 3, form, user_filter, user_paging, {})
        self.assertEqual(html, '')


# =============================================================================
class IModelsDBGroup(DBUnitTestCase):
    """Integration test class for ``models.dbgroup``."""

    # -------------------------------------------------------------------------
    def test_delete_cascade_user(self):
        """[i:models.dbgroup] delete, cascade user"""
        from ..models.dbuser import DBUser
        from ..models.dbgroup import DBGroupUser

        dbsession = self.request.dbsession
        self.add_user({
            'login': 'member2', 'first_name': 'Cécile',
            'last_name': 'OURKESSA', 'password': 'member2pwd',
            'email': 'member2@chrysal.io'})
        user_id = dbsession.query(DBUser.user_id).filter_by(
            login='member2').first()[0]
        group_id = 'managers'
        dbgroup = DBGroup(
            group_id=group_id, i18n_label=dumps({'en': 'Managers'}))
        dbgroup.users.append(
            DBGroupUser(user_id=user_id))
        dbsession.add(dbgroup)

        dbgroup = dbsession.query(DBGroup).filter_by(group_id=group_id).first()
        self.assertIsInstance(dbgroup, DBGroup)
        dbgroup_user = dbsession.query(DBGroupUser).filter_by(
            group_id=group_id).first()
        self.assertIsInstance(dbgroup_user, DBGroupUser)

        dbsession.delete(dbgroup)
        dbsession.flush()
        dbgroup = dbsession.query(DBGroup).filter_by(group_id=group_id).first()
        self.assertIsNone(dbgroup)
        dbgroup_user = dbsession.query(DBGroupUser).filter_by(
            group_id=group_id).first()
        self.assertIsNone(dbgroup_user)

    # -------------------------------------------------------------------------
    def test_delete_cascade_profile(self):
        """[i:models.dbgroup] delete, cascade group profile"""
        from ..models.dbprofile import DBProfile
        from ..models.dbgroup import DBGroupProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='group_manager',
            i18n_label=dumps({'en': 'Group manager'})))
        group_id = 'editors'
        dbgroup = DBGroup(
            group_id=group_id, i18n_label=dumps({'en': 'Editors'}))
        dbsession.add(dbgroup)
        dbsession.flush()
        dbsession.add(DBGroupProfile(
            group_id=dbgroup.group_id, profile_id='group_manager'))

        dbgroup = dbsession.query(DBGroup).filter_by(group_id=group_id).first()
        self.assertIsInstance(dbgroup, DBGroup)
        self.assertIsNotNone(dbsession.query(DBGroupProfile).filter_by(
            group_id=group_id).first())

        dbgroup.profiles.remove(dbgroup.profiles[0])
        dbsession.flush()
        self.assertIsNone(dbsession.query(DBGroupProfile).filter_by(
            group_id=group_id).first())
