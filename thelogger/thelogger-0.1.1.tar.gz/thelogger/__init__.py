# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 04:36:47 2019

Easy to use logger object for creating code logs. Just import it and it's set up, 
ready to go.

from thelogger import lg

# log messages
lg.info('Hello World')
lg.warning('warning message')
lg.error('error message')

# start logging messages to a file
lg.reset(file = './demo_log.txt')

# shorthand convenience methods for logging messages
lg.i('this is an info message')
lg.w('this is a warning message')

# remove log handlers
lg.close()
lg.i('nothing is logged because there are no log handlers')

# add default log handlers
lg.reset()

@author: tommy
"""

from .logger import logger, log, lg