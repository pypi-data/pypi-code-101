import re
import os
import toml
import json
from typing import List
from jinja2 import Template

from toca.entity.api import Api
from toca.entity.service import Service
from toca.utils.errors import HTTPMethodError
from toca.utils.parse import replace_dynamic_arg, get_dynamic_args


class Toca(object):
    def __init__(self, file_path=None):
        self.service_list: List[Service] = []
        if file_path and os.path.isfile(file_path):
            if file_path[-5:] == ".toml":
                self.load_toml(file_path)
            elif file_path[-5:] == ".json":
                self.load_json(file_path)

    def add_service(self, service: Service):
        if not isinstance(service, Service):
            raise TypeError(
                "Invalid type, type of Service is expected, but {} found".
                format(type(service)))
        self.service_list.append(service)

    def get_dynamic_name(self, dynamic_name):
        r = re.search("\{\$\s*([\w._ \-/\(\)\'\"]+)\s*\$\}", dynamic_name)
        if not r:
            return None
        return r.groups()[0].strip()

    def get_dynamic_value(self, dynamic_name):
        dynamic_name = self.get_dynamic_name(dynamic_name)
        if not dynamic_name:
            raise ValueError("Invalid dynamic_name {}".format(dynamic_name))
        service_name, dynamic_name = dynamic_name.split(".", 1)
        if service_name == "_functions":
            return eval(dynamic_name)
        for service in self.service_list:
            if not service.name == service_name:
                continue
            return service.get_dynamic_value(dynamic_name)

    def replace_dynamic_args(self, content):
        dy_names = get_dynamic_args(content)
        for dy_name in dy_names:
            dy_value = self.get_dynamic_value(dy_name)
            if isinstance(dy_value, (str, bytes)):
                content = replace_dynamic_arg(content, dy_name, dy_value)
            else:
                content = dy_value
        return content

    def load_toml(self, file_path):
        env = toml.load(file_path).get("env", {})
        with open(file_path, "r") as f:
            content = f.read()
        content = Template(content).render(**env)
        result = toml.loads(content)
        for service_name in result:
            if service_name == "env":
                continue
            service_dict = result[service_name]
            service = Service(
                name=service_name,
                host=service_dict.pop("host"),
                port=service_dict.pop("port"),
                headers=service_dict.pop("headers", None),
                scheme=service_dict.pop("scheme", "http"),
            )
            self.add_service(service)
            for api_name in service_dict:
                api_dict = service_dict[api_name]
                url = api_dict.get("url")
                method = api_dict.get("method")
                api = Api(api_name, method, url)
                service.add_api(api)
                api.add_attr("params", api_dict.get("params", {}))
                api.add_attr("files", api_dict.get("files", {}))
                api.add_attr("headers", api_dict.get("headers"))
                if not api.headers:
                    api.headers = service.headers
                elif api.headers and service.headers:
                    for key, value in service.headers.items():
                        if key in api.headers:
                            continue
                        api.headers[key] = value

    def load_json(self, file_path):
        with open(file_path, "r") as f:
            env = json.load(f).get("env", {})
        with open(file_path, "r") as f:
            content = f.read()
        content = Template(content).render(**env)
        result = json.loads(content)
        service = Service(
            name=result["project"],
            host=result.pop("host"),
            port=result.pop("port"),
            headers=result.pop("headers", None),
            scheme=result.pop("scheme", "http"),
        )
        self.add_service(service)
        requests = result["requests"]
        for request in requests:
            url = request.get("url")
            method = request.get("method")
            api = Api(name=request["name"], method=method, url=url)
            api.add_attr("params", request.get("params", {}))
            api.add_attr("files", request.get("files", {}))
            api.add_attr("headers", request.get("headers"))
            if not api.headers:
                api.headers = service.headers
            elif api.headers and service.headers:
                for key, value in service.headers.items():
                    if key in api.headers:
                        continue
                    api.headers[key] = value
            service.add_api(api)

    def run(self, service_name=None, api_list=None, show=False):
        for service in self.service_list:
            if service_name and service.name != service_name:
                continue
            for api in service.api_list:
                if api_list and api.name not in api_list:
                    continue
                try:
                    url = self.replace_dynamic_args(api.url)
                    for key, value in api.headers.items():
                        api.headers[key] = self.replace_dynamic_args(
                            api.headers[key])
                    for key, value in api.params.items():
                        api.params[key] = self.replace_dynamic_args(
                            api.params[key])
                    for key, value in api.files.items():
                        api.files[key] = self.replace_dynamic_args(value)
                except AttributeError as e:
                    print(api.name, "ERROR = ", e)
                    continue
                req = service.winney.register(method=api.method,
                                              name=api.name,
                                              uri=url)
                r = None
                if api.method.lower() == "get":
                    r = req(data=api.params, headers=api.headers)
                elif api.method.lower() in ("post", "put", "patch"):
                    r = req(data=api.params if not api.is_json() else None,
                            json=api.params if api.is_json() else None,
                            files=api.files if api.files else None,
                            headers=api.headers)
                elif api.method.lower() in ("head", "options", "delete"):
                    r = req(headers=api.headers)
                else:
                    raise HTTPMethodError("Invalid request method: ",
                                          api.method)
                if r.ok():
                    api.response = r.get_json() if api.is_json(
                    ) else r.get_bytes()
                api.status_code = r.status_code
                if show:
                    if api.is_json():
                        print(
                            json.dumps(api.response, indent=4, sort_keys=True))
                    else:
                        print(api.response)

    def ls(self, service_name=None):
        for service in self.service_list:
            if service_name and service.name != service_name:
                continue
            length = 0
            for api in service.api_list:
                if len(api.name) > length:
                    length = len(api.name)
            for api in service.api_list:
                print(api.name.ljust(length + 3), api.method.ljust(8), api.url)
