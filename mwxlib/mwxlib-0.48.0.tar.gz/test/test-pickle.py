## https://qiita.com/hatt0519/items/f1f4c059c28cb1575a93
from functools import partial
import pickle

class Singer(object):
    def __init__(self, lylics):
        self.lylics = lylics
    def sing(self):
        print(self.lylics)

def save():
    singer = Singer('Shanranran')
    songer = Singer('Doododoodo')
    singer.sing()
    songer.sing()
    with open('singer.pickle', 'wb') as f:
        pickle.dump(singer, f)
        pickle.dump(songer, f)
        ## pickle.dump(lambda:singer.sing(), f)
        ## --> AttributeError: Can't pickle local object 'save.<locals>.<lambda>'
        pickle.dump(partial(singer.sing), f)
        ## --> ok, partial object is picklable
    del singer

def restore():
    with open('singer.pickle', 'rb') as f:
        singer = pickle.load(f)
        songer = pickle.load(f)
        vocal = pickle.load(f)
    singer.sing()
    songer.sing()
    vocal()

save()
restore()
