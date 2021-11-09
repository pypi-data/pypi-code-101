import requests
import requests.auth

from redstone.client import TokenAuth


version = "2021-05-18"


class Collection(object):

    def __init__(self, client):
        self.client = client
        self.path = "/v1/%s" % self.__class__.__name__.lower()

        def find_wrapper_cls():
            try:
                return globals()[self.wrapper_class_name]
            except (AttributeError, KeyError):
                return type(self.__class__.__name__[:-1], (Wrapper,), {})

        self.wrapper_class = find_wrapper_cls()

    def list(self):
        url = "%s/%s" % (self.client.endpoint_url, self.path)
        resp = self.client.get(url)
        resp.raise_for_status()
        _, obj_key = self.path.rsplit("/", 1)
        obj_array = resp.json()[obj_key]
        return [self.wrapper_class(self.client, item) for item in obj_array]


class Wrapper(object):
    def __init__(self, client, data):
        self.client = client
        self._body = data

    def __getattr__(self, name):
        if name not in self._body:
            raise AttributeError(
                "'{0}' has no attributes '{1}'".format(self.__class__, name)
            )
        else:
            return self._body[name]

    def __str__(self):
        attrbs = []
        for k, v in self._body.items():
            attrbs.append("{0}={1}".format(k, v))
        stringified = "<{0} {1}>".format(self.__class__.__name__, ", ".join(attrbs))
        return stringified

    def __repr__(self):
        return str(self)

class Instances(Collection):
    pass

class Keys(Collection):
    pass

class Client(requests.Session):

    def __init__(self, credential, region):
        super(Client, self).__init__()
        self.endpoint_url = "https://%s.iaas.cloud.ibm.com" % region
        self._api_generation = 2

        self.auth = TokenAuth(credential)

        self.keys = Keys(self)
        self.instances = Instances(self)


    def request(self, *args, **kwargs):
        params = kwargs.get("params", {})
        params.update({"version": version, "generation": self._api_generation})
        kwargs["params"] = params
        return super(Client, self).request(*args, **kwargs)
