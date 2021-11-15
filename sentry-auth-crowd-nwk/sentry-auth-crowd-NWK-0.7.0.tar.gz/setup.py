#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sentry-auth-crowd
==================
Original work by 2016 Bas van Oostveen, updated for Sentry 21.9.0 by NWK
:copyright: (c) 2016 Bas van Oostveen, 2021 NWK
"""

from setuptools import setup, find_packages


install_requires = [
    'sentry>=21.9.0',
    'Crowd>=2.0.1',
]

tests_require = [
    'flake8>=2.0,<2.1',
]

setup(
    name='sentry-auth-crowd-NWK',
    version='0.7.0',
    author='NWK',
    author_email='NWKDenmark@protonmail.com',
    url='https://github.com/NWKDenmark/sentry-auth-crowd',
    description='Crowd authentication provider for Sentry',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
