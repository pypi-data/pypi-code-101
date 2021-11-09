#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: setup.py
# Project: t-logger
# Created Date: 2021-11-09 Tuesday 10:18:37
# Author: transpine(transpine@gmail.com)
# ----------------------------------------------
# Last Modified: 2021-11-10 Wednesday 12:03:01
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

import setuptools

setuptools.setup(
    name="devfac-py-logger",
    version="0.2.2",
    license='MIT',
    author="transpine",
    author_email="transpine@gmail.com",
    description="Simple, Colored, File and Line number printable logger",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/transpine/devfac-py-logger",
    install_requires=["colorlog", "ipython"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    py_modules=['devfacPyLogger'],
)