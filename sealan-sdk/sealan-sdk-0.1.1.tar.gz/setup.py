"""
sealan-cloud-sdk-v1
-------------

This is the description for that library
"""
import os
from setuptools import setup, find_packages

import sealan_sdk

ROOT = os.path.dirname(__file__)

setup(
    name='sealan-sdk',
    version=sealan_sdk.__version__,
    description='Sealan Cloud SDK for Python',
    long_description=open('README.rst').read(),
    author='Sealan Cloud',
    url='https://github.com/sealan-cloud/sealan-sdk-python',
    maintainer_email="zhong@sealan.tech",
    scripts=[],
    install_requires = ['requests>=2.26.0'],
    packages=find_packages(exclude=["tests*", "example*"]),
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)