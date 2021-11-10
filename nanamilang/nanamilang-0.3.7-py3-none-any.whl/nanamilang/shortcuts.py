"""NanamiLang Shortcuts"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)


import string
import random
from typing import Any


def randstr(length: int = 10) -> str:
    """Return randomly generated string"""

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def ASSERT_NOT_EMPTY_STRING(s: str, m: str = '') -> None:
    """ASSERT_NOT_EMPTY_STRING(s) -> assertion with a message"""
    assert s, m or 'This string could not be empty'


def ASSERT_LIST_LENGTH_IS(c: list, l: int, m: str = '') -> None:
    """ASSERT_LIST_LENGTH_IS(c, l) -> assertion with a message"""
    assert len(c) == l, m or f'This list instance length must be {l}'


def ASSERT_LIST_LENGTH_IS_EVEN(c: list, m: str = '') -> None:
    """AASSERT_LIST_LENGTH_IS_EVEN(c) -> assertion with a message"""
    assert len(c) % 2 == 0, m or 'This list instance length must be even'


def ASSERT_NOT_EMPTY_COLLECTION(c: (list or dict), m: str = '') -> None:
    """ASSERT_NOT_EMPTY_COLLECTION(c) -> assertion with a message"""
    assert c, m or 'This collection instance could not be empty'


def ASSERT_HAS_KEY(v: dict, k: str, m: str = '') -> None:
    """ASSERT_HAS_KEY(v, k) -> assertion with a message"""
    assert v.get(k), m or f'This dictionary instance must have a "{k}" key'


def ASSERT_IN(v: Any, c: list, m: str = '') -> None:
    """ASSERT_IN(v, c) -> assertion with a message"""
    assert v in c, m or f'You have picked wrong key, choose from these: "{c}"'


def ASSERT_IS_INSTANCE_OF(v: Any, t: Any, m: str = '') -> None:
    """ASSERT_IS_INSTANCE_OF(v, t) -> assertion with a message"""
    assert isinstance(v, t), m or f'This instance must be a type of a "{t.__name__}"'


def UNTERMINATED_SYMBOL(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL(sym) -> message"""
    return m or f'Encountered an unterminated \'{sym}\' symbol'


def UNTERMINATED_SYMBOL_AT_EOF(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL_AT_EOF(sym) -> message"""
    return m or f'Encountered an unterminated symbol \'{sym}\' symbol at the end of file'
