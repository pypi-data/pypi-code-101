# pylint: disable = import-outside-toplevel
"""Tests of ``views.panel`` functions."""

from collections import namedtuple
from unittest import TestCase

from pyramid.testing import DummyRequest, DummySession

from ..lib.panel import Panel


# =============================================================================
class DummyPanel(Panel):
    """A class to test panels."""

    uid = 'dummy'
    label = 'Side Panel'


# =============================================================================
class UViewsPanelPanelView(TestCase):
    """Unit test class for testing :func:`views.panel.panel_view`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.panel.panel_view]"""
        from ..views.panel import panel_view

        request = DummyRequest()
        request.registry = {}
        request.session = DummySession({})
        panel = DummyPanel()

        # Without panels
        panel_view(request)
        self.assertNotIn('panels', request.registry)

        # With panels but an unknown panel to open
        request.registry = {'panels': {}}
        request.matchdict = {'panel_id': 'test'}
        panel_view(request)
        self.assertNotIn('test', request.registry['panels'])

        # With panels and a known panel to open
        request.matched_route = namedtuple('Route', 'name')(name='panel_open')
        request.registry['panels']['test'] = panel
        panel_view(request)
        self.assertFalse(panel.was_open(request))
        self.assertTrue(panel.is_open(request))

        # With panels and a known panel to close
        request.matched_route = namedtuple('Route', 'name')(name='panel_close')
        panel_view(request)
        self.assertFalse(panel.was_open(request))
        self.assertFalse(panel.is_open(request))
