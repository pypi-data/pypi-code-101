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


class SetCallRating(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0x59ead627``

    Parameters:
        peer: :obj:`InputPhoneCall <telectron.raw.base.InputPhoneCall>`
        rating: ``int`` ``32-bit``
        comment: ``str``
        user_initiative (optional): ``bool``

    Returns:
        :obj:`Updates <telectron.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "rating", "comment", "user_initiative"]

    ID = 0x59ead627
    QUALNAME = "functions.phone.SetCallRating"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", rating: int, comment: str, user_initiative: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPhoneCall
        self.rating = rating  # int
        self.comment = comment  # string
        self.user_initiative = user_initiative  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetCallRating":
        flags = Int.read(data)
        
        user_initiative = True if flags & (1 << 0) else False
        peer = TLObject.read(data)
        
        rating = Int.read(data)
        
        comment = String.read(data)
        
        return SetCallRating(peer=peer, rating=rating, comment=comment, user_initiative=user_initiative)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.user_initiative else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.rating))
        
        data.write(String(self.comment))
        
        return data.getvalue()
