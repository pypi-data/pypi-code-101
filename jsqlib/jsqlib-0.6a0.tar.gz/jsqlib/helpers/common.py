""" This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Created on Aug 10, 2021

@author: pymancer@gmail.com (polyanalitika.ru)
"""
from __future__ import annotations

from re import sub as resub
from typing import Optional, Set, Dict
from dataclasses import dataclass, field
from functools import total_ordering
from jsqlib.helpers.constants import WRAP, DIALECTS, POSTGRESQL_DIALECT, NoneType
from jsqlib.helpers.types import SIBN_T


@total_ordering
@dataclass(frozen=True)
class Token:
    """Wrapped string or escaped wrapper."""

    lidx: int
    ridx: int
    value: str = field(default_factory=str)
    escaped: bool = False
    children: Set[Token] = field(default_factory=set)
    constants: Optional[Dict[str, SIBN_T]] = field(default_factory=dict)

    def __eq__(self, other: Token) -> bool:
        return self.lidx == other.lidx and self.ridx == other.ridx

    def __lt__(self, other: Token) -> bool:
        return self.ridx < other.ridx if self.ridx != other.ridx else self.lidx > other.lidx

    def __contains__(self, other: Token) -> bool:
        return other.lidx >= self.lidx and other.ridx <= self.ridx

    def __str__(self):
        merged = list()
        left_escaped = False
        right_escaped = False

        current = self
        for idx, c in enumerate(self.value):
            shifted = idx + self.lidx
            inherited = False

            for t in self.children:
                if t.lidx <= shifted < t.ridx:
                    inherited = True

                    if t != current:
                        merged.append(str(t))
                    current = t

                if t.escaped:
                    if t.lidx == self.lidx:
                        left_escaped = True
                    if t.ridx == self.ridx:
                        right_escaped = True

            if not inherited:
                merged.append(c)

        requoted = ''.join(merged)
        if not (left_escaped and right_escaped):
            # dquote only if token has no escaped border tokens
            requoted = requote(requoted, constants=self.constants)
        return requoted
        # return requote(''.join(merged), constants=self.constants)

    def __hash__(self):
        return hash((self.lidx, self.ridx))

    def intersect(self, other):
        return (self.lidx <= other.lidx and other.lidx < self.ridx <= other.ridx) or (
            self.ridx > other.ridx and other.lidx <= self.lidx < other.ridx
        )


def dquote(value: str, dialect: str = POSTGRESQL_DIALECT) -> str:
    """Double quotes a string, handles delimiters."""
    left = DIALECTS[dialect].quote.double.left
    right = DIALECTS[dialect].quote.double.right
    merged = f'{left}.{right}'.join(value.split('.'))
    return f'{left}{merged}{right}'


def squote(value: str, dialect: str = POSTGRESQL_DIALECT) -> str:
    """Single quotes a string."""
    left = DIALECTS[dialect].quote.single.left
    right = DIALECTS[dialect].quote.single.right
    return f'{left}{value}{right}'


def requote(value: str, constants: Optional[Dict[str, SIBN_T]] = None) -> str:
    """Quotes, unquotes, cuts or even replaces the value according to the token indices."""
    constants = constants or dict()
    result = value

    if len(value) >= WRAP.key_len * 2:
        wrapper = value[:2] + value[-2:]
        inner = value[2:-2]

        if wrapper == WRAP.double.left + WRAP.double.right:
            result = dquote(inner)
        elif wrapper == WRAP.const.left + WRAP.const.right:
            result = f'{constants.get(inner, inner)}'
        elif wrapper == WRAP.single.left + WRAP.single.right:
            result = squote(inner)
    else:
        # escaped wrapper
        if value[0] == WRAP.left_escape:
            result = value[1:]
        else:
            result = value[:-1]

    return result


def get_token_tree(tokens: Set[Token]) -> Token:
    """Builds tree from tokens and returns root token as tree."""
    ordered = sorted(tokens)
    adopted = set()

    for idx, child in enumerate(ordered, start=1):
        for parent in ordered[idx:]:
            if child not in adopted and child in parent:
                parent.children.add(child)
                adopted.add(child)

    return ordered[-1]  # last element will be the whole tokenized value


def tokenize(value: str, constants: Optional[Dict[str, SIBN_T]] = None) -> Token:
    """Generates a set of wrapped tokens from str value."""
    step = 1
    value_len = len(value)
    wrapped = set()  # chunks to merge
    # already handled wrapper indices
    burnt_left = set()

    ridx = WRAP.key_len  # leaving space for the left operator
    while ridx < value_len:
        right = value[ridx : (right_origin := ridx + WRAP.key_len)]

        if (
            (skipped_origin := ridx - WRAP.key_len) not in burnt_left
            and ridx > WRAP.key_len
            and value[(esc_idx := skipped_origin - step)] == WRAP.left_escape
            and value[skipped_origin:ridx] in WRAP.lefts
        ):
            # tokenizing skipped escaped left wrapper
            wrapped.add(Token(esc_idx, ridx, value=value[esc_idx:ridx], escaped=True))
            burnt_left.add(skipped_origin)

        if right in WRAP.rights:
            operation = right[0]

            if value_len > right_origin and value[right_origin] == WRAP.right_escape:
                # tokenizing escaped right wrapper
                esc_idx = right_origin + step
                wrapped.add(Token(ridx, esc_idx, value=value[ridx:esc_idx], escaped=True))
                ridx = esc_idx
                continue

            pair = WRAP.left_escape + operation
            lidx = ridx

            while lidx >= WRAP.key_len:  # leaving space for the left operator
                left = value[(left_origin := lidx - WRAP.key_len) : lidx]

                if left == pair:

                    if left_origin in burnt_left:
                        lidx -= WRAP.key_len  # skipping burnt_left wrapper
                        continue

                    burnt_left.add(left_origin)

                    if left_origin > 0 and value[(esc_idx := left_origin - step)] == WRAP.left_escape:
                        # tokenizing escaped left wrapper
                        wrapped.add(Token(esc_idx, lidx, value=value[esc_idx:lidx], constants=constants))
                        lidx = esc_idx
                        continue

                    token = Token(left_origin, right_origin, value=value[left_origin:right_origin], constants=constants)
                    for w in wrapped:
                        if token.intersect(w):
                            break  # tokens can't intersect
                    else:
                        wrapped.add(token)
                        ridx = right_origin
                        break

                else:
                    lidx -= step  # moving to the next char
            else:
                ridx += WRAP.key_len  # pair not found, skipping orphan right wrapper
        else:
            ridx += step  # moving to the next char

    wrapped.add(Token(0, value_len, value=value, constants=constants))  # root

    return get_token_tree(wrapped)


def stringify(value: SIBN_T, constants: Optional[Dict[str, SIBN_T]] = None, dialect: str = POSTGRESQL_DIALECT) -> str:
    """Stringifies value by applying wrappers."""
    true = DIALECTS[dialect].cast.true
    false = DIALECTS[dialect].cast.false
    null = DIALECTS[dialect].cast.null

    result = str(value)
    type_ = type(value)

    if type_ == bool:
        result = true if value else false
    elif type_ == NoneType:
        result = null
    elif type_ == str and len(result) >= WRAP.key_len * 2:
        result = str(tokenize(result, constants=constants))

    return result


def densify(value: str) -> str:
    """Removes duplicate spaces."""
    return resub(' +', ' ', value)
