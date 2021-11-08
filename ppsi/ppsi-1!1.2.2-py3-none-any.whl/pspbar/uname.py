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
Display OS name
'''

import os
from typing import Dict

from ppsi.pspbar.classes import BarSeg


class OSNameSeg(BarSeg):
    '''
    OS name
    '''
    @staticmethod
    def call_me(**_) -> Dict[str, object]:
        '''
        Create Linux release string

        Args:
            all are ignored

        Returns:
            dict to update ``BarSeg`` properties

        '''
        try:
            name = os.uname().release.split('.')[-2]
        except:
            return {'vis': False}
        return {'magnitude': name}


OSNAME = OSNameSeg(name="uname", symbol=chr(0x1f427), color="#7f9fffff")
'''os information segment instance'''
