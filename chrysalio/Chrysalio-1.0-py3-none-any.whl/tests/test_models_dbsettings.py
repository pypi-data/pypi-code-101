# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models.dbsettings`` classes."""

from unittest import TestCase

import transaction

from . import DBUnitTestCase


# =============================================================================
class UModelsDBSettingsDBSettingsNoDb(TestCase):
    """Unit test class for :class:`models.dbsettings.Setting` without DB."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pyramid.testing import setUp, DummyRequest
        from ..models import DB_METADATA, get_dbengine, get_dbsession_factory
        from ..models import get_tm_dbsession

        self.configurator = setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'})

        DB_METADATA.bind = get_dbengine(self.configurator.get_settings())
        dbsession_factory = get_dbsession_factory(DB_METADATA.bind)

        self.request = DummyRequest(
            dbsession=get_tm_dbsession(dbsession_factory, transaction.manager),
            matched_route=None)

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from pyramid.testing import tearDown
        from ..models import DB_METADATA

        tearDown()
        transaction.manager.abort()
        DB_METADATA.drop_all()

    # -------------------------------------------------------------------------
    def test_exists(self):
        """[u:models.dbsettings.DBSettings.exists] without database"""
        from ..models.dbsettings import DBSettings

        # pylint: disable = no-member
        self.assertFalse(DBSettings.exists(self.request.dbsession))

    # -------------------------------------------------------------------------
    def test_db2dict(self):
        """[u:models.dbsettings.DBSettings.db2dict] without database"""
        from ..models.dbsettings import DBSettings

        settings = {'site.uid': 'testchrysalio'}
        # pylint: disable = no-member
        settings_dict = DBSettings.db2dict(
            settings, self.request.dbsession, 'admin@chrysal.io')
        # pylint: enable = no-member
        self.assertIsInstance(settings_dict, dict)
        self.assertIn('title', settings_dict)
        self.assertEqual(settings_dict['title'], 'testchrysalio')


# =============================================================================
class UModelsDBSettingsDBSettings(DBUnitTestCase):
    """Unit test class for :class:`models.dbsettings.Setting`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pkg_resources import get_distribution

        super(UModelsDBSettingsDBSettings, self).setUp()

        self.request.registry.settings['site.uid'] = 'testchrysalio'
        self.request.registry['version'] = 'chrysalio {0}'.format(
            get_distribution('chrysalio').version)
        self.request.registry['settings']['populate'] = 'now'

    # -------------------------------------------------------------------------
    def test_exists(self):
        """[u:models.dbsettings.Setting.exists]"""
        from ..models.dbsettings import DBSettings

        dbsession = self.request.dbsession

        self.assertFalse(DBSettings.exists(dbsession))

        dbsession.add(DBSettings(key='populate', value='now'))
        self.assertTrue(DBSettings.exists(dbsession))

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:models.dbsettings.DBSettings.xml2db]"""
        from lxml import etree
        from ..models.dbsettings import DBSettings

        settings_elt = etree.XML(
            '<settings>'
            '  <title>Chrysalio – Test 1</title>'
            '  <email>admin@chrysal.io</email>'
            '  <password-min-length>8</password-min-length>'
            '  <remember-me>5184000</remember-me>'
            '  <page-size>80</page-size>'
            '  <download-max-size>10485760</download-max-size>'
            '  <theme>Default</theme>'
            '</settings>')
        dbsession = self.request.dbsession

        DBSettings.xml2db(dbsession, None)
        self.assertIsNone(dbsession.query(DBSettings).first())

        DBSettings.xml2db(dbsession, settings_elt)
        settings = dbsession.query(DBSettings).all()
        self.assertEqual(len(settings), 8)
        keys = [k.key for k in settings]
        self.assertIn('title', keys)
        self.assertIn('email', keys)
        self.assertIn('password-min-length', keys)
        self.assertIn('remember-me', keys)
        self.assertIn('page-size', keys)
        self.assertIn('download-max-size', keys)
        self.assertIn('theme', keys)
        self.assertIn('populate', keys)

        settings_elt = etree.XML(
            '<settings>'
            '  <title>Chrysalio – Test 2</title>'
            '  <password-min-length>8</password-min-length>'
            '  <page-size>80</page-size>'
            '</settings>')
        DBSettings.xml2db(dbsession, settings_elt)
        settings = dbsession.query(DBSettings).all()
        self.assertEqual(len(settings), 4)

        settings_elt = etree.XML(
            '<settings>'
            '  <title>Chrysalio – Test 3</title>'
            '  <password-min-length>8</password-min-length>'
            '  <page-size>80</page-size>'
            '  <foo bar="baz"/>'
            '</settings>')
        DBSettings.xml2db(dbsession, settings_elt)
        settings = dbsession.query(DBSettings).all()
        self.assertEqual(len(settings), 5)

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:models.dbsettings.DBSettings.db2xml]"""
        from ..models.dbsettings import DBSettings

        dbsession = self.request.dbsession
        dbsession.add(DBSettings(key='title', value='Chrysalio – Test'))
        dbsession.add(DBSettings(key='password-min-length', value='8'))

        settings_elt = DBSettings.db2xml(dbsession)
        self.assertEqual(settings_elt.findtext('title'), 'Chrysalio – Test')
        self.assertEqual(settings_elt.findtext('password-min-length'), '8')

    # -------------------------------------------------------------------------
    def test_db2dict(self):
        """[u:models.dbsettings.DBSettings.db2dict]"""
        from ..models.dbsettings import DBSettings

        settings = {
            'site.uid': 'testchrysalio', 'site.title': 'Chrysalio – Test 1',
            'pyramid.default_locale_name': 'en'}
        dbsession = self.request.dbsession

        settings_dict = DBSettings.db2dict(
            settings, dbsession, 'admin@chrysal.io')
        self.assertIsInstance(settings_dict, dict)
        self.assertIn('title', settings_dict)
        self.assertIn('password-min-length', settings_dict)
        self.assertIn('email', settings_dict)
        self.assertIn('populate', settings_dict)
        self.assertEqual(settings_dict['title'], 'Chrysalio – Test 1')
        self.assertEqual(settings_dict['password-min-length'], 8)
        self.assertEqual(settings_dict['email'], 'admin@chrysal.io')

        dbsession.add(DBSettings(key='title', value='Chrysalio – Test 2'))
        dbsession.add(DBSettings(key='password-min-length', value='10'))
        settings_dict = DBSettings.db2dict(
            settings, dbsession, 'admin@chrysal.io')
        self.assertEqual(settings_dict['title'], 'Chrysalio – Test 2')
        self.assertEqual(settings_dict['password-min-length'], 10)

    # -------------------------------------------------------------------------
    def test_tab4view(self):
        """[u:models.dbsettings.DBSettings.tab4view]"""
        from ..lib.form import Form
        from ..models.dbsettings import SETTINGS_DEFAULTS, DBSettings

        html = DBSettings.tab4view(self.request, 0, Form(self.request))
        self.assertIn(
            '<div>{0}</div>'.format(SETTINGS_DEFAULTS['page-size']), html)
        self.assertIn(
            '<div>{0}</div>'.format(SETTINGS_DEFAULTS['password-min-length']),
            html)

        html = DBSettings.tab4view(self.request, 1, Form(self.request))
        self.assertNotIn('You cannot modify', html)
        self.assertIn('<div>testchrysalio</div>', html)
        self.assertIn('<div>en</div>', html)
        self.assertIn('<div>sqlite</div>', html)
        self.assertIn('<div>:memory:</div>', html)

        self.assertEqual(
            DBSettings.tab4view(self.request, 2, Form(self.request)), '')

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:models.dbsettings.DBSettings.settings_schema]"""
        from colander import SchemaNode
        from ..models.dbsettings import DBSettings

        self.request.registry['themes'] = {'': {}, 'Alternative': {}}
        self.request.registry['settings']['title'] = 'testchrysalio'

        schema, defaults = DBSettings.settings_schema(self.request)
        self.assertIsInstance(schema, SchemaNode)
        serialized = schema.serialize()
        self.assertIn('title', serialized)
        self.assertIn('email', serialized)
        self.assertIn('language', serialized)
        self.assertIn('password-min-length', serialized)
        self.assertIn('page-size', serialized)
        self.assertIn('download-max-size', serialized)
        self.assertIn('theme', serialized)
        self.assertIn('title', defaults)

    # -------------------------------------------------------------------------
    def test_tab4edit(self):
        """[u:models.dbsettings.DBSettings.tab4edit]"""
        from ..lib.form import Form
        from ..models.dbsettings import DBSettings

        self.request.registry['themes'] = {
            '': {'name': {}}, 'Alternative': {'name': {'en': 'Alternative'}}}

        html = DBSettings.tab4edit(self.request, 0, Form(self.request))
        self.assertIn('<h3>Site</h3>', html)
        self.assertIn('Title:', html)
        self.assertIn('Email:', html)
        self.assertIn('<h3>Default values</h3>', html)
        self.assertIn('Language:', html)
        self.assertIn('Password length:', html)
        self.assertIn('Lines per page:', html)
        self.assertNotIn('Themes:', html)

        html = DBSettings.tab4edit(self.request, 1, Form(self.request))
        self.assertIn('You cannot modify', html)

        self.assertEqual(
            DBSettings.tab4edit(self.request, 2, Form(self.request)), '')
