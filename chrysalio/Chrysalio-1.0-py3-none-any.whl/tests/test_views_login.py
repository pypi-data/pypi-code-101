# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``views.login`` functions."""

from . import DBUnitTestCase, FunctionalTestCase


# =============================================================================
class UViewsLoginLogin(DBUnitTestCase):
    """Unit test class for testing :func:`views.login.login`."""

    users = {
        'ok': {
            'login': 'user1', 'first_name': 'Marc',
            'last_name': 'HINDÈLAIBILE', 'email': 'user1@chrysal.io',
            'password': 'user1pwd'},
        'inactive': {
            'login': 'test2', 'first_name': 'Sophie', 'last_name': 'FONFEC',
            'status': 'inactive', 'email': 'test2@chrysal.io',
            'password': 'test2pwd'},
        'locked': {
            'login': 'test3', 'first_name': 'Guy', 'last_name': 'LIGUILI',
            'status': 'locked', 'email': 'test3@chrysal.io',
            'password': 'test3pwd'},
        'expired': {
            'login': 'test4', 'first_name': 'Gédéon',
            'last_name': 'TEUSEMANIE', 'email': 'test4@chrysal.io',
            'password': 'test4pwd', 'expiration': '2018-01-01'},
        'password_change': {
            'login': 'test5', 'first_name': 'Sébastienne',
            'last_name': 'TOUSSEUL', 'email': 'test5@chrysal.io',
            'password': 'test4pwd', 'password_mustchange': True}}

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        super(UViewsLoginLogin, self).setUp()
        self.configurator.add_route('home', '/')
        self.configurator.add_route('login', '/login')
        self.configurator.add_route(
            'user_password_reset', '/user/password/reset/{user_id}/{token}')

    # -------------------------------------------------------------------------
    def fill_form(self, login, password):
        """Fill the login form.

        :param str login:
            Login value.
        :param str password:
            Clear password.
        """
        self.request.params = {'login': login, 'password': password}
        self.request.POST = self.request.params

    # -------------------------------------------------------------------------
    def test_without_login(self):
        """[u:views.login.login] without login"""
        from ..views.login import login
        from ..lib.form import Form

        url_from = 'http://localhost/foo'
        self.request.url = url_from
        response = login(self.request)
        self.assertIn('next', response)
        self.assertEqual(response['next'], url_from)
        self.assertIn('form', response)
        self.assertIsInstance(response['form'], Form)
        self.assertIn('next', response['form'].values)
        self.assertEqual(response['form'].values['next'], url_from)

    # -------------------------------------------------------------------------
    def test_empty_password(self):
        """[u:views.login.login] empty password"""
        from ..views.login import login

        self.fill_form(self.users['ok']['login'], None)
        self.add_user(self.users['ok'])

        response = login(self.request)
        alert = self.request.session.pop_flash('alert')
        self.assertFalse(alert)
        self.assertIn('form', response)

    # -------------------------------------------------------------------------
    def test_invalid_password(self):
        """[u:views.login.login] invalid password"""
        from ..views.login import login

        self.fill_form(self.users['ok']['login'], 'invalid_password')
        self.add_user(self.users['ok'])

        login(self.request)
        alert = self.request.session.pop_flash('alert')
        self.assertTrue(alert)
        self.assertIn('is incorrect', alert[0])

    # -------------------------------------------------------------------------
    def test_not_active(self):
        """[u:views.login.login] not active"""
        from ..views.login import login

        self.fill_form(
            self.users['inactive']['login'],
            self.users['inactive']['password'])
        self.add_user(self.users['inactive'])

        login(self.request)
        alert = self.request.session.pop_flash('alert')
        self.assertTrue(alert)
        self.assertIn('is not active', alert[0])

    # -------------------------------------------------------------------------
    def test_locked(self):
        """[u:views.login.login] locked"""
        from ..views.login import login

        self.fill_form(
            self.users['locked']['login'],
            self.users['locked']['password'])
        self.add_user(self.users['locked'])

        login(self.request)
        alert = self.request.session.pop_flash('alert')
        self.assertTrue(alert)
        self.assertIn('is locked', alert[0])

    # -------------------------------------------------------------------------
    def test_expired(self):
        """[u:views.login.login] expired"""
        from ..views.login import login

        self.fill_form(
            self.users['expired']['login'],
            self.users['expired']['password'])
        self.add_user(self.users['expired'])

        login(self.request)
        alert = self.request.session.pop_flash('alert')
        self.assertTrue(alert)
        self.assertIn('has expired', alert[0])

    # -------------------------------------------------------------------------
    def test_password_change(self):
        """[u:views.login.login] password change"""
        from pyramid.httpexceptions import HTTPFound
        from ..views.login import login

        self.fill_form(
            self.users['password_change']['login'],
            self.users['password_change']['password'])
        self.add_user(self.users['password_change'])

        response = login(self.request)
        self.assertIsInstance(response, HTTPFound)
        self.assertIn('password/reset', response.location)

    # -------------------------------------------------------------------------
    def test_authorized(self):
        """[u:views.login.login] authorized"""
        from pyramid.httpexceptions import HTTPFound
        from ..views.login import login

        self.fill_form(self.users['ok']['login'], self.users['ok']['password'])
        self.add_user(self.users['ok'])

        response = login(self.request)
        self.assertIsInstance(response, HTTPFound)


# =============================================================================
class FViewsLoginLogin(FunctionalTestCase):
    """Functional test class for testing :func:`views.login.login`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[f:views.login.login]"""
        response = self.testapp.get('/login', status=200)
        self.assertIn(b'Log in', response.body)


# =============================================================================
class UViewsLoginLogout(DBUnitTestCase):
    """Unit test class for testing :func:`views.login.logout`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.login.logout]"""
        from pyramid.httpexceptions import HTTPFound
        from ..views.login import logout

        self.configurator.add_route('login', '/login')
        self.request.session['user'] = {'user_id': 1, 'login': 'test1'}

        response = logout(self.request)
        self.assertIsInstance(response, HTTPFound)
