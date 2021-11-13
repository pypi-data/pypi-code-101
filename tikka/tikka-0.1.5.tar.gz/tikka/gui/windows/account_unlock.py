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
import logging
from typing import TYPE_CHECKING, TypeVar

import wx

from tikka.data.account import Account
from tikka.data.constants import ACCESS_TYPE_CLASSIC, ACCESS_TYPE_MNEMONIC, DATA_PATH
from tikka.data.pubkey import PublicKey
from tikka.domains.application import Application
from tikka.gui.images import images
from tikka.gui.widgets.password import PasswordCtrl

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow
if TYPE_CHECKING:
    import _

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class UnlockAccountWindow(wx.Frame):
    def __init__(self, parent: MainWindowType, account: Account):
        """
        Init unlock account window

        :param parent: Instance of parent widget
        :param account: Account instance
        """
        super().__init__(parent)

        self.SetTitle(
            _("Unlock account access")  # pylint: disable=used-before-assignment
        )

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()

        # images
        locked_image = images.load(images.locked)
        locked_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        locked_bitmap = wx.StaticBitmap(self, -1, locked_image.ConvertToBitmap())

        arrow_right_image = images.load(images.arrow_right)
        arrow_right_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        arrow_right_bitmap = wx.StaticBitmap(
            self, -1, arrow_right_image.ConvertToBitmap()
        )

        unlocked_image = images.load(images.unlocked)
        unlocked_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        unlocked_bitmap = wx.StaticBitmap(self, -1, unlocked_image.ConvertToBitmap())

        # variables
        self.account = account

        # public key
        pubkey_label = wx.StaticText(self, label=_("Public key"))
        pubkey_label.SetFont(default_bold_font)
        self.pubkey_value = wx.StaticText(
            self, label=str(PublicKey.from_pubkey(self.account.pubkey))
        )

        # access code
        access_code_label = wx.StaticText(self, label=_("Access code"))
        access_code_label.SetFont(default_bold_font)
        self.access_code_entry = PasswordCtrl(self)
        self.access_code_entry.SetMinSize((700, -1))
        self.access_code_entry.SetFocus()
        access_code_button = wx.Button(self, label=_("View"))

        # password
        password_label = wx.StaticText(self, label=_("Password"))
        password_label.SetFont(default_bold_font)
        self.password_entry = PasswordCtrl(self)
        self.password_entry.SetMinSize((700, -1))
        password_button = wx.Button(self, label=_("View"))

        # error
        self.error_label = wx.StaticText(self, label=" ")
        self.error_label.SetForegroundColour("red")

        # buttons
        ok = wx.Button(self, label=_("Ok"))
        cancel = wx.Button(self, label=_("Cancel"))

        # layout
        images_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        images_sizer.Add(locked_bitmap)
        images_sizer.Add(arrow_right_bitmap)
        images_sizer.Add(unlocked_bitmap)

        access_code_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        access_code_sizer.Add(self.access_code_entry)
        access_code_sizer.Add(access_code_button)
        password_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        password_sizer.Add(self.password_entry)
        password_sizer.Add(password_button)

        form_sizer = wx.FlexGridSizer(rows=5, cols=2, hgap=5, vgap=5)
        form_sizer.Add(pubkey_label)
        form_sizer.Add(self.pubkey_value)
        form_sizer.Add(access_code_label, flag=wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(access_code_sizer)
        # if no wallet, we may need password...
        if self.account.access_type != ACCESS_TYPE_MNEMONIC:
            form_sizer.Add(password_label, flag=wx.ALIGN_CENTER_VERTICAL)
            form_sizer.Add(password_sizer)
        else:
            password_label.Hide()
            self.password_entry.Hide()
            password_button.Hide()

        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer.Add(ok)
        button_sizer.Add(cancel)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(images_sizer, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(form_sizer, flag=wx.ALL | wx.EXPAND, border=10)
        sizer.Add(self.error_label, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(button_sizer, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizerAndFit(sizer)

        # events
        self.Bind(
            wx.EVT_BUTTON,
            lambda event: self.access_code_entry.ToggleHiddenMode(),
            access_code_button,
        )
        self.Bind(
            wx.EVT_BUTTON,
            lambda event: self.password_entry.ToggleHiddenMode(),
            password_button,
        )
        self.access_code_entry.Bind(wx.EVT_KEY_DOWN, self._on_key_press)
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_ok(), ok)
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_cancel(), cancel)

    def _on_key_press(self, event: wx.KeyEvent):
        """
        Detect Enter or Return keys to validate access code if no password required

        :param event: wx.KeyEvent instance
        :return:
        """
        # if only access code required and keypress is Return or NP Enter
        if not self.password_entry.IsShown() and (
            event.GetKeyCode() == wx.WXK_RETURN
            or event.GetKeyCode() == wx.WXK_NUMPAD_ENTER
        ):
            self._button_ok()
        else:
            event.Skip()

    def _button_ok(self):
        """
        Ok button handler

        :return:
        """
        password = (
            None
            if self.password_entry.GetValue().strip() == ""
            else self.password_entry.GetValue().strip()
        )
        access_code = self.access_code_entry.GetValue().strip()

        if self.account.access_type is None:
            # save the account access type
            self.account.access_type = (
                ACCESS_TYPE_MNEMONIC if password is None else ACCESS_TYPE_CLASSIC
            )
            self.GetParent().application.accounts.update_account(self.account)

        try:
            result = self.GetParent().application.accounts.unlock_account(
                self.account, access_code, password
            )
        except Exception as exception:
            logging.error(exception)
            self.error_label.SetLabel(_("Access code is not valid!"))
            self.GetSizer().Layout()
            return

        if result:
            # activate event in main window
            self.GetParent().unlock_account(self.account)
            # close window
            self.Destroy()
        else:
            self.error_label.SetLabel(_("Access code is not valid!"))
            self.GetSizer().Layout()

    def _button_cancel(self):
        """
        Cancel button handler

        :return:
        """
        # close window
        self.Close()


if __name__ == "__main__":
    wx_app = wx.App()
    # create application with gui
    application = Application(DATA_PATH)
    # create Tk gui
    main_window = MainWindow(None, application)
    _account = Account("H5RS687NT622b9LWyjdtR8BuHrAdREn3y5XpuYWkzAMk")
    UnlockAccountWindow(main_window, _account).Show()

    # start gui event loop
    wx_app.MainLoop()
