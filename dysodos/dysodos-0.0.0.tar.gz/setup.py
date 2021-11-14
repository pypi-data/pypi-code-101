# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dysodos']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dysodos',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'suizokukan',
    'author_email': 'suizokukan@orange.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
