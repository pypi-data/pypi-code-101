from .specific import Alliances, Cities, Nations, Trades, Wars
import threading
import json


class Apathy:
    def __init__(self, types=(Alliances, Cities, Nations, Trades, Wars), fs="filespace"):
        self.threads = []
        self.things = []
        self.filespace = fs

        for T in types:
            thing = T(fs=fs)
            self.things.append(thing)
            self.threads.append(threading.Thread(target=thing.run, daemon=True, name=T.__name__))


    def run(self):
        self.collect()
        self.combine()
    

    def collect(self):
        data = []

        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()


    def combine(self):
        for thing in self.things:
            with open(thing.file) as f:
                data.append(json.load(f)["timeline"])

        days = set(data[0].keys())
        for dat in data[1:]:
            days = days and set(dat.keys())

        final = {}
        for day in days:
            val = iter()
            for dat in data:
                val += data.items()
            final[day] = dict(val)

        with open(f"{self.filespace}/final.json")
