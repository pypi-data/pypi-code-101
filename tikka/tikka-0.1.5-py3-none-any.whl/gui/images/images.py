# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import wx

# images index
from tikka.data.constants import IMAGES_PATH

logo = ("logo_tikka_01.jpeg", wx.BITMAP_TYPE_JPEG)
safe = ("safe_400x400.png", wx.BITMAP_TYPE_PNG)
safe_with_background = ("safe_with_background.png", wx.BITMAP_TYPE_PNG)
safe_with_girl = ("safe_with_girl_400x400.png", wx.BITMAP_TYPE_PNG)
locked = ("locked_cartoon_400x400.png", wx.BITMAP_TYPE_PNG)
unlocked = ("unlocked_cartoon_400x400.png", wx.BITMAP_TYPE_PNG)
keys = ("keys.png", wx.BITMAP_TYPE_PNG)
hard_disk = ("hard_disk.png", wx.BITMAP_TYPE_PNG)
arrow_left = ("arrow_left.png", wx.BITMAP_TYPE_PNG)
arrow_right = ("arrow_right.png", wx.BITMAP_TYPE_PNG)
config_symbol = ("config_symbol.png", wx.BITMAP_TYPE_PNG)


def load(image_attributes: tuple) -> wx.Image:
    """
    Load image file in wxPython

    :param image_attributes: (filename, type)

    :return:
    """
    filename, _type = image_attributes
    image = wx.Image(str(IMAGES_PATH.joinpath(filename)), _type)
    return image
