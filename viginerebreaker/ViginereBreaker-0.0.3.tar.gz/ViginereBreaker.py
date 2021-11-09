#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements a viginere breaker.
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
This package implements a viginere breaker.

>>> c = ViginereBreaker("E" * 13 + "A" * 8 + "Z" * 79)
>>> c.breaker()
[['A']]

Tests:
~# python3 -m doctest -v ViginereBreaker.py

Command line:
~# python3 ViginereBreaker.py cipher.txt
{"4": [["T"], ["E"], ["S"], ["T"]], "12": [["T"], ["E"], ["S"], ["T"], ["T"], ["E"], ["S"], ["T"], ["T"], ["E"], ["S"], ["T"]]}
~# python3 ViginereBreaker.py cipher.txt -k 4 -a "ABCDEFGHIJKLMNOPQRSTUVWXYZ" -s "{\\"E\\":10,\\"A\\":7}"
[["T"], ["E"], ["S"], ["T"]]
"""

__version__ = "0.0.3"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements a viginere breaker.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/ViginereBreaker"

copyright = """
ViginereBreaker  Copyright (C) 2021  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["ViginereBreaker"]

from argparse import ArgumentParser, FileType
from typing import Union, Dict, Any, Tuple
from collections.abc import Iterable
from string import ascii_uppercase
from collections import Counter
from math import sqrt
import json
import sys


class ViginereBreaker:

    """
	This class breaks viginere cipher.

	data: should be str or bytes (it can be Iterable[Any]).
	key_length: should be the key length if you know the \
key length else None
	statistics: should be the dictionnary of pourcent of \
decipher data (for exemple if data is English text statistics\
 should be: {"E": 13, "A": 8})
	alphabet: characters to decipher (for example \
"ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	>>> c = ViginereBreaker("E" * 13 + "A" * 8 + "Z" * 79)
	>>> c.breaker()
	[['A']]
	"""

    def __init__(
        self,
        data: Iterable[Any],
        key_length: int = None,
        statistics: Dict[Any, float] = {"E": 13, "A": 8},
        alphabet: Iterable[Any] = ascii_uppercase,
    ):
        self.data = data
        self.key_length = key_length
        self.statistics = statistics
        self.alphabet = alphabet

    def breaker(self) -> Iterable[Any]:

        """
        This function break viginere cipher.

        >>> c = ViginereBreaker("E" * 13 + "A" * 8 + "Z" * 79)
        >>> c.breaker()
        [['A']]
        >>> c = ViginereBreaker("E" * 13 + "A" * 8 + "Z" * 79, 0)
        >>> c.breaker()
        [['A']]
        """

        if self.key_length:
            return self.found_chars_keys(
                self.data, self.key_length, self.statistics, self.alphabet
            )

        keys = {}
        for key_length in range(1, round(sqrt(len(self.data)) + 1)):
            key = self.found_chars_keys(
                self.data, key_length, self.statistics, self.alphabet
            )
            if key:
                keys[key_length] = key

        return keys

    @staticmethod
    def found_chars_keys(
        data: Iterable[Any],
        key_length: int,
        statistics: Dict[Any, Any],
        alphabet: Iterable[Any],
    ) -> Iterable[Any]:

        """
        This function search the key.

        >>> ViginereBreaker.found_chars_keys("E" * 13 + "A" * 8 + "Z" * 79, 0, {"E": 13, "A": 8}, ascii_uppercase)
        [['A']]
        """

        statistics_ = statistics.copy()
        data_statistics = [Counter() for i in range(key_length)]
        match_keys = [[] for i in range(key_length)]
        alphabet_length = len(alphabet)

        for key, value in statistics_.items():
            value = round(value)
            statistics_[key] = (value - 2, value + 2)

        iter_num = 0
        for char in data:
            if char in alphabet:
                data_statistics[iter_num % key_length][char] += 1
                iter_num += 1

        for j, counter in enumerate(data_statistics):
            ViginereBreaker.get_statistics(counter, alphabet)

            for i in range(len(alphabet)):
                if ViginereBreaker.match_characters(
                    counter, statistics_, alphabet, i, alphabet_length
                ):
                    match_keys[j].append(alphabet[i])

        if all(match_keys):
            return match_keys

    @staticmethod
    def get_statistics(counter: Counter, alphabet: Iterable[Any]) -> Dict[Any, int]:

        """
        This function return character statistics.

        >>> ViginereBreaker.get_statistics({"A": 1}, "A")
        {"A": 100}
        """

        caesar_length = sum(counter.values())

        for char in alphabet:
            counter[char] = counter[char] * 100 / caesar_length

        return counter

    @staticmethod
    def match(counter: Counter, char: Any, values: Tuple[int, int]) -> bool:

        """
        This function check if character statistic match.

        >>> ViginereBreaker.match({"A": 100}, "A", (100, 100))
        True
        >>> ViginereBreaker.match({"A": 100}, "A", (0, 99))
        False
        """

        if counter[char] < values[0] or counter[char] > values[1]:
            return False
        return True

    @staticmethod
    def match_characters(
        counter: Counter,
        statistics: Dict[Any, Tuple[int, int]],
        alphabet: Iterable[Any],
        index: int,
        alphabet_length: int,
    ) -> bool:

        """
        This function match any statistic characters.

        >>> ViginereBreaker.match_characters({"A": 100}, {"A": (100, 100)}, ascii_uppercase, 0, 26)
        True
        >>> ViginereBreaker.match_characters({"A": 100}, {"A": (0, 99)}, ascii_uppercase, 0, 26)
        False
        """

        first = True
        match_ = True

        for key, values in statistics.items():
            if not ViginereBreaker.match(
                counter,
                alphabet[(alphabet.index(key) + index) % alphabet_length],
                values,
            ):
                match_ = False
                break

            first = False

        return match_


def main() -> None:

    """
    This function execute this file from the command line.
    """

    parser = ArgumentParser(description="This package can break a viginere cipher.")
    parser.add_argument(
        "inputfile",
        help="File where data are encrypted with viginere.",
        type=FileType("r"),
    )
    parser.add_argument(
        "--key-length", "-k", type=int, help="The length of the key if you know it."
    )
    parser.add_argument(
        "--alphabet",
        "-a",
        help="Ordered characters used in the encryption / decryption algorithm.",
        default=ascii_uppercase,
    )
    parser.add_argument(
        "--statistics",
        "-s",
        type=json.loads,
        help="JSON object with characters as key and pourcent of occcurence as value.",
        default={"E": 11, "A": 7},
    )
    arguments = parser.parse_args()

    if (
        not isinstance(arguments.statistics, dict)
        or not all(isinstance(k, str) for k in arguments.statistics.keys())
        or not all(isinstance(v, int) for v in arguments.statistics.values())
    ):
        parser.print_usage()
        print(
            f": error: argument statistics: invalid Dict[str, int] value: {arguments.statistics}"
        )
        sys.exit(1)

    breaker = ViginereBreaker(
        arguments.inputfile.read(),
        arguments.key_length,
        arguments.statistics,
        arguments.alphabet,
    )
    print(json.dumps(breaker.breaker()))


if __name__ == "__main__":
    main()
    sys.exit(0)
