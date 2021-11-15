from io import BytesIO
from logging import Handler, LogRecord, getLogger, NOTSET
from traceback import format_exc

from httpx import Client, HTTPError, Request, HTTPStatusError

from .formatters import MarkdownFormatter


__all__ = ['TelegramHandler']


logger = getLogger(__name__)
logger.setLevel(NOTSET)
logger.propagate = False


class TelegramClient(Client):
    def __init__(self, token: str, **kwargs):
        kwargs['base_url'] = f'https://api.telegram.org/bot{token}'
        super(TelegramClient, self).__init__(**kwargs)

    def send_request(self, request: Request):
        try:
            response = self.send(request)
        except HTTPError:
            logger.exception(format_exc())
        else:
            try:
                response.raise_for_status()
            except HTTPStatusError:
                logger.exception(format_exc())
            return response

    def send_message(self, chat_id: str, text: str, **kwargs):
        kwargs.setdefault('parse_mode', 'Markdown')
        kwargs.update({'chat_id': chat_id, 'text': text})
        request = Request(method='post', url=self.base_url.join('sendMessage'), json=kwargs)
        response = self.send_request(request)
        if response:
            return response.json()

    def send_document(self, chat_id: str, caption: str, document: BytesIO, **kwargs):
        kwargs.setdefault('parse_mode', 'Markdown')
        kwargs.update({'chat_id': chat_id, 'caption': caption})
        files = {'document': (getattr(document, 'name', 'document.txt'), document)}
        request = Request(method='post', url=self.base_url.join('sendDocument'), data=kwargs, files=files)
        response = self.send_request(request)
        if response:
            return response.json()


class TelegramHandler(Handler):
    def __init__(self, token: str, chat_id: str, level=NOTSET, client_config: dict = None, message_config: dict = None):
        super(TelegramHandler, self).__init__(level=level)

        # Save initials
        self.token = token
        self.chat_id = chat_id

        # Setup client config
        self.client_config = client_config or {}
        self.client_config.setdefault('timeout', 2)

        # Initialize client
        self.client = TelegramClient(token, **self.client_config)

        # Setup message config
        self.message_config = message_config or {}
        self.message_config.setdefault('disable_notification', False)
        self.message_config.setdefault('disable_web_page_preview', False)

        # Set formatter
        self.setFormatter(MarkdownFormatter())

    def send_as_message(self, text: str):
        return self.client.send_message(self.chat_id, text, **self.message_config)

    def send_as_document(self, record: LogRecord, text: str):
        caption = f'{record.levelname} {record.asctime} [{record.name}:{record.funcName}]'
        document = BytesIO(text.encode())
        document.name = f'{record.name}_{record.funcName}_{record.asctime}.txt'
        return self.client.send_document(self.chat_id, caption, document, **self.message_config)

    def emit(self, record: LogRecord):
        text = self.format(record)

        if len(text) < 4096:
            response = self.send_as_message(text)
        else:
            response = self.send_as_document(record, text)

        if response and not response.get('ok', False):
            logger.warning('Telegram responded with ok=false status! {}'.format(response))
