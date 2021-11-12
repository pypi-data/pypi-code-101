#!/usr/bin/env python3
# encoding: utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Emporia",
    version="0.42.00",
    description="Markets for AIs",
    author="Scott McCallum (https github.com scott91e1)",
    author_email="BDFL@Emporia.AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.github.com/EMPORIA-AI/CLIENTv1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
