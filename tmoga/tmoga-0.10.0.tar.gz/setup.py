#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:37:18 2021

@author: Jungang Zou
"""

from setuptools import setup
from setuptools import find_packages

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.10.0'

setup(
    name='tmoga',  # package name
    version=VERSION,  # package version
    author="Jungang Zou",
    author_email="jungang.zou@gmail.com",
    url="https://github.com/zjg540066169/TMOGA",
    description='TMOGA(feature Transfer based Multi-Objective Genetic algorithm) is a multi-objective genetic algorithm to solve community detection problem on dynamic networks.' ,  # package description
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    project_urls={
        "Code":"https://github.com/zjg540066169/TMOGA",
        },
    python_requires=">=3.7.*",
    install_requires=[
        "networkx>=2.5",
        "argparse>=1.1",
        "python-louvain>=0.15",
        "joblib>=0.17.0",
        "tqdm>=4.50.2",
        "numpy>=1.19.2",
        "matplotlib>=3.3.2",
        "scikit-learn>=0.23",
        "pandas>=1.1.3",
        ],
    package_data={
        "":["*.edgelist", "*.comm", "*.edges", "*.txt"]

    },
    
    
)