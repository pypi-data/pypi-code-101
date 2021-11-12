#!/usr/bin/env python
# coding:utf-8

from setuptools import find_packages, setup

setup(
name='winshotor',
version='0.1.2',
description='python windows screen snapshot tool.<Windows Only>',
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
keywords = ['screenshot', 'windows'],
python_requires='>=3', 
)