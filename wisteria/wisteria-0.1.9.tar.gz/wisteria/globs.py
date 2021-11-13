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
    Wisteria project : wisteria/globs.py

    Global definitions.

    ___________________________________________________________________________

    o  ARGS

    o  CWC_MODULES

    o  DATA
    o  UNAVAILABLE_DATA

    o  DEBUG_CONSOLEWIDTH

    o  DEFAULT_CONFIGFILE_NAME
    o  DEFAULT_CONFIGFILE_URL

    o  DEFAULT_EXPORTREPORT_FILENAME

    o  DEFAULT_REPORTFILE_NAME

    o  FILECONSOLE
    o  FILECONSOLE_FILEOBJECT

    o  MODULES

    o  OUTPUT

    o  PLANNED_TRANSCODINGS

    o  PLATFORM_SYSTEM

    o  PROGRESSBAR_LENGTH

    o  REGEX_CMP
    o  REGEX_CMP__HELP

    o  REPORT_SHORTCUTS

    o  SERIALIZERS

    o  STR2REPORTSECTION_KEYS

    o  TIMEITNUMBER

    o  TMPFILENAME

    o  UNITS

    o  VERBOSITY_MINIMAL
    o  VERBOSITY_NORMAL
    o  VERBOSITY_DETAILS
    o  VERBOSITY_DEBUG



The following variables depend on previously defined variables,
hence their location at the end of this list:

    o  GRAPHS_FILENAME
    o  GRAPHS_DESCRIPTION
"""
import re


# command line arguments
# will be set to argparse.ArgumentParser(...).parse_args()
ARGS = None

# (pimydoc)cwc modules names
# ⋅
# ⋅cwc modules names start with the "wisteria.cwc" string (cf is_a_cwc_name())
# ⋅
# ⋅moduleininame        : e.g. "wisteria.cwc.pgnreader.cwc_default.chessgames"
# ⋅modulefullrealname   : e.g. "wisteria.cwc.pgnreader.cwc_default.ChessGames"
# ⋅waemodulename        : e.g. "wisteria.cwc.pgnreader.works_as_expected"
# ⋅classname            : e.g. "ChessGames" (NOT "chessgames")
# ⋅modulerealname       : e.g. "wisteria.cwc.pgnreader.cwc_default"
# ⋅
# ⋅- `moduleininame` are defined in config file;
# ⋅- conversion from `moduleininame` to `modulefullrealname` is defined in
# ⋅  data.py:DATA and is made by function
# ⋅  cwc_utils.py:moduleininame_to_modulefullrealname()
# ⋅- conversion from `modulefullrealname` to `modulerealname` is made by
# ⋅  function cwc_utils.py:modulefullrealname_to_modulerealname()
# ⋅- DATA keys (for cwc modules) use `moduleininame`, NOT `modulefullrealname`
CWC_MODULES = (
    ("wisteria.cwc.pgnreader.cwc_default.chessgames",
     "wisteria.cwc.pgnreader.cwc_default.ChessGames"),
    ("wisteria.cwc.pgnreader.cwc_iaswn.chessgames",
     "wisteria.cwc.pgnreader.cwc_iaswn.ChessGames"),

    ("wisteria.cwc.simple.cwc_default.simpleclass",
     "wisteria.cwc.simple.cwc_default.SimpleClass"),
    ("wisteria.cwc.simple.cwc_iaswn.simpleclass",
     "wisteria.cwc.simple.cwc_iaswn.SimpleClass"),
)

# dict storing all data used by the program.
#
# (pimydoc)DATA format
# ⋅Initialized by data.py::init_data()
# ⋅
# ⋅- for Python basic types, DATA values are the real value:
# ⋅    e.g. DATA["bool/false"] = False
# ⋅- for cwc modules, DATA keys are the ini name (not the real name)
# ⋅  and DATA values are the real name:
# ⋅    e.g. DATA["wisteria.cwc.pgnreader.iaswn.ChessGames"] =
# ⋅        "wisteria.cwc.pgnreader.iaswn.chessgames"
# ⋅- for third party types, DATA values are the real value:
# ⋅    e.g. DATA["dateutil(parser.parse)"] = dateutil.parser.parse("2021-03-04")
DATA = {}
# dict storing all data that the program can't use.
#
# * format: UNAVAILABLE_DATA[(str)data name] = string explaining why it's unavailable
# * initialized by data.py::init_data()
UNAVAILABLE_DATA = {}

# maximal console width used to display some debug messages:
DEBUG_CONSOLEWIDTH = 70

# default name for the config file.
DEFAULT_CONFIGFILE_NAME = "wisteria.ini"
# url of the default config file:
DEFAULT_CONFIGFILE_URL = "https://raw.githubusercontent.com/suizokukan/wisteria/main/wisteria.ini"

# default filename for --exportreport
DEFAULT_EXPORTREPORT_FILENAME = "report.md"

DEFAULT_REPORTFILE_NAME = "report.txt"

# value: rich.console.Console(file=...)
FILECONSOLE = None
# Both variables are initialized by main.py()
FILECONSOLE_FILEOBJECT = None

# imported serializers modules
MODULES = {}

# value of the --output argument
#  initialized by parse_output_argument(--output string)
# format:
#        ((bool)success, True if the --output string had been successfully parsed
#         (bool)output to the console ?,
#         (bool)output to the reportfile ?,
#         (str)reportfile open mode = 'a' or 'w',
#         (str)reportfile name,
#        )
OUTPUT = []

# (pimydoc)PLANNED_TRANSCODINGS
# ⋅list of str:
# ⋅    (str)serializer, (str)data_name, (str)fingerprint
# ⋅
# ⋅Initialized by results.py:init_planned_transcodings()
PLANNED_TRANSCODINGS = []

# = platform.system()
PLATFORM_SYSTEM = None

# progress bar length (in characters)
# 'None' is an accepted value and extends the length of the bar
# to the entire width of the terminal.
PROGRESSBAR_LENGTH = None

# (pimydoc)--cmp format
# ⋅
# ⋅(I) serializers
# ⋅Test one serializer alone(1) or one serializer against another serializer(2) or
# ⋅a serializer against all serializers(3) or all serializers(4) together.
# ⋅
# ⋅    (1) --cmp="jsonpickle(cwc)"
# ⋅    (2) --cmp="jsonpickle vs pickle (cwc)"
# ⋅    (3) --cmp="jsonpickle vs all (cwc)"
# ⋅    (4) --cmp="all vs all (cwc)"
# ⋅
# ⋅(II) data types:
# ⋅Instead of 'cwc' (=compare what's comparable)(a) you may want to test all data types
# ⋅but cwc(b) or data types defined in the config file(c) or absolutely all data types(d).
# ⋅
# ⋅    (a) --cmp="jsonpickle vs pickle (cwc)"
# ⋅    (b) --cmp="jsonpickle vs pickle (allbutcwc)"
# ⋅    (c) --cmp="jsonpickle vs pickle (ini)"
# ⋅    (d) --cmp="jsonpickle vs pickle (all)"
# ⋅
# ⋅NB: You may use 'vs' as well as 'against', as if:
# ⋅    --cmp="jsonpickle vs pickle (cwc)"
# ⋅NB: globs.py::REGEX_CMP defines exactly the expected format
# ⋅    globs.py::REGEX_CMP__HELP gives an idea of what is expected; this
# ⋅                              string is used as help message by the
# ⋅                              command line --help argument.
# ⋅
# regex used to parse the --cmp argument string
REGEX_CMP = re.compile(r"^\s*(?P<serializer1>[^\s\(\)]+)"
                       r"((\svs\s|\sversus\s|\sagainst\s)(?P<serializer2>[^\s\(\)]+))?"
                       r"(\s*\((?P<cmpdata>all|cwc|allbutcwc|ini)\))?\s*$")
# string used by --help
REGEX_CMP__HELP = "all|serializer1[vs all|serializer2][(cwc|allbutcwc|ini|all)]"

# REPORT_SHORTCUTS has two goals:
# (1) it translates a simple, human-readable string into a list of section parts
# (2) it gives all the accepted keywords that --report may understand.
REPORT_SHORTCUTS = {
    "bestof": "B1c;C2b;C2c;graphs;",
    "full": "titles;A;B;C;D1a;graphs;",
    "full+": "titles;A;B;C;D1b;graphs;",
    "full_debug": "titles;A;B;C;D;graphs;",
    "glance": "titles;B1b;C1a;C1b;C2a;C2b;C2c;graphs;",
    "laconic": "C;graphs;",
    "minimal": "C2c;graphs;",
    "none": "",
    }

# dict storing all serializers used by the program.
#
# * format: SERIALIZERS[(str)serializer name] = SerializerData object
# * initialized by serializers.py::init_serializers()
SERIALIZERS = {}
# dict storing all serializers that the program can't use.
#
# * format: UNAVAILABLE_SERIALIZERS[(str)serializer name] = SerializerData object
# * initialized by serializers.py::init_serializers()
UNAVAILABLE_SERIALIZERS = {}

#  globs.py:STR2REPORTSECTION_KEYS should be nothing but STR2REPORTSECTION.keys()
#
# Why those two variables ?
# Because the program needs to know STR2REPORTSECTION.keys() at step A
# before STR2REPORTSECTION has been initialized. Since this initialization
# requires modules that can't fit step A, we have to create a distinct list
# of keys.
#
# check_str2reportsection_keys() checks that keys from STR2REPORTSECTION and
# from STR2REPORTSECTION_KEYS are exactly the same.
STR2REPORTSECTION_KEYS = (
    'titles',
    'graphs',
    'A',
    'A1',
    'A2',
    'A3',
    'A4',
    'A5',
    'B',
    'B1',
    'B1a',
    'B1b',
    'B1c',
    'B1d',
    'B2',
    'B2a',
    'B2b',
    'C',
    'C1',
    'C1a',
    'C1b',
    'C2',
    'C2a',
    'C2b',
    'C2c',
    'D',
    'D1',
    'D1a',
    'D1b',
)

# number of times each serializer is called
TIMEITNUMBER = 1

# temp file default name
TMPFILENAME = "wisteria.tmp"

# units used in this project
UNITS = {'time': 'seconds',
         'string length': 'characters',
         'memory': 'bytes',
         }

# values defined for --verbosity:
VERBOSITY_MINIMAL = 0
VERBOSITY_NORMAL = 1
VERBOSITY_DETAILS = 2
VERBOSITY_DEBUG = 3


# =============================================================================
#
# The following variables depend on previously defined variables,
# hence their location at the end of this list.
#
# =============================================================================

# name of the graphs file
GRAPHS_FILENAME = "report__SUFFIX__.png"

# (pimydoc)GRAPHS_DESCRIPTION format
# ⋅Use GRAPHS_DESCRIPTION to store the description of each graph created by the
# ⋅report; each description is passed to hbar2png(). Note that
# ⋅len(GRAPHS_DESCRIPTION) gives the number of graphs to be created.
# ⋅
# ⋅- (str)attribute   : hbar2png will read results.hall[attribute]
# ⋅- (str)fmtstring   : format string to be applied to each value when printed
# ⋅                     on the graph; e.g. '{0}' or '{0:.1f}'
# ⋅- (int)value_coeff : each value will be multiplied by this number
# ⋅- (str)unit        : x unit
# ⋅- (str)title       : graph title
# ⋅- (str)filename    : file name to be written
GRAPHS_DESCRIPTION = (('encoding_time', "{0:.3f}", 1, UNITS['time'], 'Slowness',
                      GRAPHS_FILENAME.replace("__SUFFIX__", "1")),
                      ('mem_usage', "{0}", 1, UNITS['memory'], 'Memory Usage',
                       GRAPHS_FILENAME.replace("__SUFFIX__", "2")),
                      ('encoding_strlen', "{0}", 1, UNITS['string length'], 'Encoded String Length',
                       GRAPHS_FILENAME.replace("__SUFFIX__", "3")),
                      ('reversibility', "{0:.1f}", 100, "%", 'Coverage data (Reversibility)',
                       GRAPHS_FILENAME.replace("__SUFFIX__", "4")),)
