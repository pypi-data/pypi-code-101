# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Test cases for model conversion
"""

from sweetrpg_model_core.convert.document import to_model
import json


def test_bad_document():
    class BadDocument(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    class TestModel(object):
        def __init__(self, **kwargs) -> None:
            pass

    doc = BadDocument(x=1, y=2)
    model = to_model(doc, TestModel)
    assert model is None


def test_document():
    class GoodDocument(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

        def to_json(self):
            return self.__dict__

    class TestModel(object):
        def __init__(self, **kwargs) -> None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    doc = GoodDocument(x=1, y=2)
    model = to_model(doc, TestModel)
    assert model is not None
    assert isinstance(model, TestModel)
    assert model.x == 1
    assert model.y == 2
