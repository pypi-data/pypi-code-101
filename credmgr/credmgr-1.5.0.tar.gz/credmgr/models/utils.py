"""Provide helper utilities used by other models."""
import re

from credmgr.exceptions import NotFound

reCamelToSnake = re.compile(r"([a-z0-9](?=[A-Z])|[A-Z](?=[A-Z][a-z]))")


def _camelToSnake(name: str) -> str:
    return reCamelToSnake.sub(r"\1_", name).lower()


def _resolveUser(userAttr="owner", returnAttr="id"):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            from . import User

            value = None
            user = kwargs.get(userAttr, None)
            if user:
                if isinstance(user, User):
                    value = getattr(user, returnAttr)
                elif isinstance(user, int):
                    value = user
                elif isinstance(user, str):
                    foundUser = self._credmgr.user(user)
                    if foundUser:
                        value = getattr(foundUser, returnAttr)
                kwargs[userAttr] = value
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


def _resolveModelFromInput(credmgr, model, inputValue, returnAttr="id"):
    value = None
    if isinstance(inputValue, model):
        value = getattr(inputValue, returnAttr)
    elif isinstance(inputValue, int):
        value = inputValue
    elif isinstance(inputValue, str):
        try:
            foundItem = getattr(credmgr, model._credmgrCallable)(inputValue)
        except NotFound:
            foundItem = None
        if foundItem:
            value = getattr(foundItem, returnAttr)
    return value


class CachedProperty:
    """A decorator for caching a property's result.

    Similar to `property`, but the wrapped method's result is cached on the instance.
    This is achieved by setting an entry in the object's instance dictionary with the
    same name as the property. When the name is later accessed, the value in the
    instance dictionary takes precedence over the (non-data descriptor) property.

    This is useful for implementing lazy-loaded properties.

    The cache can be invalidated via `delattr()`, or by modifying `__dict__` directly.
    It will be repopulated on next access.

    """

    def __init__(self, func, doc=None):
        """Initialize the descriptor."""
        self.func = self.__wrapped__ = func

        if doc is None:
            doc = func.__doc__
        self.__doc__ = doc

    # This to make sphinx run properly
    def __call__(self, *args, **kwargs):  # pragma: no cover noqa: D102
        pass

    def __get__(self, item, objtype=None):
        """Implement descriptor getter.

        Calculate the property's value and then store it in the associated object's
        instance dictionary.

        """
        if item is None:
            return self

        value = item.__dict__[self.func.__name__] = self.func(item)
        return value
