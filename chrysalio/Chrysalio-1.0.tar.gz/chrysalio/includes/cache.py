"""Cache functionality."""

from time import time

from beaker.cache import CacheManager, cache_regions
from beaker.util import parse_cache_config_options

from pyramid.config import Configurator


CACHE_DEFAULT_TTL = 43200
CREATED_KEY = '__created__'


# =============================================================================
def includeme(configurator):
    """Function to include cache functionnality based on registry for global
    cache and session for user cache.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    if isinstance(configurator, Configurator):
        if 'cache_user' not in configurator.registry:
            configurator.registry['cache_user'] = CacheUser(
                configurator.get_settings())
        if 'cache_global' not in configurator.registry:
            configurator.registry['cache_global'] = CacheGlobal(
                configurator.get_settings())


# =============================================================================
class CacheUser(object):
    """Class to manage a private cache for a user based on session."""

    # -------------------------------------------------------------------------
    def __init__(self, settings):
        """Constructor method."""
        prefix = ''
        regions = settings.get('cache.regions')
        if not regions:
            prefix = 'beaker.'
            regions = settings.get('beaker.cache.regions', '')
        self.regions = {}
        for region in regions.split(','):
            region = region.strip()
            expire = settings.get(
                '{0}cache.{1}.expire'.format(prefix, region))
            self.regions[region] = int(expire) if expire and expire.isdigit() \
                else CACHE_DEFAULT_TTL

    # -------------------------------------------------------------------------
    def set(self, request, key, value, namespace='', region=None, expire=None):
        """Set value into the cache.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str key:
            Key of value to retrieve.
        :param value:
            The value associated with the key or ``None``.
        :param str namespace: (default='')
            Cache namespace.
        :param str region: (optional)
            Beaker cache region.
        :param int expire: (optional)
            Special expiration.
        """
        # pylint: disable = too-many-arguments
        if 'cache' not in request.session:
            request.session['cache'] = {}
        cache = request.session['cache']
        if namespace not in cache:
            cache[namespace] = {}

        if not expire:
            expire = self.regions.get(region, CACHE_DEFAULT_TTL)
        cache[namespace][key] = (value, time() + expire)

    # -------------------------------------------------------------------------
    def get(self, request, key, namespace=''):
        """Get value from the cache.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str key:
            Key of value to retrieve.
        :param str namespace: (default='')
            Cache namespace.
        :return:
            The value associated with the key or ``None``.
        """
        if 'cache' not in request.session or \
           namespace not in request.session['cache'] or \
           key not in request.session['cache'][namespace]:
            return None

        if request.session['cache'][namespace][key][1] < time():
            del request.session['cache'][namespace][key]
            self.purge(request, namespace)
            return None

        return request.session['cache'][namespace][key][0]

    # -------------------------------------------------------------------------
    def clear(self, request, key=None, namespace=''):
        """Clear a key/value or the entire namespace ``namespace``.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str key: (optional)
            Key of value to remove.
        :param str namespace: (default='')
            Cache namespace.
        """
        if 'cache' not in request.session or \
           namespace not in request.session['cache']:
            return

        if key is not None:
            if key in request.session['cache'][namespace]:
                del request.session['cache'][namespace][key]
            self.purge(request, namespace)
            return

        del request.session['cache'][namespace]
        self.purge(request)

    # -------------------------------------------------------------------------
    @classmethod
    def purge(cls, request, namespace=None):
        """Purge expired entries.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str namespace: (optional)
            Cache namespace.
        """
        now = time()
        namespaces = (namespace,) if namespace is not None \
            else tuple(request.session['cache'])
        for nspace in namespaces:
            for key in tuple(request.session['cache'][nspace]):
                if request.session['cache'][nspace][key][1] < now:
                    del request.session['cache'][nspace][key]
            if not request.session['cache'][nspace]:
                del request.session['cache'][nspace]
        if not request.session['cache']:
            del request.session['cache']


# =============================================================================
def cache_user_access(namespace_prefix, region=None):
    """A decorator to retrieve in the user cache the result of an access
    method whose the two first arguments are ``request`` and ``item``.
    ``item`` must have a ``uid`` attribute.

    :param str namespace_prefix:
        Prefix of the cache namespace.
    :param str region: (optional)
        Name of region.
    """
    def _decorated(method):
        """Decoration of the method `method`."""

        def _wrapper(class_, request, item, *args, **kwargs):
            """Use of user cache."""
            access_method = method.__func__ \
                if isinstance(method, classmethod) else method
            if item is None:
                return access_method(class_, request, item, *args, **kwargs)
            if not hasattr(item, 'uid'):
                raise Exception('Class must have a "uid" attribute!')

            namespace = cache_namespace(namespace_prefix, item.uid)
            access = request.registry['cache_user'].get(
                request, 'access', namespace)
            if access is not None:
                return access

            access = access_method(class_, request, item, *args, **kwargs)
            request.registry['cache_user'].set(
                request, 'access', access, namespace, region)
            return access

        return _wrapper

    return _decorated


# =============================================================================
class CacheGlobal(object):
    """Class to manage a global cache based on Beaker cache.

    :param dict settings:
         Pyramid settings.
    """

    # -------------------------------------------------------------------------
    def __init__(self, settings):
        """Constructor method."""
        self._cache_manager = CacheManager(
            **parse_cache_config_options(settings))
        self.regions = cache_regions
        self._caches = {}

    # -------------------------------------------------------------------------
    def set(self, key, value, namespace='', region=None, **kwargs):
        """Set value into the cache.

        :param str key:
            Key of value to retrieve.
        :param value:
            The value associated with the key or ``None``.
        :param str namespace: (default='')
            Cache namespace.
        :param str region: (optional)
            Beaker cache region.
        :param dict kwargs:
            Keyworded arguments.
        """
        cache = self._get_cache(namespace, region, **kwargs)
        if cache is not None:
            cache.put(key, value)

    # -------------------------------------------------------------------------
    def get(self, key, namespace='', region=None, **kwargs):
        """Get value from the cache.

        :param str key:
            Key of value to retrieve.
        :param str namespace: (default='')
            Cache namespace.
        :param str region: (optional)
            Beaker cache region.
        :param dict kwargs:
            Keyworded arguments.
        :return:
            The value associated with the key or ``None``.
        """
        cache = self._get_cache(namespace, region, **kwargs)
        try:
            return cache.get(key)
        except KeyError:
            return None

    # -------------------------------------------------------------------------
    def clear(self, key=None, namespace='', region=None):
        """Clear a key/value or the entire namespace ``namespace``.

        :param str key: (optional)
            Key of value to remove.
        :param str namespace: (default='')
            Cache namespace.
        :param str region: (optional)
            Beaker cache region.
        """
        cache = self._get_cache(namespace, region)
        if key is not None:
            cache.remove_value(key=key)
        else:
            cache.clear()
            del self._caches[namespace]

    # -------------------------------------------------------------------------
    def initialize(self, namespace='', region=None):
        """Clear a key/value or the entire namespace ``namespace`` and set
        the time of creation.

        :param str namespace: (default='')
            Cache namespace.
        :param str region: (optional)
            Beaker cache region.
        """
        cache = self._get_cache(namespace, region)
        cache.clear()
        cache.put(CREATED_KEY, time())

    # -------------------------------------------------------------------------
    def _get_cache(self, namespace, region, **kwargs):
        """Return a Cache object.

        :param str namespace:
            Cache namespace.
        :param str region:
            Name of region.
        :param dict kwargs:
            Keyworded arguments.
        :rtype: beaker.cache.Cache
        """
        if namespace in self._caches:
            return self._caches[namespace]

        if region is None or region not in self.regions:
            if 'expire' not in kwargs:
                kwargs['expire'] = CACHE_DEFAULT_TTL
            self._caches[namespace] = self._cache_manager.get_cache(
                namespace, **kwargs)
        else:
            if not self.regions[region]['expire']:
                self.regions[region]['expire'] = CACHE_DEFAULT_TTL
            region_kwargs = dict(self.regions[region])
            region_kwargs.update(kwargs)
            self._caches[namespace] = self._cache_manager.get_cache(
                namespace, **region_kwargs)

        return self._caches[namespace]


# =============================================================================
def cache_global_item(namespace_prefix, region=None, access_function=None):
    """A decorator to retrieve in the global cache the result of a creation
    method whose the two first arguments are ``request`` and ``item_id``.
    The calling class must have a ``_<item>s`` attribute where `<item>` is the
    class name in lower case. If ``access_function`` is not ``None``, the
    access rights are checked.

    :param str namespace_prefix:
        Prefix of the cache namespace.
    :param tuple region: (optional)
        Name of region.
    :param access_function: (optional)
        A function to retrieve the access tuple.
    """
    def _decorated(method):
        """Decoration of the method `method`."""

        def _wrapper(class_, request, item_id, *args, **kwargs):
            """Use of global cache."""
            create_method = method.__func__ \
                if isinstance(method, classmethod) else method
            if not hasattr(class_, '_{0}s'.format(create_method.__name__)):
                raise Exception('Class must have a "_{0}s" attribute!'.format(
                    create_method.__name__))

            items = getattr(class_, '_{0}s'.format(create_method.__name__))
            namespace = cache_namespace(namespace_prefix, item_id)
            cache_time = request.registry['cache_global'].get(
                CREATED_KEY, namespace, region)
            if cache_time is None:
                cache_time = time()
                request.registry['cache_global'].set(
                    CREATED_KEY, cache_time, namespace, region)

            # Get the object
            if item_id not in items or items[item_id].created < cache_time:
                if item_id in items:
                    del items[item_id]
                item = create_method(class_, request, item_id, *args, **kwargs)
                if item is None:
                    return None
                items[item_id] = item

            # Check access rights
            if access_function is None:
                return items[item_id]
            get_access = access_function.__func__ \
                if isinstance(access_function, classmethod) \
                else access_function
            access = get_access(class_, request, items[item_id])
            return items[item_id] if access[0] else None

        return _wrapper

    return _decorated


# =============================================================================
def cache_global_value(key, namespace_prefix, region=None):
    """A decorator to retrieve in the global cache the result of a computing
    method whose the first argument is ``request``. The class of the method
    must have an ``uid`` attribute.

    :param str key:
        Key of the value to retrieve.
    :param str namespace_prefix:
        Prefix of the cache namespace.
    :param str region: (optional)
        Name of region.
    """
    def _decorated(method):
        """Decoration of the method `method`."""

        def _wrapper(class_, request, *args, **kwargs):
            """Use of global cache."""
            if not hasattr(class_, 'uid'):
                raise Exception('Class must have a "uid" attribute!')

            namespace = cache_namespace(namespace_prefix, class_.uid)
            value = request.registry['cache_global'].get(
                key, namespace, region)
            if value is not None and not kwargs.get('refresh'):
                return value

            computing_method = method.__func__ \
                if isinstance(method, classmethod) else method
            value = computing_method(class_, request, *args, **kwargs)
            request.registry['cache_global'].set(key, value, namespace, region)
            return value

        return _wrapper

    return _decorated


# =============================================================================
def cache_namespace(namespace_prefix, item_id):
    """Return a namespace for the item ``item_id``.

    :param str namespace:
        Cache namespace.
    :param str item_id:
        ID of the item.
    :rtype: str
    """
    return '{0}-{1}'.format(namespace_prefix, item_id)
