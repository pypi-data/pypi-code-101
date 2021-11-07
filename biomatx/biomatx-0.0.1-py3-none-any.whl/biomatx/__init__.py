"""
    pybiomatx

    Python API for managing the Biomatx home automation system
    :author: Damien Merenne <dam@cosinux.org>
    :license: MIT
"""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from struct import pack
from typing import Awaitable, Callable, List

__all__: List[str] = [
    "Bus",
    "Module",
    "Relay",
    "Switch",
]  # noqa: WPS410 (the only __variable__ we use)

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class Packet:
    """A Biomatx bus packet.

    Biomatx bus uses 2 bytes packet where
    [0-4] = 01010
    [5-7] = module address
    [8]: 0 pushed / 1 released
    [9-11] = module address
    [12-15] = switch address
    """

    module: int
    switch: int
    released: bool

    @classmethod
    def from_bytes(cls, data: bytes) -> Packet:
        p1, p2 = data
        module = (p2 & 0b01110000) >> 4
        switch = 0b00001111 & p2
        released = p2 >> 7
        return Packet(module, switch, bool(released))

    @property
    def pressed(self):
        return not self.released

    def __bytes__(self) -> bytes:
        p1 = 0b01010000 | self.module
        p2 = int(self.released) << 7 | self.module << 4 | self.switch
        return pack(
            "cc", p1.to_bytes(1, byteorder="little"), p2.to_bytes(1, byteorder="little")
        )


class Switch:
    """Biomatx switches.

    Switches are buttons that can be pressed or released."""

    def __init__(self, module: Module, address: int):
        self.address = address
        self.module = module
        self.released = False

    @property
    def bus(self):
        return self.module.bus

    @property
    def pressed(self):
        return not self.released

    def _packet(self):
        return self.module._packet(self.address, self.released)

    def _process(self, packet: Packet):
        assert packet.module == self.module.address
        assert packet.switch == self.address
        self.released = packet.released
        _LOGGER.debug("switch %s %s", self, "released" if self.released else "pressed")
        return True

    async def press(self):
        _LOGGER.debug("pressing switch %s", self)
        self.released = False
        await self.bus.send_packet(self._packet())

    async def release(self):
        _LOGGER.debug("releasing switch %s", self)
        self.released = True
        await self.bus.send_packet(self._packet())

    def __repr__(self):
        return "<{}.{} module={} address={}>".format(
            self.__class__.__module__,
            self.__class__.__name,
            self.module.address,
            self.address,
        )

    def __str__(self):
        return f"{self.module.address}/{self.address}"


class Relay:
    """Biomatx relay.

    Relays are controlled by a switch, they can be on or off."""

    def __init__(self, switch: Switch):
        self.switch = switch
        self.address = switch.address
        self.module = switch.module
        self.on = False

    @property
    def off(self):
        return not self.on

    def _process(self, packet: Packet):
        assert packet.module == self.module.address
        assert packet.switch == self.address

        # Update state on release
        if packet.released:
            self.on = not self.on
            _LOGGER.debug("relay %s turned %s", self, "on" if self.on else "off")
            return True
        return False

    async def toggle(self):
        _LOGGER.debug(
            "toggling relay %s from %s to %s",
            self,
            "on" if self.on else "off",
            "off" if self.on else "on",
        )
        await self.switch.press()
        await self.switch.release()
        self.on = not self.on

    async def force_toggle(self):
        """When the computed state is different from the physical state, force the other state."""
        self.on = not self.on

    def __repr__(self):
        return "<{}.{} module={} address={}>".format(
            self.__class__.__module__,
            self.__class__.__name,
            self.module.address,
            self.address,
        )

    def __str__(self):
        return str(self.switch)


class Module:
    """A Biomatx module

    Modules contains 10 switches."""

    def __init__(self, bus: Bus, address: int):
        self.address = address
        self.bus = bus
        self.switches = [Switch(self, i) for i in range(0, 10)]
        self.relays = [Relay(i) for i in self.switches]

    def _packet(self, switch: int, released: bool):
        return Packet(self.address, switch, released)

    def __repr__(self):
        return "<{}.{} address={}>".format(
            self.__class__.__module__,
            self.__class__.__name,
            self.address,
        )


class Bus:
    """Biomatx Bus.

    The bus is a group of maximum 7 modules connected together. It uses an UTP cable
    with RJ45 connectors to convey a RS485 serial signal. Each time a switch is
    pressed/released, a packet is emitted on the bus. Sending a packet on the bus will
    trigger the matching relay.

    """

    def __init__(self, module_count: int):
        self.modules = {}
        for i in range(0, 8):
            if i < module_count or i == 7:
                self.modules[i] = Module(self, i)

    def switch(self, module: int, address: int):
        return self.modules[module].switches[address]

    def relay(self, module: int, address: int):
        return self.modules[module].relays[address]

    async def connect(
        self,
        port: str,
        callback: Callable[[Switch | Relay], Awaitable[None]],
        loop: asyncio.Loop = None,
    ):
        """Open the serial device to which the physical bus is connected."""
        import serial
        import serial_asyncio

        if loop is None:
            loop = asyncio.get_event_loop()
        self._callback = callback

        _LOGGER.debug("connecting to %s", port)
        self._reader, self._writer = await serial_asyncio.open_serial_connection(
            loop=loop,
            url=port,
            baudrate=19200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            xonxoff=False,
            rtscts=False,
        )
        _LOGGER.info("connected to %s", port)

    async def loop(self):
        """Process packets in a loop, keeping the device models state up to date."""
        self.running = True
        _LOGGER.info("bus monitoring started")
        while self.running:
            _LOGGER.debug("waiting for next packet")
            await self.process_packet()
        _LOGGER.info("bus monitoring stopped")
        self.running = False

    async def send_packet(self, packet: Packet):
        self._writer.write(bytes(packet))
        await self._writer.drain()
        # Leave time for the system to process
        await asyncio.sleep(0.1)

    async def read_packet(self) -> Packet:
        data = await self._reader.readexactly(2)
        return Packet.from_bytes(data)

    def _trigger_callback(self, device: [Switch | Relay]):
        return asyncio.create_task(self._callback(device))

    async def process_packet(self):
        try:
            packet = await self.read_packet()
        except asyncio.IncompleteReadError:
            return []

        relay = self.relay(packet.module, packet.switch)
        switch = self.switch(packet.module, packet.switch)
        tasks = []
        if switch._process(packet):
            tasks.append(self._trigger_callback(switch))
        if relay._process(packet):
            tasks.append(self._trigger_callback(relay))
        return tasks

    def stop(self):
        _LOGGER.info("stopping bus monitoring")
        self.running = False
        self._writer.close()
