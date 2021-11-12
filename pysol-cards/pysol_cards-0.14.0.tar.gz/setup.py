#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='pysol_cards',
      version='0.14.0',
      description='Deal PySol FC Cards',
      keywords='pysol_cards',
      author='Shlomi Fish',
      author_email='shlomif@cpan.org',
      url='https://github.com/shlomif/pysol_cards',
      license='3-clause BSD',
      long_description=io.open(
          './docs/README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   ],
      packages=find_packages(exclude=('tests', 'tests.*')),
      include_package_data=True,
      install_requires=['# The order of packages is significant, because pip processes them in the order','# of appearance. Changing the order has an impact on the overall integration','# process, which may cause wedges in the gate later.','coverage','pytest','pytest-cov','random2','requests','six','twine'],
      )
