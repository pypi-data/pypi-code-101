# -*- coding: utf-8 -*-
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure
from pymongo.cursor import CursorType

from idebug import *

from youtubeplayer.config import *

__all__ = [
    # pymongo 관련
    'db', 'ASCENDING', 'DESCENDING',
    # Classes
    'Collection',
]


cf = Configuration()

try:
    client = MongoClient(host=cf.db.host, port=cf.db.port,
                        document_class=dict,
                        tz_aware=cf.db.tz_aware,
                        connect=True,
                        maxPoolSize=cf.db.maxPoolSize,
                        minPoolSize=cf.db.minPoolSize,
                        connectTimeoutMS=cf.db.connectTimeoutMS,
                        waitQueueMultiple=None, retryWrites=True)
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
except ConnectionFailure:
    logger.error(f'ConnectionFailure: {ConnectionFailure}')
    raise
else:
    db = client[cf.db.DBName]


class Collection:
    # "class pymongo.collection.Collection" 에 대한 Wrapper

    def __init__(self, collName, collMode='real'):
        self.collName = collName
        self.apply_collMode(collMode)

    def apply_collMode(self, mode):
        self.collMode = mode
        if mode == 'real': pass
        elif mode == 'test': self.collName = f"_Test_{self.collName}"
        elif mode == 'sample': self.collName = f"_Sample_{self.collName}"
        else: raise

    def insert_one(self, doc):
        db[self.collName].insert_one(doc)

    def insert_many(self, data):
        msg = '빈데이터를 바로 인서트하는 경우는 비일비재하므로, 여기에서 예외처리한다'
        try: db[self.collName].insert_many(data)
        except Exception as e: pass #logger.debug(f'{self} | {msg}--> {e}')

    def distinct(self, key, filter=None, session=None, **kwargs):
        return db[self.collName].distinct(key, filter, session, **kwargs)

    def find(self, filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False,
            cursor_type=CursorType.NON_TAILABLE, sort=None, allow_partial_results=False,
            oplog_replay=False, modifiers=None, batch_size=0, manipulate=True, collation=None,
            hint=None, max_scan=None, max_time_ms=None, max=None, min=None, return_key=False,
            show_record_id=False, snapshot=False, comment=None, session=None,
            allow_disk_use=None):
        filter = None if filter == {} else filter
        projection = None if projection == {} else projection
        return db[self.collName].find(filter, projection)

    def find_one(self, filter=None, *args, **kwargs):
        return db[self.collName].find_one(filter=None, *args, **kwargs)

    def count_documents(self, filter={}, session=None, **kwargs):
        n = db[self.collName].count_documents(filter, session, **kwargs)
        logger.info(f"{self} | count_documents: {n}")
        return n

    def n_returned(self, cursor):
        n = cursor.explain()['executionStats']['nReturned']
        logger.info(f"{self} | nReturned: {n}")
        return n

    def update_one(self, filter, update, upsert=False, bypass_document_validation=False, collation=None, array_filters=None, hint=None, session=None):
        db[self.collName].update_one(filter, update, upsert, bypass_document_validation, collation, array_filters, hint, session)

    def update_many(self, filter, update, upsert=False):
        db[self.collName].update_many(filter, update, upsert)

    def delete_one(self, filter):
        db[self.collName].delete_one(filter)

    def delete_many(self, filter, collation=None, hint=None, session=None):
        db[self.collName].delete_many(filter, collation, hint, session)

    def drop(self):
        db[self.collName].drop()

    def backup(self):
        # cursor = self.find()
        # bkdb[self.collName].drop()
        # bkdb[self.collName].insert_many(list(cursor))
        # logger.info(f"{self.collName} 백업 완료.")
        print('재개발 필요')

    def rollback(self):
        # cursor = bkdb[self.collName].find()
        # self.drop()
        # self.insert_many(list(cursor))
        # logger.info(f"{self.collName} 원복 완료.")
        print('재개발 필요')
