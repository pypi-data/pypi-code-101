# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Sqrt5


import gridfs
import pymongo
import sys
from PIL import Image
from bson.objectid import ObjectId
from io import BytesIO


class GFS:

    def __init__(self, ip='127.0.0.1', port=27017, db_name='database', collection_name='image', format='bmp'):
        self.client            = None
        self.db                = None
        self.fs                = None
        self.collection_files  = None
        self.collection_chunks = None
        self.ip = ip
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.format = format

    def connect(self):
        if not self.client:
            sys.stdout.write('Connect MongoDB(IP:%s PORT:%d DATABASE:%s COLLECTION:%s)\n' %
                             (self.ip, self.port, self.db_name, self.collection_name))
            self.client = pymongo.MongoClient(self.ip, self.port)
            self.db = self.client[self.db_name]
            self.fs = gridfs.GridFS(self.db, collection=self.collection_name)
            self.collection_files = self.db[self.collection_name + '.files']
            self.collection_chunks = self.db[self.collection_name + '.chunks']
        else:
            sys.stdout.write('Already connect MongoDB(IP:%s PORT:%d DATABASE:%s COLLECTION:%s)\n' %
                             (self.ip, self.port, self.db_name, self.collection_name))

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client          = None
            self.db              = None
            self.fs              = None
            self.ip              = None
            self.port            = None
            self.db_name         = None
            self.collection_name = None
            self.format          = None
            sys.stdout.write('Connection closed.\n')
        else:
            sys.stdout.write('No connection.')

    def putImage(self, image, **kwargs):
        try:
            binary_data = BytesIO()
            image.save(binary_data, format=self.format)
            self.fs.put(binary_data.getvalue(), **kwargs)
        except Exception as e:
            sys.stdout.write('%s\n' % e)

    def getSize(self):
        return int(self.collection_files.count())

    def getImageIter(self):
        size = self.getSize()
        if size > 100000:
            raise ValueError('Data set is too large(Size:%d).', size)
        sys.stdout.write('Size:%d\n' % size)
        for info in self.collection_files.aggregate([{'$sample':{'size': size}}]):
            image = Image.open(BytesIO(self.fs.get(info['_id']).read()))
            yield image, info

    def getImage(self, batch_size):
        size = self.getSize()
        if size > 100000:
            raise ValueError('Data set is too large(Size:%d).', size)
        images = []
        infos = []
        for info in self.collection_files.aggregate([{'$sample':{'size': batch_size}}]):
            images.append(Image.open(BytesIO(self.fs.get(info['_id']).read())))
            infos.append(info)
        return images, infos

    def getImageById(self, object_id):
        return Image.open(BytesIO(self.fs.get(ObjectId(object_id)).read()))

    def getFileProperty(self, object_id, property):
        return getattr(self.fs.get(ObjectId(object_id)), property)

    def deleteFileById(self, object_id):
        self.fs.delete(ObjectId(object_id))