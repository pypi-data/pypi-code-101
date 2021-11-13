# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylaprof']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pylaprof',
    'version': '0.2.0',
    'description': 'A Python sampling profiler for AWS Lambda functions (and not only).',
    'long_description': None,
    'author': 'Giuseppe Lumia',
    'author_email': 'g.lumia@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
