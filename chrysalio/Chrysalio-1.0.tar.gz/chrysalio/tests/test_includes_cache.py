# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``includes.cache`` classes and functions."""

from time import sleep, time
from unittest import TestCase

from pyramid.testing import DummyRequest

from . import ConfiguratorTestCase


# =============================================================================
class UIncludesCacheIncludeme(ConfiguratorTestCase):
    """Unit test class for :class:`includes.cache.includeme`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.cache.includeme]"""
        self.configurator.include('..includes.cache')
        self.assertIn('cache_user', self.configurator.registry)
        self.assertIn('cache_global', self.configurator.registry)


# =============================================================================
class UIncludesCacheCacheUser(TestCase):
    """Unit test class for :class:`includes.cache.CacheUser`."""

    # -------------------------------------------------------------------------
    def test_set(self):
        """[u:includes.cache.CacheUser.set]"""
        from ..includes.cache import CACHE_DEFAULT_TTL, CacheUser

        cache_user = CacheUser({
            'beaker.cache.expire': '43200',
            'beaker.cache.regions': 'default, short, long',
            'beaker.cache.short.expire': '1',
            'beaker.cache.long.expire': '1800'})
        request = DummyRequest()

        # Without namespace and region
        cache_user.set(request, 'foo', {'one': 1, 'two': 2})
        value = cache_user.get(request, 'foo')
        self.assertIsInstance(value, dict)
        self.assertIn('one', value)
        self.assertIsNone(cache_user.get(request, 'bar'))

        # With namespace and without region
        cache_user.set(request, 'baz', {'one': 1, 'two': 2}, 'namespace1')
        value = cache_user.get(request, 'baz', 'namespace1')
        self.assertIsInstance(value, dict)
        self.assertIn('two', value)
        self.assertIsNone(cache_user.get(request, 'baz'))
        self.assertIsNone(cache_user.get(request, 'baz', 'namespace2'))
        self.assertIsNone(cache_user.get(request, 'foo', 'namespace1'))

        # With namespace and unknown region
        cache_user.set(request, 'foo2', 2, 'namespace2', 'very_short')
        self.assertEqual(cache_user.get(request, 'foo2', 'namespace2'), 2)

        # With namespace and region
        cache_user.set(request, 'foo3', 3, 'namespace3', 'short')
        self.assertEqual(cache_user.get(request, 'foo3', 'namespace3'), 3)
        sleep(1.1)
        self.assertIsNone(cache_user.get(request, 'foo3', 'namespace3'))

        # With short expiration
        cache_user.set(request, 'foo', 'première', 'namespace4', expire=.1)
        self.assertEqual(
            cache_user.get(request, 'foo', 'namespace4'), 'première')
        sleep(.2)
        self.assertIsNone(cache_user.get(request, 'foo', 'namespace4'))

        # Replace cache
        cache_user.set(request, 'foo', 'three')
        self.assertEqual(cache_user.get(request, 'foo'), 'three')

        # Default region
        cache_user.set(request, 'foo', 'five', 'namespace5', 'default')
        self.assertIn('default', cache_user.regions)
        self.assertEqual(cache_user.regions['default'], CACHE_DEFAULT_TTL)

    # -------------------------------------------------------------------------
    def test_clear(self):
        """[u:includes.cache.CacheUser.clear]"""
        from ..includes.cache import CacheUser

        cache_user = CacheUser({
            'cache.expire': '43200',
            'cache.regions': 'long',
            'cache.long.expire': '1800'})
        request = DummyRequest()

        # Clear a key
        cache_user.set(request, 'pi', 3.14)
        cache_user.set(request, 'e', 2.71828)
        self.assertEqual(cache_user.get(request, 'pi'), 3.14)
        self.assertEqual(cache_user.get(request, 'e'), 2.71828)
        cache_user.clear(request, key='pi')
        self.assertIsNone(cache_user.get(request, 'pi'))
        self.assertEqual(cache_user.get(request, 'e'), 2.71828)

        # Clear an unknown key
        cache_user.clear(request, key='foo')
        self.assertEqual(cache_user.get(request, 'e'), 2.71828)

        # Clear a region
        cache_user.clear(request)
        self.assertIsNone(cache_user.get(request, 'e'))
        cache_user.clear(request)

    # -------------------------------------------------------------------------
    def test_purge(self):
        """[u:includes.cache.CacheUser.purge]"""
        from ..includes.cache import CacheUser

        cache_user = CacheUser({})
        request = DummyRequest()
        cache_user.set(request, 'foo', 'bar', expire=.1)
        sleep(.2)
        cache_user.purge(request)
        self.assertIsNone(cache_user.get(request, 'foo'))


# =============================================================================
class UIncludesCacheCacheUserAccess(TestCase):
    """Unit test class for :class:`includes.cache.cache_user_access`."""

    # -------------------------------------------------------------------------
    def test_without_uid(self):
        """[u:includes.cache.cache_user_access] without uid"""
        from ..includes.cache import cache_user_access

        # pylint: disable = too-few-public-methods
        class Item(object):
            """Class for items."""

        class ItemManager(object):
            """Class to manage items."""

            @cache_user_access('ns0')
            @classmethod
            def item_access(cls, request, item):
                """Method for testing."""
                # pylint: disable = unused-argument
                return ('writer',)

        item_manager = ItemManager()
        request = DummyRequest()
        item = Item()
        self.assertRaises(Exception, item_manager.item_access, request, item)

    # -------------------------------------------------------------------------
    def test_cache(self):
        """[u:includes.cache.cache_user_access] cache"""
        from ..includes.cache import CacheUser, cache_user_access

        # pylint: disable = too-few-public-methods
        class Item(object):
            """Class for items."""
            uid = 'itme01'

        class ItemManager(object):
            """Class to manage items."""

            @cache_user_access('ns0')
            @classmethod
            def item_access(cls, request, item):
                """Method for testing."""
                # pylint: disable = unused-argument
                return ('writer' if item is not None else None,)

        item_manager = ItemManager()
        request = DummyRequest()
        request.registry['cache_user'] = CacheUser({})
        item = Item()

        # With None
        result = item_manager.item_access(request, None)
        self.assertEqual(result, (None,))

        # First time, from method
        result = item_manager.item_access(request, item)
        self.assertEqual(result, ('writer',))

        # Second time, from cache
        result = item_manager.item_access(request, item)
        self.assertEqual(result, ('writer',))


# =============================================================================
class UIncludesCacheCacheGlobal(TestCase):
    """Unit test class for :class:`includes.cache.CacheGlobal`."""

    # -------------------------------------------------------------------------
    def test_get(self):
        """[u:includes.cache.CacheGlobal.(set|get)]"""
        from ..includes.cache import CACHE_DEFAULT_TTL, CacheGlobal

        cache_global = CacheGlobal({
            'beaker.cache.type': 'memory',
            'beaker.cache.regions': 'default, short, long',
            'beaker.cache.short.expire': '1',
            'beaker.cache.long.expire': '1800'})

        # Without namespace and region
        cache_global.set('foo', {'one': 1, 'two': 2})
        value = cache_global.get('foo')
        self.assertIsInstance(value, dict)
        self.assertIn('one', value)
        self.assertIsNone(cache_global.get('bar'))

        # With namespace and without region
        cache_global.set('baz', {'one': 1, 'two': 2}, 'namespace1')
        value = cache_global.get('baz', 'namespace1')
        self.assertIsInstance(value, dict)
        self.assertIn('two', value)
        self.assertIsNone(cache_global.get('baz'))
        self.assertIsNone(cache_global.get('baz', 'namespace2'))
        self.assertIsNone(cache_global.get('foo', 'namespace1'))

        # With namespace and unknown region
        cache_global.set('foo2', 2, 'namespace2', 'very_short')
        self.assertEqual(cache_global.get('foo2', 'namespace2'), 2)

        # With namespace and region
        cache_global.set('foo3', 3, 'namespace3', 'short')
        self.assertEqual(cache_global.get('foo3', 'namespace3'), 3)
        sleep(1.1)
        self.assertIsNone(cache_global.get('foo3', 'namespace3'))

        # With short expiration
        cache_global.set('foo', 'première', 'namespace4', expire=1)
        self.assertEqual(cache_global.get('foo', 'namespace4'), 'première')
        sleep(1.1)
        self.assertIsNone(cache_global.get('foo', 'namespace4'))

        # Replace cache
        cache_global.set('foo', 'three')
        self.assertEqual(cache_global.get('foo'), 'three')

        # Default region without global expiration
        cache_global.set('foo', 'five', 'namespace5', 'default')
        self.assertIn('default', cache_global.regions)
        self.assertIn('expire', cache_global.regions['default'])
        self.assertEqual(
            cache_global.regions['default']['expire'], CACHE_DEFAULT_TTL)

        # Default region with global expiration
        cache_global = CacheGlobal({
            'beaker.cache.type': 'memory',
            'beaker.cache.expire': '43200',
            'beaker.cache.regions': 'default'})
        cache_global.set('foo', 'six', 'namespace6', 'default')
        self.assertIn('default', cache_global.regions)
        self.assertIn('expire', cache_global.regions['default'])
        self.assertEqual(cache_global.regions['default']['expire'], 43200)

    # -------------------------------------------------------------------------
    def test_clear(self):
        """[u:includes.cache.CacheGlobal.clear]"""
        from ..includes.cache import CacheGlobal

        cache_global = CacheGlobal({
            'cache.expire': '43200',
            'cache.regions': 'long',
            'cache.long.expire': '1800'})

        # Clear a key
        cache_global.set('pi', 3.14)
        cache_global.set('e', 2.71828)
        self.assertEqual(cache_global.get('pi'), 3.14)
        self.assertEqual(cache_global.get('e'), 2.71828)
        cache_global.clear(key='pi')
        self.assertIsNone(cache_global.get('pi'))
        self.assertEqual(cache_global.get('e'), 2.71828)

        # Clear an unknown key
        cache_global.clear(key='foo')
        cache_global.clear(key='e', namespace='bar')
        self.assertEqual(cache_global.get('e'), 2.71828)

        # Clear a region
        cache_global.clear()
        self.assertIsNone(cache_global.get('e'))
        cache_global.clear()

    # -------------------------------------------------------------------------
    def test_initialize(self):
        """[u:includes.cache.CacheGlobal.initialize]"""
        from ..includes.cache import CREATED_KEY, CacheGlobal

        cache_global = CacheGlobal({
            'cache.expire': '43200',
            'cache.regions': 'long',
            'cache.long.expire': '1800'})
        cache_global.set('pi', 3.14)
        self.assertEqual(cache_global.get('pi'), 3.14)
        self.assertIsNone(cache_global.get(CREATED_KEY))
        now = time()

        cache_global.initialize()
        self.assertIsNone(cache_global.get('e'))
        created = cache_global.get(CREATED_KEY)
        self.assertIsInstance(created, float)
        self.assertGreater(created, now)
        cache_global.clear()


# =============================================================================
class UIncludesCacheCacheGlobalItem(TestCase):
    """Unit test class for :class:`includes.cache.cache_global_item`."""

    # -------------------------------------------------------------------------
    def test_without_uid(self):
        """[u:includes.cache.cache_global_item] without _items"""
        from ..includes.cache import cache_global_item

        class ItemManager(object):
            """Class to manage items."""

            @cache_global_item('ns0')
            @classmethod
            def item(cls, request, item_id):
                """Method for testing."""
                # pylint: disable = unused-argument
                return None

        item_manager = ItemManager()
        request = DummyRequest()
        self.assertRaises(Exception, item_manager.item, request, 'item01')

    # -------------------------------------------------------------------------
    def test_cache(self):
        """[u:includes.cache.cache_global_item] cache"""
        from ..includes.cache import CacheUser, CacheGlobal, cache_global_item

        item_ok = False

        # pylint: disable = too-few-public-methods
        class Item(object):
            """Class for items."""
            uid = 'itme01'
            created = time()

        class ItemManager(object):
            """Class to manage items."""
            _item1s = {}
            _item2s = {}

            @classmethod
            def item_access(cls, request, item):
                """Method for testing."""
                # pylint: disable = unused-argument
                return ('writer',)

            @cache_global_item('ns0')
            @classmethod
            def item1(cls, request, item_id):
                """Method for testing."""
                # pylint: disable = unused-argument
                return Item() if item_ok else None

            @cache_global_item('ns0', access_function=item_access)
            @classmethod
            def item2(cls, request, item_id):
                """Method for testing."""
                # pylint: disable = unused-argument
                return Item() if item_ok else None

        item_manager = ItemManager()
        request = DummyRequest()
        request.registry['cache_user'] = CacheUser({})
        request.registry['cache_global'] = CacheGlobal({})

        # With a bad item
        item = item_manager.item1(request, 'item01')
        self.assertIsNone(item)

        # With a good item, without access rights
        item_ok = True
        item = item_manager.item1(request, 'item01')
        self.assertIsInstance(item, Item)

        # With access rights
        item = item_manager.item2(request, 'item02')
        self.assertIsInstance(item, Item)

        # Second time, from cache
        item = item_manager.item2(request, 'item02')
        self.assertIsInstance(item, Item)


# =============================================================================
class UIncludesCacheCacheGlobalValue(TestCase):
    """Unit test class for :class:`includes.cache.cache_global_value`."""

    # -------------------------------------------------------------------------
    def test_without_uid(self):
        """[u:includes.cache.cache_global_value] without uid"""
        from ..includes.cache import cache_global_value

        class Item(object):
            """Class for items."""

            @cache_global_value('field1', 'ns0')
            @classmethod
            def get_field1(cls, request):
                """Method for testing."""
                # pylint: disable = unused-argument
                return .6

        item = Item()
        request = DummyRequest()
        self.assertRaises(Exception, item.get_field1, request)

    # -------------------------------------------------------------------------
    def test_cache(self):
        """[u:includes.cache.cache_global_value] cache"""
        from ..includes.cache import cache_global_value

        class Item(object):
            """Class for items."""
            uid = 'itme01'

            @cache_global_value('field1', 'ns0')
            @classmethod
            def get_field1(cls, request):
                """Method for testing."""
                # pylint: disable = unused-argument
                return .6

        item = Item()
        request = DummyRequest()

        # First time, from method
        result = item.get_field1(request)
        self.assertEqual(result, .6)

        # Second time, from cache
        result = item.get_field1(request)
        self.assertEqual(result, .6)


# =============================================================================
class UIncludesCacheCacheNamespace(TestCase):
    """Unit test class for :func:`includes.cache.cache_namespace`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:includes.cache.cache_namespace]"""
        from ..includes.cache import cache_namespace
        self.assertEqual(cache_namespace('ns0', 'foo'), 'ns0-foo')
