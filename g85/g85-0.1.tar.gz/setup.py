#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

with open('g85/VERSION.py', 'rt') as f:
    version = f.readlines()[2].strip()

setup(
    name='g85',
    version=version,
    description='G85 wafer map reader / writer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jan Petykiewicz',
    author_email='jan@mpxd.net',
    url='https://mpxd.net/code/jan/g85',
    packages=find_packages(),
    package_data={
        'g85': ['py.typed'],
    },
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    keywords=[
        'design',
        'CAD',
        'EDA',
        'electronics',
        'photonics',
        'IC',
        'mask',
        'wafer',
        'map',
        'G85',
        'wmap',
    ],
    )
