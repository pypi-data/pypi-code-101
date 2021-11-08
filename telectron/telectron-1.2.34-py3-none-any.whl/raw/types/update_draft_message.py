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


class UpdateDraftMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.Update`.

    Details:
        - Layer: ``129``
        - ID: ``0xee2bb969``

    Parameters:
        peer: :obj:`Peer <telectron.raw.base.Peer>`
        draft: :obj:`DraftMessage <telectron.raw.base.DraftMessage>`
    """

    __slots__: List[str] = ["peer", "draft"]

    ID = 0xee2bb969
    QUALNAME = "types.UpdateDraftMessage"

    def __init__(self, *, peer: "raw.base.Peer", draft: "raw.base.DraftMessage") -> None:
        self.peer = peer  # Peer
        self.draft = draft  # DraftMessage

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateDraftMessage":
        # No flags
        
        peer = TLObject.read(data)
        
        draft = TLObject.read(data)
        
        return UpdateDraftMessage(peer=peer, draft=draft)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(self.draft.write())
        
        return data.getvalue()
