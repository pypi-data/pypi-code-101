from __future__ import annotations

import sys
import traceback
from typing import Optional, Set, TYPE_CHECKING

from botco.types import ResponseParameters

if TYPE_CHECKING:
    from botco.methods import TelegramMethod
    from botco.methods.base import TelegramType


def get_exc_info():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb)[-1]
    return f'{tb.filename}:{tb.lineno}'


GROUP_CHAT_MIGRATED = "group chat was migrated to a supergroup chat"
CHAT_NOT_FOUND = "chat not found"
INVALID_FILE_ID = "invalid file id"
MESSAGE_IS_NOT_MODIFIED = "message is not modified"
USER_NOT_FOUND = "user not found"
WRONG_PARAMETER_IN_REQUEST = "wrong parameter action in request"
CONFLICT = "terminated by other long poll or webhook"

BOT_WAS_BLOCKED = "bot was blocked by the user"
BOT_CANT_SEND_MESSAGE_TO_BOTS = "bot can't send messages to bots"
BOT_WAS_KICKED = "bot was kicked from the group chat"
USER_IS_DEACTIVATED = "user is deactivated"


class BotcoError(Exception):
    def __init__(self, method: TelegramMethod[TelegramType], error_code: Optional[int] = None,
                 description: Optional[str] = None,
                 parameters: Optional[ResponseParameters] = None):
        self.error_code = error_code
        self.description = description
        self.parameters = parameters
        self.method = method
        super(BotcoError, self).__init__(description)


class DetailedBotcoError(BotcoError):
    url: Optional[str] = None

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        message = self.message
        if self.url:
            message += f"\n(background on this error at: {self.url})"
        return message


class TelegramAPIError(DetailedBotcoError):
    def __init__(
            self,
            method: TelegramMethod[TelegramType],
            message: str,
    ) -> None:
        super().__init__(message=message)
        self.method = method


class TelegramNetworkError(TelegramAPIError):
    pass


class TelegramRetryAfter(TelegramAPIError):
    url = "https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this"

    def __init__(
            self,
            method: TelegramMethod[TelegramType],
            message: str,
            retry_after: int,
    ) -> None:
        description = f"Flood control exceeded on method {type(method).__name__!r}"
        if chat_id := getattr(method, "chat_id", None):
            description += f" in chat {chat_id}"
        description += f". Retry in {retry_after} seconds."
        description += f"\nOriginal description: {message}"

        super().__init__(method=method, message=description)
        self.retry_after = retry_after


class TelegramBadRequest(TelegramAPIError):
    pass


class GroupChatMigrated(TelegramBadRequest):
    url = "https://core.telegram.org/bots/api#responseparameters"

    def __init__(
            self,
            method: TelegramMethod[TelegramType],
            message: str,
            migrate_to_chat_id: int,
    ) -> None:
        description = f"The group has been migrated to a supergroup with id {migrate_to_chat_id}"
        if hasattr(method, "chat_id"):
            description += f" from {method.chat_id}"
        description += f"\nOriginal description: {message}"
        super().__init__(method=method, message=message)
        self.migrate_to_chat_id = migrate_to_chat_id


class ChatNotFound(TelegramBadRequest):
    def __init__(self, method: TelegramMethod[TelegramType], message: str):
        if hasattr(method, 'chat_id'):
            message += f" with id {method.chat_id}"
        super(ChatNotFound, self).__init__(method, message)


class UserNotFound(TelegramBadRequest):
    pass


class Conflict(TelegramAPIError):
    pass


class Unauthorized(TelegramAPIError):
    pass


class TelegramForbiddenError(TelegramAPIError):
    pass


class TelegramServerError(TelegramAPIError):
    pass


class RestartingTelegram(TelegramServerError):
    pass


class TelegramEntityTooLarge(TelegramNetworkError):
    url = "https://core.telegram.org/bots/api#sending-files"


class FiltersResolveError(DetailedBotcoError):
    def __init__(self, unresolved_fields: Set[str]) -> None:
        message = f"Unknown keyword filters: {unresolved_fields}"

        super().__init__(message=message)
        self.unresolved_fields = unresolved_fields


class ThrottledError(Exception):
    def __init__(self, wait: float, message: str = None):
        self.wait = wait
        self.message = message
        super().__init__(self.message)


class InvalidFileId(TelegramBadRequest):
    pass


class MessageNotModified(TelegramBadRequest):
    pass


class WrongParameterInRequest(TelegramBadRequest):
    pass


class BotBlocked(TelegramForbiddenError):
    pass


class BotKicked(TelegramForbiddenError):
    pass


class BotCantSendMessageToBots(TelegramForbiddenError):
    pass


class UserIsDeactivated(TelegramForbiddenError):
    pass


def get_exception_class(e: BotcoError):
    if e.error_code == 429:
        return TelegramRetryAfter(method=e.method, message=e.description, retry_after=e.parameters.retry_after)
    elif e.error_code == 401:
        return Unauthorized(e.method, e.description)
    elif e.error_code == 409:
        return Conflict(method=e.method, message=e.description)
    elif e.error_code == 400:
        text = e.description.split(":")[-1].strip()
        if text == GROUP_CHAT_MIGRATED:
            return GroupChatMigrated(e.method, e.description, e.parameters.migrate_to_chat_id)
        elif text == CHAT_NOT_FOUND:
            return ChatNotFound(e.method, e.description)
        elif text == INVALID_FILE_ID:
            return InvalidFileId(e.method, e.description)
        elif text == MESSAGE_IS_NOT_MODIFIED:
            return MessageNotModified(e.method, e.description)
        elif text == USER_NOT_FOUND:
            return UserNotFound(e.method, e.description)
        elif text == WRONG_PARAMETER_IN_REQUEST:
            return WrongParameterInRequest(e.method, e.description)
    elif e.error_code == 403:
        text = e.description.split(":")[-1].strip()
        if text == BOT_WAS_BLOCKED:
            return BotBlocked(e.method, e.description)
        elif text == BOT_CANT_SEND_MESSAGE_TO_BOTS:
            return BotCantSendMessageToBots(e.method, e.description)
        elif text == BOT_WAS_KICKED:
            return BotKicked(e.method, e.description)
        elif text == USER_IS_DEACTIVATED:
            return UserIsDeactivated(e.method, e.description)
