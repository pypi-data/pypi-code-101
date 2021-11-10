from typing import Any, Dict, List, Optional, Union

from .functional import dic_del, dic_get, dic_has, dic_merge, dic_set, dic_walk

DictKey = Union[Any, List[Any]]


def normalise_key(key):
    return [key] if type(key) is not list else key


class DictBelt:
    """
    Class wrapper to access utility methods in an objective fashion.
    """

    def __init__(self, data: Dict):
        self.dict = data

    def get(
        self, key: DictKey, *, default: Any = None, raise_on_missing: bool = True
    ) -> Any:
        """
        Retrieve the value at `key` in `self.dict`.

        `default` is the default value to return if missing
        `raise_on_missing` indicates whether to raise an exception if the key is not found
        """
        value = dic_get(
            self.dict,
            normalise_key(key),
            default=default,
            raise_on_missing=raise_on_missing,
        )
        if type(value) is dict:
            return DictBelt(value)
        return value

    def set(self, key: DictKey, value: Any) -> "DictBelt":
        """
        Set the value `val` in `self.dict` at `key` and returns self.

        Will raise an error if key doesn't exist.
        """
        dic_set(self.dict, normalise_key(key), value)
        return self

    def rm(self, key: DictKey) -> "DictBelt":
        """
        Delete `key` from dictionary `self.dict`. Mutates `self.dict` and return `self`.
        """
        dic_del(self.dict, normalise_key(key))
        return self

    def has(self, key: DictKey) -> bool:
        """
        Predicate to verify if `key` exists in `self.dict`.
        """
        return dic_has(self.dict, normalise_key(key))

    def walk(
        self,
        key: DictKey = list(),
        callback: Optional[callable] = None,
        context: Dict = dict(),
    ) -> "DictBelt":
        """
        Invokes `callback` for each item of `self.dict` including each sub-dict and sub-list thereof.

        The expected signature of `callback` is like so:

        ```
        def my_callback(dic: Dict, key: DictKey, val: Any, context: Dict)
        ```

        `context` is a dictionary passed along to each invocation of `callback`.
        """
        dic_walk(self.dict, normalise_key(key), callback, context)
        return self

    def merge(self, *dicts):
        """
        Merge `self.dict` with all `dicts` into one. Mutates `self.dict`.
        """

        def normalise_dict(d):
            return d if type(d) is dict else d.dict

        return dic_merge(map(normalise_dict, [self, *dicts]))

    def __add__(self, b):
        return self.merge(b)

    def __getitem__(self, key: DictKey) -> Any:
        return self.get(key)

    def __setitem__(self, key: DictKey, value: Any):
        self.set(key, value)

    def __contains__(self, key: DictKey):
        return self.has(key)

    def __len__(self) -> int:
        return len(self.dict)

    def __delitem__(self, key: DictKey):
        self.rm(key)

    def keys(self):
        return self.dict.keys()

    def items(self):
        return self.dict.items()
