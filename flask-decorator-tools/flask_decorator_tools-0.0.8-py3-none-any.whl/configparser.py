from functools import wraps
import json
import os

def parse(file_name, path):
    path = path.split(".")
    def decorator(klass):
        old_init = klass.__init__
        @wraps(klass.__init__)
        def decorated_init(self):
            with open(file_name, "r") as inputFile:
                config_data = json.loads(inputFile.read())
                for x in path:
                    config_data = config_data[x]
                old_init(self,**config_data)
        klass.__init__ = decorated_init
        return klass
    return decorator

def parse_environment_variables():
    def decorator(klass):
        old_init = klass.__init__
        @wraps(klass.__init__)
        def decorated_init(self):
            config_data = {}
            for x in klass.__dataclass_fields__.keys():
                config_data[x] = os.environ.get(x)
            old_init(self,**config_data)
        klass.__init__ = decorated_init
        return klass
    return decorator