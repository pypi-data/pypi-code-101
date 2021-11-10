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
    Wisteria project : wisteria/serializers_classes.py

    All classes required to handle serializers.


    ___________________________________________________________________________

    o  SerializersDataNMVH class
    o  SerializerData class
    o  SerializerDataObj class
    o  SerializationResult class
    o  SerializationResults class
"""
from dataclasses import dataclass

from wisteria.wisteriaerror import WisteriaError
from wisteria.reprfmt import fmt_serializer, fmt_ratio, fmt_time, fmt_nodata
from wisteria.reprfmt import fmt_strlen, fmt_boolsuccess, fmt_mem_usage
from wisteria.msg import msgerror, msgdebug
from wisteria.cwc.cwc_utils import count_dataobjs_number_without_cwc_variant
from wisteria.cwc.cwc_utils import serializer_is_compatible_with_dataobj
import wisteria.globs
from wisteria.globs import VERBOSITY_DEBUG


@dataclass
class SerializersDataNMVH:
    """
        SerializersDataNMVH class

        Class used by SerializerData to store modules' different names.
    """
    name: str
    module_name: str
    human_name: str
    module_name__version: str = None


class SerializerData:
    """
        SerializerData class

        SerializerData are used to store infos. about serializers in the SERIALIZERS dict.

        _______________________________________________________________________

        instance attributes:

        o  (str)name
        o  (str)module_name
        o  (str)human_name
        o  (str)internet
        o  (str)version
        o  (callable)func           : function to be called to use this serializer
        o  (str)cwc                 : name of the module in cwc/xxx/
        o  (None|str)comment        : human-readable comment
        o  (str)module_name__version: will be <module_name> if __init__() doesn't set it.

        methods:

        o  __init__(self,
                    name, module_name, human_name,
                    internet, func, cwc, comment=None, module_name__version=None)
        o  __repr__(self)
        o  checkup_repr(self)
        o  simple_repr(self)
    """
    def __init__(self,
                 serializersdata_nmvh,
                 internet,
                 func,
                 cwc,
                 comment=None):
        """
            SerializerData.__init__()

            ___________________________________________________________________

            ARGUMENTS:
            o  (SerializersDataNVMH)serializersdata_nmvh
            o  (str)internet
            o  (str)version
            o  (callable)func                : function to be called to use this serializer
            o  (str)cwc                      : name of the module in cwc/xxx/
            o  (None|str)comment             : human-readable comment
        """
        self.name = serializersdata_nmvh.name
        self.module_name = serializersdata_nmvh.module_name
        self.human_name = serializersdata_nmvh.human_name
        self.internet = internet
        self.version = None
        self.func = func
        self.cwc = cwc
        self.comment = comment
        self.module_name__version = serializersdata_nmvh.module_name__version \
            if serializersdata_nmvh.module_name__version is not None else self.module_name

    def __repr__(self):
        """
            SerializerData.__repr__()

            For the check up output, see .checkup_repr().

            ___________________________________________________________________

            RETURNED VALUE: (str)a basic representation of <self>.
                            See also .checkup_repr() and .simple_repr()
        """
        return f"{self.name=}; {self.module_name=}; {self.module_name__version=}; " \
            f"{self.human_name=}; " \
            f"{self.internet=}; " \
            f"{self.version=}; {self.func=}; {self.cwc=}; {self.comment=}"

    def checkup_repr(self):
        """
            SerializerData.checkup_repr()

            Does the same as .__repr__() but for the check up output.

            ___________________________________________________________________

            RETURNED VALUE: (str)a basic representation of <self>.
                            See also .__repr__() and .simple_repr()
        """
        return f"{fmt_serializer(self.name)} ({self.version}) \\[cwc: '{self.cwc}'], " \
            f"see {self.internet} ."

    def simple_repr(self):
        """
            SerializerData.simple_repr()

            Does the same as .__repr__() but for a simple output.

            ___________________________________________________________________

            RETURNED VALUE: (str)a basic representation of <self>.
                            See also .checkup_repr() and .__repr__()
        """
        return f"{fmt_serializer(self.name)} ({self.version})"


@dataclass
class SerializerDataObj:
    """
        SerializerDataObj class

        Nothing but an easy way to store (serializer, dataobj)

        _______________________________________________________________________

        methods:

        o  serializer: (str)
        o  dataobj:    (str)
    """
    serializer: str = None
    dataobj: str = None


# No useless public methods to add, indeed!
#   pylint: disable=too-few-public-methods
class SerializationResult:
    """
        SerializationResult class

        Class used to store tests results in a SerializationResults object.

        _______________________________________________________________________

        instance attributes:
        o  (bool)  encoding_success
        o  (float) encoding_time
        o  (int)   encoding_strlen
        o  (bool)  decoding_success
        o  (float) decoding_time
        o  (bool)  reversibility
        o  (int)   mem_usage

        methods:

        o  __init__(self)
        o  __repr__(self)
    """
    def __init__(self):
        """
            SerializationResult.__init__()

            ___________________________________________________________________

            ARGUMENTS:

            o  (bool)  encoding_success
            o  (float) encoding_time
            o  (int)   encoding_strlen
            o  (bool)  decoding_success
            o  (float) decoding_time
            o  (bool)  reversibility
            o  (int)   mem_usage
        """
        self.encoding_success = False
        self.encoding_time = None
        self.encoding_strlen = None
        self.decoding_success = False
        self.decoding_time = None
        self.reversibility = False
        self.mem_usage = None

    def __repr__(self):
        """
            SerializationResult.__repr__()
        """
        return f"{self.encoding_success=}; {self.encoding_time=}; {self.encoding_strlen=}; " \
            f"{self.decoding_success=}; {self.decoding_time=}; {self.reversibility=}; " \
            f"{self.mem_usage=}"


class SerializationResults(dict):
    """
        SerializationResults class

        SerializationResults objects are used to store all results created during the tests.

        A SerializationResults object has the following structure:
                SerializationResults[(str)serializer][(str)dataobj] = SerializationResult object

        Do not forget to call .finish_initialization() once you have finished initializing <self>.

        _______________________________________________________________________

        instance attributes:

        o  (list)serializers        : list of str
        o  (list)dataobjs           : list of str
        o  (int) serializers_total_number : =len(self.serializers)
        o  (int) dataobjs_number    : =len(self.dataobjs)
        o  (dict)hall         : e.g. {'encoding_success' = [(0.24, 'marshal'),
                                                                  (0.22, 'pickle')],
                                            ...

                                      keys are: 'encoding_success', 'encoding_time',
                                                'encoding_strlen',
                                                'decoding_success', 'decoding_time',
                                                'reversibility',
                                                'encoding_plus_decoding_time',
                                                'mem_usage'

        o  (dict)overallscores      : overallscores[serializer] = (int)overallscore


        methods:

        o  __init__(self)
        o  comparison_inside_hall(self, serializer, attribute)
        o  count_serializers_compatible_with_dataobj(self, dataobj)
        o  finish_initialization(self)
        o  get_hall(self, attribute, index)
        o  get_overallscore_rank(self, serializer)
        o  get_overallscore_bestrank(self)
        o  get_overallscore_worstrank(self)
        o  get_serializers_whose_overallscore_rank_is(self, rank)
        o  hall_without_none_for_attribute(self, attribute)
        o  ratio_decoding_success(self, serializer=None, dataobj=None, output="fmtstr")
        o  ratio_encoding_success(self, serializer=None, dataobj=None, output="fmtstr")
        o  ratio_reversibility(self, serializer=None, dataobj=None, output="fmtstr")
        o  repr_attr(self, serializer, dataobj, attribute_name, output="fmtstr")
        o  total_decoding_time(self, serializer=None, dataobj=None, output="fmtstr")
        o  total_encoding_plus_decoding_time(self, serializer=None, dataobj=None, output="fmtstr")
        o  total_encoding_strlen(self, serializer=None, dataobj=None, output="fmtstr")
        o  total_encoding_time(self, serializer=None, dataobj=None, output="fmtstr")
        o  total_mem_usage(self, serializer=None, dataobj=None, output="fmtstr")
    """
    def __init__(self):
        """
            SerializationResults.__init__()

            ___________________________________________________________________

            ARGUMENTS:
            o  (list)serializers        : list of str
            o  (list)dataobjs           : list of str
            o  (int) serializers_total_number : = len(self.serializers)
            o  (int) dataobjs_number
               (pimydoc)dataobjs_number
               ⋅MAY NOT BE len(self.dataobjs) since cwc variants are treated as one dataobject:
               ⋅e.g. "wisteria.cwc.pgnreader.cwc_default.ChessGame" and
               ⋅      "wisteria.cwc.pgnreader.iaswn.ChessGame"
               ⋅      ... will be counted as ONE data object.
               ⋅(class variable initialized in initialization in finish_initialization())
            o  (dict)hall         : e.g. {'encoding_success' = [(0.24, 'marshal'),
                                                                      (0.22, 'pickle')],
                                                ...

                                          keys are: 'encoding_success', 'encoding_time',
                                                    'encoding_strlen',
                                                    'decoding_success', 'decoding_time',
                                                    'reversibility',
                                                    'encoding_plus_decoding_time'
            o  (dict)overallscores      : overallscores[serializer] = (int)overallscore
        """
        dict.__init__(self)

        self.serializers = []
        self.dataobjs = []

        # <serializers_total_number>:
        # self.serializers_total_number = len(self.serializers)
        # Beware, one serializer may not be compatible with all data objects !
        # See .count_serializers_compatible_with_dataobj() to solve this problem.
        # (class variable initialized in initialization in finish_initialization())
        self.serializers_total_number = None

        # (pimydoc)dataobjs_number
        # ⋅MAY NOT BE len(self.dataobjs) since cwc variants are treated as one dataobject:
        # ⋅e.g. "wisteria.cwc.pgnreader.cwc_default.ChessGame" and
        # ⋅      "wisteria.cwc.pgnreader.iaswn.ChessGame"
        # ⋅      ... will be counted as ONE data object.
        # ⋅(class variable initialized in initialization in finish_initialization())
        self.dataobjs_number = None

        self.hall = None
        self.overallscores = None

    def comparison_inside_hall(self,
                               serializer,
                               attribute):
        """
            SerializationResults.comparison_inside_hall()

            Returns the serializers better placed than <serializer>
            (=placed before <serializer>) and the less well placed
            serializers than <serializer> (=placed after <serializer>)
            in relation to <attribute>.

            ___________________________________________________________________

            ARGUMENTS:
            o  (str)serializer
            o  (str)attribute

            RETURNED VALUE: (list of better placed serializers than <serializer>,
                             list of less well placed serializers than <serializer>)
        """
        _less = []
        _more = []

        before_serializer = False  # will be True when <serializer> will be read in the loop.
        for index in range(self.serializers_total_number):
            if self.hall[attribute][index][1] == serializer:
                before_serializer = True
            elif before_serializer:
                _less.append(self.hall[attribute][index][1])
            else:
                _more.append(self.hall[attribute][index][1])

        return _less, _more

    def count_serializers_compatible_with_dataobj(self,
                                                  dataobj):
        """
            count_serializers_compatible_with_dataobj()

            Return the number of serializer(s) compatible with <dataobj>.

            ___________________________________________________________________

            ARGUMENT: (str)dataobj

            RETURNED VALUE: (int)the number of serializer(s) compatible with <dataobj>.
        """
        res = 0
        for serializer in self:
            if serializer_is_compatible_with_dataobj(serializer,
                                                     dataobj):
                res += 1
        return res

    def finish_initialization(self):
        """
            SerializationResults.finish_initialization()

            Once the initialization of <self> is over, this method must be called to
            set self.self.serializers, self.dataobjs, self.serializers_total_number
            self.dataobjs_number, self.hall and self.overallscores

            ___________________________________________________________________

            RETURNED VALUE: (bool)success
        """
        self.serializers = sorted(self.keys())
        self.serializers_total_number = len(self.serializers)

        if self.serializers_total_number == 0:
            msgerror("(ERRORID016) Incorrect data, there's no serializer.")
            return False

        # Some dataobjs are not the same from one serializer to another, which forces us to browse
        # all dataobjs from all serializers:
        self.dataobjs = set()
        for serializer in self.serializers:
            for dataobj in self[serializer].keys():
                self.dataobjs.add(dataobj)
        self.dataobjs = list(sorted(self.dataobjs))

        # ---- <self.dataobjs_number> -----------------------------------------
        # (pimydoc)dataobjs_number
        # ⋅MAY NOT BE len(self.dataobjs) since cwc variants are treated as one dataobject:
        # ⋅e.g. "wisteria.cwc.pgnreader.cwc_default.ChessGame" and
        # ⋅      "wisteria.cwc.pgnreader.iaswn.ChessGame"
        # ⋅      ... will be counted as ONE data object.
        # ⋅(class variable initialized in initialization in finish_initialization())
        self.dataobjs_number = count_dataobjs_number_without_cwc_variant(self.dataobjs)

        # ---- <self.hall> ----------------------------------------------------
        self.hall = {}

        # we add "encoding_success" only if it makes sens:
        if not tuple(0 for serializer in self.serializers
                     if self.ratio_encoding_success(serializer=serializer,
                                                    output="value") is None):
            self.hall["encoding_success"] = \
                sorted(((self.ratio_encoding_success(serializer=serializer,
                                                     output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["encoding_success"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "decoding_success" only if it makes sens:
        if not tuple(0 for serializer in self.serializers
                     if self.ratio_decoding_success(serializer=serializer,
                                                    output="value") is None):
            self.hall["decoding_success"] = \
                sorted(((self.ratio_decoding_success(serializer=serializer,
                                                     output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["decoding_success"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "reversibility" only if it makes sens:
        if not tuple(0 for serializer in self.serializers
                     if self.ratio_reversibility(serializer=serializer,
                                                 output="value") is None):
            self.hall["reversibility"] = \
                sorted(((self.ratio_reversibility(serializer=serializer,
                                                  output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["reversibility"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "encoding_time" only if it makes sense:
        if not tuple(0 for serializer in self.serializers
                     if self.total_encoding_time(serializer=serializer,
                                                 output="value") is None):
            self.hall["encoding_time"] = \
                sorted(((self.total_encoding_time(serializer=serializer,
                                                  output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["encoding_time"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "encoding_plus_decoding_time" only if it makes sense:
        if not tuple(0 for serializer in self.serializers
                     if self.total_encoding_plus_decoding_time(serializer=serializer,
                                                               output="value") is None):
            self.hall["encoding_plus_decoding_time"] = \
                sorted(((self.total_encoding_plus_decoding_time(serializer=serializer,
                                                                output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["encoding_plus_decoding_time"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "encoding_strlen" only if it makes sense:
        if not tuple(0 for serializer in self.serializers
                     if self.total_encoding_strlen(serializer=serializer,
                                                   output="value") is None):
            self.hall["encoding_strlen"] = \
                sorted(((self.total_encoding_strlen(serializer=serializer,
                                                    output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["encoding_strlen"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "decoding_time" only if it makes sense:
        if not tuple(0 for serializer in self.serializers
                     if self.total_decoding_time(serializer=serializer,
                                                 output="value") is None):
            self.hall["decoding_time"] = \
                sorted(((self.total_decoding_time(serializer=serializer,
                                                  output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["decoding_time"] = \
                tuple((None, serializer) for serializer in self.serializers)

        # we add "mem_usage" only if it makes sense:
        if not tuple(0 for serializer in self.serializers
                     if self.total_mem_usage(serializer=serializer,
                                             output="value") is None):
            self.hall["mem_usage"] = \
                sorted(((self.total_mem_usage(serializer=serializer,
                                              output="value"),
                         serializer) for serializer in self.serializers),
                       reverse=False)
        else:
            self.hall["mem_usage"] = \
                tuple((None, serializer) for serializer in self.serializers)

        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"hall={self.hall}")

        # ---- self.overallscores ---------------------------------------------
        # overall score computing:
        # * if a serializer is #0 (first rank) for a certain attribute,
        #   its score increases by results.serializers_total_number-0.
        # * if a serializer is #1 (first rank) for a certain attribute,
        #   its score increases by results.serializers_total_number-1.
        # * ...
        self.overallscores = {}
        for serializer in self.serializers:
            self.overallscores[serializer] = 0

            for attribute in ('encoding_plus_decoding_time',
                              'encoding_strlen',
                              'reversibility',
                              'mem_usage',
                              ):
                for index in range(self.serializers_total_number):
                    if self.hall[attribute][index][1] == serializer:
                        self.overallscores[serializer] += self.serializers_total_number-index

        return True

    def get_hall(self,
                 attribute,
                 index):
        """
            SerializationResults.get_hall()

            Return the formatted string result of the 'hall of fame'
            for a given <attribute> and an <index>.
            In other words, answer the question: which serializer is number
            #<index> for a given <attribute> ?

            ___________________________________________________________________

            ARGUMENT:
            o  (str)attribute: 'encoding_success' or
                               'encoding_time' or
                               'decoding_success' or
                               'decoding_time' or
                               'encoding_strlen' or
                               'reversibility' or
                               'mem_usage' ?
            o  (int)index: 0 <= index < len(self.serializers_total_numbers-1)

            RETURNED VALUE: (str)a formatted string describing the result.
        """
        assert attribute in ('encoding_success',
                             'encoding_time',
                             'decoding_success',
                             'decoding_time',
                             'encoding_strlen',
                             'reversibility',
                             'mem_usage')

        value, serializer = self.hall[attribute][index]

        if attribute == 'encoding_success':
            return f"{fmt_serializer(serializer)} " \
                f"[{self.ratio_encoding_success(serializer=serializer)}]"

        if attribute == 'encoding_time':
            return f"{fmt_serializer(serializer)} " \
                f"[{fmt_time(value)}]"

        if attribute == 'decoding_success':
            return f"{fmt_serializer(serializer)} " \
                f"[{self.ratio_decoding_success(serializer=serializer)}]"

        if attribute == 'decoding_time':
            serializer = self.hall[attribute][index][1]
            return f"{fmt_serializer(serializer)} " \
                f"[{fmt_time(value)}]"

        if attribute == 'reversibility':
            serializer = self.hall[attribute][index][1]
            return f"{fmt_serializer(serializer)} " \
                f"[{self.ratio_reversibility(serializer=serializer)}]"

        if attribute == 'encoding_strlen':
            serializer = self.hall[attribute][index][1]
            return f"{fmt_serializer(serializer)} " \
                f"[{fmt_strlen(value)}]"

        if attribute == 'mem_usage':
            serializer = self.hall[attribute][index][1]
            return f"{fmt_serializer(serializer)} " \
                f"[{fmt_mem_usage(value)}]"

        return None  # this line should never be executed.

    def get_overallscore_rank(self,
                              serializer):
        """
            SerializationResults.get_overallscore_rank()

            Return the (int)rank of <serializer> among 'overall scores'.

            ___________________________________________________________________

            ARGUMENT:
            o  (str)serializer

            RETURNED VALUE: (int)rank, 0 <= rank < len(self.serializers_total_numbers)
        """
        _rank = None

        # for rank, (score, _serializer) ...
        for rank, (_, _serializer) in enumerate(sorted(
                ((self.overallscores[serializer],
                  serializer) for serializer in self.serializers), reverse=True)):
            if serializer == _serializer:
                _rank = rank

        return _rank

    def get_overallscore_bestrank(self):
        """
            SerializationResults.get_overallscore_bestrank()

            Return the list of the serializers with the best score
            among "overall scores". There's maybe more than one serializer
            having the highest score, hence the returned list.

            ___________________________________________________________________

            RETURNED VALUE: (list)list of (str)serializers
        """
        highestscore = sorted(
            ((self.overallscores[serializer],
              serializer) for serializer in self.serializers))[-1][0]
        res = []
        for serializer in self.serializers:
            if self.overallscores[serializer] == highestscore:
                res.append(serializer)
        return res

    def get_overallscore_worstrank(self):
        """
            SerializationResults.get_overallscore_worstrank()

            Return the list of the serializers with the worst score
            among "overall scores". There's maybe more than one serializer
            having the worst score, hence the returned list.

            ___________________________________________________________________

            RETURNED VALUE: (list)list of (str)serializers
        """
        worstscore = sorted(
            ((self.overallscores[serializer],
              serializer) for serializer in self.serializers))[0][0]
        res = []
        for serializer in self.serializers:
            if self.overallscores[serializer] == worstscore:
                res.append(serializer)
        return res

    def get_serializers_whose_overallscore_is(self,
                                              score):
        """
            SerializationResults.get_serializers_whose_overallscore_is()

            Return a list of all serializers whose overallscore is <score>.

            ___________________________________________________________________

            ARGUMENT: (int)score

            RETURNED VALUE: (list of str)list of serializers whose overallscore is <score>
        """
        return list(serializer for serializer in self.serializers
                    if self.overallscores[serializer] == score)

    def hall_without_none_for_attribute(self,
                                        attribute):
        """
            SerializationResults.hall_without_none_for_attribute()

            Return True if hall[attribute] doesn't contain any None value.

            ___________________________________________________________________

            ARGUMENT: (str)attribute

            RETURNED VALUE: (bool)True if hall[attribute] doesn't contain any None value.
        """
        res = True

        for value, _ in self.hall[attribute]:  # value, serializer
            if value is None:
                return False

        return res

    def ratio_decoding_success(self,
                               serializer=None,
                               dataobj=None,
                               output="fmtstr"):
        """
            SerializationResults.ratio_decoding_success()

            Compute and format the ratio of decoding success for a <serializer>
            OR for a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  <output>(str): "fmtstr" for a formatted returned string or "value"
               for the (float)raw value

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the ratio can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value')

        count = 0  # number of serializers or dataobjs that are taken in account.

        # serializer is not None:
        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_ratio(None) if output == "fmtstr" else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_ratio(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].decoding_success:
                    count += 1
            if output == "fmtstr":
                return fmt_ratio((count, count/self.dataobjs_number))
            if output == "value":
                return count/self.dataobjs_number

        # dataobj is not None:
        if self.dataobjs_number == 0:
            return fmt_ratio(None) if output == "fmtstr" else None

        for _serializer in self:
            if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                continue
            if self[_serializer][dataobj] is None:
                return fmt_ratio(None) if output == 'fmtstr' else None
            if dataobj in self[_serializer] and \
               self[_serializer][dataobj] is not None and \
               self[_serializer][dataobj].decoding_success:
                count += 1

        serializers_total_number = self.count_serializers_compatible_with_dataobj(dataobj)
        if output == "fmtstr":
            return fmt_ratio((count, count/serializers_total_number))
        if output == "value":
            return count/serializers_total_number

        return None  # this line should never be executed.

    def ratio_encoding_success(self,
                               serializer=None,
                               dataobj=None,
                               output="fmtstr"):
        """
            SerializationResults.ratio_encoding_success()

            Compute and format the ratio of encoding success for a <serializer>
            OR for a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  <output>(str): "fmtstr" for a formatted returned string or "value"
               for the (float)raw value

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the ratio can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ("fmtstr", "value")

        count = 0  # number of serializers or dataobjs that are taken in account.

        # serializer is not None:
        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_ratio(None) if output == "fmtstr" else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_ratio(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].encoding_success:
                    count += 1
            if output == "fmtstr":
                return fmt_ratio((count, count/self.dataobjs_number))
            if output == "value":
                return count/self.dataobjs_number

        # dataobj is not None:
        if self.dataobjs_number == 0:
            return fmt_ratio(None) if output == "fmtstr" else None

        for _serializer in self:
            if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                continue
            if self[_serializer][dataobj] is None:
                return fmt_ratio(None) if output == 'fmtstr' else None
            if dataobj in self[_serializer] and \
               self[_serializer][dataobj] is not None and \
               self[_serializer][dataobj].encoding_success:
                count += 1

        serializers_total_number = self.count_serializers_compatible_with_dataobj(dataobj)
        if output == "fmtstr":
            return fmt_ratio((count, count/serializers_total_number))
        if output == "value":
            return count/serializers_total_number

        return None  # this line should never be executed.

    def ratio_reversibility(self,
                            serializer=None,
                            dataobj=None,
                            output="fmtstr"):
        """
            SerializationResults.ratio_reversibility()

            Compute and/or format the ratio of reversibility success for a <serializer>
            OR for a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  <output>(str): "fmtstr" for a formatted returned string or "value"
               for the (float)raw value

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the ratio can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value')

        count = 0  # number of serializers or dataobjs that are taken in account.

        # serializer is not None:
        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_ratio(None) if output == "fmtstr" else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_ratio(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].reversibility:
                    count += 1
            if output == "fmtstr":
                return fmt_ratio((count, count/self.dataobjs_number))
            if output == "value":
                return count/self.dataobjs_number

        # dataobj is not None:
        if self.dataobjs_number == 0:
            return fmt_ratio(None) if output == "fmtstr" else None

        for _serializer in self:
            if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                continue
            if self[_serializer][dataobj] is None:
                return fmt_ratio(None) if output == 'fmtstr' else None
            if dataobj in self[_serializer] and \
               self[_serializer][dataobj] is not None and \
               self[_serializer][dataobj].reversibility:
                count += 1

        serializers_total_number = self.count_serializers_compatible_with_dataobj(dataobj)
        if output == "fmtstr":
            return fmt_ratio((count, count/serializers_total_number))
        if output == "value":
            return count/serializers_total_number

        return None  # this line should never be executed.

    def repr_attr(self,
                  serializer,
                  dataobj,
                  attribute_name):
        """
            SerializationResults.repr_attr()

            Format the value stored into self[serializer][dataobj].<attribute_name>.

            _______________________________________________________________

            ARGUMENTS:

            o  <str>serializer: name of the serializer to be used.
            o  <str>dataobj: name of the data object to be used.
            o  <str>attribute_name: 'decoding_success', 'decoding_time', 'encoding_strlen',
                                    'encoding_success', 'encoding_time',
                                    'reversibility', 'mem_usage'

            RETURNED VALUE: a formatted string representing
                            self[serializer][dataobj].<attribute_name>
        """
        assert serializer is not None
        assert dataobj is not None
        assert attribute_name in ('decoding_success', 'decoding_time', 'encoding_strlen',
                                  'encoding_success', 'encoding_time',
                                  'reversibility', 'mem_usage')

        res = None  # unexpected result !

        if attribute_name == "decoding_success":
            if self[serializer][dataobj] is None:
                res = fmt_nodata()
            else:
                res = fmt_boolsuccess(
                    self[serializer][dataobj].decoding_success)

        if attribute_name == "decoding_time":
            if self[serializer][dataobj] is None:
                res = fmt_nodata()
            else:
                res = fmt_time(
                    self[serializer][dataobj].decoding_time)

        if attribute_name == "encoding_strlen":
            if self[serializer][dataobj] is None or \
               self[serializer][dataobj].encoding_strlen is None:
                res = fmt_nodata()
            else:
                res = fmt_strlen(
                    self[serializer][dataobj].encoding_strlen)

        if attribute_name == "encoding_time":
            if self[serializer][dataobj] is None or \
               self[serializer][dataobj].encoding_time is None:
                res = fmt_nodata()
            else:
                res = fmt_time(
                    self[serializer][dataobj].encoding_time)

        if attribute_name == "encoding_success":
            if self[serializer][dataobj] is None or \
               self[serializer][dataobj].encoding_success is None:
                res = fmt_nodata()
            else:
                res = fmt_boolsuccess(
                    self[serializer][dataobj].encoding_success)

        if attribute_name == "reversibility":
            if self[serializer][dataobj] is None or \
               self[serializer][dataobj].reversibility is None:
                res = fmt_nodata()
            else:
                res = fmt_boolsuccess(
                    self[serializer][dataobj].reversibility)

        if attribute_name == "mem_usage":
            if self[serializer][dataobj] is None or \
               self[serializer][dataobj].mem_usage is None:
                res = fmt_nodata()
            else:
                res = fmt_mem_usage(
                    self[serializer][dataobj].mem_usage)

        return res

    def total_decoding_time(self,
                            serializer=None,
                            dataobj=None,
                            output="fmtstr"):
        """
            SerializationResults.total_decoding_time()

            Compute and format the total decoding time used by a <serializer>
            OR by a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  (str)output: output type and format
                    - "value": raw value (float)
                    - "fmtstr": formatted string (str)

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the result can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value',)

        res = None  # unexpected result !
        total = 0  # total time

        if serializer is not None:
            if self.serializers_total_number == 0:
                return None if output == "value" else fmt_time(None)

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_time(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj].encoding_success is False:
                    return None if output == "value" else fmt_time(None)

                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].decoding_success:
                    total += self[serializer][_dataobj].decoding_time
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_time(total)

        else:
            if self.dataobjs_number == 0:
                return fmt_time(None) if output == 'fmtstr' else None

            for _serializer in self:
                if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                    continue
                if self[_serializer][dataobj] is None:
                    return fmt_time(None) if output == 'fmtstr' else None
                if dataobj in self[_serializer] and \
                   self[_serializer][dataobj] is not None and \
                   self[_serializer][dataobj].decoding_success:
                    total += self[_serializer][dataobj].decoding_time
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_time(total)

        if res is None:
            raise WisteriaError("(ERRORID026) Internal error: the result could not be computed. "
                                f"{serializer=}; {dataobj=}; {output=};")
        return res

    def total_encoding_plus_decoding_time(self,
                                          serializer=None,
                                          output="fmtstr"):
        """
            SerializationResults.total_encoding_plus_decoding_time()

            Compute and format the total encoding + decoding time used by a
            <serializer>.

            _______________________________________________________________

            ARGUMENTS:
            o  <str>serializer: name of the serializer to be used.
            o  (str)output: output type and format
                    - "value": raw value (float)
                    - "fmtstr": formatted string (str)

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the result can't be computed
        """
        assert output in ('fmtstr', 'value',)

        if output == "value":
            if self.total_encoding_time(serializer=serializer, output=output) is None or \
               self.total_decoding_time(serializer=serializer, output=output) is None:
                return None
            return self.total_encoding_time(serializer=serializer, output=output) + \
                self.total_decoding_time(serializer=serializer, output=output)
        if output == "fmtstr":
            if self.total_encoding_time(serializer=serializer, output='value') is None or \
               self.total_decoding_time(serializer=serializer, output='value') is None:
                return None
            return fmt_time(self.total_encoding_time(serializer=serializer, output='value') +
                            self.total_decoding_time(serializer=serializer, output='value'))

        raise WisteriaError("(ERRORID027) Internal error: the result could not be computed. "
                            f"{serializer=}; {output=};")

    def total_encoding_strlen(self,
                              serializer=None,
                              dataobj=None,
                              output="fmtstr"):
        """
            SerializationResults.total_encoding_strlen()

            Compute and format the total encoding string length created by a <serializer>
            OR for a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  (str)output: output type and format
                    - "value": raw value (float)
                    - "fmtstr": formatted string (str)

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the result can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value',)

        res = None  # unexpected result !
        total = 0  # total time

        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_strlen(None) if output == 'fmtstr' else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_strlen(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj].encoding_success is False:
                    return fmt_strlen(None) if output == 'fmtstr' else None

                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].encoding_strlen:
                    total += self[serializer][_dataobj].encoding_strlen
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_strlen(total)

        else:
            if self.dataobjs_number == 0:
                return fmt_strlen(None) if output == 'fmtstr' else None

            for _serializer in self:
                if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                    continue
                if self[_serializer][dataobj] is None:
                    return fmt_strlen(None) if output == 'fmtstr' else None
                if dataobj in self[_serializer] and \
                   self[_serializer][dataobj] is not None and \
                   self[_serializer][dataobj].encoding_strlen:
                    total += self[_serializer][dataobj].encoding_strlen
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_strlen(total)

        if res is None:
            raise WisteriaError("(ERRORID028) Internal error: the result could not be computed. "
                                f"{serializer=}; {dataobj=}; {output=};")
        return res

    def total_encoding_time(self,
                            serializer=None,
                            dataobj=None,
                            output="fmtstr"):
        """
            SerializationResults.total_encoding_time()

            Compute and format the total decoding time used by a <serializer>
            OR by a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  (str)output: output type and format
                    - "value": raw value (float)
                    - "fmtstr": formatted string (str)

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the result can't be computed
           """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value',)

        res = None  # unexpected result !
        total = 0  # total time

        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_time(None) if output == 'fmtstr' else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_time(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj].encoding_success is False:
                    return fmt_time(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].encoding_success:
                    total += self[serializer][_dataobj].encoding_time
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_time(total)

        else:
            if self.dataobjs_number == 0:
                return fmt_time(None) if output == 'fmtstr' else None

            for _serializer in self:
                if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                    continue
                if self[_serializer][dataobj] is None:
                    return fmt_time(None) if output == 'fmtstr' else None
                if dataobj in self[_serializer] and \
                   self[_serializer][dataobj] is not None and \
                   self[_serializer][dataobj].encoding_success:
                    total += self[_serializer][dataobj].encoding_time
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_time(total)

        if res is None:
            raise WisteriaError("(ERRORID029) Internal error: the result could not be computed. "
                                f"{serializer=}; {dataobj=}; {output=};")
        return res

    def total_mem_usage(self,
                        serializer=None,
                        dataobj=None,
                        output="fmtstr"):
        """
            SerializationResults.total_mem_usage()

            Compute and format the total mem usage created by a <serializer>
            OR for a <dataobj>ect.

            _______________________________________________________________

            ARGUMENTS:
            o  <None|str>serializer: if not None, name of the serializer to be used.
            o  <None|str>dataobj: if not None, name of the data object to be used.
                BEWARE ! One and only one argument among <serializer> and <dataobj> can be set to
                         None.
            o  (str)output: output type and format
                    - "value": raw value (float)
                    - "fmtstr": formatted string (str)

            RETURNED VALUE:
                (output=='fmtstr')a formatted string representing the input argument.
                (output=='value')a float or None if the result can't be computed
        """
        assert serializer is None or dataobj is None
        assert output in ('fmtstr', 'value',)

        res = None  # unexpected result !
        total = 0  # total time

        if serializer is not None:
            if self.serializers_total_number == 0:
                return fmt_mem_usage(None) if output == 'fmtstr' else None

            for _dataobj in self[serializer]:
                if not serializer_is_compatible_with_dataobj(serializer, _dataobj):
                    continue
                if self[serializer][_dataobj] is None:
                    return fmt_mem_usage(None) if output == 'fmtstr' else None
                if self[serializer][_dataobj].encoding_success is False:
                    return fmt_mem_usage(None) if output == 'fmtstr' else None

                if self[serializer][_dataobj] is not None and \
                   self[serializer][_dataobj].mem_usage:
                    total += self[serializer][_dataobj].mem_usage
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_mem_usage(total)

        else:
            if self.dataobjs_number == 0:
                return fmt_mem_usage(None) if output == 'fmtstr' else None

            for _serializer in self:
                if not serializer_is_compatible_with_dataobj(_serializer, dataobj):
                    continue
                if self[_serializer][dataobj] is None:
                    return fmt_mem_usage(None) if output == 'fmtstr' else None
                if dataobj in self[_serializer] and \
                   self[_serializer][dataobj] is not None and \
                   self[_serializer][dataobj].mem_usage:
                    total += self[_serializer][dataobj].mem_usage
            if output == "value":
                res = total
            elif output == "fmtstr":
                res = fmt_mem_usage(total)

        if res is None:
            raise WisteriaError("(ERRORID025) Internal error: the result could not be computed. "
                                f"{serializer=}; {dataobj=}; {output=};")
        return res
