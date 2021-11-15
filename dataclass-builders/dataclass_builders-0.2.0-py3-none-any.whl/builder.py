from dataclasses import fields, Field, MISSING, is_dataclass
from functools import partial
from typing import Any, Dict, get_args, get_origin, Union, List, Optional, Set, TypeVar


TargetDataclass = TypeVar('TargetDataclass')


class Builder:
    """@DynamicAttrs"""
    NEWLINE = '\n'

    def __init__(self, target: TargetDataclass, **kwargs: Any) -> None:
        if is_dataclass(target):
            self.target = target
        else:
            raise ValueError(f"{self.target.__name__} is not a dataclass!")
        self._kwargs = kwargs
        self._dir = self.field_names
        for field in self.fields:
            self._prepare_field(field.name)

    def __contains__(self, item: str) -> bool:
        return item in self.field_names

    def __getitem__(self, item: str) -> Optional[Any]:
        return getattr(self, item)

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self:
            setattr(self, key, value)
        else:
            raise AttributeError(
                f"Target class, {self.target.__name__}, has no field: {key}\n"
                f"Available fields:\n {self.NEWLINE.join(self.field_names)}"
            )

    def __dir__(self) -> List[str]:
        return list(self._dir)

    @property
    def fields(self) -> List[Field]:
        return fields(self.target)

    @property
    def field_names(self) -> Set[str]:
        return {field.name for field in self.fields}

    def build(self, **kwargs: Any) -> TargetDataclass:
        constructor_args = self._prepare_args(**kwargs)
        return self.target(**constructor_args)

    def _prepare_field(self, field_name: str) -> None:
        setattr(self, field_name, self._kwargs[field_name] if field_name in self._kwargs else None)
        setter = f"with_{field_name}"
        setattr(self, setter, partial(self._with, field_name=field_name))
        self._dir.add(setter)

    def _with(self, value: Any, field_name: str) -> 'Builder':
        setattr(self, field_name, value)
        return self

    def _prepare_args(self, **kwargs: Any) -> Dict[str, Any]:
        return {
            field.name: self._assign_value(field, **kwargs)
            for field in self.fields
        }

    def _assign_value(self, field: Field, **kwargs: Any) -> Any:
        if field.name in kwargs:
            return kwargs[field.name]
        elif getattr(self, field.name) is not None:
            return getattr(self, field.name)
        elif field.default is not MISSING:
            return field.default
        elif self._is_optional(field):
            return None
        else:
            raise ValueError(f"Required field [{field.name}] not assigned!")

    @staticmethod
    def _is_optional(field: Field) -> bool:
        origin = get_origin(field.type)
        args = get_args(field.type)
        return origin is Union and type(None) in args
