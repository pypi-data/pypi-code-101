# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``views.settings`` class."""

from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsSettingsSettingsView(DBUnitTestCase):
    """Unit test class for testing :class:`views.settings.SettingsView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..models.dbsettings import DBSettings
        super(UViewsSettingsSettingsView, self).setUp()

        dbsession = self.request.dbsession
        dbsession.add(DBSettings(key='title', value='Test Chrysalio'))
        dbsession.add(DBSettings(key='email', value='admin@chrysal.io'))
        dbsession.add(DBSettings(key='password-min-length', value='8'))
        dbsession.add(DBSettings(key='language', value='en'))
        dbsession.add(DBSettings(key='page-size', value='80'))
        dbsession.add(DBSettings(key='download-max-size', value='10485760'))
        dbsession.add(DBSettings(key='clipboard-size', value='7'))

        self.configurator.add_route('home', '/')
        self.configurator.add_route('settings_view', '/settings/view')
        self.configurator.add_route('settings_edit', '/settings/edit')

        self.request.registry['settings']['email'] = 'admin@chrysal.io'

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:views.settings.SettingsView.view]"""
        from collections import namedtuple
        from ..views.settings import SettingsView
        from . import DummyPOST

        self.request.matched_route = namedtuple('Route', 'name')(
            name='settings_view')

        response = SettingsView(self.request).view()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'General Settings')

        self.request.is_xhr = True
        self.request.POST = DummyPOST()
        response = SettingsView(self.request).view()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    # -------------------------------------------------------------------------
    def test_view_export(self):
        """[u:views.settings.SettingsView.view] export settings"""
        from pyramid.response import Response
        from ..views.settings import SettingsView

        self.request.POST = {'exp!.x': True}

        response = SettingsView(self.request).view()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.content_type, 'application/xml')
        self.assertIn(b'<title>Test Chrysalio</title>', response.body)

    # -------------------------------------------------------------------------
    def test_view_import(self):
        """[u:views.settings.SettingsView.view] import settings"""
        from cgi import FieldStorage
        from . import TEST1_SET_XML, DummyPOST
        from ..views.settings import SettingsView
        from ..models.dbsettings import DBSettings

        dbsession = self.request.dbsession
        dbsetting = dbsession.query(DBSettings).filter_by(
            key='page-size').first()
        self.assertIsNotNone(dbsetting)
        self.assertEqual(dbsetting.value, '80')

        self.request.POST = DummyPOST({'imp!.x': True})
        with open(TEST1_SET_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_SET_XML
            self.request.POST.multikeys = {'file': (input_file,)}
            response = SettingsView(self.request).view()
        self.assertIn('dbsettings', response)
        dbsetting = dbsession.query(DBSettings).filter_by(
            key='page-size').first()
        self.assertIsNotNone(dbsetting)
        self.assertEqual(dbsetting.value, '40')

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:views.settings.SettingsView.edit]"""
        from collections import namedtuple
        from ..views.settings import SettingsView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='settings_edit')

        response = SettingsView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('dbsettings', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(),
            'General Settings Edition')

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:views.settings.SettingsView.edit] save"""
        from pyramid.httpexceptions import HTTPFound
        from ..views.settings import SettingsView

        self.request.POST = {
            'title': 'Test Chrysalio', 'email': 'admin@chrysal.io',
            'language': 'en', 'password-min-length': 8, 'remember-me': 5184000,
            'download-max-size': 10485760, 'clipboard-size': 7, 'sav!.x': True}

        SettingsView(self.request).edit()
        errors = self.request.session.pop_flash('alert')
        self.assertEqual(len(errors), 1)
        self.assertIn('Correct', errors[0])

        self.request.POST['page-size'] = 40
        self.assertIsInstance(SettingsView(self.request).edit(), HTTPFound)


# =============================================================================
class FViewsSettingsSettingsView(FunctionalTestCase):
    """Functional test class for testing
    :class:`views.settings.SettingsView`."""

    # -------------------------------------------------------------------------
    def test_view(self):
        """[f:views.settings.SettingsView.view]"""
        self.login('test1')
        self.testapp.get('/settings/view', status=403)

        self.login('admin')
        response = self.testapp.get('/settings/view', status=200)
        self.assertIn(b'Edit', response.body)

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[f:views.settings.SettingsView.edit]"""
        self.login('test1')
        self.testapp.get('/settings/edit', status=403)

        self.login('admin')
        response = self.testapp.get('/settings/edit', status=200)
        self.assertIn(b'Save', response.body)
