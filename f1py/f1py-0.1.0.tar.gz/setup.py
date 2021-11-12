# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f1py']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'f1py',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Abhimanyu Bhadauria',
    'author_email': 'abhimanyu2911@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
