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
    Wisteria project : wisteria/serializers.py

    All known serializers are defined here, in the SERIALIZERS dict. Each serializer
    has its own serializer_xxx function.
    A reference to each module imported is added in the MODULES dict.

    ___________________________________________________________________________

    o  _len(obj)
    o  win_memory()

    o  serializer_iaswn(action="serialize",
                        obj=None, obj_data_name=None,
                        fingerprint="",
                        works_as_expected=None)
    o  serializer_json(action="serialize",
                        obj=None,
                        obj_data_name=None,
                        fingerprint="",
                        works_as_expected=None)
    o  serializer_jsonpickle(action="serialize",
                             obj=None, obj_data_name=None,
                             fingerprint="",
                             works_as_expected=None)
    o  serializer_jsonpickle_keystrue(action="serialize",
                                      obj=None, obj_data_name=None,
                                      fingerprint="",
                                      works_as_expected=None)
    o  serializer_marshal(action="serialize",
                          obj=None, obj_data_name=None,
                          fingerprint="",
                          works_as_expected=None)
    o  serializer_pickle(action="serialize",
                         obj=None, obj_data_name=None,
                         fingerprint="",
                         works_as_expected=None)
    o  serializer_pyyaml(action="serialize",
                         obj=None, obj_data_name=None,
                         fingerprint="",
                         works_as_expected=None)
    o  serializer_simpleion(action="serialize",
                            obj=None, obj_data_name=None,
                            fingerprint="",
                            works_as_expected=None)
    o  serializer_yajl(action="serialize",
                       obj=None, obj_data_name=None,
                       fingerprint="",
                       works_as_expected=None)

    o  init_serializers()
"""
#   pylint: disable = wrong-import-position
import timeit

import wisteria.globs

if wisteria.globs.PLATFORM_SYSTEM == "Windows":
    # We have to import 'os' only for Windows systems, hence the useless
    # remark from Pylint when Pylint is used on non-Windows systems.
    #   pylint: disable=unused-import
    import os
    # We have to import 'WMI' only for Windows systems, hence the useless
    # remark from Pylint when Pylint is used on non-Windows systems.
    #   pylint: disable=import-error
    from wmi import WMI
else:
    # We have to import 'resource' only for non-Windows systems, hence the useless
    # remark from Pylint when Pylint is used on Windows systems.
    #   pylint: disable=import-error
    import resource

# MEMOVERUSE# --memoveruse C++ module:
# MEMOVERUSEimport cppyy

from wisteria.globs import TIMEITNUMBER, MODULES
from wisteria.globs import VERBOSITY_DEBUG, VERBOSITY_DETAILS
from wisteria.wisteriaerror import WisteriaError
from wisteria.utils import trytoimport, get_python_version
from wisteria.serializers_classes import SerializersDataNMVH, SerializerData, SerializationResult
from wisteria.msg import msgdebug, msginfo

# MEMOVERUSE# --memoveruse C++ module:
# MEMOVERUSEcppyy.include("memoveruse_cpp/memoveruse_cpp.h")
# MEMOVERUSEcppyy.load_library("memoveruse_cpp/libmemoveruse_cpp")
# MEMOVERUSE#    pylint: disable=import-error,wrong-import-position,wrong-import-order
# MEMOVERUSE#    about noqa: https://pep8.readthedocs.io/en/latest/intro.html#configuration
# MEMOVERUSEfrom cppyy.gbl import MemOverUse  # noqa


def _len(obj):
    """
        _len()

        Return the length of <obj>

        _______________________________________________________________________

        ARGUMENT: (bytes|str)<obj>

        RETURNED VALUE: the length of <obj>
    """
    if isinstance(obj, str):
        return len(bytes(obj, "utf-8"))
    return len(obj)


def win_memory():
    """
        win_memory()

        Compute using WMI the quantity of memory used by the current process.

        _______________________________________________________________________

        RETURNED VALUE: (int)the number of bytes used by the current process.
    """
    wmi = WMI('.')
    result = wmi.query(
        "SELECT WorkingSet "
        f"FROM Win32_PerfRawData_PerfProc_Process WHERE IDProcess={os.getpid()}")
    res = int(result[0].WorkingSet)
    return res


def serializer_iaswn(action="serialize",
                     obj=None,
                     obj_data_name=None,
                     fingerprint="",
                     works_as_expected=None):
    """
        serializer_iaswn()

        Serializer for the Iaswn module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'iaswn'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return module.__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.encode(obj)
        except module.IaswnError:
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID030) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.encode(obj)
        _timeit = timeit.Timer('module.encode(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except module.IaswnError as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.decode(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.decode(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except module.IaswnError as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_json(action="serialize",
                    obj=None,
                    obj_data_name=None,
                    fingerprint="",
                    works_as_expected=None):
    """
        serializer_json()

        Serializer for the json module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'json'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return module.__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except TypeError:
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID031) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except TypeError as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (TypeError, AttributeError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_jsonpickle(action="serialize",
                          obj=None,
                          obj_data_name=None,
                          fingerprint="",
                          works_as_expected=None):
    """
        serializer_jsonpickle()

        Serializer for the jsonpickle module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'jsonpickle'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return module.__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except TypeError:
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID032) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except TypeError as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (TypeError, AttributeError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_jsonpickle_keystrue(action="serialize",
                                   obj=None,
                                   obj_data_name=None,
                                   fingerprint="",
                                   works_as_expected=None):
    """
        serializer_jsonpickle_keystrue()

        Serializer for the jsonpickle module (keys=True).

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'jsonpickle'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return module.__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except TypeError:
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID042) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj, keys=True)
        _timeit = timeit.Timer('module.dumps(obj, keys=True)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except TypeError as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res, keys=True)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res, keys=True)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (TypeError, AttributeError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_marshal(action="serialize",
                       obj=None,
                       obj_data_name=None,
                       fingerprint="",
                       works_as_expected=None):
    """
        serializer_marshal()

        Serializer for the marshal module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'marshal'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return f"version {module.version}; (Python version) {get_python_version()}"

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except (TypeError, ValueError):
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID033) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except (TypeError, ValueError) as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (TypeError, AttributeError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_pickle(action="serialize",
                      obj=None,
                      obj_data_name=None,
                      fingerprint="",
                      works_as_expected=None):
    """
        serializer_pickle()

        Serializer for the pickle module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'pickle'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return f"(Python version) {get_python_version()}"

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except TypeError:
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID034) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except (AttributeError, TypeError) as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (TypeError, AttributeError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_pyyaml(action="serialize",
                      obj=None,
                      obj_data_name=None,
                      fingerprint="",
                      works_as_expected=None):
    """
        serializer_pyyaml()

        Serializer for the pyyaml module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'pyyaml'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return module.__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dump(obj, Dumper=module.Dumper)
        except (ValueError, TypeError):
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID044) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dump(obj, Dumper=module.Dumper)
        _timeit = timeit.Timer('module.dump(obj, Dumper=module.Dumper)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except (ValueError, TypeError) as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.load(_res, Loader=module.Loader)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.load(_res, Loader=module.Loader)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (module.constructor.ConstructorError, ValueError) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_simpleion(action="serialize",
                         obj=None,
                         obj_data_name=None,
                         fingerprint="",
                         works_as_expected=None):
    """
        serializer_simpleion()

        Serializer for the simpleion module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'simpleion'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name__version].__version__

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except (AssertionError, AttributeError, ValueError, TypeError):
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID050) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except (AssertionError, AttributeError, ValueError, TypeError) as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (ValueError,) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def serializer_yajl(action="serialize",
                    obj=None,
                    obj_data_name=None,
                    fingerprint="",
                    works_as_expected=None):
    """
        serializer_yajl()

        Serializer for the yajl module.

        Like every serializer_xxx() function:
        * this function may return (action='version') the version of the concerned module.
        * this function may try (action='serialize') to encode/decode an <obj>ect.
        * if the serializer raises an error, this error is silently converted and no exception
          is raised. If an internal error happpens, a WisteriaError exception is raised.

        This function assumes that the concerned module has already be imported.

        _______________________________________________________________________

        ARGUMENTS:
        o  action           : (str) "version", "serialize" or "encode"
        o  obj              : the object to be serialized
        o  obj_data_name    : (str) obj type as defined in DATA[]
        o  fingerprint      : a string describing the operation (usefull to debug)
        o  works_as_expected: (None or callable)if not None, will be called to check
                              the reversibility of the de-serialized object.

        RETURNED VALUE:
           - None if an error occcured
           - if <action> is (str)"version", return a string.
           - if <action> is (str)"encode", return the encoded string
           - if <action> is (str)"serialize", return a SerializationResult object.
    """
    serializer_name = 'yajl'

    module = MODULES[wisteria.globs.SERIALIZERS[serializer_name].module_name]

    # -------------------
    # action == "version"
    # -------------------
    if action == "version":
        return "unknown version"

    # -------------------
    # action == "encode"
    # -------------------
    if action == "encode":
        try:
            return module.dumps(obj)
        except (ValueError, TypeError):
            return None

    # ---------------------
    # action == "serialize"
    # ---------------------
    if action != "serialize":
        raise WisteriaError(f"(ERRORID051) Unknown 'action' keyword '{action}'.")

    # MEMOVERUSE# ---- --memoveruse ? -----------------------------------------------------
    # MEMOVERUSEif 'Python' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    #   pylint: disable=possibly-unused-variable
    # MEMOVERUSE    dumbstr = "0123456789"*100000
    # MEMOVERUSEif 'C++' in wisteria.globs.ARGS.memoveruse:
    # MEMOVERUSE    MemOverUse().memoveruse()

    # ---- main computation ---------------------------------------------------
    res = SerializationResult()

    if wisteria.globs.PLATFORM_SYSTEM == "Windows":
        mem0 = win_memory()
    else:
        mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    _error = False
    try:
        _res = module.dumps(obj)
        _timeit = timeit.Timer('module.dumps(obj)',
                               globals=locals())
        res.encoding_success = True
        res.encoding_strlen = _len(_res)
        res.encoding_time = _timeit.timeit(TIMEITNUMBER)

        if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
            msginfo(
                f"([{fingerprint}] '{module.__name__}' / '{obj_data_name}' (type: '{type(obj)}')) "
                f"encoded string=({type(_res)}) '{_res}'")

    except (ValueError, TypeError) as error:
        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"[{fingerprint}] '{module}': encoding failed ({error})")
        _error = True

    # incoherent result: if res.encoding_strlen is 0, everything is wrong:
    if res.encoding_strlen == 0:
        res.encoding_success = False
        res.encoding_strlen = None
        res.encoding_time = None
        res.decoding_time = None
        res.decoding_success = False
        res.reversibility = False
        res.mem_usage = None
        return res

    if not _error:
        try:
            _res2 = module.loads(_res)
            res.decoding_success = True  # True because not exception was raised.
            _timeit = timeit.Timer("module.loads(_res)",
                                   globals=locals())
            res.decoding_time = _timeit.timeit(TIMEITNUMBER)

            if obj == _res2:
                res.reversibility = True
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] res.reversibility (first part:obj == _res2) "
                         f"is {res.reversibility} ({obj=}; {_res2=};)")
            if res.reversibility and works_as_expected:
                res.reversibility = res.reversibility and works_as_expected(data_name=obj_data_name,
                                                                            obj=_res2)
                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug(f"[{fingerprint}] res.reversibility "
                             f"(second part:works_as_expected(_res2)) "
                             f"is {res.reversibility}.")

        except (ValueError,) as error:
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"[{fingerprint}] '{module}': decoding failed ({error})")
            return res

    if res.reversibility is True:
        if wisteria.globs.PLATFORM_SYSTEM == "Windows":
            res.mem_usage = win_memory() - mem0
        else:
            res.mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - mem0

    return res


def init_serializers():
    """
        init_serializers()

        Initialize wisteria.globs.SERIALIZERS
    """
    for serializerdata in (
            SerializerData(
                SerializersDataNMVH(name="iaswn",
                                    module_name="iaswn",
                                    human_name="Iaswn"),
                internet="https://github.com/suizokukan/iaswn",
                func=serializer_iaswn,
                cwc="cwc_iaswn"),
            SerializerData(
                SerializersDataNMVH(name="json",
                                    module_name="json",
                                    human_name="json"),
                internet="https://docs.python.org/3/library/json.html",
                func=serializer_json,
                cwc="cwc_default"),
            SerializerData(
                SerializersDataNMVH(name="jsonpickle",
                                    module_name="jsonpickle",
                                    human_name="jsonpickle"),
                internet="https://jsonpickle.github.io/",
                func=serializer_jsonpickle,
                cwc="cwc_default"),
            SerializerData(
                SerializersDataNMVH(name="jsonpickle_keystrue",
                                    module_name="jsonpickle",
                                    human_name="jsonpickle(keys=True)"),
                internet="https://jsonpickle.github.io/",
                func=serializer_jsonpickle_keystrue,
                cwc="cwc_default",
                comment="jsonpickle with keys=True"),
            SerializerData(
                SerializersDataNMVH(name="marshal",
                                    module_name="marshal",
                                    human_name="marshal"),
                internet="https://docs.python.org/3/library/marshal.html#module-marshal",
                func=serializer_marshal,
                cwc="cwc_default"),
            SerializerData(
                SerializersDataNMVH(name="pickle",
                                    module_name="pickle",
                                    human_name="pickle"),
                internet="https://docs.python.org/3/library/pickle.html",
                func=serializer_pickle,
                cwc="cwc_default"),
            SerializerData(
                SerializersDataNMVH(name="pyyaml",
                                    module_name="yaml",
                                    human_name="pyyaml"),
                internet="https://pyyaml.org/",
                func=serializer_pyyaml,
                cwc="cwc_default"),
            SerializerData(
                SerializersDataNMVH(name="simpleion",
                                    module_name="amazon.ion.simpleion",
                                    module_name__version="amazon.ion",
                                    human_name="Amazon Ion Python"),
                internet="https://github.com/amzn/ion-python",
                func=serializer_simpleion,
                cwc="cwc_default",
                comment="installation tip: `pip install git+https://github.com/amzn/ion-python`"),
            SerializerData(
                SerializersDataNMVH(name="yajl",
                                    module_name="yajl",
                                    human_name="yajl"),
                internet="https://lloyd.github.io/yajl/",
                func=serializer_yajl,
                cwc="cwc_default"),
            ):
        if trytoimport(serializerdata.module_name):
            # main module:
            wisteria.globs.SERIALIZERS[serializerdata.name] = serializerdata
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"Successfully imported '{serializerdata.module_name}' module.")

            # module_name__version:
            if serializerdata.module_name__version != serializerdata.module_name:
                if not trytoimport(serializerdata.module_name__version):
                    raise WisteriaError(
                        "(ERRORID049) Internal error: couldn't import "
                        f"'{serializerdata.module_name__version}' module although "
                        f"'{serializerdata.module_name}' module "
                        "has already been successfully imported.")

                if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                    msgdebug("Successfully imported "
                             f"'{serializerdata.module_name__version}' module.")

            wisteria.globs.SERIALIZERS[serializerdata.name].version = serializerdata.func("version")
        else:
            wisteria.globs.UNAVAILABLE_SERIALIZERS[serializerdata.name] = serializerdata
            if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(f"Could not import '{serializerdata.module_name}' module.")
