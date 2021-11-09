#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements encode/decode functions for GSM (SMS)
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
This package implements encode/decode functions for GSM (SMS).

>>> gsm7bitencode("Unit Test")
'55779A0EA296E774'
>>> gsm7bitdecode('55779A0EA296E774')
'Unit Test\\x00'
>>> gsm7bitdecode(gsm7bitencode(b'Unit Test'))
b'Unit Test\\x00'

~# python3 -m doctest -v gsm.py
"""

__version__ = "0.0.2"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements encode/decode functions for GSM (SMS).
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/GSMEncoding"

copyright = """
GSMEncoding  Copyright (C) 2021  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["gsm7bitencode", "gsm7bitdecode"]

from collections import deque
from typing import Union


def gsm7bitdecode(data: Union[str, bytes]) -> Union[str, bytes]:

    """
    >>> gsm7bitdecode('C7F7FBCC2E03')
    'Google\\x00'
    >>> gsm7bitdecode(bytes.fromhex('C7F7FBCC2E03'))
    b'Google\\x00'
    """

    decode1 = deque()
    is_str = False
    decode2 = []

    if isinstance(data, str):
        is_str = True
        data = bytes.fromhex(data)

    for char in data:
        decode1.appendleft(f"{char:08b}")

    decode1 = "".join(decode1)[::-1]

    for i in range(0, len(decode1), 7):
        decode2.append(int(decode1[i : i + 7][::-1], 2))

    decode2 = bytes(decode2)

    if is_str:
        return decode2.decode("ascii")

    return decode2


def gsm7bitencode(data: Union[str, bytes]) -> Union[str, bytes]:

    """
    >>> gsm7bitencode('Google')
    'C7F7FBCC2E03'
    >>> gsm7bitencode(b'Google').hex().upper()
    'C7F7FBCC2E03'
    """

    encode1 = []
    is_str = False
    encode2 = deque()
    encode1_length = len(data) * 7
    encode1_length += 8 - (encode1_length % 8)

    if not data.isascii():
        raise ValueError("ASCII data required")

    if isinstance(data, str):
        is_str = True
        data = data.encode("ascii")

    for char in data:
        encode1.append(f"{char:07b}"[::-1])

    encode1 = "".join(encode1)[::-1].rjust(encode1_length, "0")

    for i in range(0, len(encode1), 8):
        encode2.appendleft(int(encode1[i : i + 8], 2))

    encode2 = bytes(encode2)

    if is_str:
        return encode2.hex().upper()

    return encode2
