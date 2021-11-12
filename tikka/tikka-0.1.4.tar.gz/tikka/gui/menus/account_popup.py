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

from tikka.data.account import Account
from tikka.data.pubkey import PublicKey
from tikka.gui.windows.account_unlock import UnlockAccountWindow
from tikka.gui.windows.wallet_load import WalletLoadWindow
from tikka.gui.windows.wallet_save import WalletSaveWindow

if TYPE_CHECKING:
    import _

    from tikka.gui.main_window import MainWindow

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class AccountPopupMenu(wx.Menu):
    """
    Popup menu class

    """

    def __init__(self, main_window: MainWindowType, account: Account):
        """
        Init popup menu instance

        :param main_window: MainWindow instance
        :param account: Account instance
        """
        super().__init__()

        self.main_window = main_window
        self.confirm_dialog = None

        item = wx.MenuItem(
            self,
            wx.Window.NewControlId(),
            _("Copy public key"),  # pylint: disable=used-before-assignment
        )
        self.Append(item)
        self.Bind(
            wx.EVT_MENU, lambda event: self._copy_pubkey_to_clipboard(account), item
        )

        if account.signing_key is None:
            item = wx.MenuItem(
                self, wx.Window.NewControlId(), _("Unlock account access")
            )
            self.Append(item)
            self.Bind(wx.EVT_MENU, lambda event: self._unlock_account(account), item)
            item = wx.MenuItem(self, wx.Window.NewControlId(), _("Unlock by file"))
            self.Append(item)
            self.Bind(wx.EVT_MENU, lambda event: self._unlock_account_by_file(), item)
        else:
            item = wx.MenuItem(self, wx.Window.NewControlId(), _("Lock account access"))
            self.Append(item)
            self.Bind(wx.EVT_MENU, lambda event: self._lock_account(account), item)

            item = wx.MenuItem(self, wx.Window.NewControlId(), _("Save wallet to disk"))
            self.Append(item)
            self.Bind(wx.EVT_MENU, lambda event: self._save_wallet(account), item)

        item = wx.MenuItem(self, wx.Window.NewControlId(), _("Withdraw account"))
        item.SetTextColour("red")
        self.Append(item)
        self.Bind(wx.EVT_MENU, lambda event: self._delete_account(account), item)

    @staticmethod
    def _copy_pubkey_to_clipboard(account):
        """
        Copy public key with checksum to clipboard

        :param account: Account instance
        :return:
        """
        # Write some text to the clipboard
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(
                wx.TextDataObject(str(PublicKey.from_pubkey(account.pubkey)))
            )
            wx.TheClipboard.Close()

    def _unlock_account(self, account: Account):
        """
        Open account unlock window

        :param account: Account instance
        :return:
        """
        UnlockAccountWindow(self.main_window, account).Show()

    def _unlock_account_by_file(self):
        """
        Open load wallet window

        :return:
        """
        WalletLoadWindow(self.main_window).Show()

    def _load_wallet(self):
        """
        Open load wallet window

        :return:
        """
        WalletLoadWindow(self.main_window).Show()

    def _lock_account(self, account: Account):
        """
        Lock account, forgetting credentials

        :param account: Account instance
        :return:
        """
        # application event
        self.main_window.application.accounts.lock_account(account)
        # update GUI
        self.main_window.lock_account(account)

    def _delete_account(self, account: Account) -> None:
        """
        Delete account from list

        :return:
        """
        result = wx.MessageDialog(
            self.main_window,
            _("Withdraw account {pubkey}?").format(
                pubkey=PublicKey.from_pubkey(account.pubkey)
            ),
            style=wx.YES_NO | wx.ICON_EXCLAMATION,
        ).ShowModal()

        if result == wx.ID_NO:
            return

        self.main_window.application.accounts.delete_account(account)
        self.main_window.delete_account()

    def _save_wallet(self, account: Account):
        """
        Open save wallet window

        :param account: Account instance
        :return:
        """
        WalletSaveWindow(self.main_window, account).Show()
