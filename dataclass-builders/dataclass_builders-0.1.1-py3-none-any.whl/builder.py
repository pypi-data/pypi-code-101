from dataclasses import dataclass, fields, Field, MISSING
from functools import partial
from typing import Any, Dict, get_args, get_origin, Union, List


class Builder:

    def __init__(self, target: dataclass, **kwargs: Any) -> None:
        self.target = target
        self._kwargs = kwargs
        for field in self.fields:
            self._prepare_field(field.name)

    @property
    def fields(self) -> List[Field]:
        return fields(self.target)

    def build(self, **kwargs: Any) -> dataclass:
        constructor_args = self._prepare_args(**kwargs)
        return self.target(**constructor_args)

    def _prepare_field(self, field_name: str) -> None:
        setattr(self, field_name, self._kwargs[field_name] if field_name in self._kwargs else None)
        setattr(self, f"with_{field_name}", partial(self._set, field_name=field_name))

    def _set(self, value: Any, field_name: str) -> 'Builder':
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
