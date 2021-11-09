# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snap_sync_cleanup']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['snap-sync-cleanup = '
                     'snap_sync_cleanup.snap_sync_cleanup:main']}

setup_kwargs = {
    'name': 'snap-sync-cleanup',
    'version': '1.0.1',
    'description': 'Cleans up remote backups created by snap-sync.',
    'long_description': None,
    'author': 'Christopher Tam',
    'author_email': 'ohgodtamit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GodTamIt/snap-sync-cleanup',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
