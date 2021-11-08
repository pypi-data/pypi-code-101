#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
#
# Copyright 2020-2021 Pradyumna Paranjape
# This file is part of ppsi.
#
# ppsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ppsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ppsi.  If not, see <https://www.gnu.org/licenses/>.
#
'''
test ppsi client

ppsi client
'''

import os
from pathlib import Path
from unittest import TestCase

import ppsi
from ppsi.common import shell
from ppsi.pspbar.bar import pspbar
from ppsi.pspbar.network import IP_ADDR


class TestNtwk(TestCase):
    """
    Test IpAddrSeg
    """
    def test_ip_addr_seg(self):
        """
        Test ip address segment in various contexts
        """
        if os.environ.get('READTHEDOCS'):
            return
        IP_ADDR.call_me()
        ip_out = shell.process_comm(
            'sh',
            str(
                Path(ppsi.__file__).parent.joinpath(
                    'pspbar/shell_dep/netcheck.sh')), "-r=0", "-n=5")
        self.assertIsNotNone(ip_out)
        print(ip_out)
        self.assertEqual(int(ip_out.split('\t')[2]), 5)
        ip_out = shell.process_comm(
            'sh',
            str(
                Path(ppsi.__file__).parent.joinpath(
                    'pspbar/shell_dep/netcheck.sh', "-r=1")))
        self.assertIsNone(ip_out)


class TestBar(TestCase):
    """
    Test that PSPBar always sends some output
    """
    def untest_alive(self):
        pspbar(1, 1, num_iter=4)
