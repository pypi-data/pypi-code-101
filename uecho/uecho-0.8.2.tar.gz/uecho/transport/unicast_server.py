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

from .server import Server
from .multicast_server import MulticastServer


class UnicastServer(Server):
    def __init__(self):
        super(UnicastServer, self).__init__()

    def bind(self, ifaddr):
        self.socket = self.create_udp_socket()
        self.socket.bind((ifaddr, self.port))
        return True

    def announce_message(self, msg):
        if self.socket is None:
            return False
        to_addr = (MulticastServer.ADDRESS, Server.PORT)
        msg.to_addr = to_addr
        return self.socket.sendto(msg.to_bytes(), to_addr)

    def send_message(self, msg, addr):
        if not isinstance(addr, tuple) or len(addr) != 2:
            return False
        if self.socket is None:
            return False
        msg.to_addr = addr
        return self.socket.sendto(msg.to_bytes(), addr)
