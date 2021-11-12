import pytest
import yaml
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


def object_id_constructor(loader, data):
    return ObjectId(loader.construct_scalar(data))


yaml.add_constructor('!bson.ObjectId', object_id_constructor)


@pytest.fixture
def db(mongodb):
    client = AsyncIOMotorClient('{}:{}'.format(mongodb.client.HOST, mongodb.client.PORT))
    database = client[mongodb.name]
    yield database
    database.client.close()


@pytest.fixture
def collection(db):
    return db.fake
