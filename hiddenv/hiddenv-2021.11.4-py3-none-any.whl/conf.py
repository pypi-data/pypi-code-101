"""Settings and configuration for any project.

Attributes:
    settings:
        Project setting object, see class `.Setting`.
        Also matches `django.conf.settings` (if `Django` is installed).
    ENVIRONMENT_VARIABLE: environment variable for settings source module path, = "HIDDENV_SETTINGS_MODULE"
    SETTINGS_MODULE_PATH: path to set for `.settings` in `sys.modules`
    APP_NAME_SETTING: settings source module attribute to set as `.settings.app`, = "HIDDENV_APP_NAME"
"""

import importlib
import os
import sys
import warnings
from contextlib import suppress
from types import ModuleType
from typing import (
    AbstractSet,
    Any,
    Callable,
    ClassVar,
    Dict,
    Final,
    Optional,
    TypeVar,
    final,
)

import docstring_parser as docs

from hiddenv.config import Config, KwargsCallable, SettingInfo, load
from hiddenv.environment import Env, empty


with suppress(ImportError):  # yapf: disable
    import django.conf
    import django.utils.functional


ENVIRONMENT_VARIABLE: Final = "HIDDENV_SETTINGS_MODULE"
SETTINGS_MODULE_PATH: Final = "hiddenv.conf.settings"
APP_NAME_SETTING: Final = "HIDDENV_APP_NAME"

_T = TypeVar("_T")


@final
class Settings(ModuleType):
    """A proxy for global project/hiddenv settings.

    Uses module specified by the "HIDDENV_SETTINGS_MODULE" environment variable as `.__source`.
    If `Django` is installed, falls back to "DJANGO_SETTINGS_MODULE" environment variable.

    Only utilizes valid setting names, see `.name_pattern`:
        - starts with uppercase ascii letter
        - continues with any amount of digits and uppercase ascii letters, with max. two underscores between

    Setup is triggered by attempting to retrieve a setting (attribute).
        - populates `.__source` by `.__source.__annotations__` and Config classes found in `.__source.__include__`
        - reads and caches values from `.__source`
    """

    main: ClassVar["Settings"]
    name_pattern = Config.name_pattern  # regex pattern for valid setting name

    @property
    def configured(self) -> bool:
        """Whether settings have been configured or not."""

        return self.__configured is not None

    @property
    def app(self) -> Optional[str]:
        """App name, primarily for django-related Config subclass usage."""

        return getattr(self.__source, APP_NAME_SETTING, None)

    @property
    def env(self) -> Env:
        """Env to use for loading environment variables."""

        if self.__env is None:
            self.__env: Env = Env.get_default()
        return self.__env

    @env.setter
    def env(self, __env: Env):
        self.__env = __env

    @property
    def dotenv(self) -> str:
        """Textual .env file representation of settings for current `.__source`."""

        return self.__getattr__("dotenv")

    def __init__(self, name=SETTINGS_MODULE_PATH, doc=None, main=False):
        assert name not in sys.modules
        kwargs = {} if doc is None else dict(doc=doc)
        super().__init__(name, **kwargs)
        sys.modules[name] = self

        self.__django: Optional["django.conf.LazySettings"] = None
        self.__env: Optional[Env] = None
        self.__configured: Optional[AbstractSet[str]] = None
        self.__source: Any = None
        self.__source_location: Optional[str] = None
        self.__dotenv: Optional[str] = None
        if main:
            self.__class__.main = self
        self._reset()

    @classmethod
    def is_setting(cls, name: str) -> bool:
        """Whether given name string is a valid setting name."""

        return bool(cls.name_pattern.match(name))

    def load(self, __call: KwargsCallable[_T], **overrides) -> _T:
        """Returns result of given kwargs callable.

        Populates call parameters using overrides and these settings.
        """

        return load(__call, lambda key: getattr(self, key.upper()), **overrides)

    def _reset(self):
        for name in (self.__configured or ()):
            self.__delattr__(name)
        self.__django = None
        self.__source = None
        self.__configured = None
        self.__source_location = os.environ.get(ENVIRONMENT_VARIABLE)
        if self.__class__.main is self:
            try:
                _source_location = os.environ.get(django.conf.ENVIRONMENT_VARIABLE)
            except NameError:
                return
            if not self.__source_location and _source_location and _source_location != self.__name__:
                self.__source_location = os.environ[ENVIRONMENT_VARIABLE] = _source_location
            os.environ[django.conf.ENVIRONMENT_VARIABLE] = self.__name__
            self.__django = django.conf.settings

    def _setup(self, *, _from_dir=False):
        if self.configured:
            raise ValueError("Already configured.")

        self._reset()

        assert self.dotenv is not None
        if not self.__source_location:
            raise LookupError(f"Environment variable {ENVIRONMENT_VARIABLE} not set.")

        self.__source = importlib.import_module(self.__source_location)

        if hasattr(self.__source, "__include__"):
            include = getattr(self.__source, "__include__")
            for cls in ((include, ) if isinstance(include, type) else include):
                cls(None, self.env, self.app).populate_from_env(target=self.__source)

        custom_processing: Dict[str, Callable[[], Config]] = {
            k: v(None, self.env).populate_from_env
            for k, v in getattr(self.__source, "__annotations__", {}).items()
            if isinstance(v, type) and issubclass(v, Config)
        }
        for k, v in self.env.get_by_annotations(
            obj=self.__source,
            name_is_setting=self.is_setting,
            custom_processing=custom_processing,
        ):
            setattr(self.__source, k, v)
        configured = []
        for name in dir(self.__source):
            if self.is_setting(name):
                self.__dict__[name] = getattr(self.__source, name)
                configured.append(name)
        self.__configured = frozenset(configured)
        if not _from_dir and self.__django and self.__django.configured:
            if [*self.__django.__dict__] != ["_wrapped"]:
                warnings.warn("django settings configured before hiddenv; resetting django settings")
            self.__django._wrapped = django.utils.functional.empty  # pylint: disable = protected-access

    def __dir__(self):
        if not self.configured:
            self._setup(_from_dir=True)
        return super().__dir__()

    def _make_dotenv(self):
        assert not self.configured

        source_location = os.environ.get(ENVIRONMENT_VARIABLE)
        try:
            if not source_location and os.environ.get(django.conf.ENVIRONMENT_VARIABLE) != SETTINGS_MODULE_PATH:
                source_location = os.environ[django.conf.ENVIRONMENT_VARIABLE]
        except NameError:
            pass
        if not source_location:
            raise LookupError(f"Environment variable {ENVIRONMENT_VARIABLE} not set.")
        source = importlib.import_module(source_location)

        texts = []

        if hasattr(source, "__include__"):
            include = getattr(source, "__include__")
            for cls in ((include, ) if isinstance(include, type) else include):
                texts.append(cls.get_dotenv())

        was_larger_thingy = True
        descriptions = {
            x.arg_name: (x.description or "").strip()
            for x in docs.parse(source.__doc__ or "").params
            if x.args[0] == "attribute"
        }

        parsed = docs.parse(source.__doc__ or "")
        description = (parsed.short_description or "").strip() or f"local module settings ({source.__name__})"
        if (parsed.long_description or "").strip():
            description = f"{description}\n{(parsed.long_description or '').strip()}"
        description = "\n".join(f"### {x}" for x in description.split("\n"))

        for k, ann in getattr(source, "__annotations__", {}).items():
            if not self.is_setting(k):
                continue
            if isinstance(ann, type) and issubclass(ann, Config):
                texts.append(ann.get_dotenv())
                was_larger_thingy = True
            else:
                setting_info = SettingInfo(
                    key=k,
                    annotation=ann,
                    description=descriptions.get(k, "").strip(),
                    parent=Config,
                    owner=Config,
                    default=getattr(source, k, empty),
                )
                text = setting_info.dotenv
                if was_larger_thingy:
                    texts.append(f"{description}\n{text}")
                else:
                    texts[-1] = f"{texts[-1]}\n{text}"
                was_larger_thingy = False
        return "\n\n\n".join(texts)

    def __getattr__(self, name: str) -> Any:
        if name == "dotenv":
            if self.__dotenv is None:
                self.__dotenv = self._make_dotenv()
            return self.__dotenv
        if not self.is_setting(name):
            raise AttributeError(f"{name!r} is not a valid setting name")
        if not self.configured:
            self._setup()
            return self.__getattr__(name)
        if not hasattr(self.__source, name):
            raise AttributeError(f"module {self.__name__!r} has no attribute {name!r}")
        return self.__getattribute__(name)

    def __setattr__(self, name: str, value: Any):
        if hasattr(self.__class__, name) and name != "env":
            raise AttributeError(f"Can't set class attribute {name!r} on {self.__class__.__name__} object")
        super().__setattr__(name, value)
        if name.startswith("_Settings__"):
            return
        # account for django cache
        if self.__django is not None and self.__class__.main is self:
            self.__django.__dict__[name] = value

    def __delattr__(self, name: str):
        super().__delattr__(name)
        assert not name.startswith("_Settings__"), name
        # account for django cache
        if self.__django is not None and self.__class__.main is self:
            self.__django.__dict__.pop(name, None)


settings: Final = Settings(main=True)
