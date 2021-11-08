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


class FeaturedStickers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.messages.FeaturedStickers`.

    Details:
        - Layer: ``129``
        - ID: ``0xb6abc341``

    Parameters:
        hash: ``int`` ``32-bit``
        count: ``int`` ``32-bit``
        sets: List of :obj:`StickerSetCovered <telectron.raw.base.StickerSetCovered>`
        unread: List of ``int`` ``64-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetFeaturedStickers <telectron.raw.functions.messages.GetFeaturedStickers>`
            - :obj:`messages.GetOldFeaturedStickers <telectron.raw.functions.messages.GetOldFeaturedStickers>`
    """

    __slots__: List[str] = ["hash", "count", "sets", "unread"]

    ID = 0xb6abc341
    QUALNAME = "types.messages.FeaturedStickers"

    def __init__(self, *, hash: int, count: int, sets: List["raw.base.StickerSetCovered"], unread: List[int]) -> None:
        self.hash = hash  # int
        self.count = count  # int
        self.sets = sets  # Vector<StickerSetCovered>
        self.unread = unread  # Vector<long>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FeaturedStickers":
        # No flags
        
        hash = Int.read(data)
        
        count = Int.read(data)
        
        sets = TLObject.read(data)
        
        unread = TLObject.read(data, Long)
        
        return FeaturedStickers(hash=hash, count=count, sets=sets, unread=unread)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.hash))
        
        data.write(Int(self.count))
        
        data.write(Vector(self.sets))
        
        data.write(Vector(self.unread, Long))
        
        return data.getvalue()
