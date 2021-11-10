# ------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2021 Hieu Pham. All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ------------------------------------------------------------------------------

from cerebro.refactoring import Object
from typing import Union, List


class Tree(Object):
    """
    This is base node to build general tree. The tree node can have children nodes.
    ---------
    @author:    Hieu Pham.
    @created:   10.10.2021.
    @updated:   18.10.2021.
    """

    @property
    def parent(self):
        """
        Get node parent.
        :return: node parent.
        """
        return self._parent

    @property
    def is_root(self):
        """
        Check if this is root.
        :return: is root.
        """
        return self._parent is None

    @property
    def root(self):
        """
        Get tree root.
        :return: root node.
        """
        node = self
        while not node.is_root:
            node = node.parent
        return node

    @property
    def is_leaf(self):
        """
        Check if this is a leaf.
        :return: is leaf.
        """
        return len(self._nodes) == 0

    @property
    def nodes(self):
        """
        Get children nodes.
        :return: children nodes.
        """
        return None if self.is_leaf else [child for child in self._nodes]

    def __init__(self, nodes=None, **kwargs):
        """
        Create new object.
        "param children: children nodes.
        :param kwargs:   keyword arguments.
        """
        super(Tree, self).__init__(**kwargs)
        # Initialize attributes.
        self._parent = None
        # Attach children nodes.
        self._nodes = list()
        self.attach(nodes)

    def data(self, **kwargs) -> dict:
        """
        Get object data.
        :param kwargs:  keyword arguments.
        :return:        object data.
        """
        data = super().data(**kwargs)
        if not self.is_leaf:
            data.update({'nodes': [node.data(**kwargs) for node in self._nodes]})
        return data

    def attach(self, nodes=None, **kwargs):
        """
        Attach children node(s) to tree.
        :param nodes:   node(s) to be attached.
        :param kwargs:  additional keyword arguments.
        :return:        node(s).
        """
        if nodes is None:
            return None
        # Attach single node.
        elif isinstance(nodes, Tree):
            self._nodes.append(nodes)
            nodes._parent = self
            return nodes
        # Attach list of nodes.
        elif isinstance(nodes, list):
            return [self.attach(node, **kwargs) for node in nodes]
        # Otherwise raise error because of invalid nodes.
        raise TypeError("Tree can only attach tree node(s)")

    def detach(self, indexes: Union[None, int, List[int]] = None, **kwargs):
        """
        Detach node(s) from tree.
        :param indexes: index(es) of node(s) to be detached.
        :param kwargs:  additional keyword arguments.
        :return:        node(s).
        """
        if indexes is None:
            return self, None
        # Detach single node.
        elif isinstance(indexes, int):
            child = self._nodes.pop(indexes)
            child._parent = None
            return child
        # Detach list of indexes.
        elif isinstance(indexes, list):
            return self, [self.detach(index, **kwargs) for index in indexes]
        # Otherwise raise error because of invalid indexes.
        raise TypeError("Tree can only detach node(s) base on index(es) of them")

    def clean(self, **kwargs):
        """
        Clean all children.
        :param kwargs:  keyword arguments.
        """
        return self.detach([index for index in range(len(self._nodes))], **kwargs)

    def step(self, steps: Union[None, int, List[int]] = 0, **kwargs):
        """
        Step to another node from current node.
        :param steps:   steps to go.
        :param kwargs:  keyword arguments.
        :return:        destination node.
        """
        if steps is None:
            return self
        # Go single step.
        elif isinstance(steps, int):
            current = self
            # Go forward.
            if steps >= 0:
                current = self._nodes[steps]
            # Go backward.
            elif steps < 0:
                for _ in range(abs(steps)):
                    current = current.parent
            # Return result
            return current
        # Go list of steps.
        elif isinstance(steps, list):
            current = self
            for step in steps:
                current = current.step(step, **kwargs)
            return current
        # Otherwise raise error because of invalid steps.
        raise TypeError("Can only move on tree based on integer step(s)")
