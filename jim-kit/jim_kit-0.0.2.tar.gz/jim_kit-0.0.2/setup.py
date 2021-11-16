#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
 name = 'jim_kit',
 version = '0.0.2',
 description = 'jims_library ',
 long_description = 'this is jims personal library ',
 author = 'jim',
 author_email = '694067345@qq.com',
 url = '',
 license = 'MIT Licence',
 keywords = 'personal',
 platforms = 'any',
 python_requires = '>=3.7.*',
 install_requires = ['numpy','matplotlib'],
 #package_dir = {'': 'src'},
 packages = find_packages('src')
 )
