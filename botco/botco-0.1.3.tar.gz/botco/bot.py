import datetime
from typing import Union, Optional, List

from botco.contrib.session import Session
from .methods import (
    SendMessage,
    GetMe, LogOut, SendAudio, ForwardMessage, CopyMessage, GetUpdates, SendPhoto, SendDocument, SendVideo,
    SendAnimation, SendVoice, SendVideoNote, SendMediaGroup, SendLocation, EditMessageLiveLocation,
    StopMessageLiveLocation, SendVenue, SendContact, SendPoll, SendDice, SendChatAction, GetUserProfilePhotos, GetFile,
    BanChatMember, UnbanChatMember, RestrictChatMember, PromoteChatMember, SetChatAdministratorCustomTitle,
    SetChatPermissions, ExportChatInviteLink, CreateChatInviteLink, EditChatInviteLink, RevokeChatInviteLink,
    ApproveChatJoinRequest, DeclineChatJoinRequest, SetChatPhoto, DeleteChatPhoto, SetChatTitle, SetChatDescription,
    PinChatMessage, UnpinChatMessage, UnpinAllChatMessages, LeaveChat, GetChat, GetChatAdministrators,
    GetChatMemberCount, GetChatMember, SetChatStickerSet, DeleteChatStickerSet, AnswerCallbackQuery, SetMyCommands,
    DeleteMyCommands, GetMyCommands, AnswerInlineQuery, SendInvoice, AnswerShippingQuery, AnswerPreCheckoutQuery
)
from .types import (
    MessageEntity,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply, UNSET, InputFile, Update, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo,
    ChatPermissions, BotCommandScope, BotCommand, InlineQueryResult, LabeledPrice, ShippingOption
)
from .utils.helper import clean_locals
from .utils.token import validate_token


class Bot:
    def __init__(
            self, token: str, parse_mode: str = "HTML",
            session: Optional[Session] = None,
            connect_timeout=15,
            read_timeout=30,
            retry_on_error=False,
            max_retries=3
    ):
        validate_token(token)
        self.token = token
        self.parse_mode = parse_mode
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.retry_on_error = retry_on_error
        self.max_retries = max_retries
        if session is None:
            session = Session()
        self.session = session

    def __call__(self, method):
        return self.session(self, method)

    @property
    def id(self):
        return int(self.token.split(":")[0])

    def get_updates(
            self,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            timeout: Optional[int] = None,
            allowed_updates: Optional[List[str]] = None
    ) -> List[Update]:
        return self(GetUpdates(**clean_locals(locals())))

    def get_me(self):
        return self(GetMe())

    def logout(self):
        return self(LogOut())

    def send_message(
            self, chat_id: Union[int, str], text: str, parse_mode: Optional[str] = None,
            entities: List[MessageEntity] = None, disable_web_page_preview: bool = None,
            disable_notification: bool = None, reply_to_message_id: int = None,
            allow_sending_without_reply: bool = None,
            reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup,
                                ReplyKeyboardRemove, ForceReply] = None
    ):
        return self(SendMessage(**clean_locals(locals())))

    def forward_message(
            self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int,
            disable_notification: Optional[bool] = None
    ):
        return self(ForwardMessage(**clean_locals(locals())))

    def copy_message(
            self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, caption: Optional[str],
            parse_mode: Optional[str] = UNSET, caption_entities: Optional[List[MessageEntity]] = None,
            disable_notification: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None, reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(CopyMessage(**clean_locals(locals())))

    def send_photo(
            self, chat_id: Union[int, str], photo: Union[InputFile, str], caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET, caption_entities: Optional[List[MessageEntity]] = None,
            disable_notification: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ):
        return self(SendPhoto(**clean_locals(locals())))

    def send_audio(
            self,
            chat_id: Union[int, str], audio: Union[InputFile, str], caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET, caption_entities: Optional[List[MessageEntity]] = None,
            duration: Optional[int] = None, performer: Optional[str] = None, title: Optional[str] = None,
            thumb: Optional[Union[InputFile, str]] = None, disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None, allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup,
                                         ReplyKeyboardRemove, ForceReply]] = None
    ):
        return self(SendAudio(**clean_locals(locals())))

    def send_document(
            self,
            chat_id: Union[int, str],
            document: Union[InputFile, str],
            thumb: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET,
            caption_entities: Optional[List[MessageEntity]] = None,
            disable_content_type_detection: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ):
        return self(SendDocument(**clean_locals(locals())))

    def send_video(
            self,
            chat_id: Union[int, str],
            video: Union[InputFile, str],
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            thumb: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET,
            caption_entities: Optional[List[MessageEntity]] = None,
            supports_streaming: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendVideo(**clean_locals(locals())))

    def send_animation(
            self,
            chat_id: Union[int, str],
            animation: Union[InputFile, str],
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            thumb: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET,
            caption_entities: Optional[List[MessageEntity]] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendAnimation(**clean_locals(locals())))

    def send_voice(
            self,
            chat_id: Union[int, str],
            voice: Union[InputFile, str],
            caption: Optional[str] = None,
            parse_mode: Optional[str] = UNSET,
            caption_entities: Optional[List[MessageEntity]] = None,
            duration: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendVoice(**clean_locals(locals())))

    def send_video_note(
            self,
            chat_id: Union[int, str],
            video_note: Union[InputFile, str],
            duration: Optional[int] = None,
            length: Optional[int] = None,
            thumb: Optional[Union[InputFile, str]] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendVideoNote(**clean_locals(locals())))

    def send_media_group(
            self,
            chat_id: Union[int, str],
            media: List[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
    ):
        return self(SendMediaGroup(**clean_locals(locals())))

    def send_location(
            self,
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            horizontal_accuracy: Optional[float] = None,
            live_period: Optional[int] = None,
            heading: Optional[int] = None,
            proximity_alert_radius: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None

    ):
        return self(SendLocation(**clean_locals(locals())))

    def edit_message_live_location(
            self,
            latitude: float,
            longitude: float,
            chat_id: Optional[Union[int, str]] = None,
            message_id: Optional[int] = None,
            inline_message_id: Optional[str] = None,
            horizontal_accuracy: Optional[float] = None,
            heading: Optional[int] = None,
            proximity_alert_radius: Optional[int] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None
    ):
        return self(EditMessageLiveLocation(**clean_locals(locals())))

    def stop_message_live_location(
            self,
            chat_id: Optional[Union[int, str]] = None,
            message_id: Optional[int] = None,
            inline_message_id: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None
    ):
        return self(StopMessageLiveLocation(**clean_locals(locals())))

    def send_venue(
            self,
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            foursquare_id: Optional[str] = None,
            foursquare_type: Optional[str] = None,
            google_place_id: Optional[str] = None,
            google_place_type: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendVenue(**clean_locals(locals())))

    def send_contact(
            self,
            chat_id: Union[int, str],
            phone_number: str,
            first_name: str,
            last_name: Optional[str] = None,
            vcard: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendContact(**clean_locals(locals())))

    def send_poll(
            self,
            chat_id: Union[int, str],
            question: str,
            options: List[str],
            is_anonymous: Optional[bool] = None,
            type: Optional[str] = None,
            allows_multiple_answers: Optional[bool] = None,
            correct_option_id: Optional[int] = None,
            explanation: Optional[str] = None,
            explanation_parse_mode: Optional[str] = UNSET,
            explanation_entities: Optional[List[MessageEntity]] = None,
            open_period: Optional[int] = None,
            close_date: Optional[Union[datetime.datetime, datetime.timedelta, int]] = None,
            is_closed: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None

    ):
        return self(SendPoll(**clean_locals(locals())))

    def send_dice(
            self,
            chat_id: Union[int, str],
            emoji: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None
    ):
        return self(SendDice(**clean_locals(locals())))

    def send_chat_action(
            self,
            chat_id: Union[int, str],
            action: str
    ):
        return self(SendChatAction(**clean_locals(locals())))

    def get_user_profile_photos(
            self,
            user_id: int,
            offset: Optional[int] = None,
            limit: Optional[int] = None,

    ):
        self(GetUserProfilePhotos(**clean_locals(locals())))

    def get_file(
            self,
            file_id: str
    ):
        self(GetFile(**clean_locals(locals())))

    def ban_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            until_date: Optional[Union[datetime.datetime, datetime.timedelta, int]] = None,
            revoke_messages: Optional[bool] = None,
    ):
        self(BanChatMember(**clean_locals(locals())))

    def unban_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            only_if_banned: Optional[bool] = None,
    ):
        self(UnbanChatMember(**clean_locals(locals())))

    def restrict_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            permissions: ChatPermissions,
            until_date: Optional[Union[datetime.datetime, datetime.timedelta, int]] = None,
    ):
        self(RestrictChatMember(**clean_locals(locals())))

    def promote_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            is_anonymous: Optional[bool] = None,
            can_manage_chat: Optional[bool] = None,
            can_post_messages: Optional[bool] = None,
            can_edit_messages: Optional[bool] = None,
            can_delete_messages: Optional[bool] = None,
            can_manage_voice_chats: Optional[bool] = None,
            can_restrict_members: Optional[bool] = None,
            can_promote_members: Optional[bool] = None,
            can_change_info: Optional[bool] = None,
            can_invite_users: Optional[bool] = None,
            can_pin_messages: Optional[bool] = None,
    ):
        self(PromoteChatMember(**clean_locals(locals())))

    def set_chat_administrator_custom_title(
            self,
            chat_id: Union[int, str],
            user_id: int,
            custom_title: str,
    ):
        self(SetChatAdministratorCustomTitle(**clean_locals(locals())))

    def set_chat_permissions(
            self,
            chat_id: Union[int, str],
            permissions: ChatPermissions,
    ):
        self(SetChatPermissions(**clean_locals(locals())))

    def export_chat_invite_link(
            self,
            chat_id: Union[int, str]
    ):
        self(ExportChatInviteLink(**clean_locals(locals())))

    def create_chat_invite_link(
            self,
            chat_id: Union[int, str],
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
    ):
        self(CreateChatInviteLink(**clean_locals(locals())))

    def edit_chat_invite_link(
            self,
            chat_id: Union[int, str],
            invite_link: str,
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
    ):
        self(EditChatInviteLink(**clean_locals(locals())))

    def revoke_chat_invite_link(
            self,
            chat_id: Union[int, str],
            invite_link: str,
    ):
        self(RevokeChatInviteLink(**clean_locals(locals())))

    def approve_chat_join_request(
            self,
            chat_id: Union[str, int],
            user_id: int,
    ):
        self(ApproveChatJoinRequest(**clean_locals(locals())))

    def decline_chat_join_request(
            self,
            chat_id: Union[str, int],
            user_id: int,
    ):
        self(DeclineChatJoinRequest(**clean_locals(locals())))

    def set_chat_photo(
            self,
            chat_id: Union[int, str],
            photo: InputFile,
    ):
        self(SetChatPhoto(**clean_locals(locals())))

    def delete_chat_photo(
            self,
            chat_id: Union[int, str]
    ):
        self(DeleteChatPhoto(**clean_locals(locals())))

    def set_chat_title(
            self,
            chat_id: Union[int, str],
            title: str,
    ):
        self(SetChatTitle(**clean_locals(locals())))

    def set_chat_description(
            self,
            chat_id: Union[int, str],
            description: Optional[str] = None,
    ):
        self(SetChatDescription(**clean_locals(locals())))

    def pin_chat_message(
            self,
            chat_id: Union[int, str],
            message_id: int,
            disable_notification: Optional[bool] = None,
    ):
        self(PinChatMessage(**clean_locals(locals())))

    def unpin_chat_message(
            self,
            chat_id: Union[int, str],
            message_id: Optional[int] = None,
    ):
        self(UnpinChatMessage(**clean_locals(locals())))

    def unpin_all_chat_messages(
            self,
            chat_id: Union[int, str]
    ):
        self(UnpinAllChatMessages(**clean_locals(locals())))

    def leave_chat(
            self,
            chat_id: Union[int, str]
    ):
        self(LeaveChat(**clean_locals(locals())))

    def get_chat(
            self,
            chat_id: Union[int, str]
    ):
        self(GetChat(**clean_locals(locals())))

    def get_chat_administrators(
            self,
            chat_id: Union[int, str]
    ):
        self(GetChatAdministrators(**clean_locals(locals())))

    def get_chat_member_count(
            self,
            chat_id: Union[int, str]
    ):
        self(GetChatMemberCount(**clean_locals(locals())))

    def get_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
    ):
        self(GetChatMember(**clean_locals(locals())))

    def set_chat_sticker_set(
            self,
            chat_id: Union[int, str],
            sticker_set_name: str,
    ):
        self(SetChatStickerSet(**clean_locals(locals())))

    def delete_chat_sticker_set(
            self,
            chat_id: Union[int, str]
    ):
        self(DeleteChatStickerSet(**clean_locals(locals())))

    def answer_callback_query(
            self,
            callback_query_id: str,
            text: Optional[str] = None,
            show_alert: Optional[bool] = None,
            url: Optional[str] = None,
            cache_time: Optional[int] = None,

    ):
        self(AnswerCallbackQuery(**clean_locals(locals())))

    def set_my_commands(
            self,
            commands: List[BotCommand],
            scope: Optional[BotCommandScope] = None,
            language_code: Optional[str] = None,
    ):
        self(SetMyCommands(**clean_locals(locals())))

    def delete_my_commands(
            self,
            scope: Optional[BotCommandScope] = None,
            language_code: Optional[str] = None,
    ):
        self(DeleteMyCommands(**clean_locals(locals())))

    def get_my_commands(
            self,
            scope: Optional[BotCommandScope] = None,
            language_code: Optional[str] = None,
    ):
        self(GetMyCommands(**clean_locals(locals())))

    def answer_inline_query(
            self,
            inline_query_id: str,
            results: List[InlineQueryResult],
            cache_time: Optional[int] = None,
            is_personal: Optional[bool] = None,
            next_offset: Optional[str] = None,
            switch_pm_text: Optional[str] = None,
            switch_pm_parameter: Optional[str] = None,
    ):
        self(AnswerInlineQuery(**clean_locals(locals())))

    def send_invoice(
            self,
            chat_id: Union[int, str],
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            currency: str,
            prices: List[LabeledPrice],
            max_tip_amount: Optional[int] = None,
            suggested_tip_amounts: Optional[List[int]] = None,
            start_parameter: Optional[str] = None,
            provider_data: Optional[str] = None,
            photo_url: Optional[str] = None,
            photo_size: Optional[int] = None,
            photo_width: Optional[int] = None,
            photo_height: Optional[int] = None,
            need_name: Optional[bool] = None,
            need_phone_number: Optional[bool] = None,
            need_email: Optional[bool] = None,
            need_shipping_address: Optional[bool] = None,
            send_phone_number_to_provider: Optional[bool] = None,
            send_email_to_provider: Optional[bool] = None,
            is_flexible: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
    ):
        self(SendInvoice(**clean_locals(locals())))

    def answer_shipping_query(
            self,
            shipping_query_id: str,
            ok: bool,
            shipping_options: Optional[List[ShippingOption]] = None,
            error_message: Optional[str] = None,
    ):
        self(AnswerShippingQuery(**clean_locals(locals())))

    def answer_pre_checkout_query(
            self,
            pre_checkout_query_id: str,
            ok: bool,
            error_message: Optional[str] = None,
    ):
        self(AnswerPreCheckoutQuery(**clean_locals(locals())))
