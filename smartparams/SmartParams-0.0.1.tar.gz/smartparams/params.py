import argparse
import inspect
import json
import os
import re
from pathlib import Path
from pydoc import locate
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Tuple, Union, get_origin

import yaml


class Params(dict):
    OBJECT_NAME = '~name'

    LINK_NAME = '@link'
    LINK_ATTRIBUTE = 'attribute'
    LINK_IS_CALLABLE = 'is_callable'

    ENV_SEPARATOR = ':'
    ENV_PATTERN = re.compile(r'.*?\${(.*?)}.*?')

    def __init__(self, *args, **kwargs) -> None:
        super(Params, self).__init__()
        self._root: Optional[Params] = None
        self._allow_imports: bool = False
        self._function: Optional[Callable] = None
        self._evaluated: Set[str] = set()
        self._objects: Optional[Dict[str, Any]] = None
        self._casters: Dict[str, Callable] = dict()
        self.update(*args, _force=True, **kwargs)

    @property
    def root(self) -> 'Params':
        if self._root is None:
            return self
        return self._root.root

    @property
    def objects(self) -> Dict[str, Any]:
        if self.root._objects is None:
            self.root._objects = {self.LINK_NAME: self._link}
        return self.root._objects

    @property
    def allow_imports(self) -> bool:
        return self.root._allow_imports

    def set_allow_imports(self, allow_imports: bool = False) -> 'Params':
        self._allow_imports = allow_imports
        return self

    def register(self, name: str, obj: Callable) -> None:
        self.objects[name] = obj

    def child(self, *args, **kwargs) -> 'Params':
        child = Params(*args, **kwargs)
        child._root = self.root
        return child

    def is_object(self) -> bool:
        return self.OBJECT_NAME in self

    def parse_object(self) -> Tuple[Callable, Tuple[Any, ...], 'Params']:
        kwargs = self.copy()
        name = kwargs.pop(self.OBJECT_NAME)
        args = tuple(kwargs.pop(key) for key in sorted(kwargs) if str(key).isdecimal())

        if name in self.objects:
            obj = self.objects[name]
        elif self.allow_imports:
            obj = locate(name)
        else:
            raise ValueError(f"Object {name} is not registered")

        return obj, args, kwargs

    def cast(self, key: str, func: Callable) -> None:
        key, sub_key = self._parse_key(key)
        if sub_key:
            if key not in self:
                super().__setitem__(key, self.child())
            obj = super().__getitem__(key)
            if not isinstance(obj, Params):
                raise ValueError(f"Source link '{key}' must be a dict")
            obj.cast(sub_key, func)
        else:
            self._casters[key] = func

    def link(
        self,
        src_key: str,
        dst_key: str,
        attribute: Optional[str] = None,
        is_callable: bool = True,
    ) -> None:
        self[dst_key] = {
            self.OBJECT_NAME: src_key,
            self.LINK_ATTRIBUTE: attribute,
            self.LINK_IS_CALLABLE: is_callable,
        }

    def _link(self, key: str, attribute: Optional[str] = None, is_callable: bool = True) -> None:
        param = self.root[key]
        if attribute is not None:
            attr = getattr(param, attribute)
            if is_callable:
                return attr()
            return attr
        return param

    def _getter(self, obj: Any, cast: Optional[Callable] = None) -> Any:
        if isinstance(obj, Params):
            if obj.is_object():
                func, args, kwargs = obj.parse_object()
                if cast is not None:
                    return cast(func)(*args, **kwargs)
                return func(*args, **kwargs)
            else:
                return dict(**obj)
        if isinstance(obj, dict):
            return {k: self._getter(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._getter(o) for o in obj]
        if isinstance(obj, set):
            return set(self._getter(o) for o in obj)
        if isinstance(obj, tuple):
            return tuple(self._getter(o) for o in obj)
        if cast is not None:
            return cast(obj)
        return obj

    def _setter(self, obj: Any) -> Any:
        if isinstance(obj, dict):
            return self.child(**obj)
        elif isinstance(obj, list):
            return [self._setter(o) for o in obj]
        elif isinstance(obj, set):
            return set(self._setter(o) for o in obj)
        elif isinstance(obj, tuple):
            return tuple(self._setter(o) for o in obj)
        elif isinstance(obj, str):
            for group in self.ENV_PATTERN.findall(obj):
                key, _, default = str(group).partition(self.ENV_SEPARATOR)
                obj = obj.replace(f"${{{group}}}", os.getenv(key, default=default))
        return obj

    @staticmethod
    def _parse_key(key: str) -> Tuple[str, str]:
        if not key:
            raise KeyError("Key cannot be empty")
        key, _, sub_key = str(key).strip('.').partition('.')
        return key, sub_key

    def __getitem__(self, key: str) -> Any:
        key, sub_key = self._parse_key(key)
        obj = super().__getitem__(key)
        if sub_key:
            return obj[sub_key]
        if key in self._evaluated:
            return obj
        value = self._getter(obj, cast=self._casters.get(key))
        super().__setitem__(key, value)
        self._evaluated.add(key)
        return value

    def __setitem__(self, key: str, value: Any) -> None:
        key, sub_key = self._parse_key(key)
        if sub_key:
            if key not in self:
                super().__setitem__(key, self.child())
            super().__getitem__(key)[sub_key] = value
        else:
            super().__setitem__(key, self._setter(value))

    def __iter__(self) -> Iterator[Any]:
        yield from super(Params, self).__iter__()

    def update(self, *args, _force: bool = False, **kwargs) -> None:
        if _force:
            for k, v in dict(*args, **kwargs).items():
                self[k] = v
        else:
            for k, v in Params(*args, **kwargs).flatten().items():
                self[k] = v

    def flatten_keys(self) -> List[str]:
        flatten_keys = list()
        for key in self.keys():
            value = super().__getitem__(key)
            if isinstance(value, Params):
                for sub_key in value.flatten_keys():
                    flatten_keys.append(f'{key}.{sub_key}')
            else:
                flatten_keys.append(key)
        return flatten_keys

    def flatten(self) -> Dict[str, Any]:
        return {k: self[k] for k in self.flatten_keys()}

    def copy(self) -> 'Params':
        return Params(**super(Params, self).copy())

    def wrap(self, func: Callable) -> Callable:
        self._function = func
        return func

    def run(
        self,
        path: Path,
        dump: bool = False,
        skip_defaults: bool = False,
        allow_imports: bool = False,
    ) -> Any:
        self.set_allow_imports(allow_imports)

        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=Path, required=path is None or path.is_dir())
        parser.add_argument('--dump', default=dump, action='store_true')
        parser.add_argument('--skip-defaults', default=skip_defaults, action='store_true')
        args = parser.parse_args()

        if args.path:
            if path is None or not path.is_dir():
                path = args.path
            else:
                path = path.joinpath(args.path)

        if not path.is_file():
            raise ValueError("Path must be a file")

        if args.dump:
            representation = self.dump(self._function, skip_defaults=args.skip_defaults)
            with path.open('w') as file:
                if path.suffix in ('.yaml', '.yml'):
                    yaml.safe_dump(representation, file, sort_keys=False)
                elif path.suffix == '.json':
                    json.dump(representation, file)
                else:
                    raise ValueError(f"Unsupported file extension {path.suffix}")

            print('Params: \n - ' + '\n - '.join(Params(representation).flatten_keys()))
        else:
            with path.open() as file:
                if path.suffix in ('.yaml', '.yml'):
                    self.update(**yaml.safe_load(file))
                elif path.suffix == '.json':
                    self.update(**json.load(file))
                else:
                    raise ValueError(f"Unsupported file extension {path.suffix}")

            if self._function is not None:
                _kwargs = self.copy()
                _args = tuple(_kwargs.pop(key) for key in sorted(_kwargs) if str(key).isdecimal())
                return self._function(*_args, **_kwargs)

    def dump(self, obj: Any, skip_defaults: bool = False) -> Dict[str, Any]:
        representation: Dict[str, Any] = dict()

        is_class = inspect.isclass(obj)
        if is_class:
            obj = getattr(obj, '__init__')

        signature = inspect.signature(obj)

        params = iter(signature.parameters.values())
        if is_class:
            next(params)

        for i, param in enumerate(params):
            if param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
                continue

            default: Any

            annotation = param.annotation
            registered = annotation in self.objects.values()
            if (
                annotation is not inspect.Parameter.empty
                and get_origin(annotation) is not Union
                and (self.allow_imports or registered)
            ):
                if registered:
                    reversed_objects = {v: k for k, v in self.objects.items()}
                    default = {self.OBJECT_NAME: reversed_objects[annotation]}
                else:
                    default = {self.OBJECT_NAME: inspect.formatannotation(annotation)}
                default.update(self.dump(annotation, skip_defaults=skip_defaults))
            elif param.default is inspect.Parameter.empty:
                default = '?'
            elif skip_defaults:
                continue
            else:
                default = param.default

            if param.kind == inspect.Parameter.POSITIONAL_ONLY:
                representation[str(i)] = default
            else:
                representation[param.name] = default

        return representation
