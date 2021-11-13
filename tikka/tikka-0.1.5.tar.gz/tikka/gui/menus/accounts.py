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
from tikka.gui.windows.account_add import AddAccountWindow
from tikka.gui.windows.account_create import CreateAccountWindow
from tikka.gui.windows.account_list import AccountListWindow
from tikka.gui.windows.wallet_load import WalletLoadWindow

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")


class AccountsMenu(wx.Menu):
    def __init__(self, main_window: MainWindowType):
        """
        Init accounts menu with main_window

        :param main_window: MainWindow instance
        """
        super().__init__()

        self.main_window = main_window

        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        account_list_item = self.Append(
            -1,
            _("&Account list\tCtrl-L"),  # pylint: disable=used-before-assignment
            _("Open the account list"),
        )
        self.AppendSeparator()
        add_account_item = self.Append(
            -1,
            _("&Add an existing account"),
            _("Add an existing account by its public key"),
        )
        create_account_item = self.Append(
            -1,
            _("&Create an account"),
            _("Create an account with an automatically generated access code"),
        )
        load_wallet_item = self.Append(
            -1,
            _("&Load a wallet"),
            _("Load a wallet to add a new account or unlock existing one"),
        )
        self.AppendSeparator()

        # When using a stock ID we don't need to specify the menu item's
        # label
        exit_item = self.Append(wx.ID_EXIT)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(
            wx.EVT_MENU,
            lambda event: self._open_account_list_window(),
            account_list_item,
        )
        self.Bind(
            wx.EVT_MENU, lambda event: self._open_add_account_window(), add_account_item
        )
        self.Bind(
            wx.EVT_MENU,
            lambda event: self._open_create_account_window(),
            create_account_item,
        )
        self.Bind(
            wx.EVT_MENU, lambda event: self._open_load_wallet_window(), load_wallet_item
        )
        self.Bind(wx.EVT_MENU, lambda event: self._exit(), exit_item)

    def _open_account_list_window(self):
        """
        Open account list window

        :return:
        """
        AccountListWindow(self.main_window).Show()

    def _open_add_account_window(self):
        """
        Open add account window

        :return:
        """
        AddAccountWindow(self.main_window).Show()

    def _open_create_account_window(self):
        """
        Open create account window

        :return:
        """
        CreateAccountWindow(self.main_window).Show()

    def _open_load_wallet_window(self):
        """
        Open load wallet window

        :return:
        """
        WalletLoadWindow(self.main_window).Show()

    def _exit(self):
        """
        Close the main window, terminating the application.

        :return:
        """
        self.main_window.Close(True)


if __name__ == "__main__":
    app = wx.App()
    application = Application(DATA_PATH)
    main_window_ = MainWindow(None, application)
    menuBar = wx.MenuBar()
    menuBar.Append(AccountsMenu(main_window_), "&Accounts")

    # Give the menu bar to the frame
    main_window_.SetMenuBar(menuBar)

    main_window_.Show()
    app.MainLoop()
