# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylaprof']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pylaprof-merge = scripts.merge:main']}

setup_kwargs = {
    'name': 'pylaprof',
    'version': '0.3.1',
    'description': 'A Python sampling profiler for AWS Lambda functions (and not only).',
    'long_description': "# pylaprof\n🚧 **Work in progress** 🚧\n\nJust a quick note for the moment: [pprofile](https://github.com/vpelletier/pprofile)'s\ncode is awesome!\n",
    'author': 'Giuseppe Lumia',
    'author_email': 'g.lumia@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/glumia/pylaprof',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
