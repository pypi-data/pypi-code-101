# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ci_plumber_gitlab']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ci-plumber-gitlab',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Miles Budden',
    'author_email': 'git@miles.so',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
