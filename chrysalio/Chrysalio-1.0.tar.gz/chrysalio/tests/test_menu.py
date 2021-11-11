# pylint: disable = import-outside-toplevel
"""Tests of ``menu`` functions."""

from unittest import TestCase

from . import ConfiguratorTestCase


# =============================================================================
class UMenuIncludeme(ConfiguratorTestCase):
    """Unit test class for :func:`menu.includeme`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:menu.includeme]"""
        self.configurator.include('..menu')
        self.assertIn('menu', self.configurator.registry)


# =============================================================================
class UMenuBeforeRender(TestCase):
    """Unit test class for :func:`menu.before_render`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:menu.before_render]"""
        from pyramid.testing import DummyRequest
        from ..lib.menu import Menu
        from ..menu import before_render

        request = DummyRequest()
        request.registry['menu'] = ''
        event = {'request': request}
        before_render(event)
        self.assertIn('menu', event)
        self.assertIsInstance(event['menu'], Menu)
