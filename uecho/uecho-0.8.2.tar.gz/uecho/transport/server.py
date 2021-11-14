# Copyright (C) 2021 Satoshi Konno. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
import threading
# from typing import List

from ..protocol.message import Message
from ..log.logger import error


class Server(threading.Thread):
    PORT = 3610

    # socket: socket.socket
    # port: int
    # observers: List[Observer]

    def __init__(self):
        super(Server, self).__init__()
        self.socket = None
        self.port = Server.PORT
        self.observers = []

    def create_udp_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        return sock

    def bind(self, ifaddr):
        pass

    def run(self):
        while True:
            try:
                if self.socket is None:
                    break
                recv_msg_bytes, recv_from = self.socket.recvfrom(1024)
                msg = Message()
                if not msg.parse_bytes(recv_msg_bytes):
                    log_msg = '%s %s' % (recv_from, recv_msg_bytes.hex())
                    error(log_msg)
                    continue
                msg.from_addr = recv_from
                self.notify(msg)
            except:
                break

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.message_received(msg)

    def start(self):
        if self.socket is None:
            return False
        super(Server, self).start()
        return True

    def stop(self):
        if self.socket is None:
            return False
        self.socket.close()
        self.socket = None
        return True
