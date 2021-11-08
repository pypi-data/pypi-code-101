import os
import re
import json
from click import Command


class GenerateJsonForToca(Command):
    def __init__(self, api, file_path="./toca.json"):
        """
        api is an instance of flask_restful.Api
        """
        super(GenerateJsonForToca, self).__init__(name="GenerateJsonForToca")
        self.api = api
        self.file_path = file_path
        self.callback = self.run

    def run(self):
        if os.path.exists(self.file_path):
            raise FileExistsError(f"{self.file_path} already exists")
        requests = []
        for resource in self.api.resources:
            handler, urls, _ = resource
            for method in list(handler.methods):
                func = getattr(handler, method.lower())
                doc = func.__doc__
                r = re.search("@apiName\s+(\w+)", doc) if doc else None
                name = r.groups()[0] if r else f"{handler.__name__}-{method}"
                param = func.__annotations__.get("param")
                params = {}.fromkeys(param.fields.keys(), "") if param else {}
                request = {
                    "name": name,
                    "method": method,
                    "url": urls[0],
                    "params": params
                }
                requests.append(request)
        output = {
            "project": "toca",
            "headers": {
                "Content-Type": "application/json"
            },
            "host": "",
            "port": 0,
            "requests": requests,
        }
        with open(self.file_path, "w+") as f:
            f.write(json.dumps(output, indent=4, sort_keys=True))
