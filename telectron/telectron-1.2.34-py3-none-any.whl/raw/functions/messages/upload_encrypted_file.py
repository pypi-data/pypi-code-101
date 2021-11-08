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


class UploadEncryptedFile(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0x5057c497``

    Parameters:
        peer: :obj:`InputEncryptedChat <telectron.raw.base.InputEncryptedChat>`
        file: :obj:`InputEncryptedFile <telectron.raw.base.InputEncryptedFile>`

    Returns:
        :obj:`EncryptedFile <telectron.raw.base.EncryptedFile>`
    """

    __slots__: List[str] = ["peer", "file"]

    ID = 0x5057c497
    QUALNAME = "functions.messages.UploadEncryptedFile"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", file: "raw.base.InputEncryptedFile") -> None:
        self.peer = peer  # InputEncryptedChat
        self.file = file  # InputEncryptedFile

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UploadEncryptedFile":
        # No flags
        
        peer = TLObject.read(data)
        
        file = TLObject.read(data)
        
        return UploadEncryptedFile(peer=peer, file=file)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(self.file.write())
        
        return data.getvalue()
