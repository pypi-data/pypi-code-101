from typing import Dict, List, Optional, Type

from cfp.exceptions import NoResolverError
from cfp.resolver_factories import (
    AnyResolverFactory,
    ParameterStoreResolverFactory,
    StringResolverFactory,
)
from cfp.resolvers import AnyResolver
from cfp.sources import AnySource
from cfp.types import ApiParameter, StackParameterKey

Factories = Dict[Type[AnyResolverFactory], Optional[AnyResolverFactory]]


class StackParameters:
    """
    Builds a list of CloudFormation stack parameters.

    Arguments:
        default_resolvers: Register the default resolvers
    """

    def __init__(self, default_resolvers: bool = True) -> None:
        self._factories: Factories = {}
        """Factory types and lazy-loaded instances."""

        self._resolvers: List[AnyResolver] = []
        """Resolvers instantiated for this session."""

        if default_resolvers:
            self.register_resolver(StringResolverFactory)
            self.register_resolver(ParameterStoreResolverFactory)

    def _find_factory(self, source: AnySource) -> Type[AnyResolverFactory]:
        for factory_type in self._factories:
            if factory_type.can_resolve(source):
                return factory_type
        raise NoResolverError(source)

    def _get_factory(self, t: Type[AnyResolverFactory]) -> AnyResolverFactory:
        if existing := self._factories.get(t, None):
            return existing

        f = t()
        self._factories[t] = f
        return f

    def add(self, key: StackParameterKey, source: AnySource) -> None:
        """
        Adds a new stack parameter with direction for finding the value.

        Arguments:
            key:    Stack parameter key
            source: Value source
        """

        factory_type = self._find_factory(source)
        factory = self._get_factory(factory_type)
        resolver = factory.try_make(source)
        resolver.queue(key=key, source=source)
        if resolver not in self._resolvers:
            self._resolvers.append(resolver)

    @property
    def api(self) -> List[ApiParameter]:
        """
        Gets the resolved parameters as a list ready to pass directly to
        CloudFormation.

        Example:

            .. code-block:: python

                from cfp import StackParameters
                from boto3.session import Session

                sp = StackParameters()
                sp.add("ParameterA", "Value A")
                sp.add("ParameterB", "Value B")

                client = session.client("cloudformation")
                client.create_change_set(
                    StackName="MyStack",
                    ChangeSetName="MyChangeSet",
                    ChangeSetType="UPDATE,
                    Parameters=sp.api,
                    TemplateBody="...",
                )

        """

        cf_params: List[ApiParameter] = []

        for resolver in self._resolvers:
            for cf_param in resolver.resolve():
                cf_params.append(cf_param)

        return cf_params

    def register_resolver(self, factory: Type[AnyResolverFactory]) -> None:
        """
        Registers a resolver factory.

        Arguments:
            factory: Factory type
        """

        self._factories[factory] = None
