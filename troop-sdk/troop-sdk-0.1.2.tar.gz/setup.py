# !/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="troop-sdk",
    version="0.1.2",
    url="https://github.com/troopstack/troop-sdk.git",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
)