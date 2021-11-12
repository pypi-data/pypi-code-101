#!/usr/bin/env python3

import setuptools

from beizer_curves import __desc__, __version__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="beizer-curves",
    version=__version__,
    py_modules=["beizer_curves"],
    author="Layerex",
    author_email="layerex@dismail.de",
    description=__desc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Layerex/beizer-curves",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["numpy"],
)
