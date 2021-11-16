#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create the base directory"""
from pathlib import Path
import sys


Path(sys.argv[2]).mkdir()
