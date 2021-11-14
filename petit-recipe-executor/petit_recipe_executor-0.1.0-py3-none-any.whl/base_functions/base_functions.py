from typing import Any


def contains(input: str, inside: str) -> bool:
    return inside in input


def pick(input: dict, key: str) -> Any:
    return input.__getattribute__(key)


def equal(a: Any, b: Any):
    return a == b

def not_equal(a: Any, b: Any):
    return a != b

