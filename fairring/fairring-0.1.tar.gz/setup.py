#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import datetime
import os
import subprocess
from setuptools import setup


setup(
    name="fairring",
    version="0.1",
    packages=[
        "fairring",
    ],
    setup_requires=["setuptools", "torch"],
    install_requires=["torch==1.10.0"],
)
