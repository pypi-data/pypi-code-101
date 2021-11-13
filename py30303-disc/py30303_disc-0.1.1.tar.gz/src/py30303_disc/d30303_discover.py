"""
Simple 30303 discover.

USAGE:
    d30303_discover
"""

import asyncio
import logging

from .libs.py30303_disc import d30303


class run_d30303:
    def __init__(self, server, loop):
        self.server = server
        self.loop = loop
        # Subscribe for incoming udp packet event
        self.server.subscribe(self.on_datagram_received)
        asyncio.ensure_future(self.do_send(), loop=self.loop)

    async def on_datagram_received(self, data, addr):
        # Override virtual method and process incoming data
        print(f"Found: {self.server.parse(data, addr)}")
        
    async def do_send(self):
        # Delay for prevent tasks concurency
        await asyncio.sleep(0.001)
        # Enqueue data for send
        self.server.send_discovery()
        await asyncio.sleep(5)
        self.server.send_discovery(1)
        await asyncio.sleep(5)
        self.server.end_discovery()
        self.loop.stop()


async def main(loop):
    """Run the discovery."""
    logging.basicConfig(level=logging.DEBUG)

    d30303_discovery = d30303()
    d30303_discovery.bind_d30303_recv(loop=loop)

    run_d30303(server=d30303_discovery, loop=loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
