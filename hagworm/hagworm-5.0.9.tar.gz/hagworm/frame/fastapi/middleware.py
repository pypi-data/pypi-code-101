# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

from contextvars import ContextVar

from starlette.types import ASGIApp, Message, Receive, Scope, Send

from hagworm.extend.base import Utils


REQUEST_ID_CONTEXT = ContextVar(r'request_id')


class RequestIDMiddleware:

    @staticmethod
    def get_request_id():

        request_id = REQUEST_ID_CONTEXT.get(None)

        if request_id is None:
            Utils.log.warning(r'RequestIDMiddleware is not enabled!')

        return request_id

    def __init__(self, app: ASGIApp) -> None:

        self._app = app
        self._send = None

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:

        self._send = send

        REQUEST_ID_CONTEXT.set(Utils.uuid1_urn())

        await self._app(scope, receive, self.send)

    async def send(self, message: Message) -> None:

        message.setdefault(r'headers', [])
        message[r'headers'].append((b'x-timestamp', str(Utils.timestamp(True)).encode(r'latin-1')))

        request_id = self.get_request_id()

        if request_id:
            message[r'headers'].append((b'x-request-id', request_id.encode(r'latin-1')))

        await self._send(message)
