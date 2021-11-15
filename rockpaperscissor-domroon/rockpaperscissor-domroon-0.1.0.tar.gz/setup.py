# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rockpaperscissor_domroon']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rockpaperscissor-domroon',
    'version': '0.1.0',
    'description': 'A simple text-based Rock, Paper, Scissor game',
    'long_description': None,
    'author': 'Dominik Haeusser',
    'author_email': 'haeusser-dominik@web.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
