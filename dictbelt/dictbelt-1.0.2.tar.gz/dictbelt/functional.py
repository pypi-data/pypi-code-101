import copy
from functools import lru_cache
from typing import Any, Dict, List

DictKey = List[Any]


def dic_get(
    dic: Dict, key: DictKey, *, default: Any = None, raise_on_missing: bool = True
) -> Any:
    """
    Retrieve the value at `key` in `dic`.

    `default` is the default value to return if missing
    `raise_on_missing` indicates whether to raise an exception if the key is not found
    """
    buffer = dic
    for segment in key:
        try:
            buffer = buffer[segment]
        except (IndexError, TypeError, KeyError) as e:
            if default is None and raise_on_missing:
                raise KeyError(f"'{'.'.join(map(str, key))}' not found in dict") from e
            else:
                return default
    return buffer


def dic_set(dic: Dict, key: DictKey, val: Any) -> Dict:
    """
    Set the value `val` in `dic` at `key` and returns `dic`.

    Will raise an error if key doesn't exist.
    """
    if len(key) == 1:
        dic[key[0]] = val
        return
    parent = dic_get(dic, key[:-1])
    parent[key[-1]] = val
    return dic


def dic_del(dic: Dict, key: DictKey) -> Dict:
    """
    Delete `key` from dictionary `dic`. Mutates `dic`.
    """
    parent = dic_get(dic, key[:-1])
    parent[key[-1]] = None
    del parent[key[-1]]
    return dic


def dic_has(dic: Dict, key: DictKey = list()):
    """
    Predicate to verify if `key` exists in `dic`.
    """
    try:
        dic_get(dic, key)
    except (KeyError, TypeError):
        return False
    return True


def dic_walk(
    dic: Dict, key: DictKey = list(), callback: callable = None, context: Dict = dict()
) -> Dict:
    """
    Invokes `callback` for each item of `dic` including each sub-dict and sub-list thereof.

    The expected signature of `callback` is like so:

    ```
    def my_callback(dic: Dict, key: DictKey, val: Any, context: Dict)
    ```

    `context` is a dictionary passed along to each invocation of `callback`.
    """
    subject = dic_get(dic, key)

    iterator = None
    if type(subject) is dict:
        iterator = subject.items()
    elif type(subject) is list:
        iterator = enumerate(subject)
    else:
        return subject

    for segment, val in iterator:
        local_context = copy.deepcopy(context)
        if callback:
            try:
                ret = callback(dic, key + [segment], val, local_context)
                if type(ret) is dict:
                    local_context = ret
            except StopIteration:
                return
        if type(val) is dict or type(val) is list:
            dic_walk(dic, key=key + [segment], callback=callback, context=local_context)
    return dic


def dic_merge(dicts: List[Dict]) -> Dict:
    """
    Merge all `dicts` into one. Mutates `dicts[0]`.
    """

    def _merge(dic1, dic2):
        for k, v in dic2.items():
            if k in dic1 and isinstance(dic1[k], dict) and isinstance(dic2[k], dict):
                _merge(dic1[k], dic2[k])
            else:
                dic1[k] = dic2[k]

    result = {}
    for dic in dicts:
        _merge(result, dic)
    return result
