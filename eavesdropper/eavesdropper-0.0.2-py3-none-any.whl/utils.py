from mitmproxy.http import HTTPFlow


class Dropper:
    def request(self, flow: HTTPFlow):
        pass

    def response(self, flow: HTTPFlow):
        pass


