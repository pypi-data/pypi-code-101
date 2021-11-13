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
from tikka.gui.windows.about import AboutWindow
from tikka.gui.windows.configuration import ConfigurationWindow
from tikka.gui.windows.licence import LicenceWindow

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")


class HelpMenu(wx.Menu):
    def __init__(self, main_window: MainWindowType):
        """
        Init Help menu with main_window

        :param main_window: MainWindow instance
        """
        super().__init__()

        self.main_window = main_window

        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        licence_item = self.Append(
            -1,
            _("&Ğ1 licence"),  # pylint: disable=used-before-assignment
            _("Display the Ğ1 Licence"),
        )
        configuration_item = self.Append(
            -1, _("&Configuration"), _("Open the configuration window")
        )

        # When using a stock ID we don't need to specify the menu item's
        # label
        about_item = self.Append(wx.ID_ABOUT)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, lambda event: self._open_licence_window(), licence_item)
        self.Bind(
            wx.EVT_MENU,
            lambda event: self._open_configuration_window(),
            configuration_item,
        )
        self.Bind(wx.EVT_MENU, lambda event: self._open_about_window(), about_item)

    def _open_licence_window(self):
        """
        Open licence window

        :return:
        """
        LicenceWindow(self.main_window).Show()

    def _open_configuration_window(self):
        """
        Open configuration window

        :return:
        """
        ConfigurationWindow(
            self.main_window, self.main_window.application.config
        ).Show()

    def _open_about_window(self):
        """
        Open about window

        :return:
        """
        AboutWindow(self.main_window).Show()


if __name__ == "__main__":
    app = wx.App()
    application = Application(DATA_PATH)
    main_window_ = MainWindow(None, application)

    menuBar = wx.MenuBar()
    menuBar.Append(HelpMenu(main_window_), "&Help")

    # Give the menu bar to the frame
    main_window_.SetMenuBar(menuBar)

    main_window_.Show()
    app.MainLoop()
