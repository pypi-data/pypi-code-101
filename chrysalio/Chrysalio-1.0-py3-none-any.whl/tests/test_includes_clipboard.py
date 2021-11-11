# pylint: disable = import-outside-toplevel
"""Tests of ``lib.clipboard`` class."""

from unittest import TestCase

from pyramid.testing import DummyRequest

from . import ConfiguratorTestCase


# =============================================================================
class UIncludesClipboardIncludeme(ConfiguratorTestCase):
    """Unit test class for :func:`includes.clipboard.includeme`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.clipboard.includeme]"""
        self.configurator.include('..includes.clipboard')
        self.assertIn('panels', self.configurator.registry)
        self.assertIn('clipboard', self.configurator.registry['panels'])


# =============================================================================
class ULibClipboardlClipboard(TestCase):
    """Unit test class for :class:`lib.clipboard.Clipboard`."""

    # -------------------------------------------------------------------------
    def test_is_empty(self):
        """[u:lib.clipboard.Clipboard.is_empty]"""
        from ..includes.clipboard import Clipboard

        # Empty
        request = DummyRequest()
        self.assertTrue(Clipboard.is_empty(request))

        # Not empty
        request.session['clipboard'] = [('wfile', False, 'my_data', 'My data')]
        self.assertFalse(Clipboard.is_empty(request))

    # -------------------------------------------------------------------------
    def test_entries(self):
        """[u:lib.clipboard.Clipboard.entries]"""
        from ..includes.clipboard import Clipboard

        request = DummyRequest()
        request.session['clipboard'] = [
            ('wfile', False, 'my_data1', 'My data 1'),
            ('wfile', False, 'my_data2', 'My data 2')]
        entries = Clipboard.entries(request)
        self.assertEqual(len(entries), 2)

    # -------------------------------------------------------------------------
    def test_push(self):
        """[u:lib.clipboard.Clipboard.push]"""
        from ..includes.clipboard import Clipboard

        request = DummyRequest()
        request.registry = {'settings': {'clipboard-size': 3}}
        Clipboard.push(request, 'wfile', False, 'my_data', 'My data')
        entries = Clipboard.entries(request)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0][0], 'wfile')
        self.assertFalse(entries[0][1])
        self.assertEqual(entries[0][2], 'my_data')
        self.assertEqual(entries[0][3], 'My data')

    # -------------------------------------------------------------------------
    def test_selection(self):
        """[u:lib.clipboard.Clipboard.selection]"""
        from ..lib.panel import PANEL_ITEM_PREFIX
        from ..includes.clipboard import Clipboard

        # Empty clipboard
        request = DummyRequest()
        request.registry = {'settings': {'clipboard-size': 3}}
        self.assertFalse(Clipboard.selection(request, ('wfile',)))

        # Without explicit request
        Clipboard.push(request, 'wfile', True, 'my_data1', 'My data 1')
        Clipboard.push(request, 'wfile', False, 'my_data2', 'My data 2')
        Clipboard.push(request, 'user', False, 4, 'Luc SAMBOUR')
        selection = Clipboard.selection(request, ('wfile',))
        self.assertEqual(len(selection), 1)
        self.assertEqual(selection[0][2], 'my_data2')
        entries = Clipboard.entries(request)
        self.assertEqual(len(entries), 3)
        self.assertEqual(entries[0][2], 'my_data2')
        self.assertEqual(entries[1][2], 4)
        self.assertEqual(entries[2][2], 'my_data1')

        # With explicit request
        request.params = {
            '{0}1'.format(PANEL_ITEM_PREFIX): True,
            '{0}2'.format(PANEL_ITEM_PREFIX): True}
        selection = Clipboard.selection(request, ('wfile',))
        self.assertEqual(len(selection), 1)
        self.assertEqual(selection[0][2], 'my_data1')
        entries = Clipboard.entries(request)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0][2], 'my_data2')
        self.assertEqual(entries[1][2], 4)

        # Too many enntries
        Clipboard.push(request, 'wfile', True, 'my_data3', 'My data 3')
        Clipboard.push(request, 'wfile', True, 'my_data4', 'My data 4')
        entries = Clipboard.entries(request)
        self.assertEqual(len(entries), 3)
        self.assertEqual(entries[0][2], 'my_data4')
        self.assertEqual(entries[1][2], 'my_data3')
        self.assertEqual(entries[2][2], 'my_data2')
