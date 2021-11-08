import abc
from typing import Iterator, NamedTuple, Iterable, Type

from hcube.api.models.cube import Cube
from hcube.api.models.query import CubeQuery


class CubeBackend(abc.ABC):
    @abc.abstractmethod
    def get_records(self, query: CubeQuery) -> Iterator[NamedTuple]:
        """
        Takes a `CubeQuery` instance and returns the resulting records
        """

    @abc.abstractmethod
    def store_records(self, cube: Type[Cube], records: Iterable[NamedTuple]):
        """
        Stores `records` for `cube` in the backing storage
        """

    @abc.abstractmethod
    def delete_records(self, query: CubeQuery) -> None:
        """
        Takes a `CubeQuery` instance and removes all matching records
        """
