#  telectron - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of telectron.
#
#  telectron is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  telectron is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with telectron.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Callable

import telectron
from telectron.filters import Filter
from telectron.types import Message
from .handler import Handler


class DeletedMessagesHandler(Handler):
    """The deleted messages handler class. Used to handle deleted messages coming from any chat
    (private, group, channel). It is intended to be used with :meth:`~telectron.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~telectron.Client.on_deleted_messages` decorator.

    Parameters:
        callback (``callable``):
            Pass a function that will be called when one or more messages have been deleted.
            It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~telectron.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        messages (List of :obj:`~telectron.types.Message`):
            The deleted messages, as list.
    """

    def __init__(self, callback: Callable, filters: Filter = None):
        super().__init__(callback, filters)

    async def check(self, client: "telectron.Client", update: List[Message]):
        return await self.execute_filters(self.filters, client, update)

    @staticmethod
    async def execute_filters(filters, client, update: List[Message]):
        # Every message should be checked, if at least one matches the filter True is returned
        # otherwise, or if the list is empty, False is returned
        for message in update:
            if await Handler.execute_filters(filters, client, message):
                return True
        else:
            return False