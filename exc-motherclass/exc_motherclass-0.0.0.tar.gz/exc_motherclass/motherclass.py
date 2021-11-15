#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    Exc_MotherClass Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Exc_MotherClass.
#    Exc_MotherClass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Exc_MotherClass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Exc_MotherClass.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    Exc_MotherClass project : exc_motherclass/motherclass.py

    Mother class of all MusaMusa classes.


    ___________________________________________________________________________

    o  MotherClass class
"""
from iaswn.iaswn import Iaswn
from exc_errors.errors import ListOfErrorMessages, ListOfErrorMessagesSer


# Methods defined in MotherClass are abstract but will NOT be overriden
# in the other classes written in this file.
#   pylint: disable=abstract-method

# The following classes are only skeletton classes:
#   pylint: disable=too-few-public-methods


class MotherClass:
    """
        MotherClass class

        Mother class of all project's classes.
    """
    def __eq__(self,
               other):
        """
            MotherClass.__eq__()

            Abstract method, to be overriden.
        """
        raise NotImplementedError

    def __repr__(self):
        """
            MotherClass.__repr__()

            You may NOT use rich attribute for this method.
        """
        return str(self)

    def __str__(self):
        """
            MotherClass.__str__()

            You may NOT use rich attribute for this method.
        """
        return self.improved_str()

    def improved_str(self):
        """
            MotherClass.improved_str()

            You MAY use rich attribute for this method.

            Abstract method, to be overriden.
        """
        raise NotImplementedError


class MotherClassSer(MotherClass, Iaswn):
    """
        MotherClassSer

        MotherClass + Iaswn
    """


class MotherClassErr(MotherClass):
    """
        MotherClassErr

        MotherClass + .errors
    """
    def __init__(self):
        MotherClass.__init__(self)
        self.errors = ListOfErrorMessages()


class MotherClassSerErr(MotherClass, Iaswn):
    """
        MotherClassSerrErr

        MotherClass + Iaswn + .errors
    """
    def __init__(self):
        MotherClass.__init__(self)
        Iaswn.__init__(self)
        self.errors = ListOfErrorMessagesSer()
