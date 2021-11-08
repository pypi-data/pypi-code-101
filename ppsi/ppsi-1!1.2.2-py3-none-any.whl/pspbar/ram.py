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
RAM monitoring segment
'''

from typing import Dict

import psutil
from ppsi.pspbar import CONFIG
from ppsi.pspbar.classes import BarSeg

RAM_CONFIG = CONFIG['ram']


class RamSeg(BarSeg):
    '''
    RAM segment
    '''
    @staticmethod
    def call_me(**_) -> Dict[str, object]:
        '''
        Create RAM summary string

        Args:
            all are ignored

        '''
        try:
            ram_fill = psutil.virtual_memory().percent
        except AttributeError:
            return {'vis': False}
        color = None
        if ram_fill > RAM_CONFIG['red']:
            color = "#ff5f5fff"
        elif ram_fill > RAM_CONFIG['orange']:
            color = "#ffaf7fff"
        elif ram_fill > RAM_CONFIG['yellow']:
            color = "#ffff5fff"
        return {'magnitude': f"{ram_fill:.0f}", 'color': color}


RAM = RamSeg(name="ram", symbol='\uf233', units="%")
