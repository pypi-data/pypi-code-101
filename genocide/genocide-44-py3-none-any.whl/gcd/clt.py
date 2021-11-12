# This file is placed in the Public Domain.


from .bus import Bus
from .hdl import Handler
from .run import Cfg, Runtime
from .utl import getmain

class Client(Handler):

    def __init__(self):
        super().__init__()
        self.cfg = Cfg()

    def handle(self, clt, e):
        Runtime.put(self, e)

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)

    def start(self):
        k = getmain("k")
        k.add(self)
        super().start()
