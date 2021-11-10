# __init__.py
# Copyright (C) 2019 (gnyontu39@gmail.com) and contributors
#

import inspect
import os
import sys

real_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
sys.path.append(real_path)

__version__ = '0.0.1'

from .matching import dotshow as dotshow
from .matching import loadshow as loadshow
from .experiment.movie import movshow as movshow

__all__ = [dotshow, loadshow, movshow]
