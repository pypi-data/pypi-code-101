#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
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
decode commands and subcommands received via unix socket
'''

from ppsi.server.btconnect import connect_bluetooth
from ppsi.server.light import light
from ppsi.server.passmenu import password
from ppsi.server.powermenu import system
from ppsi.server.remote import call_remote
from ppsi.server.volume import vol
from ppsi.server.wificonnect import refresh_wifi
from ppsi.server.workspaces import ws_mod


def cmd_wrap(comm: int, **kwargs) -> int:
    '''
    Call commands accoding to mod

    Args:
        comm: command (mod+subcmd)
        **kwargs: passed on to command

    Returns:
        error code
    '''
    err = 0
    kwargs['subcmd'] = comm & 0x0f
    mod = comm // 0x10
    if mod == 0x1:
        err = ws_mod(**kwargs)
    elif mod == 0x2:
        err = call_remote(**kwargs)
    elif mod == 0x3:
        err = password(**kwargs)
    elif mod == 0x4:
        err = refresh_wifi(**kwargs)
    elif mod == 0x5:
        err = connect_bluetooth(**kwargs)
    elif mod == 0x6:
        err = vol(**kwargs)
    elif mod == 0x7:
        err = light(**kwargs)
    elif mod == 0xF:
        err = system(**kwargs)
    else:
        print('Empty command called')
        err = 1
    return err
