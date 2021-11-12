from abc import ABC, abstractmethod
from typing import Any, Union

from benchling_sdk.benchbots.benchling_store import Resource, Schema
from benchling_sdk.benchbots.types.manifest import (
    DropdownDependency,
    EntitySchemaDependency,
    NamedResourceDependency,
    SchemaDependency,
)
from benchling_sdk.models import DropdownOption, DropdownSummary


class DependencyResolver(ABC):
    @abstractmethod
    def resolve_resource_by_id_or_name(
        self,
        resource_dependency: NamedResourceDependency,
        initial_id_or_name: str,
    ) -> Resource:
        pass

    @abstractmethod
    def resolve_option_by_id_or_name(
        self,
        dropdown: DropdownSummary,
        initial_id_or_name: str,
        dependency_name: str,
    ) -> DropdownOption:
        pass

    @abstractmethod
    def resolve_schema_by_id_or_name(
        self,
        schema_dependency: Union[EntitySchemaDependency, SchemaDependency],
        initial_id_or_name: str,
    ) -> Schema:
        pass

    @abstractmethod
    def resolve_field_by_id_or_name(
        self,
        schema: Schema,
        initial_id_or_name: str,
        dependency_name: str,
    ) -> Any:
        pass

    @abstractmethod
    def resolve_dropdown_by_id_or_name(
        self,
        dropdown_dependency: DropdownDependency,
        initial_id_or_name: str,
    ) -> DropdownSummary:
        pass
