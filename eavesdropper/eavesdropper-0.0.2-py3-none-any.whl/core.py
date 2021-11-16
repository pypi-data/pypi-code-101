from mitmproxy.proxy.server import ProxyServer
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.options import  Options
from .utils import *
import asyncio


class EAVESDROPPER:
    Dropper = Dropper

    def __init__(self, *, host: str = "127.0.0.1", port: int = 8080, **kwargs):
        self.proxy = "{}:{}".format(host, port)
        options = Options(listen_host=host, listen_port=port, **kwargs)
        self.mitmproxy = DumpMaster(options)
        self.mitmproxy.server = ProxyServer(ProxyConfig(options))

    def configure(self):
        self.mitmproxy.addons.add(self.Dropper())

    def start(self):
        asyncio.set_event_loop(self.mitmproxy.channel.loop)
        self.mitmproxy.run()

    def __del__(self):
        self.stop()

    def stop(self):
        self.mitmproxy.shutdown()




