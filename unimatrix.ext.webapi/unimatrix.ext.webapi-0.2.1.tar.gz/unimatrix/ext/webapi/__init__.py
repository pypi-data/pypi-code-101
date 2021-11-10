# pylint: skip-file
from .asgi import Application
from .decorators import action
from .exceptions import UpstreamServiceNotAvailable
from .exceptions import UpstreamConnectionFailure
from .keytrustpolicy import KeyTrustPolicy
from .resourceendpointset import ResourceEndpointSet
from .resourceendpointset import PublicResourceEndpointSet


__all__ = [
    'action',
    'Application',
    'ResourceEndpointSet',
    'PublicResourceEndpointSet',
    'UpstreamConnectionFailure',
    'UpstreamServiceNotAvailable',
]


def policy(tags: list) -> KeyTrustPolicy:
    """Declares a policy for an endpoint to determine which public keys
    it wants to trust.

    Args:
        tags (list): The list of tags that this policy accepts.

    Returns:
        A :class:`KeyTrustPolicy` instance.
    """
    return KeyTrustPolicy(tags)
