# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.panel`` class."""

from collections import namedtuple

from pyramid.testing import DummySession

from . import DBUnitTestCase
from ..lib.panel import Panel


# =============================================================================
class DummyPanel(Panel):
    """A class to test panels."""

    uid = 'dummy'
    label = 'Side Panel'


# =============================================================================
class OtherDummyPanel(Panel):
    """Another class to test panels."""

    uid = 'other'
    label = 'Other Side Panel'


# =============================================================================
class ULibPanellPanel(DBUnitTestCase):
    """Unit test class for :class:`lib.panel.Panel`."""

    # -------------------------------------------------------------------------
    def test_register(self):
        """[u:lib.panel.Panel.register]"""
        # Register a non derived Panel
        panel = Panel.register(
            self.request.registry, Panel, area=('home',), add2systray=True)
        self.assertIsNone(panel)

        # Register
        panel = Panel.register(
            self.request.registry, DummyPanel, area=('home',),
            add2systray=True)
        self.assertIn('panels', self.request.registry)
        self.assertIn(DummyPanel.uid, self.request.registry['panels'])
        self.assertEqual(
            self.request.registry['panels'][DummyPanel.uid], panel)
        self.assertIsInstance(panel, Panel)
        self.assertEqual(panel.uid, DummyPanel.uid)
        self.assertIsInstance(panel.area, tuple)
        self.assertEqual(panel.area[0], 'home')
        self.assertIn('systray', self.request.registry)
        self.assertEqual(len(self.request.registry['systray']), 1)
        self.assertEqual(
            self.request.registry['systray'][0].uid, panel.uid)

        # Register an already registred panel
        Panel.register(self.request.registry, DummyPanel)
        panel = self.request.registry['panels'][DummyPanel.uid]
        self.assertEqual(panel.uid, DummyPanel.uid)

    # -------------------------------------------------------------------------
    def test_has_open_panel(self):
        """[u:lib.panel.Panel.has_open_panel]"""
        # Without panels
        self.assertIsNone(Panel.has_open_panel(self.request))

        # With a closed panel
        panel = Panel.register(self.request.registry, DummyPanel)
        self.assertFalse(panel.is_open(self.request))
        self.assertIsNone(Panel.has_open_panel(self.request))

        # With an open panel
        panel.open(self.request)
        self.assertIsNotNone(Panel.has_open_panel(self.request))

    # -------------------------------------------------------------------------
    def test_is_open(self):
        """[u:lib.panel.Panel.is_open]"""
        # In a right area
        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        panel = Panel.register(
            self.request.registry, DummyPanel, area=('home',))
        self.assertFalse(panel.is_open(self.request))
        panel.open(self.request)
        self.assertTrue(panel.is_open(self.request))

        # Out of a right area
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')
        self.assertFalse(panel.is_open(self.request))

    # -------------------------------------------------------------------------
    def test_was_open(self):
        """[u:lib.panel.Panel.was_open]"""
        panel = Panel.register(self.request.registry, DummyPanel)
        self.assertFalse(panel.was_open(self.request))
        panel.open(self.request)
        self.assertFalse(panel.was_open(self.request))
        panel.open(self.request)
        self.assertTrue(panel.was_open(self.request))

    # -------------------------------------------------------------------------
    def test_open(self):
        """[u:lib.panel.Panel.open]"""
        panel = Panel.register(self.request.registry, DummyPanel)
        panel_other = Panel.register(self.request.registry, OtherDummyPanel)
        panel_other.open(self.request)
        panel.open(self.request)
        self.assertTrue(panel.is_open(self.request))
        self.assertFalse(panel_other.is_open(self.request))

    # -------------------------------------------------------------------------
    def test_close(self):
        """[u:lib.panel.Panel.close]"""
        panel = Panel.register(self.request.registry, DummyPanel)
        panel.open(self.request)
        panel.close(self.request)
        self.assertFalse(panel.was_open(self.request))
        self.assertFalse(panel.is_open(self.request))

    # -------------------------------------------------------------------------
    def test_clear_values(self):
        """[u:lib.panel.Panel.clear_values]"""
        panel = DummyPanel()
        self.request.session = DummySession({'panels': {panel.uid: {
            'values': {'foo': 'bar'}}}})
        panel.clear_values(self.request)
        self.assertNotIn('values', self.request.session['panels'][panel.uid])

    # -------------------------------------------------------------------------
    def test_set_values(self):
        """[u:lib.panel.Panel.set_values]"""
        panel = DummyPanel()
        panel.set_values(self.request, {'foo': 'bar'})
        self.assertEqual(panel.value(self.request, 'foo'), 'bar')

    # -------------------------------------------------------------------------
    def test_values(self):
        """[u:lib.panel.Panel.values]"""
        self.request.session = DummySession({'panels': {DummyPanel.uid: {
            'values': {'foo': 'bar'}}}})
        values = DummyPanel().values(self.request)
        self.assertIsInstance(values, dict)
        self.assertIn('foo', values)
        self.assertEqual(values['foo'], 'bar')

    # -------------------------------------------------------------------------
    def test_set_value(self):
        """[u:lib.panel.Panel.set_value]"""
        panel = DummyPanel()
        panel.set_value(self.request, 'foo', 'bar')
        self.assertEqual(panel.value(self.request, 'foo'), 'bar')

    # -------------------------------------------------------------------------
    def test_value(self):
        """[u:lib.panel.Panel.value]"""
        panel = DummyPanel()
        self.request.session = DummySession({'panels': {panel.uid: {
            'values': {'huge': 'énorme'}}}})
        self.assertEqual(panel.value(self.request, 'huge'), 'énorme')
        self.assertIsNone(panel.value(self.request, 'none'))

    # -------------------------------------------------------------------------
    def test_render(self):
        """[u:lib.panel.Panel.render]"""
        self.configurator.add_route('home', '/')
        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        panel = Panel.register(self.request.registry, DummyPanel)
        panel.need_form = True
        html = panel.render(self.request)
        self.assertIn('data-uid="{0}"'.format(panel.uid), html)
        self.assertIn('href="/?panel={0}"'.format(panel.uid), html)

    # -------------------------------------------------------------------------
    def test_route(self):
        """[u:lib.panel.Panel.route]"""
        panel = DummyPanel()
        self.configurator.add_route('home', '/')
        self.request.GET = {'panel': panel.uid}

        route = panel.route(self.request)
        self.assertEqual(route, '')

        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        route = panel.route(self.request)
        self.assertEqual(route, '/?panel={0}'.format(panel.uid))

    # -------------------------------------------------------------------------
    def test_open_panel_css(self):
        """[u:lib.panel.Panel.open_panel_css]"""
        # Without panel
        css = Panel.open_panel_css(self.request)
        self.assertIsInstance(css, tuple)
        self.assertEqual(css, ())

        # Without open panel
        panel = Panel.register(self.request.registry, DummyPanel)
        panel.css = ('/cioxml/css/panel_cioset.css',)
        self.assertFalse(Panel.open_panel_css(self.request))

        # With open panel
        panel.open(self.request)
        css = Panel.open_panel_css(self.request)
        self.assertEqual(len(css), 1)
        self.assertEqual(css[0], '/cioxml/css/panel_cioset.css')

    # -------------------------------------------------------------------------
    def test_open_panel_js(self):
        """[u:lib.panel.Panel.open_panel_js]"""
        # Without panel
        javascripts = Panel.open_panel_js(self.request)
        self.assertIsInstance(javascripts, tuple)
        self.assertEqual(javascripts, ())

        # Without open panel
        panel = Panel.register(self.request.registry, DummyPanel)
        panel.javascripts = ('/cioxml/js/panel_cioset.js',)
        self.assertFalse(Panel.open_panel_js(self.request))

        # With open panel
        panel.open(self.request)
        javascripts = Panel.open_panel_js(self.request)
        self.assertEqual(len(javascripts), 1)
        self.assertEqual(javascripts[0], '/cioxml/js/panel_cioset.js')

    # -------------------------------------------------------------------------
    def test_manage_panels(self):
        """[u:lib.panel.Panel.manage_panels]"""
        # Without panel
        Panel.manage_panels(self.request)
        self.assertNotIn('panels', self.request.registry)

        # Open a panel
        panel = Panel.register(self.request.registry, DummyPanel)
        other_panel = Panel.register(self.request.registry, OtherDummyPanel)
        other_panel.open(self.request)
        self.assertTrue(other_panel.is_open(self.request))
        self.request.GET = {'panel': panel.uid}
        Panel.manage_panels(self.request)
        self.assertTrue(panel.is_open(self.request))
        self.assertFalse(panel.was_open(self.request))
        self.assertFalse(other_panel.is_open(self.request))

        # With panels, close
        Panel.manage_panels(self.request)
        self.assertFalse(panel.is_open(self.request))
        self.assertFalse(panel.was_open(self.request))
