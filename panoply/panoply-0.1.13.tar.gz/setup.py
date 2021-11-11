# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['panoply']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['panoply = panoply.panoply:main']}

setup_kwargs = {
    'name': 'panoply',
    'version': '0.1.13',
    'description': '',
    'long_description': None,
    'author': 'Jeremy Naccache',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
