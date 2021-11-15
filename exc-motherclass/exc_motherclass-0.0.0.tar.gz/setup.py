# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exc_motherclass']

package_data = \
{'': ['*']}

install_requires = \
['exc-errors>=0.0.0,<0.0.1', 'iaswn>=0.1.6,<0.2.0']

setup_kwargs = {
    'name': 'exc-motherclass',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'suizokukan',
    'author_email': 'suizokukan@orange.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
