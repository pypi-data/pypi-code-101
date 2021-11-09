#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: simple_py_logger
# Created Date: 2021-11-09 Tuesday 10:46:38
# Author: transpine(transpine@gmail.com)
# ----------------------------------------------
# Last Modified: 2021-11-09 Tuesday 11:36:47
# Modified By: transpine
# ----------------------------------------------
# Copyright (c) 2021 devfac
# 
# MIT License
# 
# Copyright (c) 2021 devfac
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
###
import logging
import inspect
import os

from IPython import get_ipython
from colorlog import ColoredFormatter

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = ColoredFormatter(
    "%(log_color)s[%(asctime)s.%(msecs)03d][%(levelname)s]%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    reset=True,
    log_colors={
      'DBG': 'cyan',
      'INF': 'white,bold',
      'WRN': 'yellow',
      'ERR': 'red,bold',
      'CRC': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)
ch.setFormatter(formatter)

log = logging.getLogger('devfacPyLogger')
log.setLevel(logging.DEBUG)
log.handlers = []       # No duplicated handlers
log.propagate = False   # workaround for duplicated logs in ipython
log.addHandler(ch)

logging.addLevelName(logging.DEBUG + 1, 'DBG')
logging.addLevelName(logging.INFO + 1, 'INF')
logging.addLevelName(logging.WARNING + 1, 'WRN')
logging.addLevelName(logging.ERROR + 1, 'ERR')
logging.addLevelName(logging.CRITICAL + 1, 'CRC')

def ipython_check():
  shell = get_ipython().__class__.__name__
  if shell == 'ZMQInteractiveShell' or shell == 'TerminalInteractiveShell':
    return True
  else:
    return False

def dbg(self, msg, *args, **kwargs):   
  stack = inspect.stack()
  filepath = stack[1][1]
  lineno = stack[1][2]
  if ipython_check():
    self.log(logging.DEBUG + 1, f' {msg}', *args, **kwargs)
  else:
    self.log(logging.DEBUG + 1, f'[{os.path.basename(filepath)}:{lineno}] {msg}', *args, **kwargs)
def inf(self, msg, *args, **kwargs):
  stack = inspect.stack()
  filepath = stack[1][1]
  lineno = stack[1][2]
  if ipython_check():
    self.log(logging.INFO + 1, f' {msg}', *args, **kwargs)
  else:    
    self.log(logging.INFO + 1, f'[{os.path.basename(filepath)}:{lineno}] {msg}', *args, **kwargs)
def wrn(self, msg, *args, **kwargs):
  stack = inspect.stack()
  filepath = stack[1][1]
  lineno = stack[1][2]
  if ipython_check():
    self.log(logging.WARNING + 1, f' {msg}', *args, **kwargs)
  else:
    self.log(logging.WARNING + 1, f'[{os.path.basename(filepath)}:{lineno}] {msg}', *args, **kwargs)
def err(self, msg, *args, **kwargs):
  stack = inspect.stack()
  filepath = stack[1][1]
  lineno = stack[1][2]
  if ipython_check():
    self.log(logging.ERROR + 1, f' {msg}', *args, **kwargs)
  else:
    self.log(logging.ERROR + 1, f'[{os.path.basename(filepath)}:{lineno}] {msg}', *args, **kwargs)
def crc(self, msg, *args, **kwargs):
  stack = inspect.stack()
  filepath = stack[1][1]
  lineno = stack[1][2]
  if ipython_check():
    self.log(logging.CRITICAL + 1, f' {msg}', *args, **kwargs)
  else:
    self.log(logging.CRITICAL + 1, f'[{os.path.basename(filepath)}:{lineno}] {msg}', *args, **kwargs)

logging.Logger.debug = dbg
logging.Logger.info = inf
logging.Logger.warning = wrn
logging.Logger.error = err
logging.Logger.critical = crc

__all__ = ['log']