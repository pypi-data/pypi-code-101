from .config import Config
from .http import Http
import json

class Service():
    default_config = {
            "ADDR": "127.0.0.1",
            "PORT": "10100",
            "WORKDIR": "/home/ms/5ILab/python/py-metathing/workdir"
        }

    def __init__(self, cfg: object, srv_name: str):
        self.config = Config(self.default_config)
        self.config.from_object(cfg)
        self.srv_name = srv_name
        self.http = Http(self.config, self.srv_name)
        self.http.srv = self

    def Bind(self, app):
        self.app = app
        self.http.Build()

    # def parse(self, model_str: str) -> object:

    def ReadProperty(self, key: str):
        return getattr(self.app, key)
        
    def WriteProperty(self, key:str, content:str):
        setattr(self.app, key, json.loads(content))

    def Execute(self, func_name:str, content:str):
        return getattr(self.app, func_name)(**(json.loads(content)))