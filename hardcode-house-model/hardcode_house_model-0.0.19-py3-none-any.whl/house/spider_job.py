
from typing_extensions import Required
from hardcode_house_model.house.common import (HouseLocation, HouseProperty,
                                               HouseQuotation,
                                               TransactionProperty)
from hardcode_house_model.util.mongo_mixin import DocumentMixin, MongoMixin
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import (DateTimeField, FloatField, DictField,
                                EmbeddedDocumentField, FloatField, IntField,
                                ListField, StringField, URLField)

class SpiderJob(Document, MongoMixin):
    meta = {
        "strict": False,
        "indexes": [
            {"fields": ("spider", "job"), "unique": True},
            ("job"),
            ("updated_datetime")
        ]
    }

    spider = StringField(Required=True)
    job = StringField(Required=True)
    item_count = IntField(Required=True)
    updated_datetime = DateTimeField(required=True)