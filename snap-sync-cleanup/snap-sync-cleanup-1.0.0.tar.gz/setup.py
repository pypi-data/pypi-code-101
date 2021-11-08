# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snap-sync-cleanup']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'snap-sync-cleanup',
    'version': '1.0.0',
    'description': 'Cleans up remote backups created by snap-sync.',
    'long_description': None,
    'author': 'Christopher Tam',
    'author_email': 'ohgodtamit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
