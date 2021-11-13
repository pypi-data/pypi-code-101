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

import wx

from tikka.data.constants import DATA_PATH
from tikka.domains.application import Application
from tikka.gui.menus.accounts import AccountsMenu
from tikka.gui.menus.help import HelpMenu

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")


class MenuBar(wx.MenuBar):
    def __init__(self, main_window: MainWindowType):
        """
        Init menubar with main_window

        :param main_window: MainWindow instance
        """
        super().__init__()

        self.Append(
            AccountsMenu(main_window),
            _("&Accounts"),  # pylint: disable=used-before-assignment
        )
        self.Append(HelpMenu(main_window), _("&Help"))


if __name__ == "__main__":
    app = wx.App()
    application = Application(DATA_PATH)
    main_window_ = MainWindow(None, application)

    menuBar = MenuBar(main_window_)

    # Give the menu bar to the frame
    main_window_.SetMenuBar(menuBar)

    main_window_.Show()
    app.MainLoop()
