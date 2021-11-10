#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    Wisteria Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Wisteria.
#    Wisteria is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Wisteria is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Wisteria.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    Wisteria project : wisteria/wisteria/cwc/simple/s_default.py

    Default cwc/SimpleClass class, a simple class made of the following types:
    - int
    - str
    - list
    - dict
        Note that dicts have only non string keys.

    ___________________________________________________________________________

    o  SimpleClass class
"""


class SimpleClass:
    """
        SimpleClass class
    """
    def __eq__(self,
               other):
        """SimpleClass.__eq__()"""
        return self.integer == other.integer and \
            self.string == other.string and \
            self._list == other._list and \
            self._dict == other._dict

    def __init__(self,
                 integer=3,
                 string="string",
                 _list=[1, 2, 3],
                 _dict={"key1": "value1"}):
        """SimpleClass.__init__()"""
        self.integer = integer
        self.string = string
        self._list = _list
        self._dict = _dict
