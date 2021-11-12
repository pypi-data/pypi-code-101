# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import hashlib
import re
from typing import Type, TypeVar

import base58
from duniterpy.constants import PUBKEY_REGEX

# required to type hint cls in classmethod
PublicKeyType = TypeVar("PublicKeyType", bound="PublicKey")


class PublicKey:
    """
    Class to handle base58 public key and checksum
    """

    re_checksum_pubkey = re.compile(f"({PUBKEY_REGEX}):([A-Za-z0-9]{{3}})")

    def __init__(self, pubkey: str, checksum: str) -> None:
        """
        Creates a pubkey with a checksum

        :param pubkey: Public key
        :param checksum: Checksum
        """
        self.base58 = pubkey
        self.checksum = checksum

        if not self.pubkey_is_valid():
            raise PubkeyNotValid(f"Invalid base58 public key {self.base58}")
        if not self.checksum_is_valid():
            raise PubkeyChecksumNotValid(
                f"Invalid checksum {self.checksum} for key {self.base58}"
            )

    @classmethod
    def from_str(cls: Type[PublicKeyType], pubkey_checksum: str) -> PublicKeyType:
        """
        Return PublicKey instance from public_key:checksum string

        :param pubkey_checksum: Public key with checksum
        :return:
        """
        pubkey, checksum = pubkey_checksum.split(":", 2)
        return cls(pubkey, checksum)

    @classmethod
    def from_pubkey(cls: Type[PublicKeyType], pubkey: str) -> PublicKeyType:
        """
        Return PublicKey instance from public key string

        :param pubkey: Public key
        :return:
        """
        checksum = PublicKey._calculate_checksum(pubkey)
        return cls(pubkey, checksum)

    @staticmethod
    def _calculate_checksum(base58_: str) -> str:
        """
        Return the three last character of pubkey checksum

        :param base58_: Base58 public key
        :return:
        """
        hash_root = hashlib.sha256()
        hash_root.update(base58.b58decode(base58_))
        hash_squared = hashlib.sha256()
        hash_squared.update(hash_root.digest())
        b58_checksum = base58.b58encode(hash_squared.digest())

        return b58_checksum[:3].decode("utf-8")

    def pubkey_is_valid(self) -> bool:
        """
        Return True if base58 pubkey is valid

        :return:
        """
        re_pubkey = re.compile(PUBKEY_REGEX)

        data = re_pubkey.match(self.base58)
        return data is not None

    def checksum_is_valid(self) -> bool:
        """
        Return True if checksum is valid

        :return:
        """
        return self._calculate_checksum(self.base58) == self.checksum

    @property
    def shorten(self) -> str:
        """
        Return a shorten version of public key (8 characters)

        :return:
        """
        return f"{self.base58[:8]}"

    @property
    def shorten_checksum(self) -> str:
        """
        Return a shorten version of public key (8 characters) + checksum

        :return:
        """
        return f"{self.base58[:8]}:{self.checksum}"

    def __str__(self) -> str:
        """
        Return string representation of instance

        :return:
        """
        return f"{self.base58}:{self.checksum}"

    def __eq__(self, other) -> bool:
        """
        Test PublicKey equality

        :param other: Other PublicKey instance
        :return:
        """
        if not isinstance(other, PublicKey):
            return False

        if self.base58 == other.base58:
            return True

        return False

    def __hash__(self):
        return self.base58


class PubkeyNotValid(Exception):
    pass


class PubkeyChecksumNotValid(Exception):
    pass
