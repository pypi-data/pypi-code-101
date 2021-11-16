#!/usr/bin/env python3
#
# Copyright 2021 Jonathan Lee Komar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
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
#
from .result import Result
from typing import Dict
import configparser
import logging
logger = logging.getLogger('IniConfigReader')

class IniConfigReader():
  def __init__(self, configFileName:str, onErrorHelp:str=""):
    self.config = self._readConfig(configFileName, onErrorHelp)

  def _readConfig(self, configFileName:str, onErrorHelp:str) -> Result[configparser.ConfigParser]:
    try:
      parser = configparser.ConfigParser()
      parser.read_file(open(configFileName))
      return Result.of(parser)
    except Exception as e:
      return Result.failure(f"Could not access config file at path {configFileName}: \"{e}\". {onErrorHelp}")

  def getProperty(self, section:str, key:str) -> Result[str]:
    try:
      return self.config.map(lambda parser: parser.get(section, key))
    except Exception as e:
      return Result.failure("Could not get value for section {} key {}".format(section, key))

  def getEntries(self, section:str):# -> Result[List[Tuple]]:
    try:
      return self.config.map(lambda parser: parser.items(section))
    except Exception as e:
      return Result.failure(f"Could not get entries under section {section}", e)

  def readSection(self, section:str) -> Result: # Result<configparser>
    try:
      return self.config.map(lambda parser: parser.get(section))
    except Exception as e:
      return Result.failure(f"Could not find section {section}", e)

  def __str__(self):
    return "{}({})".format(__name__, self.config)
