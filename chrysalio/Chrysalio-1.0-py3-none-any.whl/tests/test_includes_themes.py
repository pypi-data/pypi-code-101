# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``includes.themes`` classes and functions."""

from os.path import normpath, dirname, join
from unittest import TestCase

from pyramid.testing import setUp, tearDown
from pyramid.testing import DummyRequest


# =============================================================================
class ThemeTestCase(TestCase):
    """Base class for testing themes."""

    configurator = None
    layout = normpath(join(dirname(__file__), '..', 'Templates', 'layout.pt'))

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:Themes',
            'theme.patterns': 'Default, Alternative*'})
        self.configurator.registry['settings'] = {'theme': ''}

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()


# =============================================================================
class UIncludesThemesIncludeme(ThemeTestCase):
    """Unit test class for :func:`includes.themes.includeme`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.includeme]"""
        self.configurator.include('..includes.themes')
        self.assertIn('themes', self.configurator.registry)


# =============================================================================
class UIncludesThemesLoadThemes(ThemeTestCase):
    """Unit test class for :func:`includes.themes.load_themes`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes]"""
        from ..includes.themes import load_themes

        load_themes(self.configurator)
        self.assertIn('themes', self.configurator.registry)
        themes = self.configurator.registry['themes']
        self.assertIn('Default', themes)
        self.assertIn('Alternative', themes)
        self.assertIn('path', themes['Default'])
        self.assertIn('name', themes['Default'])
        self.assertIn('layout', themes['Default'])
        self.assertIsInstance(themes['Default']['name'], dict)
        self.assertEqual(themes['Default']['name']['en'], 'Chrysalio')
        self.assertEqual(themes['Default']['name']['fr'], 'Chrysalio')
        self.assertEqual(
            themes['Alternative']['name']['en'], 'Chrysalio Alternative')


# =============================================================================
class UIncludesThemesLoadThemesMissingTemplates(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with missing
    [Templates] section."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:tests/Themes',
            'theme.patterns': 'Test1'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] section [Templates] is missing"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesLoadThemesMissingLayout(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with missing
    layout."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:tests/Themes',
            'theme.patterns': 'Test2'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] layout is missing"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesLoadThemesMissingCss(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with missing
    CSS."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:tests/Themes',
            'theme.patterns': 'Test3'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] CSS is missing"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesLoadThemesEmptyCss(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with empty
    CSS."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:tests/Themes',
            'theme.patterns': 'Test4'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] CSS is empty"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesLoadThemesUnknownCss(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with unknown
    CSS."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:tests/Themes',
            'theme.patterns': 'Test5'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] CSS is unknown"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesLoadThemesUnknownDefault(TestCase):
    """Unit test class for :func:`includes.themes.load_themes` with unknown
    default theme."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp(settings={
            'theme.roots': 'chrysalio:Themes',
            'theme.patterns': 'Default, Alternative*'})
        self.configurator.registry['settings'] = {'theme': 'foo'}

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        tearDown()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.load_themes] default theme is unknown"""
        from ..includes.themes import load_themes

        self.assertRaises(SystemExit, load_themes, self.configurator)


# =============================================================================
class UIncludesThemesCreateDefaultTheme(ThemeTestCase):
    """Unit test class for ``includes.themes.create_default_theme``."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.create_default_theme]"""
        from ..includes.themes import create_default_theme

        self.assertNotIn('themes', self.configurator.registry)
        create_default_theme(self.configurator, 'chrysalio')
        self.assertIn('themes', self.configurator.registry)
        themes = self.configurator.registry['themes']
        self.assertIn('path', themes[''])
        self.assertIn('name', themes[''])
        self.assertIn('layout', themes[''])
        self.assertEqual(themes['']['layout'], self.layout)


# =============================================================================
class UIncludesThemesThemeTemplate(ThemeTestCase):
    """Unit test class for ``includes.themes.theme_template``."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.theme_template]"""
        from ..includes.themes import theme_template

        self.configurator.include('..includes.themes')
        request = DummyRequest()
        path = theme_template(request, 'layout')
        self.assertEqual(path, self.layout)


# =============================================================================
class UIncludesThemesThemeStaticPrefix(ThemeTestCase):
    """Unit test class for ``includes.themes.theme_static_prefix``."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.theme_static_prefix]"""
        from ..includes.themes import theme_static_prefix

        self.configurator.include('..includes.themes')

        prefix = theme_static_prefix(None)
        self.assertEqual(prefix, '')

        request = DummyRequest()
        prefix = theme_static_prefix(request)
        self.assertEqual(prefix, '/theme/default')


# =============================================================================
class UIncludesThemesThemeHasStatic(ThemeTestCase):
    """Unit test class for ``includes.themes.theme_has_static``."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.themes.theme_has_static]"""
        from ..includes.themes import theme_has_static

        request = DummyRequest()
        self.configurator.include('..includes.themes')
        self.assertTrue(theme_has_static(request, 'css'))
        self.assertFalse(theme_has_static(request, 'css+'))
