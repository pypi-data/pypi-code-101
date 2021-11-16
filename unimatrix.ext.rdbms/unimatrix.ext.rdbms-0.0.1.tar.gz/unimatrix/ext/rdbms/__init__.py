# pylint: skip-file
from .connectionmanager import connections
from .connection import Connection
from .connectionmanager import ConnectionManager
from .declarative import declarative_base
from .repository import Repository


__all__ = [
    'Connection',
    'ConnectionManager',
    'Repository',
    'connect',
    'declarative_base',
    'disconnect',
]


async def connect() -> None:
    """Connect all database connections that are specified in the default
    connection manager.
    """
    return await connections.connect()


async def disconnect() -> None:
    """Disconnect all database connections that are specified in the default
    connection manager.
    """
    return await connections.disconnect()


def get(name: str) -> Connection:
    """Return the named connection `name`."""
    return connections.get(name)
