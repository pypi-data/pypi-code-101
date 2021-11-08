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
Load yaml configuration file(s)

Load {action: '--flag', ...} for all available menus
'''

import os
from pathlib import Path

import yaml
from ppsi.common import shell
from ppsi.server import SWAYROOT
from yaml.composer import ComposerError


def read_config(custom_conf: os.PathLike = None) -> dict:
    '''
    Read pspbar configuration from supplied yml file or default

    Args:
        custom_conf: custom path of config file pspbar.yml

    Returns:
        pspbar config
    '''
    # default locations
    defconf = Path(__file__).parent.joinpath("config/pspbar.yml")
    config = {}
    with open(defconf, "r") as config_h:
        try:
            config = yaml.safe_load(config_h)
        except (FileNotFoundError, ComposerError):
            shell.notify("Problem with sway bar configuration")
    if custom_conf is None:
        bar_path = Path(SWAYROOT).joinpath("pspbar.yml")
        if bar_path.is_file():
            custom_conf = bar_path
    if custom_conf is not None:
        with open(custom_conf, "r") as config_h:
            try:
                config = {**config, **yaml.safe_load(config_h)}
                # NEXT: in python3.9 this simply becomes
                # config |= yaml.safe_load(config_h)
            except (FileNotFoundError, ComposerError):
                shell.notify("Problem with sway bar configuration")
    return config
