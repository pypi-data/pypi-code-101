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


class GetBlocked(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0xf57c350f``

    Parameters:
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`contacts.Blocked <telectron.raw.base.contacts.Blocked>`
    """

    __slots__: List[str] = ["offset", "limit"]

    ID = 0xf57c350f
    QUALNAME = "functions.contacts.GetBlocked"

    def __init__(self, *, offset: int, limit: int) -> None:
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetBlocked":
        # No flags
        
        offset = Int.read(data)
        
        limit = Int.read(data)
        
        return GetBlocked(offset=offset, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.offset))
        
        data.write(Int(self.limit))
        
        return data.getvalue()
