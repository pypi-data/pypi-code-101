# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nagaral26project1',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    Long_description=open('README.rst').read(),
    author='Nitesh Agarwal',
    author_email='',
    url='https://github.com/nagarwal26/project1',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

