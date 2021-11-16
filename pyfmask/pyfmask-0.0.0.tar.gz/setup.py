# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfmask',
 'pyfmask.detectors',
 'pyfmask.extractors',
 'pyfmask.extractors.auxillary_data',
 'pyfmask.extractors.metadata',
 'pyfmask.platforms',
 'pyfmask.probability_detectors',
 'pyfmask.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfmask',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'mtralka',
    'author_email': 'mtralka@umd.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
