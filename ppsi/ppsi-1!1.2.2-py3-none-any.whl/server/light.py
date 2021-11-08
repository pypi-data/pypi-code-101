#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; -*-
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
# along with ppsi. If not, see <https://www.gnu.org/licenses/>.
#
'''
light api to handle screen brightness

calls ``light`` for changes
'''

import math
import subprocess
import typing

from ppsi.common import shell


def bar_val_color(value: float, pig_order: typing.List[str] = None) -> str:
    '''
    Process magnitude to ARGB colors.

    Args:
        value: magnitude value of light [%age]
        pig_order: pigment order

    Returns:
        wob input string val(in %) #background #frame #foreground

    '''
    pig_order = pig_order or ['AA', 'RR', 'GG', 'BB']
    value /= 100  # light yields %age value
    value = max(value, 0)
    # defaults
    bgcol = {'RR': 0x00, 'GG': 0x00, 'BB': 0x00, 'AA': 0xff}
    color = {'RR': 0xff, 'GG': 0xff, 'BB': 0xff, 'AA': 0xff}
    frcol = {'RR': 0xff, 'GG': 0xff, 'BB': 0xff, 'AA': 0xff}

    if value > 1:
        value = 1
    color['RR'] = round((1 - value) * 0xff)
    color['GG'] = round((value) * 0xff)
    color['BB'] = round(math.sin(math.pi * value) * 0xff)
    frcol = color
    bg_str = ''.join([f'{bgcol[pig]:0{2}x}' for pig in pig_order])
    fr_str = ''.join([f'{frcol[pig]:0{2}x}' for pig in pig_order])
    col_str = ''.join([f'{color[pig]:0{2}x}' for pig in pig_order])
    # outputs
    cent_value = round(value * 100)
    return f"{cent_value} #{bg_str} #{fr_str} #{col_str}"


def light(subcmd: int = 1, change: float = 2) -> int:
    '''
    Call ``light``.

    Args:
        subcmd: action codes {0,1,-1}
            0: show brightness level
            1: light up by <change>%
            -1: light down by <change>%
        change: percentage change requested

    Returns:
         ``0``

    '''
    subcmd %= 3
    cmd = ['light']
    direction = ['-G', '-A', '-U'][subcmd]
    cmd += [direction, f'{change}']
    shell.process_comm(*cmd, p_name="adjusting light", timeout=-1)
    return 0


def light_feedback(wob: subprocess.Popen) -> int:
    '''
    Feedback brightness via ``wob``.

    Args:
        wob: process handle to pipe-in wob input string

    Returns:
        Error code
    '''
    brightness = shell.process_comm('light', "-G")
    if brightness is None:
        return 1
    wob_in_str = bar_val_color(value=float(brightness))
    wob.stdin.write(wob_in_str + "\n")  # type: ignore
    wob.stdin.flush()  # type: ignore
    return 0
