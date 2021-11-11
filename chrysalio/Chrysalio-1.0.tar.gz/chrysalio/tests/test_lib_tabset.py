# pylint: disable = import-outside-toplevel
"""Tests of ``lib.tabet`` class."""

from unittest import TestCase


# =============================================================================
class ULibTabsetTabset(TestCase):
    """Unit test class for :class:`lib.tabet.Tabset` and
    :class:`lib.tabet.Tab`."""

    # -------------------------------------------------------------------------
    @classmethod
    def make_one(cls):
        """Create an instance of Tabset.

        rtype: Tabset
        """
        from pyramid.testing import DummyRequest
        from ..lib.tabset import Tabset

        return Tabset(
            DummyRequest(), 'tabUser', ('Information', 'Profiles'))

    # -------------------------------------------------------------------------
    def test_begin(self):
        """[u:lib.tabset.Tabset.begin]"""
        from webhelpers2.html import literal

        html = self.make_one().begin()
        self.assertIsInstance(html, literal)
        self.assertIn('id="tabUser"', html)
        self.assertIn('id="tabUser1"', html)
        self.assertIn('href="#tabUser1_"', html)

    # -------------------------------------------------------------------------
    def test_end(self):
        """[u:lib.tabset.Tabset.end]"""
        from webhelpers2.html import literal

        html = self.make_one().end()
        self.assertIsInstance(html, literal)
        self.assertEqual(html, '</div>\n')

    # -------------------------------------------------------------------------
    def test_tab_begin(self):
        """[u:lib.tabset.Tab.tab]"""
        from webhelpers2.html import literal
        from ..lib.tabset import Tab

        tab = self.make_one().tabs[0]
        self.assertIsInstance(tab, Tab)
        html = tab.begin()
        self.assertIsInstance(html, literal)
        self.assertIn('id="tabUser0_"', html)

    # -------------------------------------------------------------------------
    def test_tab_end(self):
        """[u:lib.tabset.Tab.end]"""
        from webhelpers2.html import literal

        tab = self.make_one().tabs[1]
        html = tab.end()
        self.assertIsInstance(html, literal)
        self.assertEqual(html, '</fieldset>\n')
