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
'''
Temperature monitoring and acting segment
'''

from typing import Dict

import psutil
from ppsi.pspbar import CONFIG
from ppsi.pspbar.classes import BarSeg

TEMP_CONFIG = CONFIG['temperature']

EMOJIS = {
    "fire": chr(0x1f525),
    "temp_100": '\uf2c7',
    "temp_75": '\uf2c8',
    "temp_50": '\uf2c9',
    "temp_25": '\uf2ca',
    "temp_0": '\uf2cb',
}


class TempSeg(BarSeg):
    '''
    Temperature segment
    '''
    @staticmethod
    def call_me(**_) -> Dict[str, object]:
        '''
        Create Temperature summary string

        Args:
            all are ignored

        Returns:
            dict to update ``BarSeg`` properties

        '''
        color = None
        try:
            heat = psutil.sensors_temperatures()['coretemp'][0].current
        except:
            return {'vis': False}
        if heat > TEMP_CONFIG['fire']:
            sym, val = EMOJIS['fire'], f"{heat:.0f}"
            color = "#ff5f5fff"
        elif heat > TEMP_CONFIG['orange']:
            sym, val = EMOJIS['temp_100'], f"{heat:.0f}"
            color = "#ffaf7fff"
        elif heat > TEMP_CONFIG['yellow']:
            sym, val = EMOJIS['temp_75'], f"{heat:.0f}"
            color = "#ffff5fff"
        elif heat > TEMP_CONFIG['hot']:
            sym, val = EMOJIS['temp_50'], f"{heat:.0f}"
        elif heat > TEMP_CONFIG['warm']:
            sym, val = EMOJIS['temp_25'], f"{heat:.0f}"
        else:
            sym, val = EMOJIS['temp_0'], f"{heat:.0f}"
        return {'symbol': sym, 'magnitude': val, 'color': color}


TEMPERATURE = TempSeg(name="temperature",
                      symbol=EMOJIS['fire'],
                      units='\u2103')
'''temperature segment instance'''
