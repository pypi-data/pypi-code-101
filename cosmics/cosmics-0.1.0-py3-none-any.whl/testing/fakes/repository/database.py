from typing import Optional

from cosmics.repository import database


class FakeClient(database.AbstractClient):
    def __init__(self, contains: list[dict]):
        self.contains = contains

    def __del__(self):
        pass

    def _insert(self, target: str, data: database.Info) -> None:
        self.contains.append(data)

    def _select(
        self,
        target: str,
        where: Optional[database.Info],
    ) -> list[database.Info]:
        if where is None:
            return self.contains
        return [d for d in self.contains if _all_values_match(d, where)]

    def _update(
        self,
        target: str,
        data: database.Info,
        where: database.Info,
    ) -> None:
        self.contains = [
            d if not _all_values_match(d, where) else _update_dict(d, data)
            for d in self.contains
        ]

    def _delete(self, target: str, where: database.Info, force: bool) -> None:
        self.contains = [d for d in self.contains if not _all_values_match(d, where)]


def _all_values_match(left: dict, right: dict) -> bool:
    return all(left[k] == v for k, v in right.items())


def _update_dict(target: dict, updates: dict) -> dict:
    for k, v in updates.items():
        if k in target:
            target[k] = v
    return target
