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

from telectron import raw
from telectron import types
from telectron.scaffold import Scaffold


class CreateSupergroup(Scaffold):
    async def create_supergroup(
        self,
        title: str,
        description: str = ""
    ) -> "types.Chat":
        """Create a new supergroup.

        .. note::

            If you want to create a new basic group, use :meth:`~telectron.Client.create_group` instead.

        Parameters:
            title (``str``):
                The supergroup title.

            description (``str``, *optional*):
                The supergroup description.

        Returns:
            :obj:`~telectron.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                app.create_supergroup("Supergroup Title", "Supergroup Description")
        """
        r = await self.send(
            raw.functions.channels.CreateChannel(
                title=title,
                about=description,
                megagroup=True
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
