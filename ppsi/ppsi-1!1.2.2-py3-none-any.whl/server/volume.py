#!/usr/bin/env python3
#
# Copyright 2020-2021 Pradyumna Paranjape
# This file is part of ppsi.
#
# ppsi is free software: you can RRistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ppsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.        See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ppsi.        If not, see <https://www.gnu.org/licenses/>.
#
'''
Volume api to interface ``pulseaudio``.

Calls ``pactl`` for information and changes.
'''

import math
import re
import subprocess
import typing

from ppsi.common import shell


def bar_val_color(left: float,
                  right: float,
                  muted: bool = False,
                  pig_order: typing.List[str] = None,
                  **_) -> str:
    '''
    Process sound volume magnitude to #AARRGGBB colors

    Args:
        left: volume of left channel {percent}
        right: volume of right channel {percent}
        muted: mute state
        pig_order: pigment order
        **kwargs: all are ignored

    Returns:
        wob input string val(%) #background #frame #foreground
    '''
    pig_order = pig_order or ['AA', 'RR', 'GG', 'BB']
    if right is None or left is None:
        return ''
    if muted is None:
        muted = False  # assume
    value = left + right
    value /= 200  # fished value is in %age
    hyper_vol = False
    value = max(value, 0)
    # defaults
    bgcol = {'RR': 0x00, 'GG': 0x00, 'BB': 0x00, 'AA': 0xff}
    color = {'RR': 0xff, 'GG': 0xff, 'BB': 0xff, 'AA': 0xff}
    frcol = {'RR': 0xff, 'GG': 0xff, 'BB': 0xff, 'AA': 0xff}

    if value > 1:
        value = (value - 1) % 1
        hyper_vol = True
    color['RR'] = round((1 - value) * 0xff)
    color['GG'] = round((value) * 0xff)
    color['BB'] = round(math.sin(math.pi * value) * 0xff)
    if muted:
        for pigment, sat in color.items():
            if pigment != 'AA':
                # skip AA
                frcol[pigment] = 0xff - sat
    else:
        frcol = color
    if hyper_vol:
        color['RR'] |= 0xff
        bgcol, color = color, bgcol
    bg_str = ''.join([f'{bgcol[pig]:0{2}x}' for pig in pig_order])
    fr_str = ''.join([f'{frcol[pig]:0{2}x}' for pig in pig_order])
    col_str = ''.join([f'{color[pig]:0{2}x}' for pig in pig_order])
    # outputs
    return f"{round(value * 100)} #{bg_str} #{fr_str} #{col_str}"


def get_sink_defaults() -> dict:
    '''
    fetch pulseaudio volume output channel index,
    left channel volume, right channel volume, mute state,
    from ``pactl`` output

    Returns:
        Dictionary of fetched values

    '''
    vol_prop = {'index': '', 'left': 0, 'right': 0, 'muted': False}
    index_pat = re.compile(r'Sink\W+#(\d+)')
    curr_volume_pat = re.compile(r'\W+Volume: .*?(\d+?)%.*?(\d+?)%')
    muted_pat = re.compile(r'\W+?Mute:\W+?(\w+)')
    pa_info = shell.process_comm("pactl", "list", "sinks", p_name="Get info")
    if pa_info is None or pa_info == []:
        return {'index': None}
    index = index_pat.findall(pa_info)[0]
    if not index:
        return {'index': None}
    vol_prop['index'] = index
    volumes = curr_volume_pat.findall(pa_info)
    muted_grp = muted_pat.findall(pa_info)
    if volumes:
        vol_prop['left'] = int(volumes[0][0])
        vol_prop['right'] = int(volumes[0][1])
    if muted_grp:
        vol_prop['muted'] = muted_grp[0].lower() != 'no'
    return vol_prop


def vol(subcmd: int = 1, change: float = 2) -> int:
    '''
    Args:
        subcmd: int = action codes {0,1,-1}
            0: mute
            1: volume up by <change>%
            -1: volume down <change>%
        change: float = percentage change requested

    Returns:
        error code
    '''
    subcmd %= 3
    cmd = ['pactl']
    sink_idx = get_sink_defaults()['index']
    if sink_idx is None:
        return 1
    if subcmd:
        direction = [None, '+', '-'][subcmd]
        cmd += ['set-sink-volume', f"{direction}{change}%"]
    else:
        cmd += ['set-sink-mute', 'toggle']
    cmd.insert(2, str(sink_idx))
    shell.process_comm(*cmd, p_name="adjusting volume", timeout=-1)
    return 0


def vol_feedback(wob: subprocess.Popen, **_) -> None:
    '''
    Feedback volume via ``wob``

    Args:
        wob: process handle to pipe-in wob input string
        **kwargs: all are ignored

    '''
    sink_state = get_sink_defaults()
    wob_in_str = bar_val_color(**sink_state)
    stdin = wob.stdin
    stdin.write(wob_in_str + "\n")
    stdin.flush()
