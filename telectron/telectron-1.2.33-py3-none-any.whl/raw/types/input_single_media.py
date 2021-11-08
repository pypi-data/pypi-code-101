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


class InputSingleMedia(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.InputSingleMedia`.

    Details:
        - Layer: ``129``
        - ID: ``0x1cc6e91f``

    Parameters:
        media: :obj:`InputMedia <telectron.raw.base.InputMedia>`
        random_id: ``int`` ``64-bit``
        message: ``str``
        entities (optional): List of :obj:`MessageEntity <telectron.raw.base.MessageEntity>`
    """

    __slots__: List[str] = ["media", "random_id", "message", "entities"]

    ID = 0x1cc6e91f
    QUALNAME = "types.InputSingleMedia"

    def __init__(self, *, media: "raw.base.InputMedia", random_id: int, message: str, entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.media = media  # InputMedia
        self.random_id = random_id  # long
        self.message = message  # string
        self.entities = entities  # flags.0?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSingleMedia":
        flags = Int.read(data)
        
        media = TLObject.read(data)
        
        random_id = Long.read(data)
        
        message = String.read(data)
        
        entities = TLObject.read(data) if flags & (1 << 0) else []
        
        return InputSingleMedia(media=media, random_id=random_id, message=message, entities=entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.entities is not None else 0
        data.write(Int(flags))
        
        data.write(self.media.write())
        
        data.write(Long(self.random_id))
        
        data.write(String(self.message))
        
        if self.entities is not None:
            data.write(Vector(self.entities))
        
        return data.getvalue()
