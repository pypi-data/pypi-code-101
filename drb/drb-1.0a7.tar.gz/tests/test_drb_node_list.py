import os
import sys
import unittest

from drb.factory.factory_resolver import DrbNodeList
from drb.utils.logical_node import DrbLogicalNode

from .utils import DrbTestNode


class TestDrbNodeList(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        sys.path.append(os.path.join(
            os.path.dirname(__file__), 'resources', 'packages'))

    def test_int_item(self):
        children = DrbNodeList([DrbLogicalNode('mem://foo'),
                                DrbLogicalNode('mem://bar'),
                                DrbLogicalNode('foobar://foo'),
                                DrbLogicalNode('foobar://bar'),
                                DrbLogicalNode('s3://gael-systems/data')])
        self.assertEqual('Mem_foo', children[0].name)
        self.assertEqual('Mem_bar', children[1].name)
        self.assertEqual('Foobar_foo', children[2].name)
        self.assertEqual('Foobar_bar', children[3].name)
        self.assertEqual('data', children[4].name)
        self.assertIsInstance(children[-1], DrbLogicalNode)

    def test_slice_item(self):
        children = DrbNodeList([DrbLogicalNode('mem://foo'),
                                DrbLogicalNode('mem://bar'),
                                DrbLogicalNode('foobar://foo'),
                                DrbLogicalNode('foobar://foo')])
        result = children[1:3]
        self.assertEqual(2, len(result))
        self.assertEqual('Mem_bar', result[0].name)
        self.assertEqual('Foobar_foo', result[1].name)

    def test_unexpected_item(self):
        children = DrbNodeList([DrbLogicalNode('.')])
        with self.assertRaises(TypeError):
            print(children['.'])

    def test_replace_child(self):
        children = DrbNodeList([DrbLogicalNode('foobar://foo')])
        children[0] = DrbLogicalNode('foobar://bar')
        self.assertEqual('Foobar_bar', children[0].name)

        with self.assertRaises(TypeError):
            children[0] = 3

    def test_add_to_list(self):
        node = DrbTestNode('HelloWorld')

        node.children.append(DrbLogicalNode('mem:data1'))
        node.children.append(DrbLogicalNode('mem:data3'))
        node.children.insert(1, DrbLogicalNode('mem:data2'))

        with self.assertRaises(TypeError):
            node.children.append(42)
        with self.assertRaises(TypeError):
            node.children.insert(0, 'test')

    def test_get_resolved_node(self):
        node = DrbTestNode('foobar')
        node.append_child(DrbLogicalNode('foobar://foo'))
        self.assertEqual('Foobar_foo', node.children[0].name)
