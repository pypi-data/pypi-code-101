#!/usr/bin/env python
# coding:utf-8

from setuptools import find_packages, setup

setup(
name='uploadtool',
version='0.1.6',
description='python uploadtool for convenient.',
author="Eagle'sBaby",
author_email='2229066748@qq.com',
maintainer="Eagle'sBaby",
maintainer_email='2229066748@qq.com',
packages=find_packages(),
platforms=["windows"],
license='Apache Licence 2.0',
classifiers=[
'Programming Language :: Python',
'Programming Language :: Python :: 3',
],
install_requires = ["build", "twine"],
keywords = ['upload', 'pypi'],
python_requires='>=3', 
)