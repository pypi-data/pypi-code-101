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


class ReqPqMulti(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0xbe7e8ef1``

    Parameters:
        nonce: ``int`` ``128-bit``

    Returns:
        :obj:`ResPQ <telectron.raw.base.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0xbe7e8ef1
    QUALNAME = "functions.ReqPqMulti"

    def __init__(self, *, nonce: int) -> None:
        self.nonce = nonce  # int128

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReqPqMulti":
        # No flags
        
        nonce = Int128.read(data)
        
        return ReqPqMulti(nonce=nonce)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int128(self.nonce))
        
        return data.getvalue()
