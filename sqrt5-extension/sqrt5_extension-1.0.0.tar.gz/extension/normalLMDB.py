import os
import cv2
import json
import numpy as np
from .baseLMDB import LmdbSaver, LmdbReader


class NormalLmdbSaver(LmdbSaver):
    def __init__(self, lmdb_path, cnt=None, cache_capacity=100):
        super(NormalLmdbSaver, self).__init__(lmdb_path, cnt, cache_capacity)

    def add(self, data_dict):
        cnt = self.get_cnt()
        self.cache["image-{:09d}".format(cnt).encode("utf-8")] = data_dict["image"]
        self.cache["label-{:09d}".format(cnt).encode("utf-8")] = data_dict["label"]
        self.cache["bound-{:09d}".format(cnt).encode("utf-8")] = data_dict["bound"]
        if len(self.cache) >= 3 * self.cache_capacity:
            while True:
                if self.write_cache():
                    break
                else:
                    self.add_map_size()
            self.cache = dict()

    def close(self):
        self.cache["num-samples".encode("utf-8")] = str(self.cnt).encode("utf-8")
        while True:
            if self.write_cache():
                break
            else:
                self.add_map_size()
        self.cache = dict()
        self.env.close()


class NormalLmdbReader(LmdbReader):
    def __init__(self, lmdb_path):
        super(NormalLmdbReader, self).__init__(lmdb_path)

    def __getitem__(self, idx):
        if idx > self.num_samples:
            return None
        image_key = "image-{:09d}".format(idx).encode("utf-8")
        label_key = "label-{:09d}".format(idx).encode("utf-8")
        bound_key = "wordBB_{:09d}".format(idx).encode("utf-8")
        image = self.txn.get(image_key)
        label = self.txn.get(label_key)
        bound = self.txn.get(bound_key)
        data_dict = {
            "image": image,
            "label": label,
            "bound": bound
        }
        return data_dict

    def getitem_by_index(self, idx):
        if idx > self.num_samples:
            return None
        image_key = "image-{:09d}".format(idx).encode("utf-8")
        label_key = "label-{:09d}".format(idx).encode("utf-8")
        bound_key = "bound-{:09d}".format(idx).encode("utf-8")
        image = self.txn.get(image_key)
        label = self.txn.get(label_key)
        bound = self.txn.get(bound_key)
        data_dict = {
            "image": image,
            "label": label,
            "bound": bound
        }
        return data_dict
