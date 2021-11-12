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
import sys
from typing import TYPE_CHECKING

import wx

from tikka import __version__
from tikka.data.account import Account
from tikka.data.constants import CURRENCIES
from tikka.domains.application import Application
from tikka.gui.menus.menubar import MenuBar
from tikka.gui.tabs.account import AccountPanel
from tikka.gui.tabs.identity import IdentityPanel

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation

# supported languages
supported_languages = {
    "en_US": wx.LANGUAGE_ENGLISH,
    "fr_FR": wx.LANGUAGE_FRENCH,
}


class MainWindow(wx.Frame):
    """
    Top level Frame window class
    """

    account_list_window = None

    def __init__(self, parent, application: Application):
        """
        Init top level window
        """
        super().__init__(parent)

        self.application = application
        self.locale = None

        # configuration
        self.update_title()
        self.select_language(self.application.config.get("language"))

        # Add the menu bar to the frame
        self.SetMenuBar(MenuBar(self))

        # create tabs
        self.notebook = wx.Notebook(self)
        self.account_panel = AccountPanel(self.notebook)
        if self.application.accounts.current_account:
            self.account_panel.set_account(self.application.accounts.current_account)
        self.identity_panel = IdentityPanel(self.notebook)
        self.notebook.AddPage(
            self.account_panel, _("Account")  # pylint: disable=used-before-assignment
        )
        self.notebook.AddPage(self.identity_panel, _("Identity"))
        self.notebook.SetSelection(0)

        self.SetClientSize(self.notebook.GetBestSize())

        self.SetStatusBar(wx.StatusBar(self))

        # layout
        self.SetSize((800, 600))

    def update_title(self):
        """
        Update window title with version and currency

        :return:
        """
        self.SetTitle(
            "Tikka {version} - {currency}".format(  # pylint: disable=consider-using-f-string
                version=__version__,
                currency=CURRENCIES[self.application.config.get("currency")],
            )
        )

    def add_account(self, account: Account):
        """
        Add account in the list

        :param account: Account instance
        :return:
        """
        if self.account_list_window:
            self.account_list_window.add_account(account)
            self.account_list_window.select_current_account()

        # update gui
        self.account_panel.set_account(account)

    def select_account(self, account: Account):
        """
        Selected account from list

        :param account: Account instance
        :return:
        """
        # update gui
        self.account_panel.set_account(account)

    def delete_account(self):
        """
        Delete account from list

        :return:
        """
        if self.account_list_window:
            self.account_list_window.reset_listctrl()
        self.account_panel.set_account(self.application.accounts.current_account)

    def unlock_account(self, account: Account):
        """
        Unlock account event

        :param account: Account instance
        :return:
        """
        if account == self.application.accounts.current_account:
            # update account panel
            self.account_panel.set_unlock_status(account)

        if self.account_list_window:
            # update account in listbox
            self.account_list_window.update_account(account)

    def lock_account(self, account: Account):
        """
        Lock account event

        :param account: Account instance
        :return:
        """
        if account == self.application.accounts.current_account:
            # update account panel
            self.account_panel.set_unlock_status(account)

        if self.account_list_window:
            # update account in listbox
            self.account_list_window.update_account(account)

    def load_wallet(self, account: Account, new: bool):
        """
        Load wallet to create/update account

        :param account: Account instance
        :param new: True if the wallet created a new account, False otherwise
        :return:
        """
        if self.account_list_window:
            if new:
                self.add_account(account)
            else:
                # update account in list
                self.account_list_window.update_account(account)
        if account == self.application.accounts.current_account:
            # update account tab
            self.account_panel.set_account(account)

    def save_wallet(self, account):
        """
        Save wallet of account

        :param account: Account instance
        :return:
        """

    def select_language(self, language: str):
        """
        Update the language to the requested one.

        Make *sure* any existing locale is deleted before the new
        one is created.  The old C++ object needs to be deleted
        before the new one is created, and if we just assign a new
        instance to the old Python variable, the old C++ locale will
        not be destroyed soon enough, likely causing a crash.

        :param language: one of the supported language codes

        """
        # if an unsupported language is requested default to English
        selected_language_code = supported_languages.get(language, wx.LANGUAGE_ENGLISH)

        if self.locale:
            assert sys.getrefcount(self.locale) <= 2
            del self.locale

        # create a locale object for this language
        self.locale = wx.Locale(selected_language_code)
        if self.locale is not None and not self.locale.IsOk():
            self.locale = None

    def select_currency(self):
        """
        :return:
        """
        self.update_title()

        # update list
        if self.account_list_window:
            self.account_list_window.reset_listctrl()

        # update tabs
        self.account_panel.set_account(self.application.accounts.current_account)
