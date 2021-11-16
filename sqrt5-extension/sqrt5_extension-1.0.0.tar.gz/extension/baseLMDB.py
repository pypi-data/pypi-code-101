import os
import lmdb
import random


class LmdbSaver(object):
    def __init__(self, lmdb_path, cnt=None, cache_capacity=100):
        self.env = self.open_lmdb(lmdb_path)
        self.cnt = self.init_cnt() if cnt is None else cnt
        self.cache = dict()
        self.cache_capacity = cache_capacity

    @staticmethod
    def open_lmdb(lmdb_path):
        base_folder = os.path.split(lmdb_path)[0]
        if not os.path.exists(base_folder):
            raise FileExistsError(base_folder)
        if os.path.exists(os.path.join(lmdb_path, "data.mdb")):
            #print("Open lmdb {}".format(lmdb_path))
            pass
        else:
            #print("Create lmdb {}".format(lmdb_path))
            pass
        return lmdb.open(lmdb_path, map_size=100*1024*1024)

    def add_map_size(self, adder_size=100*1024*1024):
        lmdb_path = self.env.path()
        map_size = os.path.getsize(os.path.join(lmdb_path, "data.mdb"))
        map_size += adder_size
        self.env.set_mapsize(map_size)

    def init_cnt(self):
        txn = self.env.begin()
        num_samples = txn.get("num-samples".encode("utf-8"))
        if num_samples is None:
            return 0
        else:
            return int(num_samples.decode("utf-8"))

    def get_cnt(self):
        cnt = self.cnt
        self.cnt += 1
        return cnt

    def write_cache(self):
        txn = self.env.begin(write=True)
        for k, v in self.cache.items():
            try:
                txn.put(k, v)
            except lmdb.MapFullError:
                txn.abort()
                return False
        try:
            txn.commit()
        except lmdb.MapFullError:
            txn.abort()
            return False
        return True

    def save_samples(self):
        raise NotImplementedError

    def add(self, data):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def __del__(self):
        self.close()


class LmdbReader(object):
    def __init__(self, lmdb_path):
        self.lmdb_path = lmdb_path
        self.env = self.open_lmdb(lmdb_path)
        self.txn = self.env.begin()
        self.num_samples = self.get_num_samples()

    @staticmethod
    def open_lmdb(lmdb_path):
        base_folder = os.path.split(lmdb_path)[0]
        if not os.path.exists(base_folder):
            raise FileExistsError(base_folder)
        if not os.path.exists(os.path.join(lmdb_path, "data.mdb")):
            raise FileNotFoundError(lmdb_path)
        return lmdb.open(lmdb_path)

    def get_num_samples(self):
        num_samples = self.get("num-samples")
        if num_samples is None:
            raise ValueError("lmdb no num-samples")
        num_samples = int(num_samples.decode("utf-8"))
        return num_samples

    def get(self, k):
        if isinstance(k, str):
            k = k.encode("utf-8")
        v = self.txn.get(k)
        return v

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        raise NotImplementedError

    def close(self):
        try:
            self.txn.abort()
        except:
            pass
        self.env.close()

    def __del__(self):
        self.close()

    def randomSample(self):
        idx = random.randint(0, self.num_samples-1)
        return self.__getitem__(idx)
