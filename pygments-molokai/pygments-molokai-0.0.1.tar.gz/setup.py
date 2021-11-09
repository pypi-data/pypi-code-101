# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygments_molokai']

package_data = \
{'': ['*']}

entry_points = \
{'pygments.styles': ['molokai = pygments_molokai.molokai:MolokaiStyle']}

setup_kwargs = {
    'name': 'pygments-molokai',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Gregory Poole',
    'author_email': 'gbpoole@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
