#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='esprisendmail',
      version=1.1,
      description='CLI to send mail alerts to ESPRI users',
      author='Levavasseur Guillaume',
      author_email='glipsl@ipsl.fr',
      url='https://gitlab.in2p3.fr/ipsl/espri/espri-mod/sysadmin/mail_sender',
      packages=find_packages(),
      include_package_data=True,
      python_requires='>3.6',
      platforms=['Unix'],
      zip_safe=False,
      entry_points={'console_scripts': ['esprisendmail=sendmail.main:main']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: System Administrators',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development :: Build Tools'])
