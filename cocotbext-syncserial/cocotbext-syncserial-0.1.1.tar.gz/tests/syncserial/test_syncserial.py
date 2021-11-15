"""

Copyright (c) 2021 Cameron Weston

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

import logging
import os
from random import randint

import cocotb_test.simulator

import cocotb
from cocotb.triggers import Timer, First
from cocotb.regression import TestFactory

from cocotbext.syncserial import SyncSerialSource, SyncSerialSink, Crc_16

class TB:
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        self.sync_source = SyncSerialSource(dut.data, dut.clk)
        self.sync_sink = SyncSerialSink(dut.data, dut.clk)

        self.sync_source.log.setLevel(logging.INFO)
        self.sync_sink.log.setLevel(logging.INFO)

async def run_simple_test(dut, pkt):
    tb = TB(dut)

    await Timer(1,'us')

    # Send the packet
    await tb.sync_source.write(pkt)
    await Timer(10, 'us')

    # Read the packet
    rcv_pkt = await tb.sync_sink.read()
    assert rcv_pkt == pkt

async def run_multiple_test(dut, pkt, num_pkts):
    tb = TB(dut)

    await Timer(1, 'us')

    # Send the packet
    for i in range(num_pkts):
        tb.sync_source.write_nowait(pkt.copy())

    # Read the packets
    for i in range(num_pkts):
        rcv = await tb.sync_sink.read()
        assert rcv == pkt

def packet_generator(sizes):
    test_pkts = []
    for size in sizes:
        # Packets
        count_pkt = []
        idle_pkt = []
        random_pkt = []
        for i in range(size):
            count_pkt.append(i & 0xFF)
            idle_pkt.append(0x7E)
            random_pkt.append(randint(0, 255))
        test_pkts.append(count_pkt)
        test_pkts.append(idle_pkt)
        test_pkts.append(random_pkt)
    return test_pkts

# Setup tests
if cocotb.SIM_NAME:
    # Create some packets
    size = [256, 1028, randint(1, 4096)]
    num_pkts = [randint(2,10)]

    test_pkts = packet_generator(size)

    factory = TestFactory(run_simple_test)
    factory.add_option("pkt", test_pkts)
    factory.generate_tests()

    factory = TestFactory(run_multiple_test)
    factory.add_option("pkt", test_pkts)
    factory.add_option("num_pkts", num_pkts)
    factory.generate_tests()

# cocotb-test
tests_dir = os.path.dirname(__file__)

def test_syncSerial(request):
    dut = "test_syncserial"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = dut.lower()

    vhdl_sources = [
        os.path.join(tests_dir, f"{dut}.vhd")
    ]

    parameters = {}

    extra_env = {}

    # Uncomment for waveform file
    sim_args = [
        f"--fst={dut}.vhd"
    ]

    extra_args = []

    compile_args = []

    sim_build = os.path.join(tests_dir, "sim_build",
        request.node.name.replace('[', '-').replace(']', ''))

    cocotb_test.simulator.run(
        python_search=[tests_dir],
        vhdl_sources=vhdl_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        sim_build=sim_build,
        compile_args=compile_args,
        sim_args=sim_args,
        extra_env=extra_env,
        extra_args=extra_args,
        toplevel_lang='vhdl',
    )
