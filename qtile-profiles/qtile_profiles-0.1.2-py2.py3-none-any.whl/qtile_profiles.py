# Copyright (C) 2021 Paul Hoffmann <phfn@phfn.de>

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

"A profile manger for qtile"

__version__ = "0.1.2"

from dataclasses import dataclass
from typing import Callable, Union

import libqtile
from libqtile.core.manager import Qtile
from libqtile.log_utils import logger
from libqtile.config import Match, Rule


@dataclass
class Profile():

    programs: dict[str, str]
    init: list[tuple[int, list[str]]]
    on_load: Union[Callable[[Qtile], None], None] = None

    def spawn_init(self, qtile: Qtile):
        logger.warn(f"{self.init=}")
        for group, commands in self.init:
            logger.warn(f"{commands=}")
            for command in commands:
                logger.warn(f"{command=}")
                pid = self.spawn(qtile, command, group)
                logger.warn(f"{pid=}")

    def get_program(self, name: str):
        if name not in self.programs.keys():
            return name
        return self.programs[name]

    def spawn(self, qtile: Qtile, program: str, group=None) -> int:
        if program in self.programs:
            command = self.programs[program]
        else:
            command = program
        pid = qtile.cmd_spawn(command)
        if group is not None:
            qtile.dgroups.add_rule(Rule(Match(net_wm_pid=pid), group))
        return pid


class ProfileManager():

    def __init__(self, profiles: list[Profile]):
        if len(profiles) < 1:
            raise ValueError("profiles must have at least one Element")
        self.profiles = profiles
        self.load_profile(0, libqtile.qtile)  # type: ignore
        self.next_profile(libqtile.qtile)  # type: ignore

    def next_profile(self, qtile: Qtile):
        i = self.profiles.index(self.current_profile) + 1
        self.load_profile(i, qtile)

    def load_profile(self, i, qtile: Qtile):
        self.current_profile = self.profiles[i % len(self.profiles)]
        if self.current_profile.on_load is not None:
            self.current_profile.on_load(qtile)

    def spawn(self, qtile: Qtile, command):
        self.current_profile.spawn(qtile, command)
