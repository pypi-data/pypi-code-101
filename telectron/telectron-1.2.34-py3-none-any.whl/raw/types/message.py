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

from io import BytesIO

from telectron.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from telectron.raw.core import TLObject
from telectron import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class Message(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~telectron.raw.base.Message`.

    Details:
        - Layer: ``129``
        - ID: ``0xbce383d2``

    Parameters:
        id: ``int`` ``32-bit``
        peer_id: :obj:`Peer <telectron.raw.base.Peer>`
        date: ``int`` ``32-bit``
        message: ``str``
        out (optional): ``bool``
        mentioned (optional): ``bool``
        media_unread (optional): ``bool``
        silent (optional): ``bool``
        post (optional): ``bool``
        from_scheduled (optional): ``bool``
        legacy (optional): ``bool``
        edit_hide (optional): ``bool``
        pinned (optional): ``bool``
        from_id (optional): :obj:`Peer <telectron.raw.base.Peer>`
        fwd_from (optional): :obj:`MessageFwdHeader <telectron.raw.base.MessageFwdHeader>`
        via_bot_id (optional): ``int`` ``32-bit``
        reply_to (optional): :obj:`MessageReplyHeader <telectron.raw.base.MessageReplyHeader>`
        media (optional): :obj:`MessageMedia <telectron.raw.base.MessageMedia>`
        reply_markup (optional): :obj:`ReplyMarkup <telectron.raw.base.ReplyMarkup>`
        entities (optional): List of :obj:`MessageEntity <telectron.raw.base.MessageEntity>`
        views (optional): ``int`` ``32-bit``
        forwards (optional): ``int`` ``32-bit``
        replies (optional): :obj:`MessageReplies <telectron.raw.base.MessageReplies>`
        edit_date (optional): ``int`` ``32-bit``
        post_author (optional): ``str``
        grouped_id (optional): ``int`` ``64-bit``
        restriction_reason (optional): List of :obj:`RestrictionReason <telectron.raw.base.RestrictionReason>`
        ttl_period (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "peer_id", "date", "message", "out", "mentioned", "media_unread", "silent", "post", "from_scheduled", "legacy", "edit_hide", "pinned", "from_id", "fwd_from", "via_bot_id", "reply_to", "media", "reply_markup", "entities", "views", "forwards", "replies", "edit_date", "post_author", "grouped_id", "restriction_reason", "ttl_period"]

    ID = 0xbce383d2
    QUALNAME = "types.Message"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer", date: int, message: str, out: Union[None, bool] = None, mentioned: Union[None, bool] = None, media_unread: Union[None, bool] = None, silent: Union[None, bool] = None, post: Union[None, bool] = None, from_scheduled: Union[None, bool] = None, legacy: Union[None, bool] = None, edit_hide: Union[None, bool] = None, pinned: Union[None, bool] = None, from_id: "raw.base.Peer" = None, fwd_from: "raw.base.MessageFwdHeader" = None, via_bot_id: Union[None, int] = None, reply_to: "raw.base.MessageReplyHeader" = None, media: "raw.base.MessageMedia" = None, reply_markup: "raw.base.ReplyMarkup" = None, entities: Union[None, List["raw.base.MessageEntity"]] = None, views: Union[None, int] = None, forwards: Union[None, int] = None, replies: "raw.base.MessageReplies" = None, edit_date: Union[None, int] = None, post_author: Union[None, str] = None, grouped_id: Union[None, int] = None, restriction_reason: Union[None, List["raw.base.RestrictionReason"]] = None, ttl_period: Union[None, int] = None) -> None:
        self.id = id  # int
        self.peer_id = peer_id  # Peer
        self.date = date  # int
        self.message = message  # string
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.from_scheduled = from_scheduled  # flags.18?true
        self.legacy = legacy  # flags.19?true
        self.edit_hide = edit_hide  # flags.21?true
        self.pinned = pinned  # flags.24?true
        self.from_id = from_id  # flags.8?Peer
        self.fwd_from = fwd_from  # flags.2?MessageFwdHeader
        self.via_bot_id = via_bot_id  # flags.11?int
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.media = media  # flags.9?MessageMedia
        self.reply_markup = reply_markup  # flags.6?ReplyMarkup
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.views = views  # flags.10?int
        self.forwards = forwards  # flags.10?int
        self.replies = replies  # flags.23?MessageReplies
        self.edit_date = edit_date  # flags.15?int
        self.post_author = post_author  # flags.16?string
        self.grouped_id = grouped_id  # flags.17?long
        self.restriction_reason = restriction_reason  # flags.22?Vector<RestrictionReason>
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Message":
        flags = Int.read(data)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        from_scheduled = True if flags & (1 << 18) else False
        legacy = True if flags & (1 << 19) else False
        edit_hide = True if flags & (1 << 21) else False
        pinned = True if flags & (1 << 24) else False
        id = Int.read(data)
        
        from_id = TLObject.read(data) if flags & (1 << 8) else None
        
        peer_id = TLObject.read(data)
        
        fwd_from = TLObject.read(data) if flags & (1 << 2) else None
        
        via_bot_id = Int.read(data) if flags & (1 << 11) else None
        reply_to = TLObject.read(data) if flags & (1 << 3) else None
        
        date = Int.read(data)
        
        message = String.read(data)
        
        media = TLObject.read(data) if flags & (1 << 9) else None
        
        reply_markup = TLObject.read(data) if flags & (1 << 6) else None
        
        entities = TLObject.read(data) if flags & (1 << 7) else []
        
        views = Int.read(data) if flags & (1 << 10) else None
        forwards = Int.read(data) if flags & (1 << 10) else None
        replies = TLObject.read(data) if flags & (1 << 23) else None
        
        edit_date = Int.read(data) if flags & (1 << 15) else None
        post_author = String.read(data) if flags & (1 << 16) else None
        grouped_id = Long.read(data) if flags & (1 << 17) else None
        restriction_reason = TLObject.read(data) if flags & (1 << 22) else []
        
        ttl_period = Int.read(data) if flags & (1 << 25) else None
        return Message(id=id, peer_id=peer_id, date=date, message=message, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, from_scheduled=from_scheduled, legacy=legacy, edit_hide=edit_hide, pinned=pinned, from_id=from_id, fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, media=media, reply_markup=reply_markup, entities=entities, views=views, forwards=forwards, replies=replies, edit_date=edit_date, post_author=post_author, grouped_id=grouped_id, restriction_reason=restriction_reason, ttl_period=ttl_period)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 14) if self.post else 0
        flags |= (1 << 18) if self.from_scheduled else 0
        flags |= (1 << 19) if self.legacy else 0
        flags |= (1 << 21) if self.edit_hide else 0
        flags |= (1 << 24) if self.pinned else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 2) if self.fwd_from is not None else 0
        flags |= (1 << 11) if self.via_bot_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 6) if self.reply_markup is not None else 0
        flags |= (1 << 7) if self.entities is not None else 0
        flags |= (1 << 10) if self.views is not None else 0
        flags |= (1 << 10) if self.forwards is not None else 0
        flags |= (1 << 23) if self.replies is not None else 0
        flags |= (1 << 15) if self.edit_date is not None else 0
        flags |= (1 << 16) if self.post_author is not None else 0
        flags |= (1 << 17) if self.grouped_id is not None else 0
        flags |= (1 << 22) if self.restriction_reason is not None else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        data.write(Int(flags))
        
        data.write(Int(self.id))
        
        if self.from_id is not None:
            data.write(self.from_id.write())
        
        data.write(self.peer_id.write())
        
        if self.fwd_from is not None:
            data.write(self.fwd_from.write())
        
        if self.via_bot_id is not None:
            data.write(Int(self.via_bot_id))
        
        if self.reply_to is not None:
            data.write(self.reply_to.write())
        
        data.write(Int(self.date))
        
        data.write(String(self.message))
        
        if self.media is not None:
            data.write(self.media.write())
        
        if self.reply_markup is not None:
            data.write(self.reply_markup.write())
        
        if self.entities is not None:
            data.write(Vector(self.entities))
        
        if self.views is not None:
            data.write(Int(self.views))
        
        if self.forwards is not None:
            data.write(Int(self.forwards))
        
        if self.replies is not None:
            data.write(self.replies.write())
        
        if self.edit_date is not None:
            data.write(Int(self.edit_date))
        
        if self.post_author is not None:
            data.write(String(self.post_author))
        
        if self.grouped_id is not None:
            data.write(Long(self.grouped_id))
        
        if self.restriction_reason is not None:
            data.write(Vector(self.restriction_reason))
        
        if self.ttl_period is not None:
            data.write(Int(self.ttl_period))
        
        return data.getvalue()
