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
from tikka.data.constants import DATA_PATH
from tikka.data.pubkey import PubkeyChecksumNotValid, PubkeyNotValid, PublicKey
from tikka.domains.application import Application
from tikka.gui.images import images

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow
if TYPE_CHECKING:
    import _

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class AddAccountWindow(wx.Frame):
    def __init__(self, parent: MainWindowType):
        """
        Init add account window

        :param parent: Instance of parent widget
        """
        super().__init__(parent)

        self.SetTitle(_("Add account"))  # pylint: disable=used-before-assignment

        self.pubkey = None

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()

        safe_image = images.load(images.safe_with_girl)
        safe_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        safe_bitmap = wx.StaticBitmap(self, -1, safe_image.ConvertToBitmap())

        # pubkey entry
        pubkey_label = wx.StaticText(self, label=_("Public key"))
        pubkey_label.SetFont(default_bold_font)
        self.pubkey_entry = wx.TextCtrl(self)
        self.pubkey_entry.SetMinSize((500, -1))
        self.pubkey_entry.SetFocus()

        # error
        self.error_label = wx.StaticText(self, label=" ")
        self.error_label.SetForegroundColour("red")

        # buttons
        ok = wx.Button(self, label=_("Ok"))
        cancel = wx.Button(self, label=_("Cancel"))

        # layout
        pubkey_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        pubkey_sizer.Add(
            pubkey_label, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10
        )
        pubkey_sizer.Add(self.pubkey_entry, flag=wx.ALL | wx.EXPAND, border=10)

        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer.Add(ok)
        button_sizer.Add(cancel)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(safe_bitmap, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(pubkey_sizer, flag=wx.ALL | wx.EXPAND)
        sizer.Add(self.error_label, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(button_sizer, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizerAndFit(sizer)

        # events
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_ok(), ok)
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_cancel(), cancel)

    def _button_ok(self):
        """
        Ok button handler

        :return:
        """
        entry = self.pubkey_entry.GetValue()
        if ":" in entry:
            base58, checksum = self.pubkey_entry.GetValue().split(":", 2)
            try:
                pubkey = PublicKey(base58, checksum)
            except PubkeyChecksumNotValid:
                self.error_label.SetLabel(_("Checksum is not valid!"))
                self.GetSizer().Layout()
                return
        else:
            try:
                pubkey = PublicKey.from_pubkey(entry)
            except PubkeyNotValid:
                self.error_label.SetLabel(_("Public key is not valid!"))
                self.GetSizer().Layout()
                return

        # create account instance
        account = Account(pubkey.base58)
        for existing_account in self.GetParent().application.accounts.list:
            if account == existing_account:
                self.error_label.SetLabel(_("Account already exists!"))
                self.GetSizer().Layout()
                return

        # add instance in application
        self.GetParent().application.accounts.add_account(account)
        # update gui
        self.GetParent().add_account(account)

        # close window
        self.Close()

    def _button_cancel(self):
        """
        Cancel button handler

        :return:
        """
        # close window
        self.Close()


if __name__ == "__main__":

    app = wx.App()
    # create application with gui
    application = Application(DATA_PATH)
    # create Tk gui
    main_window = MainWindow(None, application)
    about_window = AddAccountWindow(main_window)
    about_window.Show()

    app.MainLoop()
