"""Config classes to be used alone or a predefined parts for `hiddenv.settings` source module `.__include__`."""

import inspect
import re
import textwrap
import warnings
from contextlib import suppress
from dataclasses import dataclass
from functools import partial
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    ClassVar,
    Collection,
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

from hiddenv.environment import (
    Env,
    NotAnnotated,
    NotNull,
    as_property_name,
    empty,
    validate_setting_value,
)


_Tco = TypeVar("_Tco", covariant=True)


class KwargsCallable(Protocol[_Tco]):  # pylint: disable = too-few-public-methods
    """Protocol for keyword-only parameters callable, e.g. a NamedTuple class."""

    def __call__(self, **kwargs) -> _Tco:
        ...


@dataclass(frozen=True)
class _Info:
    key: str
    annotation: Any
    owner: Type["Config"]

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
    def is_immutable(self):
        """Whether annotation is immutable (e.g. ClassVar) or not."""

        annotation = get_origin(self.annotation) or self.annotation
        return annotation in (get_origin(ClassVar[str]), get_origin(Final[str]))


@dataclass(frozen=True)
class _AnnotationInfo(_Info):
    source: type


@dataclass(frozen=True)
class SettingInfo(_Info):
    """Metadata for a Config subclass' annotated setting."""

    parent: Type["Config"]
    description: str
    default: Any = empty

    @property
    def allow_null(self):
        """Whether None is allowed as a value."""

        return self.default is None or self.is_property

    @property
    def attr_ann(self):
        """Attribute annotation for this setting."""

        assert not self.is_immutable
        ann = NotAnnotated[self.annotation]
        if self.allow_null:
            ann = NotNull[self.annotation]
        assert get_origin(ann) is not Union, (self.key, self.annotation, ann)
        if self.is_property:
            assert isinstance(ann, type) or get_origin(ann) in (list, tuple, dict), (self.key, self.annotation, ann)
            return ann
        assert hasattr((get_origin(ann) or ann), "__name__"), (self.key, self.annotation, ann)
        env_call = getattr(Env, (get_origin(ann) or ann).__name__, None)
        process_name = f"_process_{self.property_name}"
        process_call = getattr(self.owner, process_name, None)
        if callable(env_call) or callable(process_call):
            return ann
        if isinstance(ann, type) and issubclass(ann, Config):
            return ann
        assert False, f"missing {process_name} for {self.key}: {inspect.formatannotation(self.annotation)}"

    @property
    def is_config(self):
        """Whether the attribute annotation is a Config subclass."""

        return isinstance(self.attr_ann, type) and issubclass(self.attr_ann, Config)

    @property
    def env_name(self):
        """Environment variable name."""

        if isinstance(self.annotation, type(Annotated[str, ""])) and isinstance(self.annotation.__metadata__[-1], str):
            return self.annotation.__metadata__[-1]
        return self.name

    @property
    def dotenv(self):
        """Textual .env representation of this setting."""

        if self.is_property:  # coverage: exclude
            raise ValueError(f"{_Reserved(self.owner)}.{self.key} is a property setting")

        name = self.env_name
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

    def __post_init__(self):
        assert self.is_immutable or self.attr_ann

    def __str__(self):
        text = f"{self.key}: {inspect.formatannotation(self.annotation)}"
        if self.default is not empty:
            text = f"{text} = {self.default!r}"
        description = self.description.strip().replace("\n", "\t")
        if description:
            text = f"{text}  # {description}"
        return text


EMPTY_NAMESPACE: Final[str] = type("CustomNamespace", (str, ), dict(__slots__=()))()


class _Reserved(NamedTuple):
    source: type

    @property
    def reserved(self):
        """All reserved names of `self.source`"""

        if issubclass(self.source, Config):
            if "__reserved__" in self.source.__dict__:
                return tuple(self.source.__reserved__)
            return tuple(
                k for k in {*self.source.__dict__}.difference(getattr(self.source, "__annotations__", {}))
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


_T = TypeVar("_T")


def load(__call: KwargsCallable[_T], __get: Callable[[str], Any], **overrides) -> _T:
    """Returns result of given kwargs callable.

    Populates call parameters using overrides and the __get callable.
    """

    for key in frozenset(inspect.signature(__call).parameters).difference(overrides):
        with suppress(AttributeError):
            overrides[key] = __get(key)
    return __call(**overrides)


def _get_doc(cls, target, descriptions):
    if descriptions is not None:
        descriptions = dict(descriptions)
        descriptions.setdefault(None, "")
    else:
        descriptions = {}
        parsed = docs.parse(getattr(target, "__doc__", None) or "")
        descriptions[None] = (parsed.short_description or "").strip()
        if parsed.long_description:  # coverage: exclude
            descriptions[None] = f"{descriptions[None]}\n\n{parsed.long_description.strip()}"
        for param in parsed.params:
            descriptions[cls.as_setting_name(param.arg_name)] = param.description or ""
    parts = [f"{textwrap.dedent(descriptions.pop(None).rstrip())}\n"]
    if descriptions:
        parts.append("Attributes:")
    for k, v in descriptions.items():
        parts.append(f"    {k}:\n{textwrap.indent(textwrap.dedent(v).rstrip(), ' ' * 8)}")
    return "\n".join(parts).rstrip()


def _get_attributes_from_target(cls, target, exclude, raise_error) -> Dict[str, Union[Type, Tuple[Type, Any]]]:

    skip = f"while extending {cls.__module__}.{cls.__qualname__} for {target!r}, skipping parameter {{}}: {{}}"

    existing: Dict[str, Any] = {cls.as_setting_name(k): ann for k, ann in cls.__annotations__.items()}

    attributes: Dict[str, Union[Type, Tuple[Type, Any]]] = {}

    for parameter in (
        parameter for i, parameter in enumerate(inspect.signature(target).parameters.values())
        if i not in exclude and parameter.name not in exclude
    ):

        if parameter.kind in (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL):
            reason = skip.format(parameter.name, "variadic parameters not allowed")
            if raise_error:
                raise TypeError(reason)
            warnings.warn(reason)
            continue

        if parameter.annotation is inspect.Parameter.empty:
            reason = skip.format(parameter.name, "parameter missing annotation")
            if raise_error:
                raise TypeError(reason)
            warnings.warn(reason)
            continue

        name = cls.as_setting_name(parameter.name)
        if name in exclude:
            continue

        if not cls.is_setting(name):
            reason = skip.format(parameter.name, f"the generated setting name {name} is invalid")
            if raise_error:
                raise TypeError(reason)
            warnings.warn(reason)
            continue

        if name in existing and existing[name] != parameter.annotation:
            raise TypeError(
                skip.format(
                    parameter.name,
                    (
                        f"the annotation {inspect.formatannotation(parameter.annotation)} does not match "
                        f"old annotation {inspect.formatannotation(existing[name])}"
                    ),
                ),
            )

        if name in attributes:
            raise TypeError(skip.format(parameter.name, f"duplicate setting name {name}"))

        if parameter.default is not inspect.Parameter.empty:
            attributes[name] = (parameter.annotation, parameter.default)
        else:
            attributes[name] = parameter.annotation

    return attributes


class Config:
    """Settings class for use in specific cases (as opposed to project-wide) or as part of a source settings module.

    Attributes:  # noqa
        dotenv:
            Textual .env file representation of settings for this Config class, generated using `.__info__`
        name_pattern:
            regex pattern for valid setting (or namespace) name
        namespace:
            prefix to use when getting settings from environment variables

    Args:
        namespace:
            prefix to use when getting settings from environment variables;
            defaults to class namespace
        __env:
        __app: App name, primarily for django-related Config subclass usage.
        **attributes: additional annotations to use
    """

    __info__: ClassVar[Mapping[str, SettingInfo]] = MappingProxyType({})
    __reserved__: ClassVar[frozenset] = frozenset()  # reserved setting names, i.e. not available for annotating/usage
    dotenv: ClassVar[str] = ""
    namespace: ClassVar[str] = ""
    name_pattern: ClassVar[Pattern[str]] = re.compile(r"^[A-Z][A-Z0-9]*(__?[A-Z0-9]+)*$")

    @classmethod
    def extend(
        cls: "_TConfig",
        namespace: str = "",
        exclude: Collection[str] = (),
        doc: str = "",
        **attributes: Union[Type, Tuple[Type, Any]],
    ) -> "_TConfig":
        """Returns a subclass of this Config class.

        Args:
            doc: docstring/descriptions of new subclass
            exclude: names of existing setting attributes to exclude from new subclass
            namespace: namespace for the new subclass
            **attributes: new setting attributes, as annotation or (annotation, default) tuples
        """

        defaults = {}
        for k, v in attributes.items():
            if isinstance(v, tuple):
                attributes[k], defaults[k] = v  # pylint: disable = unnecessary-dict-index-lookup

        return type(  # type: ignore
            cls.__name__,
            (cls, ),
            {
                "__doc__": doc,
                "__annotations__": attributes,
                **defaults,
            },
            namespace=namespace,
            exclude=exclude,
        )

    @classmethod
    def extend_for(
        cls: "_TConfig",
        target: Callable,
        *,
        exclude: Collection[Union[int, str]] = (),
        namespace: str = "",
        descriptions: Dict[Optional[str], str] = None,
        raise_error=False,
    ) -> "_TConfig":
        """Returns a subclass update with setting attributes from given target's call signature.

        Args:
            target: callable to get additional setting parameters from
            exclude: positions or names of target parameters; and/or names of existing setting attributes to exclude
            namespace: namespace for the new subclass
            descriptions: new settings' descriptions; use None key for the new class description
            raise_error: whether to raise an error on invalid target parameters
        """

        return cls.extend(
            namespace=namespace,
            exclude=tuple(key for key in exclude if isinstance(key, str)),
            doc=_get_doc(cls, target, descriptions),
            **_get_attributes_from_target(cls, target, exclude, raise_error),
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

    def __new__(
        cls,
        namespace: Optional[str] = None,
        __env: Env = None,
        __app: str = None,
        **attributes: type,
    ):
        if attributes:
            for key, annotation in attributes.items():
                assert cls.is_setting(cls.as_setting_name(key)), (key, annotation)
            return type(  # type: ignore
                cls.__name__,
                (cls, ),
                {
                    "__annotations__": attributes,
                    "__doc__": {}
                },
            )(namespace, __env, __app)
        return super().__new__(cls)

    def __init__(  # pylint: disable = unused-argument
        self,
        namespace: Optional[str] = None,
        __env: Env = None,
        __app: str = None,
        **attributes: type,  # noqa: F841
    ):
        self.__attributes: Dict[str, SettingInfo] = {}
        self.__env = __env
        self.__app = __app
        self.__configured = False

        if namespace is not EMPTY_NAMESPACE:
            namespace = namespace or self.__class__.namespace
        if namespace is not EMPTY_NAMESPACE and not self.is_setting(namespace):
            raise ValueError(f"Invalid namespace {namespace!r}")
        self.__namespace = namespace

        for key, setting_info in self.__info__.items():
            assert self.is_setting(setting_info.name)  # should be ok from __init_subclass__
            assert not setting_info.is_immutable  # should be ok from __init_subclass__
            assert setting_info.name not in self.__attributes, (key, setting_info)
            self.__attributes[setting_info.name] = setting_info

    def _get(self, name):
        assert self.is_setting(name), name
        if self.__attributes[name].is_property:
            return super().__getattribute__(as_property_name(name))
        if self.__attributes[name].is_config:
            obj = self.__attributes[name].attr_ann(None, self.env)
            return obj.populate_from_env(parent_namespace=self.__namespace)
        env_name = "_".join(filter(None, (self.__namespace, self.__attributes[name].env_name)))
        (k, v), = self.env.get_by_annotations(
            self,
            key_to_name=lambda key: env_name if key == name else "",
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
        if not self.__configured:
            self.__configured = True
            self.populate_from_env()
        if setting_name not in self.__dict__:
            setattr(self, setting_name, self._get(setting_name))
        return super().__getattribute__(setting_name)

    def __setattr__(self, __name: str, __value: Any, *, no_validation=False) -> None:
        name = self.as_setting_name(__name)

        if not __name.startswith("_") and self.is_setting(name):
            assert no_validation or validate_setting_value(
                name=name,
                value=__value,
                annotation=self.__attributes[name].attr_ann,
                allow_null=self.__attributes[name].allow_null,
            )
            __name = name

        super().__setattr__(__name, __value)

    def load(self, __call: KwargsCallable[_T], **overrides) -> _T:
        """Returns result of given kwargs callable.

        Populates call parameters using overrides and this Config instance.
        """

        return load(__call, partial(getattr, self), **overrides)

    def populate_from_env(
        self,
        env: Env = None,
        parent_namespace: str = None,
        *,
        target: Any = None,
    ):
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
        set_attribute = partial(self.__setattr__, no_validation=True) if target is None else partial(setattr, target)
        for k, v in self.env.get_by_annotations(
            self,
            key_to_name=lambda key: "_".join(filter(None, (namespace, self.as_setting_name(key)))),
            name_is_setting=lambda name: bool(self.is_setting(name)),
            custom_processing=custom_processing,
        ):
            set_attribute(k, v)
        return self if target is None else target

    @classmethod
    def get_dotenv(cls, exclude=()):
        """Creates and returns `cls.dotenv` using `cls.__info__`."""

        data: Dict[Type[Config], List[SettingInfo]] = {}
        for setting_info in cls.__info__.values():
            if setting_info.is_property:
                continue
            if setting_info.parent not in data:
                data[setting_info.parent] = []
            if isinstance(setting_info.annotation, type) and issubclass(setting_info.annotation, Config):
                for sub_si in setting_info.annotation.__info__.values():
                    if sub_si.is_property or sub_si.name in exclude:
                        continue
                    assert not (isinstance(sub_si.annotation, type) and issubclass(sub_si.annotation, Config))
                    data[setting_info.parent].append(sub_si)
            else:
                if setting_info.name not in exclude:
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
        for source in map(_Reserved, (*cls.__bases__[::-1], cls)):
            reserved.update({k: source for k in source.get_reserved(cls.as_setting_name, cls.is_setting)})
        return reserved

    @classmethod
    def _get_reviewable(cls, reserved: Dict[str, _Reserved], exclude: Collection[str]) -> Tuple[_AnnotationInfo, ...]:
        reviewable: Dict[str, _AnnotationInfo] = {}

        for base in (b for b in (*cls.__bases__[::-1], cls) if issubclass(b, Config)):

            for key, annotation in base.__annotations__.items():

                if key in exclude:
                    continue

                new = _AnnotationInfo(
                    key=key,
                    annotation=annotation,
                    source=base,
                    owner=cls,
                )

                if cls.is_setting(new.name):  # check anything that is a setting

                    if not new.is_immutable and new.name in reserved:
                        raise TypeError(f"{key} reserved by {reserved[new.name]}")

                    if new.name in reviewable and (reviewable[new.name].is_immutable or new.is_immutable):
                        if reviewable[new.name].annotation != new.annotation:
                            raise TypeError(f"\nIncompatible annotations:\n    {reviewable[new.name]}\n    {new}")

                    reviewable[new.name] = new

        return tuple(x for x in reviewable.values() if not x.is_immutable)

    @classmethod
    def _get_info(cls, reviewable: Tuple[_AnnotationInfo, ...]) -> Dict[str, SettingInfo]:
        if "__info__" in cls.__dict__:  # coverage: exclude
            raise TypeError("do not define autogenerated class attribute __info__")

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

            default = cls.__dict__.get(obj.key, empty)
            if default is not empty:
                delattr(cls, obj.key)

            if obj.key in info:
                if not description:
                    description = info[obj.key].description
                if default is empty:
                    default = info[obj.key].default
                parent = info[obj.key].parent

            info[obj.key] = SettingInfo(
                key=obj.key,
                annotation=obj.annotation,
                parent=parent,
                owner=cls,
                description=description,
                default=default,
            )

        return info

    def __init_subclass__(cls, *, namespace: str = "", exclude: Tuple[str, ...] = (), **kwargs):
        if namespace is EMPTY_NAMESPACE:
            cls.namespace = namespace
        elif namespace:
            if not cls.is_setting(namespace):
                raise ValueError(f"Invalid namespace {namespace!r}")
            cls.namespace = namespace

        super().__init_subclass__(**kwargs)  # type: ignore

        if "__doc__" not in cls.__dict__:  # coverage: exclude
            cls.__doc__ = ""
        if "__annotations__" not in cls.__dict__:
            cls.__annotations__ = {}

        reserved = cls._get_reserved()
        reviewable = cls._get_reviewable(reserved, exclude)
        info = cls._get_info(reviewable)

        cls.__reserved__ = frozenset(reserved)
        cls.__annotations__ = {obj.key: obj.annotation for obj in reviewable}
        cls.__info__ = MappingProxyType(info)
        cls.get_dotenv()


Config.__new__.__doc__ = Config.__init__.__doc__ = Config.__doc__

_TConfig = TypeVar("_TConfig", bound=Type[Config])
