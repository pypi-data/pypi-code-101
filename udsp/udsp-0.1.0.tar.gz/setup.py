#!/usr/bin/env python
# coding:utf-8

from setuptools import find_packages, setup

setup(
name='udsp',
version='0.1.0',
description='Uart Data Stream Processor (Whether using Uart is not import at all. it can also support other commulication protocal.). It is used to format C data into strings and easily manage send and receive buffers in python and micropython.(We used it with uart in Electronic Design Competition.)',
author="Eagle'sBaby",
author_email='2229066748@qq.com',
maintainer="Eagle'sBaby",
maintainer_email='2229066748@qq.com',
packages=find_packages(),
platforms=["all"],
license='Apache Licence 2.0',
classifiers=[
'Programming Language :: Python',
'Programming Language :: Python :: 3',
],
keywords = ['pymouse', 'PyHook3'],
python_requires='>=3', 
)