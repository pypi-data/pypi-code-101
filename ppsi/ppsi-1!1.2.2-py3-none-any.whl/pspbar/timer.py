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
Display date-time clock
'''

import datetime
from typing import Dict

from ppsi.pspbar import CONFIG
from ppsi.pspbar.classes import BarSeg

TIME_CONFIG = CONFIG['time']


class TimeSeg(BarSeg):
    '''
    Time Segment

    Attributes:
        full = full 24 hour format?
    '''
    def __init__(self, **kwargs):
        self.fmt24 = TIME_CONFIG.get('fmt24') or "%Y-%m-%d %H:%M:%S"
        self.fmt12 = TIME_CONFIG.get('fmt12') or "%Y-%m-%d %I:%M:%S"
        self.full: bool = TIME_CONFIG['full']
        self.strfmt = self.fmt24 if self.full else self.fmt12
        super().__init__(**kwargs)

    def call_me(self, **_) -> Dict[str, str]:
        '''
        create Time summary string

        Args:
            all are ignored

        Returns:
            dict to update ``BarSeg`` properties

        '''
        return {'magnitude': datetime.datetime.now().strftime(self.strfmt)}

    def callback(self, **_) -> None:
        '''
        Toggle 12/24 hour format

        Args:
            all are ignored

        '''
        self.full = not self.full
        self.strfmt = self.fmt24 if self.full else self.fmt12


TIME = TimeSeg(name="time", symbol='\u23f0')
'''time segment instance'''
