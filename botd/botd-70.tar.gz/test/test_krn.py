# This file is placed in the Public Domain.

import unittest

from bot.obj import Cfg
from bot.run import Runtime, getmain
from bot.run import Cfg as RunCfg


class Test_Kernel(unittest.TestCase):
    def test_cfg(self):
        k = getmain("k")
        self.assertEqual(type(k.cfg), RunCfg)
