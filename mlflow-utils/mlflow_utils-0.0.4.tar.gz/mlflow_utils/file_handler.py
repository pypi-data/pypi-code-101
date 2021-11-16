import json
import pickle as pkl
import pandas as pd


class Handler:
    def load(self, fp):
        raise NotImplementedError

    def save(self, data, fp):
        raise NotImplementedError


class JSONHandler(Handler):
    def load(self, fp):
        with open(fp) as f:
            file = json.load(f)
        return file

    def save(self, data, fp):
        with open(fp, "w+") as f:
            json.dump(data, f)


class PklHandler(Handler):
    def load(self, fp):
        with open(fp, "rb") as f:
            file = pkl.load(f)
        return file

    def save(self, data, fp):
        with open(fp, "wb") as f:
            pkl.dump(data, f)


class CSVHandler(Handler):
    def load(self, fp):
        file = pd.read_csv(fp)
        return file

    def save(self, data, fp):
        data.to_csv(fp, index=False)


HANDLER_MAPPING = {"json": JSONHandler,
                   "pkl": PklHandler,
                   "csv": CSVHandler}
