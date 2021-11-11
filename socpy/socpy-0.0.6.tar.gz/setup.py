#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

"""
Query the SOCcer API with Python. Returns results in a
structured format (pandas dataframes).
"""

setup(
    name="socpy",
    version="0.0.6",
    author="Daniel Molitor",
    author_email="molitdj97@gmail.com",
    description="Query the SOCcer API",
    long_description=__doc__,
    long_description_content_type="text/plain",
    url="https://github.com/dmolitor/socpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas",
        "requests",
        "setuptools"
    ],
    include_package_data=True,
    package_data={"": ["data/*.csv"]},
    python_requires=">=3.6",
)