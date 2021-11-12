"""
Key-Value

Oops...TODO - copy in the features from dict_cache
"""
import json

from typing import Any, Dict, Tuple, Set, Union, List

import dataset

from .sqlite import get_or_create, ConnectMode
from .buffered_writer import BufferedTableWriter, ConflictChecker

class KVLite(object):

    @classmethod
    def resolve_type(cls, elem_type):
        if elem_type == 'json':
            return 'string'
        return elem_type

    def __init__(self, path, key_name='key', value_name='value', key_type='string', value_type='string', table_name='items', connect_mode=ConnectMode.JOURNAL):
        self.key_type = key_type
        self.value_type = value_type
        self.key_name = key_name
        self.value_name = value_name
        if isinstance(path, dataset.Database):
            self.table = path[table_name]
        elif isinstance(path, dataset.Table):
            self.table = path
        else:
            assert isinstance(path, str)
            db, self.table = get_or_create(
                path, table_name, mode=connect_mode, primary_id=self.key_name, columns=[self.value_name],
                types={self.key_name: self.resolve_type(self.key_type), self.value_name: self.resolve_type(self.value_type)}
            )

    @classmethod
    def is_type(cls, elem_type, elem):
        if elem_type == 'string':
            return isinstance(elem, str)
        else:
            raise Exception('Unknown type: ' + elem_type)

    @classmethod
    def serialize_type(cls, elem_type, elem):
        if elem_type in ('string', 'integer', 'float'):
            return elem
        elif elem_type == 'json':
            return json.dumps(elem)
        else:
            raise Exception('Do not know how to serialize type: ' + elem_type)

    @classmethod
    def deserialize_type(cls, elem_type, elem):
        if elem_type in ('string', 'integer', 'float'):
            assert cls.is_type(elem_type, elem)
            return elem
        elif elem_type == 'json':
            return json.loads(elem)
        else:
            raise Exception('Do not know how to serialize type: ' + elem_type)

    def _find_elem(self, key_):
        return self.table.find_one(**{self.key_name: key_})

    def get(self, key_, default=None):
        elem = self._find_elem(key_)
        if elem is None:
            return default
        tmp_val = elem[self.value_name]
        return self.deserialize_type(self.value_type, tmp_val)

    # TODO - implement def items(...)

    def __getitem__(self, key_):
        val = self.get(key_)
        if val is None:
            raise KeyError('Error no key in db: ' + key_)
        return val

    def __contains__(self, key_):
        return self._find_elem(key_) is not None

    def __setitem__(self, key_, value):
        #assert self.is_type(self.key_type, key_)
        #assert self.is_type(self.value_type, value)
        self.table.upsert({
            # TODO - for now, we are not serializing the key
            self.key_name: key_,
            self.value_name: self.serialize_type(self.value_type, value)
        }, [self.key_name])

    def set_multiple(self, d: Dict[str, Dict[str, Any]]):
        b = BufferedTableWriter(self.table, key_column=self.key_name, key_conflicts=ConflictChecker.OVERWRITE)
        for k, v in d.items():
            assert isinstance(k, str)
            b.insert({self.key_name: k, self.value_name: self.serialize_type(self.value_type, v)})
        b.force_flush()

    def get_multiple(self, keys: Union[List[str], str]) -> Tuple[Dict[str, Any], Set[str]]:
        if isinstance(keys, str):
            keys = [keys]
        assert isinstance(keys, list)
        keys_set = set(keys)
        assert len(keys) == len(keys_set), 'Error: there are duplicate keys in your request'
        results = {}
        for e in self.table.find(key=keys):
            k, v = e[self.key_name], e[self.value_name]
            assert isinstance(k, str)
            results[k] = self.deserialize_type(self.value_type, v)
        remaining = keys_set - set(results.keys())
        assert len(results) + len(remaining) == len(keys)
        return results, remaining
