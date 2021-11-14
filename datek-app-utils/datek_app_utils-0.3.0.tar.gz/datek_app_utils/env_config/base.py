from os import getenv
from typing import Any, get_type_hints

from datek_app_utils.env_config.errors import InstantiationForbiddenError


class Variable:
    def __init__(self, type_: type = str):
        self._type = type_

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, type_=None):
        return self.value

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def value(self) -> Any:
        value = getenv(self._name)
        if value is None:
            return None

        return self._type(value)


class ConfigMeta(type):
    def __new__(mcs, name: str, bases: tuple, namespace: dict):
        temporary_class = type(f"_{name}", (), namespace)
        for class_ in bases + (temporary_class,):
            for key, value in get_type_hints(class_).items():
                namespace[key] = Variable(value)

        return super().__new__(mcs, name, bases, namespace)

    def __iter__(cls):
        return (value for value in cls.__dict__.values() if isinstance(value, Variable))


class BaseConfig(metaclass=ConfigMeta):
    def __new__(cls, *args, **kwargs):
        raise InstantiationForbiddenError
