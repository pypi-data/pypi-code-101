"""
py30303_disc library

Contains:
    - d30303
"""
import asyncio
import logging
import socket
from collections import deque

D30303_PORT = 30303
D30303_MSG = [
    "Discovery: Who is out there?",
    "D",
]


class d30303:
    """Documentation of d30303."""
    
    def __init__(self):
        """Initiatlizes d30303 class."""
        self.log = logging.getLogger(__name__)

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self._sock.setblocking(False)

        self._send_event = asyncio.Event()
        self._send_queue = deque()

        self._subscribers = {}

    def end_discovery(self):
        """End the discovery."""
        self.log.debug("Closing socket and ending discovery.")
        self._sock.close()
        
    def bind_d30303_recv(self, loop):
        """Bind to a port to recieve replies."""

        self.loop = loop
        
        self._sock.bind(('', 0))
        addr, port = self._sock.getsockname()
        self.log.info("Listening on port %d:udp for discovery events", port)

        self._connection_made()

        self._run_future(self._send_periodically(), self._recv_periodically())

    def subscribe(self, fut):
        """Subscribe to be notified on discovery."""
        self._subscribers[id(fut)] = fut

    def unsubscribe(self, fut):
        """Unsubscribe from notifications."""
        self._subscribers.pop(id(fut), None)

    def send_discovery(self, msg_type=0):
        """Initiate a 30303 discovery of type X."""
        self.log.debug("Initiating type %s discovery.", msg_type)
        self._send_queue.append((
            bytes(D30303_MSG[msg_type], 'utf-8'),
            ('<broadcast>', D30303_PORT)))
        self._send_event.set()

    def _run_future(self, *args):
        """Kick it off."""
        for fut in args:
            asyncio.ensure_future(fut, loop=self.loop)

    def _sock_recv(self, fut=None, registered=False):
        """Recieve data on the listen socket."""
        fd = self._sock.fileno()

        if fut is None:
            fut = self.loop.create_future()

        if registered:
            self.loop.remove_reader(fd)

        try:
            data, addr = self._sock.recvfrom(1024)
        except (BlockingIOError, InterruptedError):
            self.loop.add_reader(fd, self._sock_recv, fut, True)
        except Exception as e:
            fut.set_exception(e)
            self._socket_error(e)
        else:
            fut.set_result((data, addr))

        return fut

    def _sock_send(self, data, addr, fut=None, registered=False):
        """Send data to the broadcast addr."""
        fd = self._sock.fileno()

        if fut is None:
            fut = self.loop.create_future()

        if registered:
            self.loop.remove_writer(fd)

        if not data:
            return

        try:
            bytes_sent = self._sock.sendto(data, addr)
        except (BlockingIOError, InterruptedError):
            self.loop.add_writer(fd, self._sock_send, data, addr, fut, True)
        except Exception as e:
            fut.set_exception(e)
            self._socket_error(e)
        else:
            fut.set_result(bytes_sent)

        return fut

    async def _send_periodically(self):
        """If we have data, send it."""
        while True:
            await self._send_event.wait()
            try:
                while self._send_queue:
                    data, addr = self._send_queue.popleft()
                    await self._sock_send(data, addr)
            finally:
                self._send_event.clear()

    async def _recv_periodically(self):
        """Check for new data, get it."""
        while True:
            data, addr = await self._sock_recv()
            self.log.debug("Got Data: %s", data)
            self.log.debug("From ADDR: %s", addr)
            self._notify_subscribers(*self._datagram_received(data, addr))

    def _connection_made(self):
        pass

    def _socket_error(self, e):
        pass

    def _datagram_received(self, data, addr):
        """Internal: Got some data."""
        return data, addr

    def _notify_subscribers(self, data, addr):
        self._run_future(
            *(fut(data, addr) for fut in self._subscribers.values()))

    def parse(self, data, addr, mac_prefix=None, hostname=None):
        """Parse a d30303 message."""

        ip_addr = addr[0]
        data_string = data.decode("utf-8").split('\r\n')
        self.log.info("Hostname: %s", data_string[0])

        message = (ip_addr, data_string[0].strip(), data_string[1])
        
        if mac_prefix is None and hostname is None:
            return message

        if mac_prefix is not None:
            if data_string[1].startswith(mac_prefix):
                if hostname is not None:
                    if hostname == data_string[0]:
                        return message
                    return None
                return message
            return None

        if hostname is not None:
            if hostname == data_string[0]:
                return message
            return None
        return None
