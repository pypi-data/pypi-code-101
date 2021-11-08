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


class InputBotInlineResultGame(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``129``
        - ID: ``0x4fa417f2``

    Parameters:
        id: ``str``
        short_name: ``str``
        send_message: :obj:`InputBotInlineMessage <telectron.raw.base.InputBotInlineMessage>`
    """

    __slots__: List[str] = ["id", "short_name", "send_message"]

    ID = 0x4fa417f2
    QUALNAME = "types.InputBotInlineResultGame"

    def __init__(self, *, id: str, short_name: str, send_message: "raw.base.InputBotInlineMessage") -> None:
        self.id = id  # string
        self.short_name = short_name  # string
        self.send_message = send_message  # InputBotInlineMessage

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputBotInlineResultGame":
        # No flags
        
        id = String.read(data)
        
        short_name = String.read(data)
        
        send_message = TLObject.read(data)
        
        return InputBotInlineResultGame(id=id, short_name=short_name, send_message=send_message)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(String(self.id))
        
        data.write(String(self.short_name))
        
        data.write(self.send_message.write())
        
        return data.getvalue()
