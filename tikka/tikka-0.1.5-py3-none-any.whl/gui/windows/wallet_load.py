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


class WalletLoadWindow(wx.Frame):
    def __init__(self, parent: MainWindowType):
        """
        Init wallet load window

        :param parent: Instance of parent widget
        """
        super().__init__(parent)

        # variables
        self.wallet = None

        self.SetTitle(
            _("Load wallet from disk")  # pylint: disable=used-before-assignment
        )

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()

        keys_image = images.load(images.keys)
        keys_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        keys_bitmap = wx.StaticBitmap(self, -1, keys_image.ConvertToBitmap())

        arrow_right_image = images.load(images.arrow_right)
        arrow_right_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        arrow_right_bitmap = wx.StaticBitmap(
            self, -1, arrow_right_image.ConvertToBitmap()
        )

        disk_image = images.load(images.hard_disk)
        disk_image.Rescale(200, 200, wx.IMAGE_QUALITY_HIGH)
        disk_bitmap = wx.StaticBitmap(self, -1, disk_image.ConvertToBitmap())

        # path to wallet
        path_label = wx.StaticText(self, label=_("Path"))
        path_label.SetFont(default_bold_font)
        self.path_value = wx.StaticText(self)

        # browse
        self.browse_button = wx.Button(self, label=_("Browse disk..."))

        # access_code entry
        access_code_label = wx.StaticText(self, label=_("Access code"))
        access_code_label.SetFont(default_bold_font)
        self.access_code_entry = PasswordCtrl(self)
        self.access_code_entry.SetMinSize((300, -1))
        access_code_view_button = wx.Button(
            self,
            label=_("View"),
        )

        # public key label
        self.pubkey_label = wx.StaticText(self, label=_("Public key"))
        self.pubkey_label.SetFont(default_bold_font)
        self.pubkey_value = wx.StaticText(self)

        # error
        self.error_label = wx.StaticText(self, label=" ")
        self.error_label.SetForegroundColour("red")

        # buttons
        self.ok_button = wx.Button(self, label=_("Ok"))
        cancel = wx.Button(self, label=_("Cancel"))
        self.ok_button.Disable()

        # layout
        images_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        images_sizer.Add(disk_bitmap)
        images_sizer.Add(arrow_right_bitmap)
        images_sizer.Add(keys_bitmap)

        access_code_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        access_code_sizer.Add(self.access_code_entry)
        access_code_sizer.Add(access_code_view_button)

        form_sizer = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        form_sizer.Add(path_label, flag=wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.path_value)
        form_sizer.Add(access_code_label, flag=wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(access_code_sizer)
        form_sizer.Add(self.pubkey_label, flag=wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.pubkey_value)

        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer.Add(self.ok_button)
        button_sizer.Add(cancel)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(images_sizer)
        sizer.Add(self.browse_button, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(form_sizer, flag=wx.ALL | wx.EXPAND, border=10)
        sizer.Add(self.error_label, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(button_sizer, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizerAndFit(sizer)

        # events
        self.Bind(wx.EVT_BUTTON, lambda event: self._get_path(), self.browse_button)
        self.Bind(
            wx.EVT_BUTTON,
            lambda event: self.access_code_entry.ToggleHiddenMode(),
            access_code_view_button,
        )
        self.access_code_entry.Bind(wx.EVT_KEY_DOWN, self._on_key_press_unlock)

        self.Bind(wx.EVT_BUTTON, lambda event: self._button_ok(), self.ok_button)
        self.Bind(wx.EVT_BUTTON, lambda event: self._button_cancel(), cancel)

    def _get_path(self):
        """
        Browse button handler

        :return:
        """
        # otherwise ask the user what new file to open
        with wx.FileDialog(
            self,
            "Load wallet from disk",
            wildcard=_(
                "All files (*.*)|*.*|DEWIF files (*.dewif)|*.dewif|EWIF files (*.ewif)|*.ewif"
            ),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = file_dialog.GetPath()

        self.path_value.SetLabel(pathname)
        self.GetSizer().Fit(self)

    def _on_key_press_unlock(self, event: wx.KeyEvent):
        """
        Detect Enter or Return keys to validate access code

        :param event: wx.KeyEvent instance
        :return:
        """
        # if only access code required and keypress is Return or NP Enter
        if (
            not event.GetKeyCode() == wx.WXK_RETURN
            and not event.GetKeyCode() == wx.WXK_NUMPAD_ENTER
        ):
            event.Skip()
            return
        self._unlock()

    def _unlock(self):
        """
        Unlock handler

        :return:
        """
        access_code = self.access_code_entry.GetValue()
        if access_code != "":
            try:
                self.wallet = self.GetParent().application.wallets.get(
                    self.path_value.GetLabel(), access_code
                )
            except Exception:
                self.error_label.SetLabel(_("Unable to decrypt file!"))
                self.GetSizer().Layout()
                return
            if not self.wallet.signing_key:
                self.error_label.SetLabel(_("Access code is not valid!"))
                self.GetSizer().Layout()
                return
        else:
            return
        self.error_label.SetLabel("")
        self.pubkey_value.SetLabel(
            str(PublicKey.from_pubkey(self.wallet.signing_key.pubkey))
        )
        self.ok_button.Enable()

    def _button_ok(self):
        """
        Ok button event

        :return:
        """
        accounts_count_before_load = len(self.GetParent().application.accounts.list)
        account = self.GetParent().application.accounts.load_wallet(self.wallet)
        self.GetParent().load_wallet(
            account,
            accounts_count_before_load
            < len(self.GetParent().application.accounts.list),
        )

        # close window
        self.Close()

    def _button_cancel(self):
        """
        Cancel button event

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
    WalletLoadWindow(main_window).Show()

    # start gui event loop
    wx_app.MainLoop()
