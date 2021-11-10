# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['caspius']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'caspius',
    'version': '1.2',
    'description': 'Simple log system for python',
    'long_description': None,
    'author': 'Dan Gost',
    'author_email': 'dangost16@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
