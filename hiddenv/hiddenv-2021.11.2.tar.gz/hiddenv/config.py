"""Config classes to be used alone or a predefined parts for `hiddenv.settings` source module `.__include__`."""

import inspect
import re
import warnings
from contextlib import suppress
from functools import partial
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Final,
    List,
    Mapping,
    NamedTuple,
    Optional,
    Pattern,
    Protocol,
    Tuple,
    Type,
    TypeVar,
    Union,
    get_origin,
)

import docstring_parser as docs
from typing_extensions import Annotated

from hiddenv.environment import Env, NotNull, as_property_name, empty


_Tco = TypeVar("_Tco", covariant=True)


class KwargsCallable(Protocol[_Tco]):  # pylint: disable = too-few-public-methods
    """Protocol for keyword-only parameters callable, e.g. a NamedTuple class."""

    def __call__(self, **kwargs) -> _Tco:
        ...


class SettingInfo(NamedTuple):
    """Metadata for a Config subclass' annotated setting."""

    key: str
    annotation: Any
    description: str
    parent: Type["Config"]
    owner: Type["Config"]
    default: Any = empty

    @property
    def name(self):
        """Setting name."""

        return self.owner.as_setting_name(self.key)

    @property
    def property_name(self):
        """Property (or method) name."""

        return as_property_name(self.name)

    @property
    def is_property(self):
        """Whether the actual attribute is a property."""

        return isinstance(getattr(self.owner, self.property_name, None), property)

    @property
    def dotenv(self):
        """Textual .env representation of this setting."""

        if self.is_property:  # coverage: exclude
            raise ValueError(f"{_Reserved(self.owner)}.{self.key} is a property setting")

        name = self.name
        if isinstance(self.annotation, type(Annotated[str, ""])):
            if len(self.annotation.__metadata__) == 1 and isinstance(self.annotation.__metadata__[0], str):
                name = self.annotation.__metadata__[0]
        if self.owner.namespace:
            name = f"{self.owner.namespace}_{name}"
        text = f"{name}="
        default_text = ""
        if self.default is not empty:
            default_text = f" (default {self.default!r})"
            text = f"#{text}"
        if self.description.strip():
            *lines, line = self.description.strip().split("\n")[::-1]
            for line in lines:
                text = f"#     {line}\n{text}"  # coverage: exclude
            text = f"# setting {name}{default_text}: {line}\n{text}"
        else:
            text = f"# setting {name}{default_text}\n{text}"
        return f"\n{text}"

    def __str__(self):
        text = f"{self.key}: {inspect.formatannotation(self.annotation)}"
        if self.default is not empty:
            text = f"{text} = {self.default!r}"
        description = self.description.strip().replace("\n", "\t")
        if description:
            text = f"{text}  # {description}"
        return text


EMPTY_NAMESPACE: Final[str] = type("CustomNamespace", (str, ), dict(__slots__=()))()


def _is_immutable(annotation):
    return annotation is Final or get_origin(annotation) in (get_origin(ClassVar[str]), get_origin(Final[str]))


class _Reserved(NamedTuple):
    source: type

    @property
    def reserved(self):
        """All reserved names of `self.source`"""

        if issubclass(self.source, Config):
            if "__reserved__" in self.source.__dict__:
                return tuple(self.source.__reserved__)
            return tuple(
                k for k in {*self.source.__dict__}.difference(self.source.__annotations__)
                if not isinstance(getattr(self.source, as_property_name(k)), property)
            )
        return tuple(dir(self.source))  # coverage: exclude

    def get_reserved(
        self,
        transformer: Callable[[str], str] = lambda x: x,
        filterer: Callable[[str], Any] = lambda x: True,
    ):
        """Returns reserved names of `self.source`, transformed and filtered using given input."""

        return tuple(filter(filterer, map(transformer, self.reserved)))

    def __str__(self):
        return f"{self.source.__module__}.{self.source.__qualname__}"


class _Annotation(NamedTuple):
    key: str
    annotation: Any
    source: type
    name: str
    property_name: str

    @property
    def immutable(self):
        """Whether annotation is immutable (e.g. ClassVar) or not."""

        return _is_immutable(self.annotation)


_T = TypeVar("_T")


def load(__call: KwargsCallable[_T], __get: Callable[[str], Any], **overrides) -> _T:
    """Returns result of given kwargs callable.

    Populates call parameters using overrides and the __get callable.
    """

    for key in frozenset(inspect.signature(__call).parameters).difference(overrides):
        with suppress(AttributeError):
            overrides[key] = __get(key)
    return __call(**overrides)


# def _get_doc(target, description, **attribute_descriptions):
#     if isinstance(getattr(target, "__doc__", None), str) and getattr(target, "__doc__").strip():
#         parsed = docs.parse(getattr(target, "__doc__"))
#         if description is None:
#             description = (parsed.short_description or "").strip()
#             if parsed.long_description:
#                 description = f"{description}\n\n{parsed.long_description.strip()}"
#         for param in parsed.params:
#             attribute_descriptions.setdefault(param.arg_name, param.description)  # type: ignore
#
#     parts = [f"{textwrap.dedent((description or '').rstrip())}\n"]
#     if attribute_descriptions:
#         parts.append("Attributes:")
#     for k, v in attribute_descriptions.items():
#         parts.append(f"    {k}:\n{textwrap.indent(textwrap.dedent(v).rstrip(), ' ' * 8)}")
#     return "\n".join(parts).rstrip()
#
#
# def _get_class_namespace(cls, target, skip_parameters, raise_error) -> dict:
#     if target is None:
#         return {}
#
#     skip = f"while extending {cls.__module__}.{cls.__qualname__} for {target!r}, skipping parameter {{}}: {{}}"
#
#     existing: Dict[str, Any] = {cls.as_setting_name(k): ann for k, ann in cls.__annotations__.items()}
#
#     annotations: Dict[str, Any] = {}
#     defaults: Dict[str, Any] = {}
#
#     for i, parameter in enumerate(inspect.signature(target).parameters.values()):
#
#         if i in skip_parameters or parameter.name in skip_parameters:
#             continue
#
#         if parameter.kind in (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL):
#             reason = skip.format(parameter.name, "variadic parameters not allowed")
#             if raise_error:
#                 raise TypeError(reason)
#             warnings.warn(reason)
#             continue
#
#         if parameter.annotation is inspect.Parameter.empty:
#             reason = skip.format(parameter.name, "parameter missing annotation")
#             if raise_error:
#                 raise TypeError(reason)
#             warnings.warn(reason)
#             continue
#
#         name = cls.as_setting_name(parameter.name)
#         if not cls.is_setting(name):
#             reason = skip.format(parameter.name, f"the generated setting name {name} is invalid")
#             if raise_error:
#                 raise TypeError(reason)
#             warnings.warn(reason)
#             continue
#
#         if name in existing and existing[name] != parameter.annotation:
#             raise TypeError(
#                 skip.format(
#                     parameter.name,
#                     (
#                         f"the annotation {inspect.formatannotation(parameter.annotation)} does not match "
#                         f"old annotation {inspect.formatannotation(existing[name])}"
#                     ),
#                 ),
#             )
#
#         if name in annotations:
#             raise TypeError(skip.format(parameter.name, f"duplicate setting name {name}"))
#
#         annotations[name] = parameter.annotation
#
#         if parameter.default is not inspect.Parameter.empty:
#             defaults[name] = parameter.default
#
#     return {
#         "__annotations__": annotations,
#         **defaults,
#     }


class Config:
    """Settings class for use in specific cases (as opposed to project-wide) or as part of a source settings module.

    Attributes:
        dotenv:
            Textual .env file representation of settings for this Config class, generated using `.__info__`
        name_pattern:
            regex pattern for valid setting (or namespace) name
        namespace:
            prefix to use when getting settings from environment variables
    """

    __info__: ClassVar[Mapping[str, SettingInfo]] = MappingProxyType({})
    __reserved__: ClassVar[frozenset] = frozenset()  # reserved setting names, i.e. not available for annotating/usage
    dotenv: ClassVar[str] = ""
    namespace: ClassVar[str] = ""
    name_pattern: ClassVar[Pattern[str]] = re.compile(r"^[A-Z][A-Z0-9]*(__?[A-Z0-9]+)*$")

    @classmethod
    def extend_for(
        cls: "_TConfig",
        *,
        namespace: str = "",
        # target: Optional[Callable] = None,
        # skip_parameters: Collection[Union[int, str]] = (),
        # raise_error=False,
        # description: str = None,
        # **attribute_descriptions: str,
    ) -> "_TConfig":
        """Returns a subclass update using given input.

        Args:
            namespace: new namespace for the class
            # target: callable to get additional setting parameters from
            # skip_parameters: names of target parameters to skip
            # raise_error: whether to raise an error on invalid target parameters
            # description: new class description; do not use with doc parameter
            # **attribute_descriptions: new settings' descriptions; do not use with doc parameter
        """

        # class_namespace = _get_class_namespace(cls, target, skip_parameters, raise_error)
        # class_namespace["__doc__"] = _get_doc(target, description, **attribute_descriptions)

        return type(  # type: ignore
            cls.__name__,
            (cls, ),
            {},
            namespace=namespace,
        )

    @property
    def env(self) -> Env:
        """Env to use for loading environment variables."""

        if self.__env is None:
            self.__env: Optional[Env] = Env.get_default()
        return self.__env

    @property
    def app(self) -> Optional[str]:
        """App name, primarily for django-related Config subclass usage."""

        return self.__app

    def __init__(
        self,
        namespace: Optional[str] = None,
        __env: Env = None,
        __app: str = None,
        **attributes: type,
    ):
        """
        Args:
            namespace:
                prefix to use when getting settings from environment variables;
                defaults to class namespace
            __env:
            __app: App name, primarily for django-related Config subclass usage.
            **attributes: additional annotations to use
        """

        self.__attributes: dict = {}
        self.__defaults = {}
        self.__env = __env
        self.__app = __app

        if namespace is not EMPTY_NAMESPACE:
            namespace = namespace or self.__class__.namespace
        if namespace is not EMPTY_NAMESPACE and not self.is_setting(namespace):
            raise ValueError(f"Invalid namespace {namespace!r}")
        self.__namespace = namespace

        reserved = frozenset(k.upper() for k in dir(self) if self.is_setting(k.upper()))
        for key, ann in attributes.items():
            name = key.upper()
            assert name not in reserved, (key, ann)
            assert name not in self.__attributes, (key, ann)
            assert self.is_setting(name), (key, ann)
            assert callable(getattr(Env, ann.__name__)), (key, ann)
            self.__attributes[name] = ann

        for key, ann in self.__annotations__.items():
            # should be ok from __init_subclass__
            assert not _is_immutable(ann) and self.is_setting(self.as_setting_name(key))
            if hasattr(self.__class__, key) and getattr(self.__class__, key) is None:
                if isinstance(ann, type(Annotated[str, ""])):  # coverage: exclude
                    ann = Annotated[(NotNull[ann.__origin__], *ann.__metadata__)]  # type: ignore
                else:
                    ann = NotNull[ann]
            name = self.as_setting_name(key)
            if isinstance(getattr(self.__class__, as_property_name(name), None), property):
                assert not (isinstance(ann, type(Annotated[str, ""])) or get_origin(NotNull[ann]) is Union), (key, ann)
                self.__attributes[name] = Annotated[NotNull[ann], empty]
                continue
            assert get_origin(ann) is not Union, (key, ann)
            if name not in self.__attributes:
                _ann = ann
                if isinstance(ann, type(Annotated[str, ""])):
                    _ann = ann.__origin__
                    assert get_origin(_ann) is not Union, (key, ann)
                _ann = get_origin(_ann) or _ann
                assert hasattr(_ann, "__name__"), (_ann, ann)
                env_call = getattr(Env, _ann.__name__, None)
                process_name = f"_process_{as_property_name(name)}"
                process_call = getattr(self, process_name, None)
                error_text = f"missing {process_name} for {key}: {inspect.formatannotation(ann)}"
                if not (callable(env_call) or callable(process_call)):
                    assert isinstance(_ann, type) and issubclass(_ann, Config), error_text
                self.__attributes[name] = ann
            received = self.__attributes[name]
            assert ann is received, f"`{name}` should be of type {ann.__name__}, got {received.__name__}"
            if hasattr(self.__class__, key):
                self.__defaults[name] = getattr(self.__class__, key)

    def _get(self, name):
        assert self.is_setting(name), name
        ann = self.__attributes[name]
        if isinstance(getattr(self.__class__, as_property_name(name), None), property):
            return super().__getattribute__(as_property_name(name))
        if isinstance(ann, type) and issubclass(ann, Config):
            return ann(None, self.env).populate_from_env(parent_namespace=self.__namespace)
        env_name = name
        if (
            isinstance(ann, type(Annotated[str, ""])) and len(getattr(ann, "__metadata__")) == 1 and
            isinstance(getattr(ann, "__metadata__")[0], str)
        ):
            env_name = getattr(ann, "__metadata__")[0]
        env_name = "_".join(filter(None, (self.__namespace, env_name)))
        (k, v), = self.env.get_by_annotations(
            self,
            key_to_name=lambda key: "_".join(filter(None, (self.__namespace, key))),
            name_is_setting=lambda name_: name_ == env_name,
        )
        assert name == k, (name, k, v)
        return v

    def __getattribute__(self, __name: str) -> Any:
        if __name.startswith("_") or __name in ("as_setting_name", "is_setting"):
            return super().__getattribute__(__name)
        orig_name, setting_name = __name, self.as_setting_name(__name)
        if setting_name not in self.__attributes:
            return super().__getattribute__(orig_name)
        if setting_name not in self.__dict__:
            setattr(self, setting_name, self._get(setting_name))
        return super().__getattribute__(setting_name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        env_name = self.as_setting_name(__name)

        if not __name.startswith("_") and self.is_setting(env_name):
            assert env_name in self.__attributes, env_name
            ann = self.__attributes[env_name]
            if (
                isinstance(ann, type(Annotated[str, ""])) and len(ann.__metadata__) == 1 and
                (isinstance(ann.__metadata__[0], str) or ann.__metadata__[0] is empty)
            ):
                ann = ann.__origin__

            received = type(__value)
            error_message = f"`{env_name}` should be of type {ann}, got {received.__name__} {__value!r}"

            origin = get_origin(ann)
            multi = False
            if origin in (list, dict, tuple):
                args = ann.__args__
                if origin is tuple and args == ((), ):
                    args = ()
                elif origin is tuple and len(args) == 2 and args[-1] is ...:
                    args = (args[0], )
                    multi = True
                assert all(isinstance(arg, type) for arg in args), ann
            else:
                assert origin is None and isinstance(ann, type), ann
                args = empty

            if __value is None:
                info_ann = self.__info__[env_name].annotation
                assert Optional[info_ann] == info_ann, error_message
            elif origin is None:
                assert received is ann, error_message
            else:
                assert received is origin, error_message
                if origin is tuple and not multi:
                    assert len(args) == len(__value), error_message
                    assert all(isinstance(x, t) for x, t in zip(__value, args)), error_message
                elif origin is list or origin is tuple:
                    item_ann, = args
                    assert all(isinstance(x, item_ann) for x in __value), error_message
                else:
                    assert origin is dict
                    kat, vat = args
                    assert all(isinstance(k, kat) and isinstance(v, vat) for k, v in __value.items()), error_message

            __name = env_name

        super().__setattr__(__name, __value)

    def get_default(self, key, default):
        """Fetches default value. Primarily for hiddenv.environment.Env.get_by_annotations."""

        return self.__defaults.get(key, default)

    def load(self, __call: KwargsCallable[_T], **overrides) -> _T:
        """Returns result of given kwargs callable.

        Populates call parameters using overrides and this Config instance.
        """

        return load(__call, partial(getattr, self), **overrides)

    def populate_from_env(self, env: Env = None, parent_namespace: str = None, *, target: Any = empty):
        """Populates settings to target (default self) from environment and returns the target."""

        if env is not None:  # coverage: exclude
            self.__env = env
        if parent_namespace:
            namespace = parent_namespace
            if self.__namespace:
                namespace = f"{namespace}_{self.__namespace}"
        else:
            namespace = self.__namespace
        assert namespace is EMPTY_NAMESPACE or self.is_setting(namespace), namespace

        custom_processing: Dict[str, Callable[[], Any]] = {
            k: partial(v(None, self.env).populate_from_env, parent_namespace=namespace)
            for k, v in self.__annotations__.items()
            if isinstance(v, type) and issubclass(v, Config)
        }
        if target is empty:
            target = self
        for k, v in self.env.get_by_annotations(
            self,
            key_to_name=lambda key: "_".join(filter(None, (namespace, self.as_setting_name(key)))),
            name_is_setting=lambda name: bool(self.is_setting(name)),
            custom_processing=custom_processing,
        ):
            setattr(target, k, v)
        return target

    @classmethod
    def get_dotenv(cls):
        """Creates and returns `cls.dotenv` using `cls.__info__`."""

        data: Dict[Type[Config], List[SettingInfo]] = {}
        for setting_info in cls.__info__.values():
            if setting_info.is_property:
                continue
            if setting_info.parent not in data:
                data[setting_info.parent] = []
            if isinstance(setting_info.annotation, type) and issubclass(setting_info.annotation, Config):
                for sub_si in setting_info.annotation.__info__.values():
                    if sub_si.is_property:
                        continue
                    assert not (isinstance(sub_si.annotation, type) and issubclass(sub_si.annotation, Config))
                    data[setting_info.parent].append(sub_si)
            else:
                data[setting_info.parent].append(setting_info)
        full_text = ""
        for parent, info_list in data.items():
            parsed = docs.parse(parent.__doc__ or "")
            text = (parsed.short_description or "").strip() or str(_Reserved(parent))
            if (parsed.long_description or "").strip():
                text = f"{text}\n{(parsed.long_description or '').strip()}"
            text = "\n".join(f"### {x}" for x in text.split("\n"))
            for setting_info in info_list:
                text = f"{text}\n{setting_info.dotenv}"
            full_text = f"{full_text}\n\n\n{text}" if full_text else text
        cls.dotenv = full_text
        return cls.dotenv

    @classmethod
    def is_setting(cls, name: str) -> bool:
        """Whether given name string is a valid setting name."""

        return bool(cls.name_pattern.match(name))

    @classmethod
    def as_setting_name(cls, name: str) -> str:
        """Transforms given name to a setting name. Does not validate."""

        return name.upper()

    @classmethod
    def _get_reserved(cls) -> Dict[str, _Reserved]:
        reserved = {}
        for source in map(cls._Reserved, (*cls.__bases__[::-1], cls)):
            reserved.update({k: source for k in source.get_reserved(cls.as_setting_name, cls.is_setting)})
        return reserved

    @classmethod
    def _get_reviewable(cls, reserved: Dict[str, _Reserved]) -> Tuple[_Annotation, ...]:
        reviewable: Dict[str, _Annotation] = {}

        for base in (b for b in (*cls.__bases__[::-1], cls) if issubclass(b, Config)):

            for key, annotation in base.__annotations__.items():

                new = cls._Annotation(
                    key=key,
                    annotation=annotation,
                    source=base,
                    name=cls.as_setting_name(key),
                    property_name=as_property_name(cls.as_setting_name(key)),
                )

                if cls.is_setting(new.name):  # check anything that is a setting

                    if not new.immutable and new.name in reserved:
                        raise TypeError(f"{key} reserved by {reserved[new.name]}")

                    if new.name in reviewable and (reviewable[new.name].immutable or new.immutable):
                        if reviewable[new.name].annotation != new.annotation:
                            raise TypeError(f"\nIncompatible annotations:\n    {reviewable[new.name]}\n    {new}")

                    reviewable[new.name] = new

        return tuple(x for x in reviewable.values() if not x.immutable)

    @classmethod
    def _get_info(cls, reviewable: Tuple[_Annotation, ...]) -> Dict[str, SettingInfo]:

        info: Dict[str, SettingInfo] = {}
        for base in (b for b in cls.__bases__[::-1] if issubclass(b, Config)):
            info.update({k: v for k, v in base.__info__.items() if k in {obj.key for obj in reviewable}})

        doc_string = (cls.__doc__ or "")
        if "Attributes:  # noqa\n" in doc_string:
            start, _, end = doc_string.partition("Attributes:  # noqa\n")
            if not start.rpartition("\n")[2].strip():
                cls.__doc__ = doc_string = f"{start}Attributes:\n{end}"
        descriptions: Dict[str, str] = {
            x.arg_name: (x.description or "").strip()
            for x in docs.parse(doc_string).params
            if x.args[0] == "attribute"
        }

        for obj in reviewable:

            if obj.key in cls.__annotations__ and obj.key not in descriptions:
                if not isinstance(getattr(cls, obj.property_name, None), property):
                    warnings.warn(f"{cls.__module__}.{cls.__qualname__} missing attribute {obj.key} from __doc__")

            description = descriptions.get(obj.key, "")
            parent = cls
            if obj.key in info:
                if not description:
                    description = info[obj.key].description
                parent = info[obj.key].parent

            info[obj.key] = SettingInfo(
                key=obj.key,
                annotation=obj.annotation,
                parent=parent,
                owner=cls,
                description=description,
                default=getattr(cls, obj.key, empty),
            )

        return info

    def __init_subclass__(cls, *, namespace: str = "", **kwargs):
        if namespace or namespace is EMPTY_NAMESPACE:
            cls.namespace = namespace
        if cls.namespace:
            assert cls.is_setting(cls.namespace), cls.namespace

        super().__init_subclass__(**kwargs)  # type: ignore

        if "__info__" in cls.__dict__:  # coverage: exclude
            raise TypeError("do not define autogenerated class attribute __info__")
        if "__doc__" not in cls.__dict__:  # coverage: exclude
            cls.__doc__ = ""
        if "__annotations__" not in cls.__dict__:
            cls.__annotations__ = {}

        reserved = cls._get_reserved()
        reviewable = cls._get_reviewable(reserved)
        info = cls._get_info(reviewable)

        cls.__reserved__ = frozenset(reserved)
        cls.__annotations__ = {obj.key: obj.annotation for obj in reviewable}
        cls.__info__ = MappingProxyType(info)
        cls.get_dotenv()

    _Reserved = _Reserved
    _Annotation = _Annotation


_TConfig = TypeVar("_TConfig", bound=Type[Config])
