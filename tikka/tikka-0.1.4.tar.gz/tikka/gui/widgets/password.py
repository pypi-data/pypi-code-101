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

import wx


class PasswordCtrl(wx.Panel):
    def __init__(self, parent: wx.Object):
        super().__init__(parent)

        # hidden status
        self.password_hidden = True

        # widgets
        self.hidden_password_entry = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.clear_password_entry = wx.TextCtrl(self)
        self.clear_password_entry.Hide()

        # layout
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.hidden_password_entry, flag=wx.EXPAND)
        sizer.Add(self.clear_password_entry, flag=wx.EXPAND)
        self.SetSizer(sizer)

    def SetFocus(self):
        """
        Set focus on entry

        :return:
        """
        if self.password_hidden:
            self.hidden_password_entry.SetFocus()
        else:
            self.clear_password_entry.SetFocus()

    def SetValue(self, value: str):
        """
        Set entry value

        :param value: Value to set in entry
        :return:
        """
        self.hidden_password_entry.SetValue(value)
        self.clear_password_entry.SetValue(value)

    def GetValue(self) -> str:
        """
        Return entry value

        :return:
        """
        if self.password_hidden:
            return self.hidden_password_entry.GetValue()

        return self.clear_password_entry.GetValue()

    def ToggleHiddenMode(self):
        """
        Toggle hidden password mode

        :param _: dummy event
        :return:
        """
        self.password_hidden = not self.password_hidden
        self.clear_password_entry.Show(not self.password_hidden)
        self.hidden_password_entry.Show(self.password_hidden)
        if self.password_hidden:
            self.hidden_password_entry.SetValue(self.clear_password_entry.GetValue())
            self.hidden_password_entry.SetFocus()
        else:
            self.clear_password_entry.SetValue(self.hidden_password_entry.GetValue())
            self.clear_password_entry.SetFocus()
        self.clear_password_entry.GetParent().Layout()

    def Bind(self, *args, **kwargs):
        """
        Overide event binding to entry widgets

        :param args:*args
        :param kwargs: **kwargs
        :return:
        """
        self.clear_password_entry.Bind(*args, **kwargs)
        self.hidden_password_entry.Bind(*args, **kwargs)


if __name__ == "__main__":
    wx_app = wx.App()

    main_window = wx.Frame(None)
    password = PasswordCtrl(main_window)
    password.SetMinSize((200, -1))

    toggle_button = wx.Button(main_window, label="toggle view")
    main_window.Bind(
        wx.EVT_BUTTON, lambda event: password.ToggleHiddenMode(), toggle_button
    )
    password.Bind(
        wx.EVT_KEY_DOWN, lambda event: print(event.GetKeyCode(), event.GetRawKeyCode())
    )

    sizer_ = wx.BoxSizer()
    sizer_.Add(password)
    sizer_.Add(toggle_button, wx.EXPAND)
    main_window.SetSizer(sizer_)

    main_window.Show()
    # start gui event loop
    wx_app.MainLoop()
