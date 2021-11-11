import abc
import dataclasses
from typing import Any
from typing import Union


@dataclasses.dataclass(eq=False)
class AbstractModel(abc.ABC):
    """Any database model.

    Any inheriting dataclass should use `eq=False`.

    """

    @property
    @abc.abstractmethod
    def _key(self) -> Union[Any, tuple[Any]]:
        """Return a ``tuple`` of attributes.

        These are used in the ``__eq__`` and ``__hash__`` methods.

        """
        return NotImplementedError

    @property
    @abc.abstractmethod
    def identifier(self) -> dict[str, Any]:
        """Return an identifier representing one or multiple database keys."""

    def __eq__(self, other) -> bool:
        """Compare ``_key``s."""
        if isinstance(other, self.__class__):
            return self._key == other._key
        return NotImplemented

    def __hash__(self) -> int:
        """Create hash from ``_key``."""
        return hash(self._key)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return dataclasses.asdict(self)
