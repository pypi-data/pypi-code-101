
from enum import Enum

from hardcode_house_model.house.common import (HouseLocation, HouseProperty,
                                               HouseQuotation,
                                               TransactionProperty)
from hardcode_house_model.util.mongo_mixin import DocumentMixin, MongoMixin
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import (DateTimeField, DictField,
                                EmbeddedDocumentField, FloatField, IntField,
                                ListField, StringField, URLField)


class SpiderJob(Document, MongoMixin):
    class Status(Enum):
        Running = 0
        Completed = 100

    meta = {
        "strict": False,
        "indexes": [
            {"fields": ("spider", "job"), "unique": True},
            ("job"),
            ("status"),
            ("updated_datetime")
        ]
    }

    spider = StringField(required=True)
    job = StringField(required=True)
    status = IntField(required=True)
    item_count = IntField(required=True)
    updated_datetime = DateTimeField(required=True)
