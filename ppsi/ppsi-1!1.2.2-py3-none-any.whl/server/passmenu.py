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
# inspired by pass's passmenu
'''
password manager pass api

Interactive password manager using `menu`
'''

import os
import re
from pathlib import Path
from time import sleep
from typing import Optional

from launcher_menus import menu
from ppsi.common import shell


def generate_password(user_idx: Optional[str] = None) -> int:
    '''
    Generate password interactively and copy it to ``wl-copy``

    Args:
        user_idx: user-requested password index

    Returns:
        error

    '''
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    if user_idx is None:
        user_idx = menu(opts=[], prompt='password for')
    if user_idx is None:
        return 1
    pass_gen = shell.process_comm('pass',
                                  'generate',
                                  user_idx,
                                  p_name='generating password')
    if pass_gen is None:
        return 1
    pass_text = pass_gen.split('\n')
    pass_text.remove('')
    pass_plain = ansi_escape.sub('', pass_text[-1])
    shell.process_comm('wl-copy',
                       '-o',
                       '-n',
                       '-f',
                       pass_plain.strip("\n"),
                       p_name='grabbing password')
    return 0


def grab_password() -> Optional[str]:
    '''
    Select password interactively and copy it to ``wl-copy``
    flush ``wl-paste`` after 45 sec to forget it

    Returns:
        if user entered an unknown password index, return it else, ``None``
    '''
    prefix = os.environ.get('PASSWORD_STORE_DIR',
                            f'{os.environ["HOME"]}/.password-store')
    password_files = []
    for target in Path(prefix).glob("**/*.gpg"):
        password_files.append(str(target.with_suffix("").relative_to(prefix)))
    user_idx = menu(opts=password_files, prompt='password for')
    if user_idx is None:
        # User hit Escape
        return None
    if user_idx not in password_files:
        return user_idx
    # Password is known
    pass_text = shell.process_comm('pass',
                                   'show',
                                   user_idx,
                                   p_name='reading password db')
    if pass_text is None:
        return None
    shell.process_comm('wl-copy',
                       '-o',
                       '-n',
                       '-f',
                       pass_text.strip("\n"),
                       p_name='grabbing password',
                       timeout=-1)
    sleep(45)  # block for 45 seconds
    shell.process_comm('wl-paste', p_name='throwing password', timeout=-1)
    return None


def password(subcmd: int = 0) -> int:
    '''
    Handle password requests

    Args:
        subcmd:
            0: grab password else offer generate (default)
            1: grab password else fail
            2: generate password
    Returns:
        error code

    '''
    subcmd %= 3
    user_idx = None

    if subcmd < 2:
        # grab
        user_idx = grab_password()

    if user_idx is None:
        # password (if any) was copied to wl-copy and deleted
        return 0

    if subcmd == 1:
        # fail
        return 1

    if menu(opts=['No', 'Yes'], prompt='Create?') == 'Yes':
        return generate_password(user_idx=user_idx)

    # user aborted generation of password
    return 0
