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

import builtins
from typing import TYPE_CHECKING, Optional, TypeVar

import wx

from tikka import __version__
from tikka.gui.images import images

if TYPE_CHECKING:
    import _

    from tikka.gui.main_window import MainWindow

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class AboutWindow(wx.Frame):
    def __init__(self, parent: Optional[MainWindowType]):
        """
        Init about window

        :param parent: Instance of parent widget
        """
        super().__init__(parent)

        self.SetTitle(_("About"))  # pylint: disable=used-before-assignment
        self.SetBackgroundColour("white")

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()
        default_italic_font = default_font.Italic()

        logo_image = images.load(images.logo)
        logo = wx.StaticBitmap(self, -1, logo_image.ConvertToBitmap())

        description = wx.StaticText(
            self,
            label=_(
                "A desktop client for Duniter.\nManage your Ǧ1 accounts securely and easily!"
            ),
        )
        description.SetFont(default_italic_font)

        version = wx.StaticText(self, label=_(f"Version {__version__}"))
        version.SetFont(default_bold_font)

        authors = ("Vincent Texier",)

        authors_title = wx.StaticText(self, label=_("Author"))
        authors_title.SetFont(default_bold_font)

        # layout
        grid_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        grid_sizer.Add(logo, flag=wx.ALL, border=10)
        grid_sizer.Add(description, flag=wx.ALL, border=10)
        grid_sizer.Add(version, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        grid_sizer.Add(authors_title, flag=wx.ALL | wx.ALIGN_CENTER, border=2)
        for author in authors:
            label = wx.StaticText(self, label=author)
            grid_sizer.Add(label, flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        self.SetSizerAndFit(grid_sizer)


if __name__ == "__main__":

    app = wx.App()

    about_window = AboutWindow(None)
    about_window.Show()

    app.MainLoop()
