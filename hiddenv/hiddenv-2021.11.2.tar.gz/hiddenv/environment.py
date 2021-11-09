"""Reading and casting environment variables."""

import json
import os
from contextlib import suppress
from functools import partial
from typing import ClassVar, Final, Optional, Union, get_origin

from typing_extensions import Annotated

from . import dotenv


class JSONDict(dict):
    """For use in Config and settings module annotations only."""

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError


class JSONList(list):
    """For use in Config and settings module annotations only."""

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError


class _NotNull:  # pylint: disable = too-few-public-methods

    def __getitem__(self, item):
        if isinstance(item, type(Annotated[str, ""])):
            return NotNull[item.__origin__]
        return Union[tuple(x for x in Optional[item].__args__ if x is not type(None))]  # noqa: E721


NotNull = _NotNull()


class _Empty:  # pylint: disable = too-few-public-methods

    def __str__(self):
        return "EMPTY"


empty = _Empty()


def as_property_name(name: str) -> str:
    """Transforms given name to a property (or method) name. Does not validate."""

    return name.lower()


class Env:
    """Class for reading and casting environment variables."""

    @classmethod
    def get_default(cls):
        """Returns the default runtime-wide Env; loads dotenv file on first call."""

        if "_default_env" not in cls.__dict__:
            setattr(cls, "_default_env", cls.load(strict=False))
        return getattr(cls, "_default_env")

    @classmethod
    def load(cls, strict=True, **kwargs):
        """Creates a new Env, loading environment variables from dotenv file in the process."""

        data = dotenv.read_dotenv(dotenv.find_dotenv(**kwargs))
        if data is None and strict:
            raise FileNotFoundError("dotenv file not found.")
        return cls(data or ())

    def __init__(self, __updates=(), **updates):
        # update parameters to os.environ, only if they are not set
        dict(__updates, **updates).items()
        env = {k: v for k, v in dict(__updates, **updates).items() if k not in os.environ}
        os.environ.update(env)

    @staticmethod
    def read(key, cast, *, default=empty):
        """Reads environment variable value and casts it using given callable.

        If variable is missing and `default` is given, returns it (without casting).
        """

        with suppress(KeyError):
            return cast(os.environ[key])
        if default is not empty:
            return default
        raise LookupError(f"Could not find {key!r} in environment, and default was not provided")

    def str(self, key, *, default=empty):
        """Reads environment variable value and casts it as a string.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(key, cast=str, default=default)

    def bool(self, key, *, default=empty):
        """Reads environment variable value and casts it as a boolean.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(key, cast=lambda v: v.lower() == "true", default=default)

    def int(self, key, *, default=empty):
        """Reads environment variable value and casts it as an integer.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(key, cast=int, default=default)

    def float(self, key, *, default=empty):
        """Reads environment variable value and casts it as a float.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(key, cast=float, default=default)

    def json(self, key, *, default=empty):
        """Reads environment variable value and loads it as json data.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(key, cast=json.loads, default=default)

    def json_list(self, key, *, default=empty):
        """Reads environment variable value and loads it as json data, then validates it as a list.

        If variable is missing and `default` is given, returns it (without casting or validation).
        """

        ret = self.json(key, default=default)
        if ret is not default and not isinstance(ret, list):
            raise ValueError(f"environment variable {key} did not produce a list, got {ret}")
        return ret

    def json_dict(self, key, *, default=empty):
        """Reads environment variable value and loads it as json data, then validates it as a list.

        If variable is missing and `default` is given, returns it (without casting or validation).
        """

        ret = self.json(key, default=default)
        if ret is not default and not isinstance(ret, dict):
            raise ValueError(f"environment variable {key} did not produce a dict, got {ret}")
        return ret

    def list(self, key, *, default=empty):
        """Reads environment variable value and casts it as a list of strings.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(
            key,
            cast=lambda v: [i.strip() for i in v.split(",")],
            default=default,
        )

    def tuple(self, key, *, default=empty):
        """Reads environment variable value and casts it as a tuple of strings.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(
            key,
            lambda v: tuple(i.strip() for i in v.lstrip("(").rstrip(")").split(",")),
            default=default,
        )

    def dict(self, key, *, default=empty):
        """Reads environment variable value and casts it as a string-to-string dict.

        If variable is missing and `default` is given, returns it (without casting).
        """

        return self.read(
            key,
            cast=lambda v: dict(p.partition("=")[::2] for p in filter(None, (p.strip() for p in v.split(";")))),
            default=default,
        )

    def get_by_annotations(
        self,
        obj,
        key_to_name=None,
        name_is_setting=None,
        custom_processing=(),
    ):
        """Returns transformed attribute names and values from environment by `obj.__annotations__`."""

        if callable(getattr(obj, "get_default", None)) and hasattr(type(obj), "__info__"):
            get_default = partial(obj.get_default, default=empty)
        else:
            get_default = partial(lambda k: getattr(obj, k, empty))

        for key, annotation in getattr(obj, "__annotations__", {}).items():
            name = _get_setting_name(
                attribute_name=key,
                attribute_annotation=annotation,
                key_to_name=key_to_name,
                name_is_setting=name_is_setting,
            )
            if name is None:
                continue
            if key in custom_processing:
                yield key, custom_processing[key]()
                continue
            property_name = as_property_name(key)
            maybe_property = getattr(getattr(obj, "__class__", None), property_name, None)
            if isinstance(maybe_property, property):
                yield key, maybe_property.fget(obj)
                continue
            assert not (isinstance(obj, type) and isinstance(getattr(obj, property_name, None), property)), (obj, name)
            getter = _get_getter(self, fixed_annotation=NotNull[annotation])
            processing = _get_processing(
                obj=obj,
                attribute_name=key,
                required=not callable(getter),
            )
            preprocessing = _get_preprocessing(fixed_annotation=NotNull[annotation])

            if not callable(getter):
                assert preprocessing is None, (key, name, preprocessing, processing, getter)
                assert processing is not None, (key, name, preprocessing, processing, getter)
                getter = self.str

            value = _get_setting_value(
                get_value=getter,
                setting_name=name,
                process=processing if processing is not None else lambda x: x,
                preprocess=preprocessing,
                value_default=get_default(key),
            )
            yield key, value


def _get_setting_name(
    attribute_name,
    attribute_annotation,
    key_to_name,
    name_is_setting,
):
    if isinstance(attribute_annotation, type(Annotated[str, ""])):
        if len(attribute_annotation.__metadata__) == 1 and isinstance(attribute_annotation.__metadata__[0], str):
            attribute_name = attribute_annotation.__metadata__[0]
        attribute_annotation = attribute_annotation.__origin__
    origin = get_origin(attribute_annotation)
    if origin is None:
        origin = attribute_annotation
    if origin is ClassVar or origin is Final:
        return None  # coverage: exclude
    setting_name = attribute_name if key_to_name is None else key_to_name(attribute_name)
    if name_is_setting is None or name_is_setting(setting_name):
        return setting_name
    return None


def _process_tuple(args: tuple, inst: tuple):
    if len(args) != len(inst):
        raise ValueError(f"Expected {len(args)}-tuple, got {inst!r}")
    return tuple(v(k) for k, v in zip(inst, args))


def _get_preprocessing(fixed_annotation):

    if get_origin(fixed_annotation) is dict:
        process_key, process_value = fixed_annotation.__args__
        return lambda inst: {process_key(k): process_value(v) for k, v in inst.items()}

    if get_origin(fixed_annotation) is list:
        process_item, = fixed_annotation.__args__
        return lambda inst: [*map(process_item, inst)]

    if get_origin(fixed_annotation) is tuple:
        if len(fixed_annotation.__args__) == 2 and fixed_annotation.__args__[1] is ...:
            process_item, _ = fixed_annotation.__args__
            return lambda inst: (*map(process_item, inst), )
        return partial(_process_tuple, (() if fixed_annotation.__args__ == ((), ) else fixed_annotation.__args__))

    return None


def _get_getter(env: Env, fixed_annotation):
    if fixed_annotation is JSONDict:
        return env.json_dict
    if fixed_annotation is JSONList:
        return env.json_list
    if get_origin(fixed_annotation) in (dict, list, tuple):
        return getattr(env, get_origin(fixed_annotation).__name__)
    with suppress(AttributeError):
        return getattr(env, fixed_annotation.__name__)
    return None


def _get_processing(obj, attribute_name, required: bool):
    process_name = f"_process_{attribute_name}"
    process = getattr(obj, process_name, empty)
    if process is empty:
        process_name = f"_process_{as_property_name(attribute_name)}"
        process = getattr(obj, process_name, empty)

    if callable(process):
        return process
    if required:  # coverage: exclude
        # Config classes raise error before getting here
        getattr(obj, process_name)  # raises internal AttributeError if missing
        raise AttributeError(f"{getattr(obj, '__name__', obj)} attribute {process_name} is not callable")
    return None


def _get_setting_value(
    get_value,
    setting_name,
    process,
    preprocess,
    value_default,
):

    if preprocess is None:
        return process(get_value(setting_name, default=value_default))

    if value_default is empty:
        setting_value = get_value(setting_name)
    else:
        try:
            setting_value = get_value(setting_name)
        except LookupError:
            return process(value_default)
    return process(preprocess(setting_value))
