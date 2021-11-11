# -----------------------------------------------------------------------------
# sheng: utils.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/sheng-lang/sheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# BEGIN utils.py
# -----------------------------------------------------------------------------

import sys


class Global(object):

    class __Global(object):

        def __init__(self):
            self._is_debug = False
            self._input_stream = sys.stdin
            self._output_stream = sys.stdout
            self._log_stream = sys.stderr

        @property
        def input_stream(self):
            return self._input_stream

        @input_stream.setter
        def input_stream(self, other):
            self._input_stream = other
            
        @property
        def output_stream(self):
            return self._output_stream

        @output_stream.setter
        def output_stream(self, other):
            self._output_stream = other

        @property
        def log_stream(self):
            return self._log_stream

        @log_stream.setter
        def log_stream(self, other):
            self._log_stream = other

        @property
        def is_debug(self):
            return self._is_debug

        @is_debug.setter
        def is_debug(self, other):
            self._is_debug = other

        def log(self, message):
            print(message, file=Global().log_stream)

    __instance = None

    def __new__(cls):
        if (not Global.__instance):
            Global.__instance = Global.__Global()
        return Global.__instance


# -----------------------------------------------------------------------------
# END utils.py
# -----------------------------------------------------------------------------
