#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build your custom ciper
#    Copyright (C) 2021  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This file implements tools to build your custom ciper.

>>> CustomCrypto(xor).dynamic_key_1(b'00', [ord('0')])
[0, 48]
>>> CustomCrypto(xor).reverse_dynamic_key_1([0, 48], [ord('0')])
[48, 48]
>>> CustomCrypto(viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_2('ACCA', ('C', 'A'))
['C', 'C', 'C', 'C']
>>> CustomCrypto(decipher_viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_2('CCCC', ('C', 'A'))
['A', 'C', 'C', 'A']
>>> CustomCrypto(None).shuffle('ABCDEFGH', 4)
['A', 'E', 'B', 'F', 'C', 'G', 'D', 'H']
>>> CustomCrypto(None).unshuffle('AEBFCGDH', 4)
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
>>> CustomCrypto(None).reverse('ABCD')
['D', 'C', 'B', 'A']
>>> lines = CustomCrypto(None).group('0' * 40, '0')
>>> lines = "\\n".join(" ".join("".join(chars) for chars in words) for words in lines)
>>> print(lines)
30303030 30303030 30303030 30303030 30303030
30303030 30303030 30303030 30303030 30303030
>>> CustomCrypto(None).shift(b'\\xff\\x00\\xf0\\xa5\\xaa')
b'\\xff\\x00\\x0fZ\\xaa'

~# python3 -m doctest -v CustomCrypto.py
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements tools to build your custom ciper.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/CustomCrypto"

copyright = """
CustomCrypto  Copyright (C) 2021  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = [
    "CustomCrypto",
    "xor",
    "viginere",
    "decipher_viginere",
    "monoalphabetique",
    "decipher_monoalphabetique",
]

from typing import List, Any, Union, Dict, Tuple
from collections.abc import Callable, Iterable
from functools import singledispatch
from collections import deque
from binascii import b2a_hex
from operator import xor
import operator
import string
import sys

latin_1_bytes = bytes(list(range(256)))
latin_1_str = [chr(char) for char in latin_1_bytes]


@singledispatch
def viginere(
    char_data: Union[str, bytes],
    char_key: Union[str, bytes],
    alphabet: Union[str, bytes] = latin_1_str,
    *,
    alphabet_length: int = None
) -> Union[str, int]:

    """
    This function implement VIGINERE cipher.

    char_data: should be a str or bytes of length 1
    char_key:  should be a str or bytes of length 1
    alphabet: should contains char_data and char_key
    alphabet_length: should be the alphabet length

    >>> viginere('A', 'C', string.ascii_uppercase)
    'C'
    >>> viginere(b'A', b'C', string.ascii_uppercase.encode('ascii'))
    67
    """

    if alphabet_length is None:
        alphabet_length = len(alphabet)

    if isinstance(char_data, bytes):
        char_data = char_data[0]

    if isinstance(char_key, bytes):
        char_key = char_key[0]

    data_index = operator.indexOf(alphabet, char_data)  # alphabet.index(char_data)
    key_index = operator.indexOf(alphabet, char_key)  # alphabet.index(key_data)
    new_index = operator.mod(operator.add(data_index, key_index), alphabet_length)

    return operator.getitem(alphabet, new_index)


@viginere.register
def _viginere(
    char_data: int,
    char_key: int,
    alphabet: bytes = latin_1_bytes,
    *,
    alphabet_length: int = None
) -> int:

    """
    This function implement VIGINERE cipher.

    char_data: should be a integer (0 <= char_data <= alphabet_length)
    char_key:  should be a integer (0 <= char_data <= alphabet_length)
    alphabet_length: should be the alphabet length

    >>> viginere(0, 2, string.ascii_uppercase.encode('ascii'))
    2
    """

    if alphabet_length is None:
        alphabet_length = len(alphabet)

    return operator.mod(operator.add(char_data, char_key), alphabet_length)


@singledispatch
def decipher_viginere(
    char_data: Union[str, bytes],
    char_key: Union[str, bytes],
    alphabet: Union[str, bytes] = latin_1_str,
    *,
    alphabet_length: int = None
) -> Union[str, int]:

    """
    This function implement VIGINERE cipher.

    char_data: should be a str or bytes of length 1
    char_key:  should be a str or bytes of length 1
    alphabet: should contains char_data and char_key
    alphabet_length: should be the alphabet length

    >>> decipher_viginere('C', 'C', string.ascii_uppercase)
    'A'
    >>> decipher_viginere(b'C', b'C', string.ascii_uppercase.encode('ascii'))
    65
    """

    if alphabet_length is None:
        alphabet_length = len(alphabet)

    if isinstance(char_data, bytes):
        char_data = char_data[0]

    if isinstance(char_key, bytes):
        char_key = char_key[0]

    data_index = operator.indexOf(alphabet, char_data)  # alphabet.index(char_data)
    key_index = operator.indexOf(alphabet, char_key)  # alphabet.index(key_data)
    new_index = operator.mod(operator.sub(data_index, key_index), alphabet_length)

    return operator.getitem(alphabet, new_index)


@decipher_viginere.register
def _decipher_viginere(
    char_data: int,
    char_key: int,
    alphabet: bytes = latin_1_bytes,
    *,
    alphabet_length: int = None
) -> int:

    """
    This function implement VIGINERE cipher.

    char_data: should be a integer (0 <= char_data <= alphabet_length)
    char_key:  should be a integer (0 <= char_data <= alphabet_length)
    alphabet_length: should be the alphabet length

    >>> _decipher_viginere(2, 2, string.ascii_uppercase.encode('ascii'))
    0
    """

    if alphabet_length is None:
        alphabet_length = len(alphabet)

    return operator.mod(operator.sub(char_data, char_key), alphabet_length)


def monoalphabetique(
    data: Iterable[Any],
    key: Union[Dict[Any, Any], Iterable[Tuple[Any, Any]], Tuple[Iterable[Any, Any]]],
) -> List[Any]:

    """
    This function implement monoalphabetique cipher.

    key as dict:
        - key: should contains any element of data

    key as tuples:
        - key[x][0] should contains any element of data

    key as tuple:
        - key[0] should contains any element of data

    >>> monoalphabetique("A", {"A": "B"})
    ['B']
    >>> monoalphabetique("A", [("A","B")])
    ['B']
    >>> monoalphabetique("A", ("A","B"))
    ['B']
    >>> monoalphabetique("A", 10)
    Traceback (most recent call last):
        ...
    TypeError: 'key' should be a Dict[Any, Any], a Tuple[Iterable[Any, Any]] or Iterable[Tuple[Any, Any]].
    """

    if isinstance(key, dict):
        return monoalphabetique_dict(data, key)
    elif isinstance(key, tuple) and len(key) == 2:
        return monoalphabetique_tuple_iter(data, key)
    elif isinstance(key, Iterable) and all(
        isinstance(elem, Iterable) and len(elem) == 2 for elem in key
    ):
        return monoalphabetique_iter_tuple(data, key)
    else:
        raise TypeError(
            "'key' should be a Dict[Any, Any], a Tuple["
            "Iterable[Any, Any]] or Iterable[Tuple[Any, Any]]."
        )


def decipher_monoalphabetique(
    data: Iterable[Any],
    key: Union[Dict[Any, Any], Iterable[Tuple[Any, Any]], Tuple[Iterable[Any, Any]]],
) -> List[Any]:

    """
    This function implement monoalphabetique cipher.

    key as dict:
        - key: should contains any element of data

    key as tuples:
        - key[x][0] should contains any element of data

    key as tuple:
        - key[0] should contains any element of data

    >>> decipher_monoalphabetique("B", {"A": "B"})
    ['A']
    >>> decipher_monoalphabetique("B", [("A","B")])
    ['A']
    >>> decipher_monoalphabetique("B", ("A","B"))
    ['A']
    >>> decipher_monoalphabetique("B", 10)
    Traceback (most recent call last):
        ...
    TypeError: 'key' should be a Dict[Any, Any], a Tuple[Iterable[Any, Any]] or Iterable[Tuple[Any, Any]].
    """

    if isinstance(key, dict):
        return monoalphabetique_dict(data, {v: k for k, v in key.items()})
    elif isinstance(key, tuple) and len(key) == 2:
        return monoalphabetique_tuple_iter(data, tuple(reversed(key)))
    elif isinstance(key, Iterable) and all(
        isinstance(elem, Iterable) and len(elem) == 2 for elem in key
    ):
        return monoalphabetique_iter_tuple(data, [(elem[1], elem[0]) for elem in key])
    else:
        raise TypeError(
            "'key' should be a Dict[Any, Any], a Tuple["
            "Iterable[Any, Any]] or Iterable[Tuple[Any, Any]]."
        )


def monoalphabetique_dict(data: Iterable[Any], key: Dict[Any, Any]) -> List[Any]:

    """
    This function implement monoalphabetique cipher.

    key: should contains any element of data

    >>> monoalphabetique("A", {"A": "B"})
    ['B']
    >>> monoalphabetique([0], {0: 1})
    [1]
    >>> monoalphabetique("A", ("A","B"))
    ['B']
    """

    cipher = []

    for block in data:
        cipher.append(key[block])

    return cipher


def monoalphabetique_iter_tuple(
    data: Iterable[Any], key: Iterable[Tuple[Any, Any]]
) -> List[Any]:

    """
    This function implement monoalphabetique cipher.

    key: key[x][0] should contains any element of data

    >>> monoalphabetique("A", [("A","B")])
    ['B']
    >>> monoalphabetique([0], [(0, 1)])
    [1]
    """

    cipher = []

    for block in data:
        for element in key:
            if key[0] == block:
                break
        cipher.append(element[1])

    return cipher


def monoalphabetique_tuple_iter(
    data: Iterable[Any], key: Tuple[Iterable[Any, Any]]
) -> List[Any]:

    """
    This function implement monoalphabetique cipher.

    key: key[0] should contains any element of data

    >>> monoalphabetique("A", ("A","B"))
    ['B']
    >>> monoalphabetique([0], ([0], [1]))
    [1]
    """

    cipher = []

    for block in data:
        for i, element in enumerate(key[0]):
            if element == block:
                break
        cipher.append(key[1][i])

    return cipher


class CustomCrypto:

    """
    This class implements tools to build custom crypto.

    >>> CustomCrypto(viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_1('AC', ('C',))
    ['C', 'E']
    """

    def __init__(self, crypt: Callable, *args, **kwargs):
        self.crypt = crypt
        self.args = args
        self.kwargs = kwargs

    def reverse_dynamic_key_1(
        self, data: Iterable[Any], key: Iterable[Any], *args, **kwargs
    ) -> List[Any]:

        """
        This function decrypt data with the key and precedent character/block.

        >>> c = CustomCrypto(xor)
        >>> key = [ord('0')]
        >>> c.reverse_dynamic_key_1(c.dynamic_key_1(b'00', key), key)
        [48, 48]
        >>> c = CustomCrypto(viginere)
        >>> d = c.dynamic_key_1('AC', ('C',), string.ascii_uppercase, alphabet_length=26)
        >>> c = CustomCrypto(decipher_viginere)
        >>> c.reverse_dynamic_key_1(d, ('C',), string.ascii_uppercase, alphabet_length=26)
        ['A', 'C']
        """

        precedent = self.crypt(
            data[0], key[0], *self.args, *args, **self.kwargs, **kwargs
        )
        key_length = len(key)
        decipher = [precedent]

        for i, block in enumerate(data[1:]):
            char_decipher = self.crypt(
                block, key[i % key_length], *self.args, *args, **self.kwargs, **kwargs
            )
            char_decipher = self.crypt(
                char_decipher, precedent, *self.args, *args, **self.kwargs, **kwargs
            )
            decipher.append(char_decipher)
            precedent = block

        return decipher

    def dynamic_key_1(
        self, data: Iterable[Any], key: Iterable[Any], *args, **kwargs
    ) -> List[Any]:

        """
        This function crypt data with the key and precedent character/block.

        >>> CustomCrypto(xor).dynamic_key_1(b'00', [ord('0')])
        [0, 48]
        >>> CustomCrypto(viginere).dynamic_key_1('AC', ('C',), string.ascii_uppercase, alphabet_length=26)
        ['C', 'E']
        """

        precedent = data[0]
        key_length = len(key)
        cipher = [
            self.crypt(data[0], key[0], *self.args, *args, **self.kwargs, **kwargs)
        ]

        for i, block in enumerate(data[1:]):
            char_cipher = self.crypt(
                block, precedent, *self.args, *args, **self.kwargs, **kwargs
            )
            char_cipher = self.crypt(
                char_cipher,
                key[i % key_length],
                *self.args,
                *args,
                **self.kwargs,
                **kwargs
            )
            cipher.append(char_cipher)
            precedent = block

        return cipher

    def dynamic_key_2(
        self, data: Iterable[Any], key: Iterable[Any], *args, **kwargs
    ) -> List[Any]:

        """
        This function crypt data with .

        >>> CustomCrypto(xor).dynamic_key_2(b'0110', [ord('0'), ord('1')])
        [0, 0, 0, 0]
        >>> CustomCrypto(viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_2('ACCA', ('C', 'A'))
        ['C', 'C', 'C', 'C']
        """

        key_length = len(key)
        cipher = []

        for i, block in enumerate(data):
            cipher.append(
                self.crypt(
                    block,
                    key[(i + i // key_length) % key_length],
                    *self.args,
                    *args,
                    **self.kwargs,
                    **kwargs
                )
            )

        return cipher

    def shuffle(self, data: Iterable[Any], number: int = 2) -> List[Any]:

        """
        This function shuffle data in <number> sections.

        >>> CustomCrypto(None).shuffle('ABCD')
        ['A', 'C', 'B', 'D']
        >>> CustomCrypto(None).shuffle('ABCDEFGH', 4)
        ['A', 'E', 'B', 'F', 'C', 'G', 'D', 'H']
        """

        sections = [[] for i in range(number)]

        for i, block in enumerate(data):
            sections[i % number].append(block)

        all_ = []

        for section in sections:
            all_ += section

        return all_

    def unshuffle(self, data: Iterable[Any], number: int = 2) -> List[Any]:

        """
        This function shuffle data in <number> sections.

        >>> CustomCrypto(None).unshuffle('ACBD')
        ['A', 'B', 'C', 'D']
        >>> c = CustomCrypto(None); c.unshuffle(c.shuffle('ABCDEFGH', 4), 4)
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        """

        sections = [deque() for i in range(number)]

        data_length = len(data)

        elements_by_section = data_length // number
        elements_by_section = [elements_by_section] * number

        section_id = 0
        additional = data_length % data_length

        while additional:
            elements_by_section[section_id] += 1
            section_id += 1
            additional -= 1

        counter = 0
        for i, section in enumerate(elements_by_section):
            counter += section
            elements_by_section[i] = counter

        elements = 0
        counter = -1
        for i, block in enumerate(data):
            if i >= elements:
                counter += 1
                elements = elements_by_section[counter]

            sections[counter].append(block)

        all_ = []

        for i, block in enumerate(sections[-1]):
            for section in sections[:-1]:
                all_.append(section.popleft())
            all_.append(block)

        i += 1
        for section in sections[:-1]:
            if section:
                all_.append(section.popleft())

        return all_

    def reverse(self, data: Iterable[Any]) -> List[Any]:

        """
        This function reverse data.

        >>> CustomCrypto(None).reverse('ABCD')
        ['D', 'C', 'B', 'A']
        >>> c = CustomCrypto(None); c.reverse(c.reverse('ABCD'))
        ['A', 'B', 'C', 'D']
        """

        return list(reversed(data))

    def group(
        self,
        data: Iterable[Any],
        alphabet: Iterable[Any],
        hexa: bool = True,
        lines_size: int = 5,
        word_size: int = 4,
    ) -> List[List[Any]]:

        """
        This function format elements in data.

        data: should be bytes or str (can be Iterable[Any])
        alphabet: should be bytes or str (can be Iterable[Any])
        hexa: should be boolean (True only with data and alphabet as bytes or str)

        >>> lines = CustomCrypto(None).group('0' * 40, '0')
        >>> lines = "\\n".join(" ".join("".join(chars) for chars in words) for words in lines)
        >>> print(lines)
        30303030 30303030 30303030 30303030 30303030
        30303030 30303030 30303030 30303030 30303030
        >>> lines = CustomCrypto(None).group(b'0' * 40, b'0', hexa=False)
        >>> lines = "\\n".join(" ".join("".join(chars) for chars in words) for words in lines)
        >>> print(lines)
        0000 0000 0000 0000 0000
        0000 0000 0000 0000 0000
        """

        if isinstance(data, str) and hexa:
            data = data.encode("utf-8")
            if isinstance(alphabet, str):
                alphabet = alphabet.encode("utf-8")
        elif isinstance(data, bytes) and not hexa:
            data = data.decode("latin-1")
            if isinstance(alphabet, bytes):
                alphabet = alphabet.decode("latin-1")

        word = []
        line = [word]
        lines = [line]

        for char in data:
            if char in alphabet:
                word.append(
                    char.to_bytes(1, byteorder=sys.byteorder).hex() if hexa else char
                )

                if not (len(word) % word_size):
                    word = []
                    line.append(word)

                    if len(line) == lines_size:
                        line = []
                        lines.append(line)

        if not word:
            line = line[:-1]
        if not line:
            lines = lines[:-1]

        return lines

    def shift(self, data: bytes, shifter: int = 4, decode: bool = False) -> bytes:

        """
        This function shift bits.

        >>> CustomCrypto(None).shift(b'\\xff\\x00\\xf0\\xa5\\xaa')
        b'\\xff\\x00\\x0fZ\\xaa'
        >>> CustomCrypto(None).shift(b'\\xff\\x00\\x0fZ\\xaa', decode=True)
        b'\\xff\\x00\\xf0\\xa5\\xaa'
        >>> CustomCrypto(None).shift(b'', shifter=8)
        Traceback (most recent call last):
            ...
        ValueError: 'shifter' should be smaller than 8.
        >>> CustomCrypto(None).shift(b'', shifter=9)
        Traceback (most recent call last):
            ...
        ValueError: 'shifter' should be smaller than 8.
        """

        if shifter >= 8:
            raise ValueError("'shifter' should be smaller than 8.")

        if decode:
            shifter, a = 8 - shifter, shifter
        else:
            shifter, a = shifter, 8 - shifter

        new_data = []
        for byte in data:
            new_data.append((byte << shifter | byte >> a) % 256)

        return bytes(new_data)