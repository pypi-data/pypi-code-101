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
    Wisteria project : wisteria/cwc/simple/works_as_expected.py

    initialize() and works_as_expected() functions for all cwc/simple/ classes.


    ___________________________________________________________________________

    o  initialize(obj)
    o  works_as_expected(obj)
"""


def initialize(obj):
    """
        initialize() function

        _______________________________________________________________________

        ARGUMENT: <obj>, the object to be initialized

        RETURNED OBJECT: <obj>, the now initialized object
    """
    return obj


def works_as_expected(data_name=None,
                      obj=None):
    """
        works_as_expected()

        works_as_expected() function for basic types defined DATA/UNAVAILABLE_DATA.


        _______________________________________________________________________

        (pimydoc)works_as_expected arguments and returned value
        ⋅All works_as_expected() functions are supposed to (1) say if <data_name> is in
        ⋅the scope of this function (2) and say if <obj> works as expected.
        ⋅
        ⋅ARGUMENTS:
        ⋅    o  data_name:   (None or str)data_name of the <obj>ect
        ⋅    o  obj:         (None or any object) object to be checked
        ⋅
        ⋅RETURNED VALUE:
        ⋅    (<obj> is None, <data_name> is not None) (bool)<data_name> is known
        ⋅    (<obj> is not None, <data_name> may be None or a str.) <obj> works as expected.
    """
    if obj is None:
        # for CWC objects, this case is never reached.
        return True

    return obj.integer == 3 and \
        obj.string == "string" and \
        obj._list == [1, 2, 3] and \
        obj._dict == {"key1": "value1"}
