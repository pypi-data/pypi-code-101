from __future__ import annotations

from typing import Union, TYPE_CHECKING, Dict, Any

from .base import Request, TelegramMethod

if TYPE_CHECKING:
    from ..bot import Bot


class ApproveChatJoinRequest(TelegramMethod[bool]):
    __returning__ = bool

    chat_id: Union[str, int]
    user_id: int

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="approveChatJoinRequest", data=data)
