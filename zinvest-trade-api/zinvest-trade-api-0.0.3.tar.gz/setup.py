# -*- coding: utf-8 -*-
# @File  : setup.py.py
# @Author: qingtao.kong
# @Date  : 2021/11/12
# @Desc  :

import setuptools


#!/usr/bin/env python

import ast
import os
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('zinvest_trade_api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.md') as readme_file:
    README = readme_file.read()

with open("requirements.txt") as reqs:
    REQUIREMENTS = reqs.readlines()


setup(
    name='zinvest-trade-api',
    version=version,
    description='Zinvest API python client',
    long_description=README,
    long_description_content_type='text/markdown',
    author='zinvest',
    author_email='api@zvsthk.com',
    url='https://github.com/zvsts/zinvest-trade-api-python',
    keywords='financial,stock,market data, api,trade',
    packages=[
        'zinvest_trade_api',
    ],
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

