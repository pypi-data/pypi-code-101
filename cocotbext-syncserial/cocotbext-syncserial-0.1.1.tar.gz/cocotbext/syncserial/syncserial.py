"""

Copyright (c) 2021 Cameron Weston

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import logging
from collections import deque

import cocotb
from cocotb.triggers import FallingEdge, RisingEdge, Event, Timer, First
from cocotb.clock import Clock

from .version import __version__

class SyncSerialSource:
    def __init__(self, data, clock, clock_rate_mhz = 10, append_crc = True, crc_polynomial = 0x1021, crc_init = 0xFFFF, crc_final_xor = 0x0000, *args, **kwargs):
        self.log = logging.getLogger(f"cocotb.{data._path}")
        self._data = data
        self._clock = clock
        self._clock_rate_mhz = clock_rate_mhz
        self._append_crc = append_crc
        self._crc = Crc_16(crc_polynomial, crc_init, crc_final_xor)

        self.log.info("Synchronous Serial source")
        self.log.info("cocotbext-syncserial version %s", __version__)
        self.log.info("Copyright (c) 2021 Cameron Weston")
        self.log.info("https://github.com/cameronweston/cocotbext-syncserial")

        super().__init__(*args, **kwargs)

        self.queue = deque()

        self._data.setimmediatevalue(0)
        self._clock.setimmediatevalue(0)

        self.log.info("Synchronous Serial source configuration:")
        self.log.info(" Clock Rate: %f Mhz", self._clock_rate_mhz)
        self.log.info(" Append CRC: %s", self._append_crc)
        if self._append_crc == True:
            self.log.info(" Initial Value: %s", hex(crc_init))
            self.log.info(" CRC Polynomial: %s", hex(crc_polynomial))
            self.log.info(" CRC Final Xor: %s", hex(crc_final_xor))

        self._data_cr = None
        self._clk_cr = None
        self._restart()

    def _restart(self):
        if self._data_cr is not None:
            self._data_cr.kill()
        if self._clk_cr is not None:
            self._clk_cr.kill()

        # Start the data and clock coroutines
        self._data_cr = cocotb.start_soon(self._run())
        self._clk_cr = cocotb.start_soon(Clock(self._clock, 1 / self._clock_rate_mhz * 1000, units = 'ns').start())

    # Blocking write calls non blocking write function
    async def write(self, packet):
        self.write_nowait(packet)

    # Adds packet to the queue
    def write_nowait(self, packet):
        self.queue.append(packet.copy())

    # Returns the number of packets
    def count(self):
        return len(self.queue)

    def empty(self):
        return not self.queue

    def clear(self):
        self.queue.clear()

    async def _send_byte(self, byte, num_consecutive_ones, isIdleByte = False):
        num_ones = num_consecutive_ones
        orig_byte = byte
        for i in range(8):
            # Grab the LSB
            bit = byte & 1
            byte = byte >> 1

            # Send the bit
            await RisingEdge(self._clock)
            self._data.value = bit

            # If bit is 1 then we need to increase our counter
            if bit == 1:
                num_ones = num_ones + 1
            else:
                num_ones = 0

            # Determine if we need to zero fill
            if num_ones == 5 and not isIdleByte:
                num_ones = 0
                await RisingEdge(self._clock)
                self._data.value = 0


        return num_ones

    async def _run(self):
        while True:
            while not self.queue:
                # No data so send idle bytes
                await self._send_byte(0x7E, 0, True)

            # Grab the next packet
            packet = self.queue.popleft()

            # Calculate the CRC and append to the packet
            if self._append_crc:
                crc = self._crc.calculate_crc(packet)
                packet.append(crc >> 8 & 0xFF)
                packet.append(crc & 0xFF)

            # Need to keep track of the number of consecutive ones
            num_consecutive_ones = 0
            for byte in packet:
                num_consecutive_ones = await self._send_byte(byte, num_consecutive_ones)

            # Send the idle byte to indicate the end of the packet
            await self._send_byte(0x7E, 0, True)

class SyncSerialSink:
    def __init__(self, data, clock, validate_crc = True, strip_crc = True, crc_polynomial = 0x1021, crc_init = 0xFFFF, crc_final_xor = 0x0000, *args, **kwargs):
        self.log = logging.getLogger(f"cocotb.{data._path}")
        self._data = data
        self._clock = clock
        self._validate_crc = validate_crc
        self._strip_crc = strip_crc
        self._crc = Crc_16(crc_polynomial, crc_init, crc_final_xor)

        self.log.info("Synchronous Serial sink")
        self.log.info("cocotbext-syncserial version %s", __version__)
        self.log.info("Copyright (c) 2021 Cameron Weston")
        self.log.info("https://github.com/cameronweston/cocotbext-syncserial")

        super().__init__(*args, **kwargs)

        self.queue = deque()
        self.sync = Event()

        self.log.info("Synchronous Serial sink configuration:")
        self.log.info(" Validate CRC: %s", self._validate_crc)
        if self._validate_crc == True:
            self.log.info(" Initial Value: %s", hex(crc_init))
            self.log.info(" CRC Polynomial: %s", hex(crc_polynomial))
            self.log.info(" CRC Final Xor: %s", hex(crc_final_xor))
            self.log.info(" Strip Crc: %s", hex(self._strip_crc))

        self._cr = None
        self._restart()

    def _restart(self):
        if self._cr is not None:
            self._cr.kill()

        # Start the coroutine
        self._cr = cocotb.start_soon(self._run())

    # Blocking read call to read a packet
    async def read(self):
        # Wait for a packet to arrive
        while self.empty():
            self.sync.clear()
            await self.sync.wait()
        return self.read_nowait()

    # Non-blocking read to read a packet
    def read_nowait(self):
        pkt = []

        if not self.empty():
            pkt = self.queue.popleft()
        return pkt

    # Returns the number of packets
    def count(self):
        return len(self.queue)

    def empty(self):
        return not self.queue

    def clear(self):
        self.queue.clear()

    # Waits for queue to have a packet
    async def wait(self, timeout = 0, time_unit = 'ns'):
        if not self.empty():
            return
        self.sync.clear()
        if timeout:
            await First(self.sync.wait(), Timer(timeout, time_unit))
        else:
            await self.sync.wait()

    # Reads byte from interface
    async def _read_byte(self, num_consecutive_ones):
        num_ones = num_consecutive_ones
        byte = 0
        bit_location = 0
        isIdleFlag = False
        if num_ones != 5:
            dropNextZero = False
        else:
            dropNextZero = True
        bit_dropped = False
        while bit_location < 8:
            await FallingEdge(self._clock)
            valid_bit = True
            bit = self._data.value.integer

            # Drop bit true after 5 bits, a 6th bit indicates it should be a idle flag
            if dropNextZero and not bit:
                valid_bit = False
                bit_dropped = True
                dropNextZero = False
            elif dropNextZero and bit:
                dropNextZero = False

            # Increament counter if bit = 1
            if bit:
                num_ones = num_ones + 1
            else:
                num_ones = 0
            # If it was a 0, determine if it needs to be dropped
            if num_ones ==  5:
                dropNextZero = True
            # If it's not a bit to drop then add it to the byte
            if valid_bit:
                byte = byte | bit << bit_location
                bit_location = bit_location + 1

        # Check and see if it's the idle frame
        if not bit_dropped and byte == 0x7E:
            isIdleFlag = True

        return byte, num_ones, isIdleFlag

    # Performs a bitwise search for the idle flag 0x7E
    async def _find_sync(self):
        found_sync = False
        byte = 0
        while not found_sync:
            await FallingEdge(self._clock)
            bit = self._data.value.integer

            # Data is shifted in least significant bit first
            byte = (bit << 7) | (byte >> 1)

            if byte == 0x7E:
                found_sync = True

    async def _run(self):
        inSync = False
        while True:
            if not inSync:
                # Synchronize to flags
                await self._find_sync()
                inSync = True

            # Need to keep track of the number of consecutive ones
            num_consecutive_ones = 0
            endOfPacket = False
            pkt = []
            # Read a packet
            while not endOfPacket:
                byte, num_consecutive_ones, isIdleFlag = await self._read_byte(num_consecutive_ones)

                # Check if a bad byte was received, we're also probably out of sync
                if num_consecutive_ones >= 7:
                    self.log.debug("Bad packet received, dropping packet, length: %s", len(pkt))
                    pkt = []
                    inSync = False
                    endOfPacket = True
                    break
                # Check if we've reached the end of the packet
                elif isIdleFlag:
                    endOfPacket = True

                    # Check if we have a packet or if we're just receiving idle flags
                    if pkt:
                        if self._validate_crc:
                            # calculate the CRC
                            pkt_crc = pkt[-2] << 8 | pkt[-1]
                            if self._crc.validate_crc(pkt[:-2], pkt_crc):
                                self.log.debug("Received packet with valid crc")
                                #Remove CRC if desired
                                if self._strip_crc:
                                    pkt = pkt[:-2]
                            else:
                                self.log.debug("Recevied packet failed crc")
                                pkt = []
                                break

                        # Add packet to queue
                        self.queue.append(pkt)
                        self.sync.set()
                # Just another byte in the packet so append it
                else:
                    pkt.append(byte)

class Crc_16:
    def __init__(self, crc_polynomial = 0x1021, crc_init = 0xFFFF, crc_final_xor = 0x0000, *args, **kwargs):
        self._crc_polynomial = crc_polynomial
        self._crc_init = crc_init
        self._crc_final_xor = crc_final_xor

        super().__init__(*args, **kwargs)

    def validate_crc(self, data, crc):
        data_crc = self._crc_init
        for b in data:
            data_crc = data_crc ^ b << 8
            for i in range(8):
                if data_crc & 0x8000:
                    data_crc = (data_crc << 1) ^ self._crc_polynomial
                else:
                    data_crc = data_crc << 1

        data_crc = data_crc & 0xFFFF
        data_crc = data_crc ^ self._crc_final_xor
        return data_crc == crc

    def calculate_crc(self, data):
        crc = self._crc_init
        for b in data:
            crc = crc ^ b << 8
            for i in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ self._crc_polynomial
                else:
                    crc = crc << 1

        crc = crc & 0xFFFF
        crc = crc ^ self._crc_final_xor

        return crc
