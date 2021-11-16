# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redocker']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['redocker = redocker.redocker:main']}

setup_kwargs = {
    'name': 'redocker',
    'version': '0.1.2',
    'description': 'reverse docker image, container and network',
    'long_description': None,
    'author': 'junka',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
