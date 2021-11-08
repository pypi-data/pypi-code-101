#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re
from collections import OrderedDict
from typing import Dict, Any, List

import yaml

from cli_rack_validation.domain import TimePeriodMilliseconds, HexInt, IPAddress, MACAddress, TimePeriod
from cli_rack_validation.validate import SensitiveStr
from strome.utils import get_first_existing_file

from jointbox_cli.esphome_ext.expressions.core import EvaluatedObject


class _ListMerge:
    def __init__(self, _list) -> None:
        super().__init__()
        self.data = _list


class JointboxYamlTools:
    @classmethod
    def initialize(cls):
        yaml.add_representer(EvaluatedObject, cls.__represent_dict_subclass)
        yaml.add_representer(SensitiveStr, cls.__represent_sensitive_str)
        yaml.add_representer(TimePeriodMilliseconds, cls.__represent_to_str_class)
        yaml.add_representer(HexInt, cls.__represent_to_str_class)
        yaml.add_representer(IPAddress, cls.__represent_to_str_class)
        yaml.add_representer(MACAddress, cls.__represent_to_str_class)
        yaml.add_representer(TimePeriod, cls.__represent_to_str_class)
        yaml.add_constructor("tag:yaml.org,2002:map", cls.__construct_mapping)
        yaml.add_constructor("tag:yaml.org,2002:seq", cls.__construct_seq)
        yaml.add_implicit_resolver("tag:jointbox.io,2021:merge_list", re.compile(r"^(?:<<\[\])$"), ["<"])
        # yaml.add_constructor("/", cls.__construct_mapping)
        yaml.add_constructor("!include", cls.__construct_include)
        # Dumper
        yaml.add_representer(OrderedDict, cls.__represent_mapping)
        yaml.add_multi_representer(dict, lambda dumper, value: dumper.represent_mapping("tag:yaml.org,2002:map", value))

    @classmethod
    def __represent_dict_subclass(cls, dumper, data: dict):
        node = dumper.represent_dict(dict(data))
        return node

    @classmethod
    def __represent_sensitive_str(cls, dumper, data: SensitiveStr):
        node = dumper.represent_str(data.data)
        return node

    @classmethod
    def __represent_to_str_class(cls, dumper, data: SensitiveStr):
        node = dumper.represent_str(str(data))
        return node

    @classmethod
    def __represent_merge_list(cls, dumper: yaml.Dumper, mapping):
        pass

    @classmethod
    def __represent_mapping(cls, dumper: yaml.Dumper, mapping):
        value: Any = []
        node = yaml.MappingNode("tag:yaml.org,2002:map", value, flow_style=None)
        if dumper.alias_key is not None:
            dumper.represented_objects[dumper.alias_key] = node
        best_style = True
        if hasattr(mapping, "items"):
            mapping = list(mapping.items())
        for item_key, item_value in mapping:
            node_key = dumper.represent_data(item_key)
            node_value = dumper.represent_data(item_value)
            if not (isinstance(node_key, yaml.ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, yaml.ScalarNode) and not node_value.style):
                best_style = False
            value.append((node_key, node_value))

        if dumper.default_flow_style is not None:
            node.flow_style = dumper.default_flow_style
        else:
            node.flow_style = best_style
        return node

    @classmethod
    def __construct_include(cls, loader: yaml.Loader, node: yaml.Node):
        include_file_name = node.value
        candidates = []
        if os.path.isabs(include_file_name):
            candidates.append(include_file_name)
        else:
            parent_dir_path = os.path.dirname(loader.name)
            candidates.append(os.path.join(parent_dir_path, include_file_name))
            candidates.append(include_file_name)

        file_to_load = get_first_existing_file(candidates)
        if file_to_load is None:
            raise ValueError(
                "Unable to include yaml file: "
                + include_file_name
                + ". File: {}, line: {}".format(loader.name, loader.line)
            )
        return cls.__load_yaml_internal(file_to_load)

    @classmethod
    def __construct_seq(self, loader: yaml.Loader, node: yaml.Node):
        seq = loader.construct_sequence(node)
        result = []
        for el in seq:
            if isinstance(el, _ListMerge):
                result.extend(el.data)
            else:
                result.append(el)
        return result

    @classmethod
    def __construct_mapping(cls, loader: yaml.Loader, node: yaml.Node):  # noqa: C901
        """Traverses the given mapping node and returns a list of constructed key-value pairs."""
        # This code is borrowed from ESPHome (esphome/yaml_util.py)

        assert isinstance(node, yaml.MappingNode)
        # A list of key-value pairs we find in the current mapping
        pairs = []
        # A list of key-value pairs we find while resolving merges ('<<' key), will be
        # added to pairs in a second pass
        merge_pairs: List[Any] = []
        # A dict of seen keys so far, used to alert the user of duplicate keys and checking
        # which keys to merge.
        # Value of dict items is the start mark of the previous declaration.
        seen_keys: Dict[str, Any] = {}
        for key_node, value_node in node.value:
            # merge list is '<<[]'
            is_list_merge = key_node.tag == "tag:jointbox.io,2021:merge_list"
            # merge key is '<<'
            is_merge_key = key_node.tag == "tag:yaml.org,2002:merge"
            # key has no explicit tag set
            is_default_tag = key_node.tag == "tag:yaml.org,2002:value"

            if is_default_tag:
                # Default tag for mapping keys is string
                key_node.tag = "tag:yaml.org,2002:str"

            if not is_merge_key and not is_list_merge:
                # base case, this is a simple key-value pair
                key = loader.construct_object(key_node)
                value = loader.construct_object(value_node)

                # Check if key is hashable
                try:
                    hash(key)
                except TypeError:
                    # pylint: disable=raise-missing-from
                    raise yaml.constructor.ConstructorError(f'Invalid key "{key}" (not hashable)', key_node.start_mark)

                key = str(key)
                # key.from_node(key_node)

                # Check if it is a duplicate key
                if key in seen_keys:
                    raise yaml.constructor.ConstructorError(
                        f'Duplicate key "{key}"',
                        key_node.start_mark,
                        "NOTE: Previous declaration here:",
                        seen_keys[key],
                    )
                seen_keys[key] = key_node.start_mark

                # Add to pairs
                pairs.append((key, value))
                continue

            # This is a merge key, resolve value and add to merge_pairs
            value = loader.construct_object(value_node)
            if isinstance(value, dict):
                if is_list_merge:
                    raise yaml.constructor.ConstructorError(
                        f'Invalid list merge instruction "{key}". List is expected', key_node.start_mark
                    )
                # base case, copy directly to merge_pairs
                # direct merge, like "<<: {some_key: some_value}"
                merge_pairs.extend(value.items())
            elif isinstance(value, list):
                if is_list_merge:
                    return _ListMerge(value)
                # # sequence merge, like "<<: [{some_key: some_value}, {other_key: some_value}]"
                for item in value:
                    if not isinstance(item, dict):
                        raise yaml.constructor.ConstructorError(
                            "While constructing a mapping",
                            node.start_mark,
                            "Expected a mapping for merging, but found {}".format(type(item)),
                            value_node.start_mark,
                        )
                    merge_pairs.extend(item.items())
                # Corvis: do we really need to merge the content of the list?
                # return value
            else:
                raise yaml.constructor.ConstructorError(
                    "While constructing a mapping",
                    node.start_mark,
                    "Expected a mapping or list of mappings for merging, " "but found {}".format(type(value)),
                    value_node.start_mark,
                )

        if merge_pairs:
            # We found some merge keys along the way, merge them into base pairs
            # https://yaml.org/type/merge.html
            # Construct a new merge set with values overridden by current mapping or earlier
            # sequence entries removed
            for key, value in merge_pairs:
                if key in seen_keys:
                    # key already in the current map or from an earlier merge sequence entry,
                    # do not override
                    #
                    # "... each of its key/value pairs is inserted into the current mapping,
                    # unless the key already exists in it."
                    #
                    # "If the value associated with the merge key is a sequence, then this sequence
                    #  is expected to contain mapping nodes and each of these nodes is merged in
                    #  turn according to its order in the sequence. Keys in mapping nodes earlier
                    #  in the sequence override keys specified in later mapping nodes."
                    continue
                pairs.append((key, value))
                # Add key node to seen keys, for sequence merge values.
                seen_keys[key] = None

        return OrderedDict(pairs)

    @classmethod
    def __load_yaml_internal(cls, file_path: str):
        with open(file_path, "r") as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        return content
