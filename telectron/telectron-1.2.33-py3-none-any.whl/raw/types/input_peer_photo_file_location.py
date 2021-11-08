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


class InputPeerPhotoFileLocation(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.InputFileLocation`.

    Details:
        - Layer: ``129``
        - ID: ``0x37257e99``

    Parameters:
        peer: :obj:`InputPeer <telectron.raw.base.InputPeer>`
        photo_id: ``int`` ``64-bit``
        big (optional): ``bool``
    """

    __slots__: List[str] = ["peer", "photo_id", "big"]

    ID = 0x37257e99
    QUALNAME = "types.InputPeerPhotoFileLocation"

    def __init__(self, *, peer: "raw.base.InputPeer", photo_id: int, big: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.photo_id = photo_id  # long
        self.big = big  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPeerPhotoFileLocation":
        flags = Int.read(data)
        
        big = True if flags & (1 << 0) else False
        peer = TLObject.read(data)
        
        photo_id = Long.read(data)
        
        return InputPeerPhotoFileLocation(peer=peer, photo_id=photo_id, big=big)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Long(self.photo_id))
        
        return data.getvalue()
