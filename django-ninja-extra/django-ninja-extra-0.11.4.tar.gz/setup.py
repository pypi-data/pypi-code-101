#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['ninja_extra',
 'ninja_extra.controllers',
 'ninja_extra.controllers.route',
 'ninja_extra.permissions',
 'ninja_extra.schemas',
 'ninja_extra.testing']

package_data = \
{'': ['*']}

install_requires = \
['Django >=2.1', 'django-ninja >= 0.15.0', 'injector']

extras_require = \
{'test': ['pytest',
          'pytest-cov',
          'pytest-django',
          'pytest-asyncio',
          'black',
          'isort',
          'injector',
          'flake8',
          'mypy',
          'django-stubs']}

setup(name='django-ninja-extra',
      version='0.11.4',
      description='Django Ninja Extra - Class Based Utility and more for Django Ninja(Fast Django REST framework)',
      author='Ezeudoh Tochukwu',
      author_email='tochukwu.ezeudoh@gmail.com',
      url='https://github.com/eadwinCode/django-ninja-extra',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.6',
     )
