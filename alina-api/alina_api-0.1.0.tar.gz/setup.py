# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['alina', 'alina.irena', 'alina.irena.parsers', 'alina.tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alina-api',
    'version': '0.1.0',
    'description': 'irena1.intercity.pl API for intercity employees.',
    'long_description': None,
    'author': 'Konrad Nowara',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
