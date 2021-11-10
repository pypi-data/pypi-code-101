from setuptools import setup, find_packages
import os

VERSION = '0.0.3'
DESCRIPTION = 'Jack\'s Tools'
LONG_DESCRIPTION = 'Jack\'s Tools. Basically a Hello World'

setup(
    name='jaxtoolz',
    version=VERSION,
    author='jingus',
    author_email='<dev.jingus@protonmail.com>',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "python",
        "jaxtoolz",
        "jackstools"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)