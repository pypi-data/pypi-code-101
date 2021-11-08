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
Load yaml configuration file(s), temp storage folder

Load {action: '--flag', ...} for all available menus
Determine a root directory for temporary storage and log files
'''

import os
from pathlib import Path
from typing import Tuple

from xdgpspconf import ConfDisc

CONF_DISC = ConfDisc('sway', Path(__file__).parent / 'config/ppsi.yml')


def read_config(custom_conf: os.PathLike = None,
                swayroot: os.PathLike = None) -> Tuple[Path, dict]:
    '''
    Read ppsi configuration from supplied yml file or default
    Define swayroot to store log files.

    Args:
        custom_conf: custom path of config file ppsi.yml
        swayroot: custom path of root directory to store sway data

    Returns:
        swayroot, config referenced by ``menu``
    '''
    # default locations
    configs = CONF_DISC.read_config(flatten=True,
                                    custom=custom_conf,
                                    cname='ppsi',
                                    ext='yml')
    config = list(configs.values())[0]
    if swayroot is None:
        swayroot = CONF_DISC.safe_config()[-1].parent
    swayroot = Path(swayroot)
    return swayroot.absolute(), config
