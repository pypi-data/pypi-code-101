# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.filter`` class methods."""

from json import dumps
from unittest import TestCase

from pyramid.testing import DummyRequest
from pyramid.httpexceptions import HTTPForbidden

from ..models.dbgroup import DBGroup
from . import DBUnitTestCase


# =============================================================================
class ULibFilterFilter(TestCase):
    """Unit test class for :class:`lib.filter.Filter`."""

    # -------------------------------------------------------------------------
    @classmethod
    def make_one(cls, request):
        """Create an instance of Filter.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        rtype: Filter
        """
        from ..lib.filter import Filter

        return Filter(
            request, 'users', (
                ('login', 'Login', True, None),
                ('name', 'Name', True, ''),
                ('active', 'Active', False, True),
                ('age', 'Age', False, 0),
                ('group', 'Group', False, [
                    ('', ' '), ('foo', 'Foo'), ('bar', 'Bar')])),
            (('active', '=', True), ('group', '!=', 'foo')), '1')

    # -------------------------------------------------------------------------
    def test__str__(self):
        """[u:lib.filter.Filter.__str__]"""
        afilter = self.make_one(DummyRequest())
        text = str(afilter)
        self.assertEqual(text, "[[('active', '=', True)]]")

    # -------------------------------------------------------------------------
    def test_is_empty(self):
        """[u:lib.filter.Filter.is_empty]"""
        afilter = self.make_one(DummyRequest())
        self.assertFalse(afilter.is_empty())

        afilter.remove_condition('0')
        self.assertTrue(afilter.is_empty())

    # -------------------------------------------------------------------------
    def test_clear(self):
        """[u:lib.filter.Filter.clear]"""
        request = DummyRequest()
        afilter = self.make_one(request)
        afilter.clear()
        self.assertTrue(afilter.is_empty())
        self.assertIn('filters', request.session)
        self.assertIn('users', request.session['filters'])
        self.assertFalse(len(request.session['filters']['users']))

    # -------------------------------------------------------------------------
    def test_append_condition(self):
        """[u:lib.filter.Filter.append_condition]"""
        afilter = self.make_one(DummyRequest(params={
            'filter': True,
            'filter_key_login': 'login', 'filter_value_login': 'user1',
            'filter_key': 'group', 'filter_value': 'bar'}))
        afilter.remove_condition('0')
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition('1')
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition('0')
        self.assertTrue(afilter.is_empty())

        afilter = self.make_one(DummyRequest())
        afilter.remove_condition('0')
        afilter.append_condition('foo', '=', True)
        self.assertTrue(afilter.is_empty())

        afilter.append_condition('login', '=', '')
        self.assertTrue(afilter.is_empty())

        afilter.append_condition('login', '=', 'user1', 'OR')
        self.assertFalse(afilter.is_empty())

        afilter.append_condition('age', '>', 'foo')
        self.assertIn('<span>Age > 0</span>', afilter.html_conditions())
        afilter.append_condition('age', '<', '18', 'OR')
        self.assertIn('<span>Age < 18</span>', afilter.html_conditions())

    # -------------------------------------------------------------------------
    def test_remove_condition(self):
        """[u:lib.filter.Filter.remove_condition]"""
        afilter = self.make_one(DummyRequest(params={
            'filter': True,
            'filter_key': 'login', 'filter_value': 'user1'}))
        afilter.remove_condition('a')
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition(None)
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition('1')
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition('1')
        self.assertFalse(afilter.is_empty())
        afilter.remove_condition('0')
        self.assertTrue(afilter.is_empty())

    # -------------------------------------------------------------------------
    def test_html_conditions(self):
        """[u:lib.filter.Filter.html_conditions]"""
        afilter = self.make_one(DummyRequest())
        afilter.remove_condition('0')
        self.assertEqual(afilter.html_conditions(), '')

        afilter = self.make_one(DummyRequest())
        afilter.append_condition('login', '=', 'user1')
        afilter.append_condition('login', '=', 'user2', 'OR')
        afilter.append_condition('group', '=', 'foo')
        html = afilter.html_conditions()
        self.assertIn('name="crm!0.x"', html)
        self.assertIn('<span>Active</span>', html)
        self.assertIn('<strong>AND</strong>', html)
        self.assertIn('name="crm!1.x"', html)
        self.assertIn('<span>Login = user1</span>', html)
        self.assertIn('<strong>OR</strong>', html)
        self.assertIn('<span>Login = user2</span>', html)
        self.assertIn('name="crm!2.x"', html)
        self.assertIn('<span>Group = Foo</span>', html)
        self.assertNotIn('name="crm!3.x"', html)

    # -------------------------------------------------------------------------
    def test_html_inputs(self):
        """[u:lib.filter.Filter.html_inputs]"""
        from ..lib.form import Form
        from ..lib.filter import Filter

        request = DummyRequest()
        form = Form(request)
        afilter = Filter(
            request, 'users1', (
                ('login', 'Login', True, None),
                ('active', 'Active', False, True),
                ('group', 'Group', False, [
                    ('', ' '), ('foo', 'Foo'), ('bar', 'Bar')])))

        html = afilter.html_inputs(form)
        self.assertNotIn('id="filter_operator_login"', html)
        self.assertIn('id="filter_comparison_login"', html)
        self.assertIn('id="filter_value_login"', html)
        self.assertNotIn('id="filter_value_active', html)
        self.assertNotIn('id="filter_operator"', html)
        self.assertIn('id="filter_comparison"', html)
        self.assertIn('id="filter_value"', html)

        afilter = self.make_one(request)
        html = afilter.html_inputs(form)
        self.assertNotIn('id="filter_operator_login"', html)
        self.assertIn('id="filter_operator"', html)
        self.assertIn('id="filter_comparison"', html)
        self.assertIn('id="filter_value"', html)

        afilter = Filter(
            request, 'users2', (
                ('login', 'Login', True, None),
                ('name', 'Name', True, ''),
                ('active', 'Active', True, True),
                ('group', 'Group', True, [
                    ('', ' '), ('foo', 'Foo'), ('bar', 'Bar')])))
        html = afilter.html_inputs(form)
        self.assertIn('id="filter_value_login"', html)
        self.assertIn('id="filter_value_active"', html)
        self.assertNotIn('id="filter_value"', html)
        self.assertIn('class="cioAutocomplete"', html)

    # -------------------------------------------------------------------------
    def test_whoosh(self):
        """[u:lib.filter.Filter.whoosh]"""
        from ..lib.filter import Filter

        wfilter = self.make_one(DummyRequest())
        wfilter.append_condition('login', '=', 'user1')
        wfilter.append_condition('login', '=', 'user2', 'OR')

        # Complex query
        fieldnames, wquery = wfilter.whoosh()
        self.assertEqual(len(fieldnames), 2)
        self.assertIn('active', fieldnames)
        self.assertIn('login', fieldnames)
        self.assertEqual(
            wquery, '(active:TRUE) AND (login:(user1) OR login:(user2))')

        # Equal with space
        wfilter = Filter(
            DummyRequest(), 'users', (('name', 'Name', False, ''),),
            (('name', '=', 'John DOE'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(name:"John DOE")')

        # Different
        wfilter = Filter(
            DummyRequest(), 'users', (('login', 'Login', False, None),),
            (('login', '!=', 'user1'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(NOT login:(user1))')

        # Different with space
        wfilter = Filter(
            DummyRequest(), 'users', (('name', 'Name', False, ''),),
            (('name', '!=', 'John DOE'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(NOT name:"John DOE")')

        # Greater
        wfilter = Filter(
            DummyRequest(), 'users', (('login', 'Login', False, None),),
            (('login', '>', 'user1'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(login:{user1 TO})')

        # Greater or equal
        wfilter = Filter(
            DummyRequest(), 'users', (('login', 'Login', False, None),),
            (('login', '>=', 'user1'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(login:[user1 TO])')

        # Lower
        wfilter = Filter(
            DummyRequest(), 'users', (('login', 'Login', False, None),),
            (('login', '<', 'user1'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(login:{TO user1})')

        # Lower or equal
        wfilter = Filter(
            DummyRequest(), 'users', (('login', 'Login', False, None),),
            (('login', '<=', 'user1'),))
        wquery = wfilter.whoosh()[1]
        self.assertEqual(wquery, '(login:[TO user1])')


# =============================================================================
class ULibFilterFilterSql(DBUnitTestCase):
    """Unit test class for SQL method of :class:`lib.filter.Filter` class."""

    # -------------------------------------------------------------------------
    def test_sql(self):
        """[u:lib.filter.Filter.sql]"""
        from ..lib.filter import Filter
        from ..models.dbuser import DBUser

        dbsession = self.request.dbsession
        pfilter = Filter(
            self.request, 'users1',
            (('login', 'Login', False, None),
             ('active', 'Active', False, True)))
        dbquery = pfilter.sql(
            dbsession.query(DBUser.user_id, DBUser.login), 'users')
        self.assertIn('users.user_id AS users_user_id', str(dbquery.params()))

        pfilter = Filter(
            self.request, 'users2',
            (('login', 'Login', False, None),
             ('active', 'Active', False, True)),
            (('login', '=', 'user1'), ('login', '!=', 'user2', 'OR'),
             ('active', '=', True)))
        dbquery = pfilter.sql(
            dbsession.query(DBUser.user_id, DBUser.login), 'users')
        sql = str(dbquery.params())
        self.assertIn('users.login LIKE ? OR users.login NOT LIKE ?', sql)
        self.assertIn('users.active = ?', sql)

        pfilter = Filter(
            self.request, 'users3',
            (('login', 'Login', False, None),
             ('active', 'Active', False, True)),
            (('login', '=', 'user1'), ('active', '=', True, 'OR'),
             ('active', '=', True)))
        dbquery = pfilter.sql(
            dbsession.query(DBUser.user_id, DBUser.login),
            'users', ('active',))
        self.assertNotIn('users.active = ?', str(dbquery.params()))

    # -------------------------------------------------------------------------
    def test_sql_autocomplete(self):
        """[u:lib.filter.Filter.autocomplete]"""
        from ..lib.filter import Filter
        from ..models.dbprofile import DBProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='profile_manager',
            i18n_label=dumps({'en': 'Profile manager'}),
            i18n_description={'en': 'Permission to create profiles'}))
        dbsession.add(DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User manager'}),
            i18n_description={'en': 'Permission to create users'}))
        dbsession.add(DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'})))

        # Not an AJAX call
        self.request.is_xhr = False
        self.assertRaises(
            HTTPForbidden, Filter.sql_autocomplete, self.request, DBProfile)

        # Unknown field
        self.request.is_xhr = True
        self.request.params = {'field': 'foo'}
        self.assertRaises(
            HTTPForbidden, Filter.sql_autocomplete, self.request, DBProfile)

        # Field i18n_label
        self.request.params = {'field': 'i18n_label', 'value': 'profile'}
        data = Filter.sql_autocomplete(self.request, DBProfile)
        self.assertIsInstance(data, list)
        self.assertIn('Profile manager', data)

        # Field profile_id with WHERE clause
        data = Filter.sql_autocomplete(
            self.request, DBProfile, where={'profile_id': 'profile_manager'},
            width=7)
        self.assertIn('Profile', data)
        self.request.params = {'field': 'i18n_label', 'value': 'user'}
        data = Filter.sql_autocomplete(
            self.request, DBProfile, where={'profile_id': 'profile_manager'})
        self.assertFalse(data)
