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
from tikka.data.constants import ACCESS_TYPE_MNEMONIC, DATA_PATH
from tikka.data.pubkey import PublicKey
from tikka.data.signing_key import TikkaSigningKey
from tikka.domains.application import Application
from tikka.gui.images import images
from tikka.libs.secret import generate_mnemonic

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow
if TYPE_CHECKING:
    import _

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class CreateAccountWindow(wx.Frame):
    def __init__(self, parent: MainWindowType):
        """
        Init create account window

        :param parent: Instance of parent widget
        """
        super().__init__(parent)

        self.SetTitle(_("Create account"))  # pylint: disable=used-before-assignment

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()

        safe_image = images.load(images.safe_with_background)
        safe_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        safe_bitmap = wx.StaticBitmap(self, -1, safe_image.ConvertToBitmap())

        # access code
        self.access_code_label = wx.StaticText(self, label=_("Access code"))
        self.access_code_label.SetFont(default_bold_font)
        self.access_code_value = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.access_code_value.SetMinSize((700, -1))
        self.access_code_value.SetFocus()

        # public key
        self.pubkey_label = wx.StaticText(self, label=_("Public key"))
        self.pubkey_label.SetFont(default_bold_font)
        self.pubkey_value = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.pubkey_value.SetMinSize((500, -1))

        # change button
        change = wx.Button(self, label=_("Change"))

        # buttons
        ok = wx.Button(self, label=_("Ok"))
        cancel = wx.Button(self, label=_("Cancel"))

        # layout
        access_code_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        access_code_sizer.Add(
            self.access_code_label, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10
        )
        access_code_sizer.Add(
            self.access_code_value, flag=wx.ALL | wx.EXPAND, border=10
        )

        public_key_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        public_key_sizer.Add(
            self.pubkey_label, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10
        )
        public_key_sizer.Add(self.pubkey_value, flag=wx.ALL | wx.EXPAND, border=10)

        buttons_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        buttons_sizer.Add(ok)
        buttons_sizer.Add(cancel)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(safe_bitmap, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(access_code_sizer, flag=wx.ALL, border=10)
        sizer.Add(public_key_sizer, flag=wx.ALL, border=10)
        sizer.Add(change, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(buttons_sizer, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizerAndFit(sizer)

        # events
        self.Bind(
            wx.EVT_BUTTON, lambda event: self._generate_mnemonic_and_pubkey(), change
        )
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_ok(), ok)
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_cancel(), cancel)

        self._generate_mnemonic_and_pubkey()

    def _generate_mnemonic_and_pubkey(self):
        """
        Generate mnemonic access_code and pubkey

        :return:
        """
        access_code = generate_mnemonic(
            self.GetParent().application.config.get("language")
        )
        self.access_code_value.SetValue(access_code)
        self.pubkey_value.SetValue(
            str(
                PublicKey.from_pubkey(
                    TikkaSigningKey.from_dubp_mnemonic(access_code).pubkey
                )
            )
        )

    def _button_ok(self):
        """
        Ok button handler

        :return:
        """
        # create pubkey instance
        pubkey = PublicKey.from_str(self.pubkey_value.GetValue())
        # create account instance
        account = Account(pubkey.base58, access_type=ACCESS_TYPE_MNEMONIC)
        # add instance in application
        self.GetParent().application.accounts.add_account(account)
        # update GUI
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
    about_window = CreateAccountWindow(main_window)
    about_window.Show()

    app.MainLoop()
