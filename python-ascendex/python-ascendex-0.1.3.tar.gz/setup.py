# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ascendex']

package_data = \
{'': ['*']}

install_requires = \
['aiosonic>=0.12.0,<0.13.0',
 'chardet>=4.0.0,<5.0.0',
 'ujson>=4.0.2,<5.0.0',
 'websockets>=9.1,<10.0']

setup_kwargs = {
    'name': 'python-ascendex',
    'version': '0.1.3',
    'description': 'Python API for AscendEx',
    'long_description': None,
    'author': 'Jan Skoda',
    'author_email': 'skoda@jskoda.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
