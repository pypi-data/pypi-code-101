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


class ChatAdminWithInvites(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.ChatAdminWithInvites`.

    Details:
        - Layer: ``129``
        - ID: ``0xdfd2330f``

    Parameters:
        admin_id: ``int`` ``32-bit``
        invites_count: ``int`` ``32-bit``
        revoked_invites_count: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["admin_id", "invites_count", "revoked_invites_count"]

    ID = 0xdfd2330f
    QUALNAME = "types.ChatAdminWithInvites"

    def __init__(self, *, admin_id: int, invites_count: int, revoked_invites_count: int) -> None:
        self.admin_id = admin_id  # int
        self.invites_count = invites_count  # int
        self.revoked_invites_count = revoked_invites_count  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatAdminWithInvites":
        # No flags
        
        admin_id = Int.read(data)
        
        invites_count = Int.read(data)
        
        revoked_invites_count = Int.read(data)
        
        return ChatAdminWithInvites(admin_id=admin_id, invites_count=invites_count, revoked_invites_count=revoked_invites_count)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.admin_id))
        
        data.write(Int(self.invites_count))
        
        data.write(Int(self.revoked_invites_count))
        
        return data.getvalue()
