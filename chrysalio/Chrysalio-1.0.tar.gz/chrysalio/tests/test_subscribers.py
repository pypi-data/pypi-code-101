# pylint: disable = import-outside-toplevel
"""Tests of ``subscribers`` classes and functions."""

from unittest import TestCase

from pyramid import testing
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('chrysalio')


# =============================================================================
class SubscribersTestCase(TestCase):
    """Base class for testing subscribers."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = testing.setUp(settings={
            'testing': 'true',
            'theme.roots': 'chrysalio:Themes',
            'theme.patterns': 'Default, Alternative*'})

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects ``pyramid.testing.setUp()``."""
        testing.tearDown()


# =============================================================================
class USubscribersIncludeme(SubscribersTestCase):
    """Unit test class for :func:`subscribers.includeme`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = testing.setUp()

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:routes.includeme]"""
        self.configurator.include('..subscribers')
        self.assertIsNotNone(
            self.configurator.registry.introspector.get_category(
                'subscribers'))


# =============================================================================
class USubscribersBeforeRender(SubscribersTestCase):
    """Unit test class for :func:`subscribers.before_render`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:routes.before_render]"""
        from ..includes.themes import load_themes
        from ..subscribers import before_render

        self.configurator.include('pyramid_chameleon')
        self.configurator.registry['settings'] = {
            'title': 'Test Chrysalio', 'theme': ''}
        load_themes(self.configurator)
        request = testing.DummyRequest()
        request.session['theme'] = 'Default'
        event = {
            'request': request, 'renderer_name': 'chrysalio:Templates/home.pt'}
        before_render(event)
        self.assertIn('layout', event)
        self.assertIn('theme', event)
        self.assertIn('theme_has', event)
        self.assertIn('_', event)
        self.assertIn('title', event)

        msg = event['_'](_('Foo'))
        self.assertEqual(msg, 'Foo')
