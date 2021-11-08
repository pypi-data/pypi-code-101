#!/usr/bin/env python
from setuptools import Extension, find_packages, setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='uniprop_fixed',
    version='1.7.post1',
    description="'uniprop' provides the Unicode properties of codepoints similar to those of the unicodedata module.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Matthew Barnett; Patrick Reader',
    author_email='uniprop@pxeger.com',
    url='https://github.com/pxeger/uniprop',
    license='Apache Software License',

    packages=find_packages(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'License :: OSI Approved :: Apache Software License',
    ],

    package_dir={'uniprop': ''},
    ext_modules=[Extension('uniprop', ['source/unicode_tables.c', 'source/uniprop.c'])],
    python_requires='>=3.8',
)
