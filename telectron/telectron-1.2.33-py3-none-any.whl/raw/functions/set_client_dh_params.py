#  telectron - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of telectron.
#
#  telectron is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  telectron is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with telectron.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from telectron.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from telectron.raw.core import TLObject
from telectron import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SetClientDHParams(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0xf5045f1f``

    Parameters:
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        encrypted_data: ``bytes``

    Returns:
        :obj:`SetClientDHParamsAnswer <telectron.raw.base.SetClientDHParamsAnswer>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "encrypted_data"]

    ID = 0xf5045f1f
    QUALNAME = "functions.SetClientDHParams"

    def __init__(self, *, nonce: int, server_nonce: int, encrypted_data: bytes) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.encrypted_data = encrypted_data  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetClientDHParams":
        # No flags
        
        nonce = Int128.read(data)
        
        server_nonce = Int128.read(data)
        
        encrypted_data = Bytes.read(data)
        
        return SetClientDHParams(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int128(self.nonce))
        
        data.write(Int128(self.server_nonce))
        
        data.write(Bytes(self.encrypted_data))
        
        return data.getvalue()
