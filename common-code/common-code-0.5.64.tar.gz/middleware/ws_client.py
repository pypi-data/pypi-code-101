#!/usr/bin/python3
import json
import socket
from threading import Thread
from time import sleep

from common.logging_config import logger

import websocket


class WebSocketClient:
    def conn_ws(self, host="127.0.0.1", port=5678):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        return self.sock

    def send_msg(self, msg, encoding="utf-8"):
        if isinstance(msg, dict) or isinstance(msg, list):
            msg = json.dumps(msg)
        logger.debug("send msg ", self.host, self.port, msg)
        if not isinstance(msg, bytes):
            msg = msg.encode(encoding)
        self.sock.send(msg)

    def recv_msg(self, encoding="utf-8"):
        while True:
            msg = self.sock.recv(1024)
            msg = msg.decode(encoding)
            logger.debug("recv msg", self.host, self.port, msg)


class WebSocketAppClient:
    def __init__(self, address, on_message=None, on_open=None, on_close=None, on_error=None, on_ping=None):
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(
            address,
            on_message=on_message if on_message else self.on_message,
            on_error=on_error if on_error else self.on_error,
            on_close=on_close if on_close else self.on_close,
            on_open=on_open if on_open else self.on_open,
            on_ping=on_ping if on_ping else self.on_ping,
        )

    def on_message(self, ws, message):
        logger.debug(message)

    def on_error(self, ws, error):
        logger.error("on_error错误：", error)

    def on_ping(self, ws):
        while True:
            ws.send(" ")
            sleep(30)

    def on_close(self, ws):
        logger.warning("websocket close!!!")

    def on_open(self, ws):
        logger.info("websocket open!!!")

    def run_forever(self):
        Thread(target=self._bg_run_forever).start()

    def _bg_run_forever(self):
        while True:
            self.ws.run_forever()
            sleep(10)


if __name__ == "__main__":
    client = WebSocketClient()
    client.conn_ws()
    Thread(target=client.recv_msg).start()
    while True:
        client.send_msg("示范法")
        sleep(2)
