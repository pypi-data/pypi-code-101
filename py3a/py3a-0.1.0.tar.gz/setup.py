# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py3a', 'py3a.py3a', 'py3a.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py3a',
    'version': '0.1.0',
    'description': 'Lib for reading and writing 3a format',
    'long_description': None,
    'author': 'DomesticMoth',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
