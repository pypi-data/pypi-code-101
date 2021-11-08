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


class IpPortSecret(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.IpPort`.

    Details:
        - Layer: ``129``
        - ID: ``0x37982646``

    Parameters:
        ipv4: ``int`` ``32-bit``
        port: ``int`` ``32-bit``
        secret: ``bytes``
    """

    __slots__: List[str] = ["ipv4", "port", "secret"]

    ID = 0x37982646
    QUALNAME = "types.IpPortSecret"

    def __init__(self, *, ipv4: int, port: int, secret: bytes) -> None:
        self.ipv4 = ipv4  # int
        self.port = port  # int
        self.secret = secret  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "IpPortSecret":
        # No flags
        
        ipv4 = Int.read(data)
        
        port = Int.read(data)
        
        secret = Bytes.read(data)
        
        return IpPortSecret(ipv4=ipv4, port=port, secret=secret)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.ipv4))
        
        data.write(Int(self.port))
        
        data.write(Bytes(self.secret))
        
        return data.getvalue()
