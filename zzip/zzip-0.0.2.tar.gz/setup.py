# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zzip']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zzip',
    'version': '0.0.2',
    'description': 'Zipper tool for interacting with data',
    'long_description': None,
    'author': 'Stephen Mizell',
    'author_email': 'smizell@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
