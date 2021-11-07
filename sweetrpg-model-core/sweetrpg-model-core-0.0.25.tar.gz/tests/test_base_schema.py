# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Test cases for BaseSchema
"""

from sweetrpg_model_core.schema.base import BaseSchema, BaseEmbeddedSchema
from marshmallow import fields
from datetime import datetime


def test_base_schema():
    class TestSchema(BaseSchema):
        name = fields.Str()

    data = {"id": "1", "name": "Test", "created_at": datetime.utcnow(), "created_by": "test", "updated_at": datetime.utcnow(), "updated_by": "test"}
    schema = TestSchema()
    obj = schema.from_dict(data)
    assert obj is not None
    assert obj.id == "1"
    assert obj.name == "Test"
    assert isinstance(obj.created_at, datetime)
    assert obj.created_by == "test"
    assert isinstance(obj.updated_at, datetime)
    assert obj.updated_by == "test"
    assert not hasattr(obj, "deleted_at") or obj.deleted_at is None
    assert not hasattr(obj, "deleted_by") or obj.deleted_by is None


def test_base_schema_with_deleted():
    class TestSchema(BaseSchema):
        name = fields.Str()

    data = {
        "id": "1",
        "name": "Test",
        "created_at": datetime.utcnow(),
        "created_by": "test",
        "updated_at": datetime.utcnow(),
        "updated_by": "test",
        "deleted_at": datetime.utcnow(),
        "deleted_by": "test",
    }
    schema = TestSchema()
    obj = schema.from_dict(data)
    assert obj is not None
    assert obj.id == "1"
    assert obj.name == "Test"
    assert isinstance(obj.created_at, datetime)
    assert obj.created_by == "test"
    assert isinstance(obj.updated_at, datetime)
    assert obj.updated_by == "test"
    assert isinstance(obj.deleted_at, datetime)
    assert obj.deleted_by == "test"


def test_base_embedded_schema():
    class TestEmbeddedSchema(BaseEmbeddedSchema):
        name = fields.Str()

    data = {"id": "1", "name": "Test"}
    schema = TestEmbeddedSchema()
    obj = schema.from_dict(data)
    assert obj is not None
    assert obj.id == "1"
    assert obj.name == "Test"
