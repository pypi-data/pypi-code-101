# pylint: disable = import-outside-toplevel
"""Tests of ``lib.config`` classes and functions."""

from os.path import dirname
from configparser import ConfigParser
from unittest import TestCase

from pyramid.security import Authenticated, Allow, ALL_PERMISSIONS

from . import ConfiguratorTestCase


# =============================================================================
class ConfigTestCase(TestCase):
    """Base class for testing config functions."""

    config = None

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..lib.utils import tounicode
        from . import TEST_INI

        self.config = ConfigParser({'here': dirname(TEST_INI)})
        self.config.read(tounicode(TEST_INI), encoding='utf8')


# =============================================================================
class ULibConfigUpdateACL(ConfiguratorTestCase):
    """Unit test class for :func:`lib.config.update_acl`."""

    # -------------------------------------------------------------------------
    def test_update(self):
        """[u:lib.config.update_acl]"""
        from ..lib.config import update_acl

        class DummyRootFactory(object):
            """Dummy Access Control List (ACL) definition."""
            # pylint: disable = too-few-public-methods
            __acl__ = [
                (Allow, Authenticated, 'authenticated'),
                (Allow, 'system.administrator', ALL_PERMISSIONS)]

            def __init__(self, request):
                """Constructor method."""

        principals = (
            ('document', 'Document management', (
                ('viewer', 'View all documents', (
                    'document-view',)),
                ('editor', 'Edit any document', (
                    'document-view', 'document-edit')))),)
        self.configurator.set_root_factory(DummyRootFactory)
        root_factory = self.configurator.introspector.get(
            'root factories', None).get('factory')
        self.assertEqual(len(root_factory.__acl__), 2)
        update_acl(self.configurator, principals)
        self.assertEqual(len(root_factory.__acl__), 4)
        self.assertEqual(root_factory.__acl__[2][0], Allow)
        self.assertIn(
            root_factory.__acl__[2][1], ('document.viewer', 'document.editor'))
        self.assertIn('document-view', root_factory.__acl__[2][2])


# =============================================================================
class ULibConfigConfigGet(ConfigTestCase):
    """Unit test class for :func:`lib.config.config_get`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.config.config_get]"""
        from ..lib.config import config_get

        self.assertEqual(config_get(
            self.config, 'app:main', 'site.uid'), 'testchrysalio')
        self.assertEqual(config_get(self.config, 'app:main', 'foo'), None)
        self.assertEqual(
            config_get(self.config, 'app:main', 'foo', 'bar'), 'bar')


# =============================================================================
class ULibConfigConfigGetList(ConfigTestCase):
    """Unit test class for :func:`lib.config.config_get_list`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.config.config_get_list]"""
        from ..lib.config import config_get_list

        self.assertEqual(
            config_get_list(self.config, 'app:main', 'site.uid'),
            ['testchrysalio'])
        self.assertEqual(config_get_list(self.config, 'app:main', 'foo'), [])
        self.assertEqual(
            config_get_list(self.config, 'app:main', 'foo', 'bar'), 'bar')
        self.assertEqual(
            config_get_list(self.config, 'loggers', 'keys'),
            ['root', 'chrysalio', 'sqlalchemy'])


# =============================================================================
class ULibConfigConfigGetNamespace(ConfigTestCase):
    """Unit test class for :func:`lib.config.config_get_namespace`."""

    # -------------------------------------------------------------------------
    def test_unknown_section(self):
        """[u:lib.config.config_get_namespace] unknown section"""
        from ..lib.config import config_get_namespace

        theme = config_get_namespace(self.config, 'foo', 'theme')
        self.assertEqual(len(theme), 0)

    # -------------------------------------------------------------------------
    def test_existing_section(self):
        """[u:lib.config.config_get_namespace] existing section"""
        from ..lib.config import config_get_namespace

        theme = config_get_namespace(self.config, 'app:main', 'theme')
        self.assertIn('roots', theme)
        self.assertIn('patterns', theme)
        self.assertEqual(theme['patterns'], 'Default')


# =============================================================================
class ULibConfigSettingsGetList(TestCase):
    """Unit test class for :func:`lib.config.settings_get_list`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.config.settings_get_list]"""
        from ..lib.config import settings_get_list

        settings = {
            'option1': '',
            'option2': 'test',
            'option3': 'test1, test2'}
        self.assertEqual(settings_get_list(settings, 'option1'), [])
        self.assertEqual(settings_get_list(settings, 'optionX'), [])
        self.assertEqual(
            settings_get_list(settings, 'option1', ['vide']), ['vide'])
        self.assertEqual(
            settings_get_list(settings, 'optionX', ['vide']), ['vide'])
        self.assertEqual(
            settings_get_list(settings, 'option2'), ['test'])
        self.assertEqual(
            settings_get_list(settings, 'option3'), ['test1', 'test2'])


# =============================================================================
class ULibConfigSettingsGetNamespace(TestCase):
    """Unit test class for :func:`lib.config.settings_get_namespace`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.config.settings_get_namespace]"""
        from ..lib.config import settings_get_namespace

        settings = {
            'processor.roots': 'cioprocessor:Processors',
            'build.develop': 'true',
            'build.root': '%(here)s/Builds',
            'build.foo.bar': 'baz'}
        builds = settings_get_namespace(settings, 'build')
        self.assertIsInstance(builds, dict)
        self.assertIn('develop', builds)
        self.assertIn('foo_bar', builds)
        self.assertNotIn('processor.roots', builds)
        self.assertNotIn('roots', builds)


# =============================================================================
class ULibConfigSettingsGetDirectories(TestCase):
    """Unit test class for :func:`lib.config.settings_get_directories`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.config.settings_get_directories]"""
        from ..lib.config import settings_get_directories

        settings = {
            'theme.roots': 'chrysalio:Themes, chrysalio:Foo, chrysalio:Static',
            'theme.patterns':  'Default, Alternative*'}
        directories = settings_get_directories(settings, 'theme', 'theme.conf')
        self.assertIn('Default', directories)
        self.assertIn('Alternative', directories)
