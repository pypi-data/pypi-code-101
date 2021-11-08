# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['peatland_time_series']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.4,<2.0.0', 'pandas>=1.3.4,<2.0.0']

setup_kwargs = {
    'name': 'peatland-time-series',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Gabriel Couture',
    'author_email': 'gacou54@ulaval.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
