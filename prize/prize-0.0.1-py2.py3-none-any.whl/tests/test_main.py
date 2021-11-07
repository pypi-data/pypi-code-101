#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @PypiSeedTag: MainTest
# @Project : prize

import os
import unittest

import prize.main as main


"""
generated by PypiSeed(PPC) - Unittest
"""

class MainTestCase(unittest.TestCase):
    def test_main(self):
        actual = main.demo()
        expect = "hello prize"
        self.assertEqual(expect, actual, "Must match")


if __name__ == '__main__':
    unittest.main()
