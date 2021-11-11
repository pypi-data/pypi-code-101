# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.i18n`` functions."""

from unittest import TestCase

from pkg_resources import register_loader_type, DefaultProvider
from _pytest.assertion.rewrite import AssertionRewritingHook
import colander

from pyramid.testing import DummyRequest

# pylint: disable = unused-import
from ..models.dbgroup import DBGroup  # noqa
# pylint: enable = unused-import
from . import DBUnitTestCase


# =============================================================================
class ULibI18nLocaleNegotiator(TestCase):
    """Unit test class for :func:`lib.i18n.locale_negotiator`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.locale_negotiator]"""
        from webob.acceptparse import AcceptLanguageValidHeader
        from ..lib.i18n import locale_negotiator

        request = DummyRequest(accept_language=AcceptLanguageValidHeader(
            'fr-FR, fr;q=0.8, en-US;q=0.5, en;q=0.3'))
        request.registry.settings = {}
        request.registry['settings'] = {'language': 'en'}
        language = locale_negotiator(request)
        self.assertEqual(language, 'en')

        request.session['lang'] = 'fr'
        language = locale_negotiator(request)
        self.assertEqual(language, 'fr')


# =============================================================================
class ULibI18nAddTranslationDirs(TestCase):
    """Unit test class for :func:`lib.i18n.add_translation_dirs`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pyramid.testing import setUp
        self.configurator = setUp(settings={})
        register_loader_type(AssertionRewritingHook, DefaultProvider)

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from pyramid.testing import tearDown
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.add_translation_dirs]"""
        from ..lib.i18n import add_translation_dirs

        add_translation_dirs(self.configurator, 'chrysalio')
        self.assertRaises(
            SystemExit, add_translation_dirs, self.configurator, 'foo')

        self.configurator.get_settings()['translation_dirs'] = 'bar'
        self.assertRaises(
            SystemExit, add_translation_dirs, self.configurator, 'foo')


# =============================================================================
class ULibI18nTranslate(TestCase):
    """Unit test class for :func:`lib.i18n.translate`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.translate]"""
        from ..lib.i18n import _, translate

        request = DummyRequest()
        request.session = {'lang': 'fr'}

        self.assertEqual(
            translate(_('Hello ${n},', {'n': 'Mr Foo'}), 'fr'),
            'Bonjour Mr Foo,')
        self.assertEqual(
            translate(_('Hello ${n},', {'n': 'Mr Foo'}), request=request),
            'Bonjour Mr Foo,')
        self.assertIn('Mr Foo', translate(_('Hello ${n},', {'n': 'Mr Foo'})))


# =============================================================================
class ULibI18nTranslateField(TestCase):
    """Unit test class for :func:`lib.i18n.translate_field`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.translate_field]"""
        from ..lib.i18n import translate_field

        request = DummyRequest()
        request.registry['settings'] = {'language': 'en'}
        self.assertEqual(translate_field(request, None), '')

        i18n_field = {'en': 'User editor', 'fr': 'Éditeur des utilisateurs'}
        self.assertEqual(translate_field(request, i18n_field), 'User editor')

        request.locale_name = 'fr'
        self.assertEqual(
            translate_field(request, i18n_field), 'Éditeur des utilisateurs')

        request.locale_name = 'en'
        request.session['lang'] = 'fr'
        self.assertEqual(
            translate_field(request, i18n_field), 'Éditeur des utilisateurs')

        request.locale_name = 'es'
        request.session['lang'] = 'es'
        self.assertEqual(translate_field(request, i18n_field), 'User editor')


# =============================================================================
class ULibI18nRecordFormatI18n(TestCase):
    """Unit test class for :func:`lib.i18n.record_format_i18n`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.record_format_i18n]"""
        from json import dumps
        from ..lib.i18n import record_format_i18n

        # Without label
        record = {}
        self.assertFalse(record_format_i18n(record))

        # With label in 2 different ways
        record = {'i18n_label': dumps({'en': 'foo'}), 'label_fr': 'toto'}
        self.assertTrue(record_format_i18n(record))
        self.assertIn('i18n_label', record)
        self.assertIn('en', record['i18n_label'])
        self.assertIn('fr', record['i18n_label'])
        self.assertNotIn('i18n_description', record)

        record['description_en'] = 'Lorem ipsum'
        self.assertTrue(record_format_i18n(record))
        self.assertIn('i18n_description', record)


# =============================================================================
class ULibI18nViewI18nLabels(DBUnitTestCase):
    """Unit test class for :func:`lib.i18n.view_i18n_labels`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.view_i18n_labels]"""
        from json import dumps
        from ..lib.form import Form
        from ..lib.i18n import view_i18n_labels
        from ..models.dbprofile import DBProfile

        dbprofile = DBProfile(
            profile_id='user_creator',
            i18n_label=dumps({'en': 'Profile manager'}),
            i18n_description={'en': 'Permission to create profiles'})
        self.request.locale_name = 'en'
        html = view_i18n_labels(self.request, Form(self.request), dbprofile)
        self.assertIn('Profile manager', html)
        self.assertIn('Permission to create profiles', html)


# =============================================================================
class ULibI18nSchemaI18nLabels(DBUnitTestCase):
    """Unit test class for :func:`lib.i18n.schema_i18n_labels`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.schema_i18n_labels]"""
        from ..lib.i18n import schema_i18n_labels
        from ..models import LABEL_LEN, DESCRIPTION_LEN

        schema = colander.SchemaNode(colander.Mapping())
        schema_i18n_labels(self.request, schema, LABEL_LEN, DESCRIPTION_LEN)
        serialized = schema.serialize()
        self.assertIn('label_en', serialized)
        self.assertIn('description_en', serialized)

        self.request.registry['settings']['language'] = 'fr'
        schema = colander.SchemaNode(colander.Mapping())
        schema_i18n_labels(self.request, schema, LABEL_LEN)
        serialized = schema.serialize()
        self.assertIn('label_en', serialized)
        self.assertNotIn('description_en', serialized)


# =============================================================================
class ULibI18nDefaultsI18nLabels(TestCase):
    """Unit test class for :func:`lib.i18n.defaults_i18n_labels`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.defaults_i18n_labels]"""
        from json import dumps
        from ..lib.i18n import defaults_i18n_labels
        from ..models.dbprofile import DBProfile

        dbprofile = DBProfile(
            profile_id='user_creator',
            i18n_label=dumps({'en': 'Profile manager'}),
            i18n_description={'en': 'Permission to create profiles'})
        defaults = defaults_i18n_labels(dbprofile)
        self.assertIn('label_en', defaults)
        self.assertEqual(defaults['label_en'], 'Profile manager')
        self.assertIn('description_en', defaults)
        self.assertEqual(
            defaults['description_en'], 'Permission to create profiles')


# =============================================================================
class ULibI18nEditI18nLabels(DBUnitTestCase):
    """Unit test class for :func:`lib.i18n.edit_i18n_labels`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.i18n.edit_i18n_labels]"""
        from ..lib.form import Form
        from ..lib.i18n import edit_i18n_labels
        from ..models import LABEL_LEN, DESCRIPTION_LEN

        html = edit_i18n_labels(
            self.request, Form(self.request), LABEL_LEN, DESCRIPTION_LEN)
        self.assertIn('name="label_en"', html)
        self.assertIn('name="description_en"', html)

        html = edit_i18n_labels(
            self.request, Form(self.request), LABEL_LEN, 0)
        self.assertIn('name="label_en"', html)
        self.assertNotIn('name="description_en"', html)

        html = edit_i18n_labels(
            self.request, Form(self.request), 0, DESCRIPTION_LEN)
        self.assertNotIn('name="label_en"', html)
        self.assertIn('name="description_en"', html)
