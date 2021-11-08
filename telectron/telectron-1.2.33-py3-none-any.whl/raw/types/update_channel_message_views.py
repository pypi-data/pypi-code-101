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


class UpdateChannelMessageViews(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.Update`.

    Details:
        - Layer: ``129``
        - ID: ``0x98a12b4b``

    Parameters:
        channel_id: ``int`` ``32-bit``
        id: ``int`` ``32-bit``
        views: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["channel_id", "id", "views"]

    ID = 0x98a12b4b
    QUALNAME = "types.UpdateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        self.channel_id = channel_id  # int
        self.id = id  # int
        self.views = views  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        # No flags
        
        channel_id = Int.read(data)
        
        id = Int.read(data)
        
        views = Int.read(data)
        
        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.channel_id))
        
        data.write(Int(self.id))
        
        data.write(Int(self.views))
        
        return data.getvalue()
