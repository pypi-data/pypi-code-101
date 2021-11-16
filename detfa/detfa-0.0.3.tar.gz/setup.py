#!/usr/bin/env python

from io import open
from setuptools import setup

# long_description = """
# :authors: Alexander Goncharenko
# :license: Apache License, Version 2.0, see LICENSE file
# :copyright: (c) 2021 Alexander Goncharenko
# """

version = '0.0.3'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='detfa',
    version=version,

    author='Alexander Goncharenko',
    author_email='goncharenko.stat@gmail.com',

    description=(
        u'Deterministic factor analysis'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/alexandergoncharenko/detfa',
    download_url='https://github.com/alexandergoncharenko/detfa/archive/main.zip',

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['detfa'],
    install_requires=[],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)