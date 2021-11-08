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
Battery monitor and action segment
"""

from re import findall
from shutil import which
from typing import Dict, Optional

import psutil
from ppsi.common import shell
from ppsi.pspbar import CONFIG
from ppsi.pspbar.classes import BarSeg
from ppsi.server.sway_api import sway_nag

EMOJIS = {
    "bat_100": '\uf240',
    "bat_75": '\uf240',
    "bat_50": '\uf242',
    "bat_25": '\uf243',
    "bat_0": '\uf244',
}

UPOWER_AVAIL = bool(which("upower"))
BAT_CONF = CONFIG['battery']


def bat_time() -> Optional[float]:
    """
    Parse upower and estimate

    Returns
        Estimated hours to empty/full battery if available, else ``None``
    """
    if not UPOWER_AVAIL:
        return None
    upower_dump = shell.process_comm("upower", "-d")
    if upower_dump is None:
        return None
    matches = findall(r"time +to +\w+: +(.+?) +(.+)", upower_dump)
    if not matches:
        return None
    time_str, units = matches[0]
    try:
        hours = float(time_str) * {
            "days": 24,
            "hours": 1,
            "minutes": 1 / 60,
            "seconds": 1 / 3600
        }.get(units, 1)
    except (AttributeError, ValueError, IndexError, KeyError):
        return None
    return hours


class BatSeg(BarSeg):
    '''
    Battery segment,
    '''
    def __init__(self, **kwargs):
        # display: 0 -> None, 1 -> percentage, [2 -> estimated time]
        self.display = {'time': 2, 'percent': 1}.get(BAT_CONF['display'], 0)
        if not UPOWER_AVAIL and self.display == 2:
            self.display = 1
        super().__init__(**kwargs)

    @staticmethod
    def _bat_act(conn: bool, fill: float, mem: int) -> int:
        '''
        Emergency Actions.

        Args:
            conn: charger connected?
            fill: battery charge fill percentage
            mem: count memory of warning flash notifications

        Returns:
            updated mem

        Notifies:
            ``notify`` emergency multiple times and suspends if critical

        '''
        if conn:
            mem = max(mem, 0)
            if fill > 99 and mem < 5:
                mem += 1
                # Send only 5 notifications
                shell.notify('Battery_charged')
        else:
            time_left = bat_time() or 0xffff
            mem = min(mem, 0)
            if fill < BAT_CONF['suspend'] or time_left < (1 / 24):
                shell.process_comm('systemctl',
                                   'suspend',
                                   timeout=-1,
                                   fail='notify')
            elif fill < BAT_CONF['critical'] or time_left < (1 / 12):
                shell.notify('Battery Too Low Suspending Session...',
                             timeout=0,
                             send_args=('-u', 'critical'))
                sway_nag("Battery Too Low Suspending Session...")
            elif fill < BAT_CONF['minimal'] or time_left < (1 / 6):
                mem -= 1
                if mem % 5 == 0:
                    shell.notify('Battery Too Low',
                                 timeout=0,
                                 send_args=('-u', 'critical'))
            elif fill < BAT_CONF['low'] or time_left < (1 / 3):
                mem -= 1
                if mem % 10 == 0:
                    shell.notify('Low battery', timeout=0)
        return mem

    def call_me(self, mem: int = None, **_) -> Dict[str, object]:
        '''
        Create Battery summary string

        Args:
            mem: int = count memory of warning flash notifications
            **kwargs: all are ignored

        Returns:
            dict to update ``BarSeg`` properties

        '''
        color = None
        sym_pango = ['', '']
        bat_probe = psutil.sensors_battery()
        if not bat_probe:
            return {'symbol': EMOJIS['bat_0'], 'vis': False}
        try:
            bat_fill = bat_probe.percent
            bat_conn = bat_probe.power_plugged
        except AttributeError:
            return {'symbol': EMOJIS['bat_0'], 'vis': False}
        if bat_conn:
            sym_pango = ['<span foreground="#7fffffff">', '</span>']
        # Action
        mem = self._bat_act(conn=bat_conn, fill=bat_fill, mem=mem or 0)
        # returns
        if bat_fill >= 100:
            sym, color = EMOJIS['bat_100'], "#7fffffff"
        elif bat_fill > BAT_CONF['green']:
            sym, color = EMOJIS['bat_75'], "#7fff7fff"
        elif bat_fill > BAT_CONF['yellow']:
            sym, color = EMOJIS['bat_50'], "#ffff7fff"
        elif bat_fill > BAT_CONF['red']:
            sym, color = EMOJIS['bat_25'], "#ff7f7fff"
        else:
            sym, color = EMOJIS['bat_0'], "#ff5f5fff"
        if self.display == 2:
            # time
            time = bat_time()
            if time is None:
                val = f"{bat_fill:.2f} %"
            else:
                val = f"{int(time)}:{int((time%1) * 60)}"
        elif self.display == 1:
            # battery in percentage
            val = f"{bat_fill:.2f}"
        else:
            val = ''

        sym = sym_pango[0] + sym + sym_pango[1]
        return {'symbol': sym, 'magnitude': val, 'mem': mem, 'color': color}

    def callback(self, **_) -> None:
        """
        toggle between percentage and estimated time
        """
        self.display = (self.display + 1) % (int(UPOWER_AVAIL) + 2)
        self.units = ["", "%", "h"][self.display]


BATTERY = BatSeg(name="battery",
                 symbol=EMOJIS['bat_0'],
                 units="h" if UPOWER_AVAIL else "%",
                 mem=0,
                 pango=True)
'''
battery segment instance
'''
BATTERY.set_proto(markup='pango')
