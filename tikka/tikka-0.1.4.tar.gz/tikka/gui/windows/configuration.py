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

from tikka.adapters.config import Config
from tikka.data.constants import CURRENCIES, DATA_PATH, LANGUAGES
from tikka.domains.application import Application
from tikka.gui.images import images

if TYPE_CHECKING or __name__ == "__main__":
    from tikka.gui.main_window import MainWindow
if TYPE_CHECKING:
    import _

MainWindowType = TypeVar("MainWindowType", bound="MainWindow")

builtins.__dict__["_"] = wx.GetTranslation


class ConfigurationWindow(wx.Frame):
    def __init__(self, parent: MainWindowType, config: Config):
        """
        Init configuration window

        :param parent: Instance of parent widget
        :param config: Config adapter instance
        """
        super().__init__(parent)

        # access to config adapter
        self.config_ = config

        self.SetTitle(_("Configuration"))  # pylint: disable=used-before-assignment

        default_font = self.GetFont()
        default_italic_font = default_font.Italic()

        # images
        config_symbol_image = images.load(images.config_symbol)
        config_symbol_image.Rescale(100, 100, wx.IMAGE_QUALITY_HIGH)
        config_symbol_bitmap = wx.StaticBitmap(
            self, -1, config_symbol_image.ConvertToBitmap()
        )

        # language selection
        self.languages_radio_box = wx.RadioBox(
            self,
            label=_("Language"),
            pos=(0, 0),
            choices=list(LANGUAGES.values()),
            majorDimension=0,
            style=wx.RA_SPECIFY_ROWS,
        )
        self.languages_radio_box.SetSelection(
            list(LANGUAGES.keys()).index(self.config_.get("language"))
        )

        language_warning = wx.StaticText(
            self, label=_("Restart application to apply change")
        )
        language_warning.SetFont(default_italic_font)
        # currency selection
        self.currencies_radio_box = wx.RadioBox(
            self,
            label=_("Currency"),
            pos=(0, 0),
            choices=list(CURRENCIES.values()),
            majorDimension=0,
            style=wx.RA_SPECIFY_ROWS,
        )
        self.currencies_radio_box.SetSelection(
            list(CURRENCIES.keys()).index(self.config_.get("currency"))
        )

        # layout
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(config_symbol_bitmap, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        sizer.Add(self.languages_radio_box, flag=wx.ALL | wx.EXPAND, border=10)
        sizer.Add(language_warning, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
        sizer.Add(self.currencies_radio_box, flag=wx.ALL | wx.EXPAND, border=10)

        self.SetSizerAndFit(sizer)

        # events
        self.Bind(
            wx.EVT_RADIOBOX,
            lambda event: self._select_language(),
            self.languages_radio_box,
        )
        self.Bind(
            wx.EVT_RADIOBOX,
            lambda event: self._select_currency(),
            self.currencies_radio_box,
        )

    def _select_language(self):
        """
        Select language handler

        :return:
        """
        selected_index = self.languages_radio_box.GetSelection()
        self.GetParent().application.select_language(
            list(LANGUAGES.keys())[selected_index]
        )
        self.GetParent().select_language(list(LANGUAGES.keys())[selected_index])

    def _select_currency(self):
        """
        Select currency handler

        :return:
        """
        selected_index = self.currencies_radio_box.GetSelection()
        self.GetParent().application.select_currency(
            list(CURRENCIES.keys())[selected_index]
        )
        self.GetParent().select_currency()


if __name__ == "__main__":

    app = wx.App()
    # create application with gui
    application = Application(DATA_PATH)

    # create Tk gui
    main_window = MainWindow(None, application)
    about_window = ConfigurationWindow(main_window, application.config)
    about_window.Show()

    app.MainLoop()
