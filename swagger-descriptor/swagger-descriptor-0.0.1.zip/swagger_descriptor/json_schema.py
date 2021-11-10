#!/usr/bin/env python
# -*- coding=utf-8 -*-
from typing import Dict


class JsonSchema(dict):
    def __init__(self, descriptor: Dict):
        super().__init__(descriptor)

    @property
    def type(self):
        return self.get("type")

    @property
    def title(self):
        return self.get("title")

    @property
    def default(self):
        return self.get("default")

    @property
    def examples(self):
        return self.get("examples")

    @property
    def description(self):
        return self.get("description")

    def get_py_type_name(self):
        py_type = "Unknow"
        if self.get("$ref"):
            return self.get("$ref").split("/")[-1]
        if self.get("type") == "string":
            py_type = "str"
        elif self.get("type") == "integer":
            py_type = "int"
        elif self.get("type") == "boolean":
            py_type = "bool"
        elif self.get("type") == "number":
            py_type = "float"
        elif self.get("type") == "array":
            py_type = "List[{}]".format(JsonSchema(self.get("items")).get_py_type_name())
        elif self.get("type") == "object":
            if self.get("additionalProperties") is not None:
                if self.get("additionalProperties").get("$ref"):
                    py_type = JsonSchema(self.get("additionalProperties")).get_py_type_name()
                else:
                    py_type = "Dict[str, {}]".format(JsonSchema(self.get("additionalProperties")).get_py_type_name())
            else:
                py_type = "Dict"
        else:
            raise Exception("Unkown schema type: {}".format(self))
        return py_type
