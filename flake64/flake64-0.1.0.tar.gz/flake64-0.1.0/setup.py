# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake64']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'flake64',
    'version': '0.1.0',
    'description': 'A squared Flake8',
    'long_description': None,
    'author': 'Axel H.',
    'author_email': 'noirbizarre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
