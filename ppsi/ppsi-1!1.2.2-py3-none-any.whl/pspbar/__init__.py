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
Personal Swaybar in Python

Bar that follows swaybar-protocol with an interface to ``ppsi`` functions.

Defines:

  * An interface to input and output data according to swaybar protocol.
  * Simplified Generic segment-object ``BarSeg`` to feed segments.
  * ``SBar`` bar manager to update various segments at different intervals.

'''
import shutil
import typing

from ppsi.pspbar.classes import BarSeg, SBar
from ppsi.pspbar.config import read_config

CONFIG = read_config()
"""
Configuration read from SWAYROOT
"""


def check_installation() -> None:
    '''
    Check if the following dependencies are available:
        - nothing here yet

    '''
    dependencies: typing.List[str] = []
    for proc in dependencies:
        if shutil.which(proc) is None:
            raise FileNotFoundError(f'{proc} not found')


__all__ = ['BarSeg', 'SBar', 'CONFIG']
