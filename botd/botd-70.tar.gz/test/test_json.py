# This file is placed in the Public Domain.

import unittest

from bot.obj import Object

class Test_JSON(unittest.TestCase):
    def test_jsondump(self):
        o = Object()
        o.test = "bla"
        self.assertEqual(o.__json__(), "{'test': 'bla'}")
