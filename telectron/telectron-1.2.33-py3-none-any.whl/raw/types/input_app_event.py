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


class InputAppEvent(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.InputAppEvent`.

    Details:
        - Layer: ``129``
        - ID: ``0x1d1b1245``

    Parameters:
        time: ``float`` ``64-bit``
        type: ``str``
        peer: ``int`` ``64-bit``
        data: :obj:`JSONValue <telectron.raw.base.JSONValue>`
    """

    __slots__: List[str] = ["time", "type", "peer", "data"]

    ID = 0x1d1b1245
    QUALNAME = "types.InputAppEvent"

    def __init__(self, *, time: float, type: str, peer: int, data: "raw.base.JSONValue") -> None:
        self.time = time  # double
        self.type = type  # string
        self.peer = peer  # long
        self.data = data  # JSONValue

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputAppEvent":
        # No flags
        
        time = Double.read(data)
        
        type = String.read(data)
        
        peer = Long.read(data)
        
        data = TLObject.read(data)
        
        return InputAppEvent(time=time, type=type, peer=peer, data=data)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Double(self.time))
        
        data.write(String(self.type))
        
        data.write(Long(self.peer))
        
        data.write(self.data.write())
        
        return data.getvalue()
