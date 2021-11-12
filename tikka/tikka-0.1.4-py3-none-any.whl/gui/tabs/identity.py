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
from typing import TYPE_CHECKING

import wx

from tikka.data.account import Account

if TYPE_CHECKING:
    import _

builtins.__dict__["_"] = wx.GetTranslation


class IdentityPanel(wx.Panel):
    def __init__(self, master: wx.Notebook):
        super().__init__(master)

        default_font = self.GetFont()
        default_bold_font = default_font.Bold()

        uid_label = wx.StaticText(
            self, label=_("Nickname")  # pylint: disable=used-before-assignment
        )
        uid_label.SetFont(default_bold_font)
        self.uid = wx.StaticText(self, label="Not implemented")

        # layout
        grid_sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)
        grid_sizer.Add(uid_label, flag=wx.TOP | wx.LEFT, border=10)
        grid_sizer.Add(self.uid, flag=wx.TOP, border=10)

        self.SetSizerAndFit(grid_sizer)

        # Hide the work in progress
        self.Hide()


if __name__ == "__main__":

    class Application(wx.App):
        def __init__(self):
            super().__init__()
            self.current_account = Account(
                "732SSfuwjB7jkt9th1zerGhphs6nknaCBCTozxUcPWPU"
            )

    class MockMainWindow(wx.Frame):
        def __init__(self, parent, application=None):
            super().__init__(parent)
            self.application = application

    app = Application()

    main_window_ = MockMainWindow(None, application=app)
    notebook = wx.Notebook(main_window_)
    identity_panel = IdentityPanel(notebook)
    notebook.AddPage(identity_panel, _("Identity"))
    main_window_.SetClientSize(notebook.GetBestSize())
    main_window_.Show()

    app.MainLoop()
