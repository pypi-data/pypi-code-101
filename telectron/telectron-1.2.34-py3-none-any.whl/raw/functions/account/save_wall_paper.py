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


class SaveWallPaper(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``129``
        - ID: ``0x6c5a5b37``

    Parameters:
        wallpaper: :obj:`InputWallPaper <telectron.raw.base.InputWallPaper>`
        unsave: ``bool``
        settings: :obj:`WallPaperSettings <telectron.raw.base.WallPaperSettings>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["wallpaper", "unsave", "settings"]

    ID = 0x6c5a5b37
    QUALNAME = "functions.account.SaveWallPaper"

    def __init__(self, *, wallpaper: "raw.base.InputWallPaper", unsave: bool, settings: "raw.base.WallPaperSettings") -> None:
        self.wallpaper = wallpaper  # InputWallPaper
        self.unsave = unsave  # Bool
        self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SaveWallPaper":
        # No flags
        
        wallpaper = TLObject.read(data)
        
        unsave = Bool.read(data)
        
        settings = TLObject.read(data)
        
        return SaveWallPaper(wallpaper=wallpaper, unsave=unsave, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.wallpaper.write())
        
        data.write(Bool(self.unsave))
        
        data.write(self.settings.write())
        
        return data.getvalue()
