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
from typing import TYPE_CHECKING, TypeVar

import markdown
import wx
from wx.html import HtmlWindow

from tikka.data.constants import DATA_PATH, LOCALES_PATH
from tikka.domains.application import Application

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow
if TYPE_CHECKING:
    import _

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class LicenceWindow(wx.Frame):
    def __init__(self, parent: MainWindowType):
        """
        Init licence window

        :param parent: Instance of parent widget
        """
        super().__init__(parent)

        self.SetTitle(_("Ğ1 licence"))  # pylint: disable=used-before-assignment
        self.SetSize((800, 600))

        with open(
            LOCALES_PATH.joinpath(
                self.GetParent().application.config.get("language"), "licence_g1.txt"
            ),
            "r",
            encoding="utf-8",
        ) as input_file:
            text = input_file.read()
        html = markdown.markdown(text)

        html_display = HtmlWindow(self)
        html_display.SetPage(html)

        sizer = wx.BoxSizer()
        sizer.Add(html_display, 1, wx.EXPAND)

        self.SetSizer(sizer)


if __name__ == "__main__":

    app = wx.App()
    # create application with gui
    application = Application(DATA_PATH)

    # create Tk gui
    main_window = MainWindow(None, application)
    about_window = LicenceWindow(main_window)
    about_window.Show()

    app.MainLoop()
