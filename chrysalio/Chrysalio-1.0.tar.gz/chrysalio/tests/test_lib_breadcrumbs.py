# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.breadcrumbs`` class methods."""

from unittest import TestCase


# =============================================================================
class ULibBreadcrumbsBreadcrumbs(TestCase):
    """Unit test class for :class:`lib.breadcrumbs.Breadcrumbs`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pyramid.testing import setUp, DummyRequest

        self.configurator = setUp()
        self.request = DummyRequest(matched_route=None)

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from pyramid.testing import tearDown
        tearDown()

    # -------------------------------------------------------------------------
    def make_one(self):
        """Create an instance of breadcrumbs.

        rtype: Breadcrumbs
        """
        from ..lib.breadcrumbs import Breadcrumbs

        self.configurator.add_route('home', '/')
        self.configurator.add_route('user_index', '/user/index')
        self.configurator.add_route('user_edit', '/user/edit')
        self.configurator.add_route('profile_index', '/profile/index')
        return Breadcrumbs(self.request)

    # -------------------------------------------------------------------------
    def test_call_home(self):
        """[u:lib.breadcrumbs.Breadcrumbs.__call__] home"""
        from collections import namedtuple

        breadcrumbs = self.make_one()
        breadcrumbs('Home', 1)
        self.assertIn('breadcrumbs', self.request.session)
        crumbs = self.request.session['breadcrumbs']
        self.assertEqual(len(crumbs), 1)
        self.assertEqual(crumbs[0][0], 'Home')
        self.assertIsNone(crumbs[0][1])
        self.assertEqual(crumbs[0][2], {})
        self.assertEqual(crumbs[0][3], 20)

        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        breadcrumbs('Home', 0)
        crumbs = self.request.session['breadcrumbs']
        self.assertEqual(crumbs[0][1], 'home')

    # -------------------------------------------------------------------------
    def test_call_replace(self):
        """[u:lib.breadcrumbs.Breadcrumbs.__call__] with replacement"""
        from collections import namedtuple

        breadcrumbs = self.make_one()
        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        breadcrumbs('Home', 1)
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')
        breadcrumbs('User List')
        self.assertEqual(len(self.request.session['breadcrumbs']), 2)
        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_index')
        breadcrumbs('Profile List', replace=breadcrumbs.current_path())
        self.assertEqual(len(self.request.session['breadcrumbs']), 2)
        breadcrumbs('Profile List')
        self.assertEqual(len(self.request.session['breadcrumbs']), 2)

    # -------------------------------------------------------------------------
    def test_call_anchor(self):
        """[u:lib.breadcrumbs.Breadcrumbs.__call__] with anchor"""
        breadcrumbs = self.make_one()
        breadcrumbs('Home', forced_route=('home', {}))
        breadcrumbs(
            'User Edition', anchor='current',
            forced_route=('user_index', {'user_id': 0}))
        self.assertEqual(len(self.request.session['breadcrumbs']), 2)
        last_crumb = self.request.session['breadcrumbs'][-1]
        self.assertEqual(len(last_crumb[2]), 2)
        self.assertIn('user_id', last_crumb[2])
        self.assertIn('_anchor', last_crumb[2])
        self.assertEqual(last_crumb[2]['user_id'], 0)
        self.assertEqual(last_crumb[2]['_anchor'], 'current')

    # -------------------------------------------------------------------------
    def test_pop(self):
        """[u:lib.breadcrumbs.Breadcrumbs.pop]"""
        breadcrumbs = self.make_one()
        breadcrumbs('Home', forced_route=('home', {}))
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(len(self.request.session['breadcrumbs']), 2)
        breadcrumbs.pop()
        self.assertEqual(len(self.request.session['breadcrumbs']), 1)
        self.assertEqual(self.request.session['breadcrumbs'][0][1], 'home')

    # -------------------------------------------------------------------------
    def test_trail(self):
        """[u:lib.breadcrumbs.Breadcrumbs.trail]"""
        from webhelpers2.html import literal

        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.trail(), literal('&nbsp;'))
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.trail(), literal('&nbsp;'))
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(
            breadcrumbs.trail(), literal('<a href="/">Home</a> ‣ User List'))
        breadcrumbs.pop()
        breadcrumbs('User List')
        breadcrumbs('Profile List')
        self.assertEqual(
            breadcrumbs.trail(),
            literal('<a href="/">Home</a> ‣ User List ‣ Profile List'))

    # -------------------------------------------------------------------------
    def test_current_title(self):
        """[u:lib.breadcrumbs.Breadcrumbs.current_title]"""
        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.current_title(), 'Home')
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.current_title(), 'Home')
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(breadcrumbs.current_title(), 'User List')

    # -------------------------------------------------------------------------
    def test_current_route_name(self):
        """[u:lib.breadcrumbs.Breadcrumbs.current_route_name]"""
        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.current_route_name(), 'home')
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.current_route_name(), 'home')
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(breadcrumbs.current_route_name(), 'user_index')

    # -------------------------------------------------------------------------
    def test_current_path(self):
        """[u:lib.breadcrumbs.Breadcrumbs.current_path]"""
        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.current_path(), '/')
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.current_path(), '/')
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(breadcrumbs.current_path(), '/user/index')

    # -------------------------------------------------------------------------
    def test_crumb_trail(self):
        """[u:lib.breadcrumbs.Breadcrumbs.crumb_trail]"""
        from collections import namedtuple
        from ..lib.breadcrumbs import DEFAULT_ROOT_CHUNKS

        breadcrumbs = self.make_one()
        self.assertEqual(len(breadcrumbs.crumb_trail()), 0)

        self.request.matched_route = namedtuple('Route', 'name')(name='home')
        crumb_trail = breadcrumbs.crumb_trail()
        self.assertEqual(len(crumb_trail), 1)
        self.assertEqual(crumb_trail[0], ([''], DEFAULT_ROOT_CHUNKS))

        breadcrumbs('Home', forced_route=('home', {}))
        crumb_trail = breadcrumbs.crumb_trail()
        self.assertEqual(len(crumb_trail), 1)
        self.assertEqual(crumb_trail[0], ([''], DEFAULT_ROOT_CHUNKS))

        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')
        breadcrumbs('User Management', forced_route=('user_index', {}))
        self.assertEqual(len(breadcrumbs.crumb_trail()), 2)

        self.request.matched_route = namedtuple('Route', 'name')(
            name='profile_index')
        self.assertEqual(len(breadcrumbs.crumb_trail()), 3)

    # -------------------------------------------------------------------------
    def test_back_title(self):
        """[u:lib.breadcrumbs.Breadcrumbs.back_title]"""
        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.back_title(), 'Home')
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.back_title(), 'Home')
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(breadcrumbs.back_title(), 'Home')
        breadcrumbs('Profile List', forced_route=('user_profile', {}))
        self.assertEqual(breadcrumbs.back_title(), 'User List')

    # -------------------------------------------------------------------------
    def test_back_path(self):
        """[u:lib.breadcrumbs.Breadcrumbs.back_path]"""
        breadcrumbs = self.make_one()
        self.assertEqual(breadcrumbs.back_path(), '/')
        breadcrumbs('Home', forced_route=('home', {}))
        self.assertEqual(breadcrumbs.back_path(), '/')
        breadcrumbs('User List', forced_route=('user_index', {}))
        self.assertEqual(breadcrumbs.back_path(), '/')
        breadcrumbs('Profile List', forced_route=('profile_index', {}))
        self.assertEqual(breadcrumbs.back_path(), '/user/index')
