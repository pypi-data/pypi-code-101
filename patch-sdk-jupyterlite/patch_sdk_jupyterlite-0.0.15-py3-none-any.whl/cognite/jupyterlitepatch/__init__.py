import os

requests_code = '''"""
This is not the real requests Python module
but a partial API implementation for Basthon.
"""

import js
import json

__author__ = "Romain Casati"
__license__ = "GNU GPL v3"
__email__ = "romain.casati@basthon.fr"


__all__ = ["request"]


# This warning is no longer needed.
# print("Warning: this is not the real requests Python module"
#       " but a partial API implementation for Basthon.")


class ConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Headers(dict):
    """ Case insensitive dict build from request """
    def __init__(self, req):
        for h in req.getAllResponseHeaders().rstrip().split("\\r\\n"):
            h = h.split(":")
            self[h[0]] = ":".join(h[1:]).lstrip()

    def __setitem__(self, key, value):
        super(Headers, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(Headers, self).__getitem__(key.lower())


class Response(object):
    """ See requests.Response API """
    def __init__(self, req):
        self._req = req  # only for debuging purpose
        self.url = req.responseURL
        self.headers = Headers(req)
        self.status_code = req.status
        self.reason = req.statusText
        self.ok = self.status_code < 400
        self.cookies = None
        content_type = self.headers.get("content-type", "")
        self.encoding = next((x.replace("charset=", "").replace(" ", "")
                              for x in content_type.split(";")
                              if "charset=" in x), None)
        # throw away high-order bytes (& 255)
        self.content = bytes([ord(c) & 255 for c in req.response])
        try:
            self.text = self.decode(self.encoding)
        except Exception:
            self.text = req.responseText

    def decode(self, charset="utf-8"):
        return self.content.decode(charset)

    def json(self, charset="utf-8", **kwargs):
        import json
        return json.loads(self.decode(charset), **kwargs)


def request(method, url, **kwargs):
    """ See requests.request """
    # url params
    # print("kwargs: ", kwargs)
    if "params" in kwargs and kwargs["params"] is not None:
      url += "?" + "&".join((f"{k}={v}" for k, v in kwargs["params"].items()))

    if "json" in kwargs:
      kwargs["data"] = json.dumps(kwargs["json"])
    
    req = js.eval("var __basthon_req = new XMLHttpRequest(); __basthon_req")  # hack for using js try/catch (see below)
    req.open(method.lower(), url, False)  # synchronous request
    req.overrideMimeType("text/plain; charset=x-user-defined")
    # headers
    for k, v in kwargs.get("headers", {}).items():
        req.setRequestHeader(k, v)

    def send():
        req.send(kwargs.get("data"))

    def onerror(error):
        cors_message = ""
        raise ConnectionError(f"{error.js_error.toString()}{cors_message} Please check error message in browser console.")

    req._patched_send = send
    req._patched_onerror = onerror
    # big hack since try/catch of JS code is not available on Python side
    js.eval("try { __basthon_req._patched_send(); } catch (e) { __basthon_req._patched_onerror(e); }")
    return Response(req)


for name in ("GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"):
    __all__.append(name.lower())
    globals()[name.lower()] = lambda url, _=name, **kwargs: request(_, url, **kwargs)'''

def apply_patch():
    requests2_path = "/lib/python3.9/site-packages/cognite/client/requests2"
    if os.path.exists(requests2_path):
      print("Patch already applied, stopping.")
      return

    os.mkdir(requests2_path)
    with open(os.path.join(requests2_path,"__init__.py"), "w") as f:
        f.write(requests_code)

    with open("/lib/python3.9/site-packages/cognite/client/_http_client.py") as f:
        content = f.read()
    lines = content.split("\n")
    lines.insert(0, "import cognite.client.requests2 as requests2")

    with open("/lib/python3.9/site-packages/cognite/client/_http_client.py", "w") as f:
        for line in lines:
            line = line.replace("res = self.session.request(method=method, url=url, **kwargs)", "res = requests2.request(method=method, url=url, **kwargs)")
            f.write(line+"\n")

    with open("/lib/python3.9/site-packages/cognite/client/_api_client.py") as f:
        content = f.read()
    lines = content.split("\n")

    with open("/lib/python3.9/site-packages/cognite/client/_api_client.py", "w") as f:
        for line in lines:
            f.write(line+"\n")
            if "def _log_request(cls, res: Response, **kwargs):" in line:
                f.write("        return\n")
    os.environ["COGNITE_DISABLE_GZIP"] = "1"

import asyncio

async def get_credentials():
    import js
    op = js.indexedDB.open("DSHubDB", 5)
    await asyncio.sleep(0.1)
    db = op.result
    tx = db.transaction("TokenStore", "readonly")
    store = tx.objectStore("TokenStore")
    token = store.get(1)
    await asyncio.sleep(0.1)
    return token.result.token, token.result.project, token.result.cluster
