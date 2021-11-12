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
from typing import TYPE_CHECKING, Optional

import wx

from tikka.data.account import Account
from tikka.data.pubkey import PublicKey
from tikka.gui.images import images
from tikka.gui.menus.account_popup import AccountPopupMenu

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation


class AccountPanel(wx.Panel):
    def __init__(self, parent: wx.Notebook):
        """
        Init account tab frame

        :param parent: Parent Notebook
        """
        super().__init__(parent)

        safe_image = images.load(images.safe)
        safe_image.Rescale(100, 100, wx.IMAGE_QUALITY_HIGH)
        safe_icon = wx.StaticBitmap(self, -1, safe_image.ConvertToBitmap())

        self.balance = wx.StaticText(self, label="0")
        balance_font = self.balance.GetFont().Bold().Scale(4)
        self.balance.SetFont(balance_font)

        locked_image = images.load(images.locked)
        locked_image.Rescale(50, 50, wx.IMAGE_QUALITY_HIGH)
        self.locked_bitmap = locked_image.ConvertToBitmap()
        unlocked_image = images.load(images.unlocked)
        unlocked_image.Rescale(50, 50, wx.IMAGE_QUALITY_HIGH)
        self.unlocked_bitmap = unlocked_image.ConvertToBitmap()
        self.locked_status_icon = wx.StaticBitmap(self, -1, self.locked_bitmap)

        self.pubkey = wx.StaticText(self, label="")
        pubkey_font = self.pubkey.GetFont().Bold()
        self.pubkey.SetFont(pubkey_font)

        # layout
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.grid_sizer = wx.GridBagSizer(vgap=10, hgap=10)
        self.grid_sizer.Add(safe_icon, pos=(0, 0), flag=wx.ALIGN_CENTER, border=10)
        self.grid_sizer.Add(self.balance, pos=(0, 1), flag=wx.ALIGN_CENTER, border=10)
        self.grid_sizer.Add(
            self.locked_status_icon, pos=(1, 0), flag=wx.ALIGN_CENTER, border=10
        )
        self.grid_sizer.Add(
            self.pubkey, pos=(1, 1), flag=wx.TOP | wx.ALIGN_CENTER_VERTICAL, border=10
        )

        sizer.Add(self.grid_sizer, flag=wx.ALL | wx.CENTER, border=10)

        self.SetSizer(sizer)

        self.set_account(self.GetGrandParent().application.accounts.current_account)  # type: ignore

        # events
        safe_icon.Bind(wx.EVT_RIGHT_DOWN, lambda event: self._right_click())
        self.balance.Bind(
            wx.EVT_RIGHT_DOWN,
            lambda event: self._right_click(),
        )
        self.locked_status_icon.Bind(
            wx.EVT_RIGHT_DOWN,
            lambda event: self._right_click(),
            self.locked_status_icon,
        )
        self.pubkey.Bind(wx.EVT_RIGHT_DOWN, lambda event: self._right_click())
        self.Bind(wx.EVT_RIGHT_DOWN, lambda event: self._right_click())

    def _right_click(self):
        """
        Display popup menu on listbox

        :return:
        """

        # create popup menu
        popup_menu = AccountPopupMenu(
            self.GetGrandParent(),
            self.GetGrandParent().application.accounts.current_account,
        )

        # show popup menu
        self.PopupMenu(popup_menu)

    def set_account(self, account: Optional[Account]):
        """
        Set account to display

        :param account: Account instance
        :return:
        """
        if account is None:
            self.Hide()
        else:
            self.Show()
            self.balance.SetLabel("0")
            self.set_unlock_status(account)
            self.pubkey.SetLabel(str(PublicKey.from_pubkey(account.pubkey)))

            self.Layout()

    def set_unlock_status(self, account: Account):
        """
        Set access status in display from account

        :param account: Account instance
        :return:
        """
        self.locked_status_icon.SetBitmap(
            self.locked_bitmap if account.signing_key is None else self.unlocked_bitmap
        )
        self.locked_status_icon.Layout()


if __name__ == "__main__":

    class AccountsMock:
        current_account = Account("732SSfuwjB7jkt9th1zerGhphs6nknaCBCTozxUcPWPU")

    class Application(wx.App):
        def __init__(self):
            super().__init__()
            self.accounts = AccountsMock()

    class MockMainWindow(wx.Frame):
        def __init__(self, parent, application=None):
            super().__init__(parent)
            self.application = application

    app = Application()

    main_window_ = MockMainWindow(None, application=app)
    notebook = wx.Notebook(main_window_)
    account_panel = AccountPanel(notebook)
    notebook.AddPage(
        account_panel, _("Account")  # pylint: disable=used-before-assignment
    )
    main_window_.SetClientSize(notebook.GetBestSize())
    main_window_.Show()

    app.MainLoop()
