# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Test cases for document conversion
"""

from sweetrpg_model_core.convert.model import to_document


def test_bad_model():
    class BadModel(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    class TestDocument(object):
        def __init__(self, **kwargs) -> None:
            pass

    model = BadModel(x=1, y=2)
    doc = to_document(model, TestDocument)
    assert doc is None


def test_model():
    class GoodModel(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

        def to_dict(self):
            return self.__dict__

    class TestDocument(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    model = GoodModel(x=1, y=2)
    doc = to_document(model, TestDocument)
    assert doc is not None
    assert isinstance(doc, TestDocument)
    assert doc.x == 1
    assert doc.y == 2
