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


class GetPaymentForm(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0x8a333c8d``

    Parameters:
        peer: :obj:`InputPeer <telectron.raw.base.InputPeer>`
        msg_id: ``int`` ``32-bit``
        theme_params (optional): :obj:`DataJSON <telectron.raw.base.DataJSON>`

    Returns:
        :obj:`payments.PaymentForm <telectron.raw.base.payments.PaymentForm>`
    """

    __slots__: List[str] = ["peer", "msg_id", "theme_params"]

    ID = 0x8a333c8d
    QUALNAME = "functions.payments.GetPaymentForm"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, theme_params: "raw.base.DataJSON" = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetPaymentForm":
        flags = Int.read(data)
        
        peer = TLObject.read(data)
        
        msg_id = Int.read(data)
        
        theme_params = TLObject.read(data) if flags & (1 << 0) else None
        
        return GetPaymentForm(peer=peer, msg_id=msg_id, theme_params=theme_params)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.msg_id))
        
        if self.theme_params is not None:
            data.write(self.theme_params.write())
        
        return data.getvalue()
