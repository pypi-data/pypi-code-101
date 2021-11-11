# -*- coding: utf-8 -*-

"""Tester class

This module contains the CommandTester class.

Author: G.J.J. van den Burg
License: See the LICENSE file.
Copyright: 2021, G.J.J. van den Burg

This file is part of Wilderness.
"""

from .command import Command

class CommandTester:
    def __init__(self, command: Command) -> None:
        self._command = command

    def run(self, args: str) -> None:
        pass
