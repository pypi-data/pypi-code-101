# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models.dbprofile`` classes."""

from json import loads, dumps

from lxml import etree
from colander import SchemaNode

from pyramid.i18n import TranslationString

from . import DBUnitTestCase


# =============================================================================
class UModelsDBProfileDBProfile(DBUnitTestCase):
    """Unit test class for :class:`models.dbprofile.Profile`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _make_one(cls):
        """Make an `DBProfile`` object."""
        from ..models.dbprofile import DBProfile

        return DBProfile(
            profile_id='user_creator',
            i18n_label=dumps({'en': 'Profile manager'}),
            i18n_description={'en': 'Permission to create profiles'})

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:models.dbprofile.Profile.xml2db]"""
        from ..models.dbprofile import DBProfile

        profile_elt = etree.XML(
            '<profile id="profile_manager">'
            '  <label xml:lang="en">Profile manager</label>'
            '  <description xml:lang="en">'
            '    Permission to create, edit and view profiles.'
            '  </description>'
            '  <principals>'
            '    <principal>profile.creator</principal>'
            '  </principals>'
            '</profile>')
        dbsession = self.request.dbsession

        DBProfile.xml2db(dbsession, profile_elt)
        dbprofile = dbsession.query(DBProfile).filter_by(
            profile_id='profile_manager').first()
        self.assertIsInstance(dbprofile, DBProfile)
        self.assertIn('Profile manager', dbprofile.i18n_label)
        self.assertIsInstance(dbprofile.i18n_description, dict)
        self.assertIn('en', dbprofile.i18n_description)
        self.assertEqual(
            dbprofile.i18n_description['en'],
            'Permission to create, edit and view profiles.')
        self.assertIsNotNone(dbprofile.principals)
        self.assertEqual(len(dbprofile.principals), 1)

        error = DBProfile.xml2db(dbsession, profile_elt)
        self.assertIsInstance(error, TranslationString)
        error = DBProfile.xml2db(dbsession, profile_elt, error_if_exists=False)
        self.assertIsNone(error)

        profile_elt = etree.XML('<profile id="profile_editor"></profile>')
        error = DBProfile.xml2db(dbsession, profile_elt)
        self.assertIsInstance(error, TranslationString)

    # -------------------------------------------------------------------------
    def test_record_from_xml(self):
        """[u:models.dbprofile.DBProfile.record_from_xml]"""
        from ..models.dbprofile import DBProfile

        profile_elt = etree.XML(
            '<profile id="user_editor">'
            '  <label xml:lang="en">User account editor</label>'
            '  <label xml:lang="fr">Éditeur des comptes utilisateurs</label>'
            '  <description xml:lang="en">'
            '    These users can view and edit user accounts.'
            '  </description>'
            '  <principals>'
            '    <principal>user.editor</principal>'
            '  </principals>'
            '</profile>')
        record = DBProfile.record_from_xml('user_editor', profile_elt)
        self.assertIn('profile_id', record)
        self.assertEqual(record['profile_id'], 'user_editor')
        self.assertIn('i18n_label', record)
        labels = loads(record['i18n_label'])
        self.assertIn('fr', labels)
        self.assertEqual(labels['fr'], 'Éditeur des comptes utilisateurs')

    # -------------------------------------------------------------------------
    def test_record_format(self):
        """[u:models.dbprofile.DBProfile.record_format]"""
        from ..models.dbprofile import DBProfile

        record = {'profile_id': None}
        error = DBProfile.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without ID', error)

        record = {'profile_id': 'user_creator'}
        error = DBProfile.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without label', error)

        record = {
            'profile_id': 'user_creator', 'label_en': 'User account creator',
            'label_fr': 'Créateur de comptes utilisateurs',
            'description_en': 'These users can create user accounts'}
        error = DBProfile.record_format(record)
        self.assertIsNone(error)
        self.assertIn('i18n_label', record)
        labels = loads(record['i18n_label'])
        self.assertEqual(len(labels), 2)
        self.assertIn('fr', labels)
        self.assertEqual(labels['fr'], 'Créateur de comptes utilisateurs')
        self.assertIn('i18n_description', record)
        self.assertEqual(len(record['i18n_description']), 1)

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:models.dbprofile.DBProfile.db2xml]"""
        from ..models.dbprofile import DBProfile, DBProfilePrincipal

        dbsession = self.request.dbsession
        dbprofile = DBProfile(
            profile_id='profile_manager',
            i18n_label=dumps({'en': 'Profile manager'}),
            i18n_description={'en': 'Permission to view, edit and create.'})
        dbprofile.principals.append(
            DBProfilePrincipal(principal='profile.creator'))

        profile_elt = dbprofile.db2xml(dbsession)
        self.assertEqual(profile_elt.get('id'), 'profile_manager')
        self.assertEqual(
            profile_elt.findtext('label'), 'Profile manager')
        self.assertEqual(
            profile_elt.findtext('description').strip(),
            'Permission to view, edit and create.')
        self.assertIsNotNone(profile_elt.find('principals'))
        self.assertEqual(
            profile_elt.findtext('principals/principal'), 'profile.creator')

    # -------------------------------------------------------------------------
    def test_tab4view(self):
        """[u:models.dbprofile.DBProfile.tab4view]"""
        from ..lib.form import Form
        from ..models.dbprofile import DBProfilePrincipal

        dbprofile = self._make_one()
        dbprofile.principals.append(
            DBProfilePrincipal(principal='user.creator'))
        self.configurator.add_route(
            'profile_view', '/profile/view/{profile_id}')
        principals = (
            ('user', 'User management', (
                ('editor', 'Edit or view any user', (
                    'user-edit', 'user-view')),
                ('creator', 'Create a new one or edit or view any user', (
                    'user-create', 'user-edit', 'user-view'))
            )),)
        self.request.registry['principals'] = principals

        html = dbprofile.tab4view(self.request, 0, Form(self.request))
        self.assertIn('Profile manager', html)

        html = dbprofile.tab4view(self.request, 1, Form(self.request))
        self.assertIn('Edit or view any user', html)

        self.assertEqual(
            dbprofile.tab4view(self.request, 2, Form(self.request)), '')

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:models.dbprofile.DBProfile.settings_schema]"""
        from ..models.dbprofile import DBProfile, DBProfilePrincipal

        self.request.registry.settings['languages'] = 'en, fr'
        principals = (
            ('user', 'User management', (
                ('editor', 'Edit or view any user', (
                    'user-edit', 'user-view')),
                ('creator', 'Create a new one or edit or view any user', (
                    'user-create', 'user-edit', 'user-view'))
            )),)
        self.request.registry['principals'] = principals

        # Creation
        schema, defaults = DBProfile.settings_schema(self.request)
        self.assertIsInstance(schema, SchemaNode)
        serialized = schema.serialize()
        self.assertIn('profile_id', serialized)
        self.assertIn('label_en', serialized)
        self.assertIn('label_fr', serialized)
        self.assertIn('description_en', serialized)
        self.assertIn('description_fr', serialized)
        self.assertIn('pcpl:user.editor', serialized)
        self.assertIsInstance(defaults, dict)
        self.assertFalse(defaults)

        # Update
        dbprofile = self._make_one()
        dbprofile.principals.append(
            DBProfilePrincipal(principal='user.creator'))
        schema, defaults = DBProfile.settings_schema(self.request, dbprofile)
        self.assertNotIn('profile_id', schema.serialize())
        self.assertIn('label_en', defaults)
        self.assertIn('description_en', defaults)
        self.assertIn('pcpl:user.creator', defaults)

    # -------------------------------------------------------------------------
    def test_tab4edit(self):
        """[u:models.dbprofile.DBProfile.tab4edit]"""
        from ..lib.form import Form
        from ..models.dbprofile import DBProfile

        self.request.registry.settings['languages'] = 'en, fr'
        principals = (
            ('user', 'User management', (
                ('editor', 'Edit or view any user', (
                    'user-edit', 'user-view')),
                ('creator', 'Create a new one or edit or view any user', (
                    'user-create', 'user-edit', 'user-view'))
            )),)
        self.request.registry['principals'] = principals
        dbprofile = self._make_one()

        # Information, creation
        html = DBProfile.tab4edit(self.request, 0, Form(self.request))
        self.assertIn('Identifier:', html)
        self.assertIn('profile_id', html)
        self.assertIn('label_en', html)
        self.assertIn('label_fr', html)
        self.assertIn('description_en', html)
        self.assertIn('description_fr', html)

        # Information, update
        html = DBProfile.tab4edit(
            self.request, 0, Form(self.request), dbprofile)
        self.assertNotIn('profile_id', html)

        # Principals
        html = DBProfile.tab4edit(self.request, 1, Form(self.request))
        self.assertIn('pcpl:user.editor', html)
        self.assertIn('for="pcplusereditor"', html)

        # Other
        html = DBProfile.tab4edit(self.request, 2, Form(self.request))
        self.assertEqual(html, '')


# =============================================================================
class IModelsDBProfile(DBUnitTestCase):
    """Integration test class for ``models.dbprofile``."""

    # -------------------------------------------------------------------------
    def test_delete_cascade_principal(self):
        """[i:models.dbprofile] delete, cascade principal"""
        from ..models.dbprofile import DBProfile, DBProfilePrincipal

        dbsession = self.request.dbsession
        profile_id = 'profile_manager'
        dbprofile = DBProfile(
            profile_id=profile_id,
            i18n_label=dumps({'en': 'Profile manager'}))
        dbprofile.principals.append(
            DBProfilePrincipal(principal='profile.creator'))
        dbsession.add(dbprofile)

        dbprofile = dbsession.query(DBProfile).filter_by(
            profile_id=profile_id).first()
        self.assertIsInstance(dbprofile, DBProfile)
        dbprincipal = dbsession.query(DBProfilePrincipal).filter_by(
            profile_id=profile_id).first()
        self.assertIsInstance(dbprincipal, DBProfilePrincipal)

        dbsession.delete(dbprofile)
        dbsession.flush()
        dbprofile = dbsession.query(DBProfile).filter_by(
            profile_id=profile_id).first()
        self.assertIsNone(dbprofile)
        dbprincipal = dbsession.query(DBProfilePrincipal).filter_by(
            profile_id=profile_id).first()
        self.assertIsNone(dbprincipal)
