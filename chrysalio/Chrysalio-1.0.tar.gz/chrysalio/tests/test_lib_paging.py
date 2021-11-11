# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.paging`` function and classes."""

from re import match
from collections import namedtuple

from webhelpers2.html import literal

# pylint: disable = unused-import
from ..models.dbgroup import DBGroupUser  # noqa
# pylint: enable = unused-import
from . import DBUnitTestCase


# =============================================================================
class ULibPagingSortableColumn(DBUnitTestCase):
    """Unit test class for :func:`lib.paging.sortable_column`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.paging.sortable_column]"""
        from ..lib.paging import sortable_column

        self.configurator.add_route('user_index', '/usr/index')
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')
        self.request.GET = {'quick': 1}

        html = sortable_column(
            self.request, 'Foo Column', 'login', current_sorting='+login')
        self.assertIsInstance(html, literal)
        self.assertIn('Foo Column', html)
        self.assertIn('quick=1', html)
        self.assertIn('sort=-login', html)
        self.assertNotIn('sort=+login', html)


# =============================================================================
class ULibPagingPaging(DBUnitTestCase):
    """Unit test class for :class:`lib.paging.Paging`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        super(ULibPagingPaging, self).setUp()
        self.configurator.add_route('user_index', '/usr/index')
        self.request.matched_route = namedtuple('Route', 'name')(
            name='user_index')

        self.add_user({
            'login': 'test1', 'last_name': 'AVULEUR', 'first_name': 'Édith',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        self.add_user({
            'login': 'test2', 'first_name': 'Sophie', 'last_name': 'FONFEC',
            'status': 'inactive', 'password': 'test2pwd',
            'email': 'test2@chrysal.io'})
        self.add_user({
            'login': 'test3', 'first_name': 'Guy', 'last_name': 'LIGUILI',
            'status': 'locked',
            'password': 'test3pwd', 'email': 'test3@chrysal.io'})

    # -------------------------------------------------------------------------
    def test_init(self):
        """[u:lib.paging.Paging.__init__]"""
        from ..models.dbuser import DBUser
        from ..lib.paging import PAGE_DEFAULT_SIZE, Paging

        self.assertRaises(TypeError, Paging, None, 'users', 12, item_count=1)

        paging = Paging(None, 'users1', ('user1', 'user2'))
        self.assertEqual(paging.paging_id, 'users1')
        self.assertEqual(paging.page_size, PAGE_DEFAULT_SIZE)
        self.assertEqual(paging.item_count, 2)
        self.assertEqual(paging.page_count, 1)

        # pylint: disable = no-member
        query = self.request.dbsession.query(DBUser.user_id, DBUser.login)
        # pylint: enable = no-member
        paging = Paging(None, 'users2', query)
        self.assertEqual(paging.paging_id, 'users2')
        self.assertEqual(paging.item_count, 3)
        self.assertEqual(paging.page_count, 1)

        self.request.params = {
            'page_size': '2', 'sort': 'login', 'display': 'cards', 'page': '3'}
        paging = Paging(self.request, 'users3', query)
        self.assertEqual(paging.page_size, 2)
        self.assertEqual(paging.page, 2)

        self.request.params = {'page_size': '0'}
        paging = Paging(self.request, 'users4', query)
        self.assertEqual(paging.page_size, 0)
        self.assertEqual(paging.page, 1)
        self.assertEqual(paging.item_count, 3)
        self.assertEqual(paging.page_count, 1)

    # -------------------------------------------------------------------------
    def test_params(self):
        """[u:lib.paging.Paging.params]"""
        from ..lib.paging import PAGE_DEFAULT_SIZE, Paging

        params = Paging.params(None, 'users', '+login')
        self.assertEqual(len(params), 4)
        self.assertIn('page_size', params)
        self.assertEqual(params['page_size'], PAGE_DEFAULT_SIZE)

        self.request.registry['settings']['page-size'] = 40
        params = Paging.params(self.request, 'users', '+login')
        self.assertIn('page_size', params)
        self.assertEqual(params['page_size'], 40)

        self.request.POST = {'page_size': '160'}
        self.request.params = self.request.POST
        params = Paging.params(self.request, 'users', '+login')
        self.assertIn('sort', params)
        self.assertEqual(params['sort'], '+login')
        self.assertIn('page_size', params)
        self.assertEqual(params['page_size'], 160)
        self.assertIn('display', params)
        self.assertEqual(params['display'], 'cards')
        self.assertIn('paging', self.request.session)
        self.assertEqual(self.request.session['paging'][0], 40)
        self.assertIn('users', self.request.session['paging'][1])
        paging = self.request.session['paging'][1]['users']
        self.assertEqual(paging['page'], 1)
        self.assertEqual(paging['sort'], '+login')

        self.request.POST = {'sort': '-login'}
        self.request.params = self.request.POST
        params = Paging.params(self.request, 'users', '+login')
        self.assertEqual(params['sort'], '-login')
        paging = self.request.session['paging'][1]['users']
        self.assertEqual(paging['sort'], '-login')

    # -------------------------------------------------------------------------
    def test_get_sort(self):
        """[u:lib.paging.Paging.get_sort]"""
        from ..lib.paging import Paging

        self.assertIsNone(Paging.get_sort(self.request, 'users'))

        Paging.params(self.request, 'users', '+login')
        self.assertEqual(Paging.get_sort(self.request, 'users'), '+login')

    # -------------------------------------------------------------------------
    def test_get_page(self):
        """[u:lib.paging.Paging.get_page]"""
        from ..lib.paging import Paging

        self.assertEqual(Paging.get_page(self.request, 'users'), 1)

        params = Paging.params(self.request, 'numbers')
        params['page'] = 2
        paging = Paging(self.request, 'numbers', range(100), params)
        self.assertEqual(paging.get_page(self.request, 'numbers'), 2)

    # -------------------------------------------------------------------------
    def test_get_item(self):
        """[u:lib.paging.Paging.get_item]"""
        from ..lib.paging import Paging

        paging = Paging(None, 'users1', ('user1', 'user2'))
        self.assertIsNone(paging.get_item('file_id', 'user1'))

        paging = Paging(None, 'files', (
            {'file_id': 'qsRz', 'name': 'foo'},
            {'file_id': 'sqdh', 'name': 'bar'},
            {'file_id': 'qsRz', 'name': 'baz'}))
        pitem = paging.get_item('file_id', 'qsRz')
        self.assertIsNotNone(pitem)
        self.assertIsInstance(pitem, dict)
        self.assertIn('name', pitem)
        self.assertEqual(pitem['name'], 'foo')

    # -------------------------------------------------------------------------
    def test_set_current_ids(self):
        """[u:lib.paging.Paging.set_current_ids]"""
        from ..models.dbuser import DBUser
        from ..lib.paging import Paging

        # pylint: disable = no-member
        query = self.request.dbsession.query(DBUser.user_id, DBUser.login)
        # pylint: enable = no-member

        # Without request
        paging = Paging(None, 'users', query)
        paging.set_current_ids('user_id')
        self.assertNotIn('paging', self.request.session)

        # With a SQLAlchemy query
        paging = Paging(self.request, 'users', query)
        paging.set_current_ids('user_id')
        self.assertIn('paging', self.request.session)
        self.assertIn('users', self.request.session['paging'][1])
        self.assertIn(
            'current_ids', self.request.session['paging'][1]['users'])
        self.assertEqual(
            len(self.request.session['paging'][1]['users']['current_ids']), 3)

        # With an empty collection
        paging = Paging(self.request, 'files', [])
        paging.set_current_ids('file_id')
        self.assertEqual(
            len(self.request.session['paging'][1]['files']['current_ids']), 0)

    # -------------------------------------------------------------------------
    def test_pager(self):
        """[u:lib.paging.Paging.pager]"""
        from ..models.dbuser import DBUser
        from ..lib.paging import Paging

        # pylint: disable = no-member
        dbquery = self.request.dbsession.query(DBUser.user_id, DBUser.login)
        # pylint: enable = no-member

        html = Paging(None, 'users', dbquery).pager()
        self.assertEqual(html, '')

        html = Paging(self.request, 'users', dbquery).pager()
        self.assertIn('<span>1</span>', html)

        html = Paging(
            self.request, 'users', dbquery,
            params={'page_size': 2, 'page': 1, 'display': 'cards'}).pager()
        self.assertIn('<span>1</span>', html)
        self.assertIn('page=2', html)

    # -------------------------------------------------------------------------
    def test_pager_top(self):
        """[u:lib.paging.Paging.pager_top]"""
        from ..models.dbuser import DBUser
        from ..lib.paging import Paging

        # pylint: disable = no-member
        dbquery = self.request.dbsession.query(
            DBUser.user_id, DBUser.login, DBUser.last_name)
        # pylint: enable = no-member

        html = Paging(None, 'users', dbquery).pager_top()
        self.assertEqual(html, '&nbsp;')

        html = Paging(self.request, 'users', dbquery).pager_top()
        self.assertIn('first_off', html)
        self.assertIn('previous_off', html)
        self.assertIn('next_off', html)
        self.assertIn('last_off', html)

        params = {'page_size': 2, 'page': 1, 'sort': None, 'display': 'cards'}
        html = Paging(self.request, 'users', dbquery, params).pager_top()
        self.assertIn('page=2', html)
        self.assertIn('src="/images/paging_go_next.png"', html)
        self.assertIn('src="/images/paging_go_last.png"', html)

    # -------------------------------------------------------------------------
    def test_pager_bottom(self):
        """[u:lib.paging.Paging.pager_bottom]"""
        from ..models.dbuser import DBUser
        from ..lib.paging import Paging

        # pylint: disable = no-member
        dbquery = self.request.dbsession.query(
            DBUser.user_id, DBUser.login, DBUser.last_name)
        # pylint: enable = no-member

        html = Paging(self.request, 'users', dbquery).pager_bottom()
        self.assertIn('<span>1</span>', html)

        params = {'page_size': 2, 'page': 1, 'sort': None, 'display': 'cards'}
        html = Paging(self.request, 'users', dbquery, params).pager_bottom()
        self.assertIn('page=2', html)

    # -------------------------------------------------------------------------
    def test_display_modes(self):
        """[u:lib.paging.Paging.display_mode]"""
        from ..lib.paging import Paging

        html = Paging(None, 'users', ['user1']).display_modes()
        self.assertEqual(html, '')

        self.request.GET = {'quick': 1}
        paging = Paging(self.request, 'users', ['user1'])
        html = paging.display_modes()
        self.assertNotIn('display=cards', html)
        self.assertIn('display=list', html)
        self.assertIn('quick=1', html)

        paging.display = 'list'
        html = paging.display_modes()
        self.assertIn('display=cards', html)
        self.assertNotIn('display=list', html)

    # -------------------------------------------------------------------------
    def test_sortable_column(self):
        """[u:lib.paging.Paging.sortable_column]"""
        from ..lib.paging import Paging

        html = Paging(None, 'users', ['user1']).sortable_column(
            'Foo Column', 'login')
        self.assertEqual(html, '&nbsp;')

        html = Paging(self.request, 'users', ['user1']).sortable_column(
            'Foo Column', 'login')
        self.assertIn('Foo Column', html)
        self.assertIn('sort=%2Blogin', html)
        self.assertNotIn('sort=-login', html)

    # -------------------------------------------------------------------------
    def test_navigator(self):
        """[u:lib.paging.Paging.navigator]"""
        from ..lib.paging import Paging

        # With an empty session
        html = Paging.navigator(
            self.request, 'profiles', 'main_manager', '/profile/view/_ID_')
        self.assertFalse(html)

        # With an item which is not in current IDs
        self.request.session['paging'] = (
            80, {'profiles': {'current_ids': [
                'main_manager', 'user_creator', 'user_editor']}})
        html = Paging.navigator(
            self.request, 'profiles', 'foo', '/profile/view/_ID_')
        self.assertFalse(html)

        # With the first item
        html = Paging.navigator(
            self.request, 'profiles', 'main_manager', '/profile/view/_ID_')
        self.assertIn('<span>1</span>', html)
        self.assertIn('user_creator', html)

        # With the last item
        html = Paging.navigator(
            self.request, 'profiles', 'user_editor', '/profile/view/_ID_')
        self.assertIn('<span>3</span>', html)
        self.assertIn('user_creator', html)

    # -------------------------------------------------------------------------
    def test_range(self):
        """[u:lib.paging.Paging._range]"""
        from ..lib.paging import Paging

        collection = [
            'user01', 'user02', 'user03', 'user04', 'user05', 'user06',
            'user07', 'user08', 'user09', 'user10', 'user11', 'user12']
        params = {'page_size': 2, 'page': 5, 'sort': None, 'display': 'cards'}
        paging = Paging(self.request, 'users', collection, params)

        # pylint: disable = protected-access
        html = paging._range(match(r'~(\d+)~', '~2~'))
        self.assertIn('page=1', html)
        self.assertIn('<span>5</span>', html)

        paging.page = 2
        html = paging._range(match(r'~(\d+)~', '~2~'))
        self.assertIn('<span>2</span>', html)
