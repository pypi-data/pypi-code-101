#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
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
"""
pspbar callable function
"""

import datetime
import json
import sys
import time
import warnings

from ppsi.pspbar import CONFIG
from ppsi.pspbar.battery import BATTERY
from ppsi.pspbar.classes import SBar
from ppsi.pspbar.cpu import CPU
from ppsi.pspbar.load_average import LOAD
from ppsi.pspbar.network import IP_ADDR, NETSPEED
from ppsi.pspbar.ram import RAM
from ppsi.pspbar.temperature import TEMPERATURE
from ppsi.pspbar.timer import TIME
from ppsi.pspbar.uname import OSNAME


def pspbar(period: int = None, multi: int = None, num_iter: int = -1):
    '''
    Fetch parameters from cli and launch pspbar

    Args:
        num_iter: number of iterations to loop and print

    Returns:
        ``None``

    Main Routine
    '''
    if 'psutil' not in sys.modules or not CONFIG:
        while num_iter != 0:
            # basic output
            if num_iter >= 0:
                num_iter -= 1
            print('<span foreground=\\"#ff7f7fff\\"> Install psutil',
                  'meanwhile, falling back to basic:\t',
                  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  '</span>',
                  flush=True)
            time.sleep(1)
    else:
        warnings.filterwarnings('ignore')
        period = period or CONFIG['update']
        multi = multi or CONFIG['slow']
        topbar = SBar()
        NETSPEED.mem = [period * multi, 0, 0]
        if CONFIG['time']['active']:
            topbar.add_segs(segment=TIME, position=0, interval=1)
        if CONFIG['battery']['active']:
            topbar.add_segs(segment=BATTERY, position=1, interval=2)
        if CONFIG['cpu']['active']:
            topbar.add_segs(segment=CPU, position=2, interval=1)
        if CONFIG['temperature']['active']:
            topbar.add_segs(segment=TEMPERATURE, position=3, interval=2)
        if CONFIG['ram']['active']:
            topbar.add_segs(segment=RAM, position=4, interval=1)
        if CONFIG['network']['active']:
            topbar.add_segs(segment=IP_ADDR, position=5, interval=0)
        if CONFIG['network']['active']:
            topbar.add_segs(segment=NETSPEED, position=6, interval=2)
        if CONFIG['uname']['active']:
            topbar.add_segs(segment=OSNAME, position=7, interval=0)
        if CONFIG['load']['active']:
            topbar.add_segs(segment=LOAD, position=8, interval=2)
        header = {'version': 1, "click_events": True}
        print(json.dumps(header), "[", "[]", sep="\n")
        topbar.loop(period=period, multi=multi, num_iter=num_iter)
