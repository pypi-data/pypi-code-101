from __future__ import annotations

from typing import TYPE_CHECKING, List

from .base import MutableTelegramObject

if TYPE_CHECKING:
    from .inline_keyboard_button import InlineKeyboardButton


class InlineKeyboardMarkup(MutableTelegramObject):
    def __init__(self):
        super(InlineKeyboardMarkup, self).__init__()

    """
    This object represents an `inline keyboard <https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating>`_ that appears right next to the message it belongs to.
    **Note:** This will only work in Telegram versions released after 9 April, 2016. Older clients will display *unsupported message*.

    Source: https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List[InlineKeyboardButton]]
    """Array of button rows, each represented by an Array of :class:`aiogram.types.inline_keyboard_button.InlineKeyboardButton` objects"""

    # def add(self, *args):
    #     """
    #     Add buttons
    #     :param args:
    #     :return: self
    #     :rtype: :obj:`types.InlineKeyboardMarkup`
    #     """
    #     row = []
    #     for index, button in enumerate(args, start=1):
    #         row.append(button)
    #         if index % self.row_width == 0:
    #             self.inline_keyboard.append(row)
    #             row = []
    #     if row:
    #         self.inline_keyboard.append(row)
    #     return self
    #
    # def row(self, *args):
    #     """
    #     Add row
    #     :param args:
    #     :return: self
    #     :rtype: :obj:`types.InlineKeyboardMarkup`
    #     """
    #     btn_array = [button for button in args]
    #     self.inline_keyboard.append(btn_array)
    #     return self
    #
    # def insert(self, button):
    #     """
    #     Insert button to last row
    #     :param button:
    #     :return: self
    #     :rtype: :obj:`types.InlineKeyboardMarkup`
    #     """
    #     if self.inline_keyboard and len(self.inline_keyboard[-1]) < self.row_width:
    #         self.inline_keyboard[-1].append(button)
    #     else:
    #         self.add(button)
    #     return self
