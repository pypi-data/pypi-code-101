# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smartthings_rest']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'smartthings-rest',
    'version': '0.1.1',
    'description': 'Smart and straightforward lib for controlling things with smartthings',
    'long_description': None,
    'author': 'Viktor Freiman',
    'author_email': 'freiman.viktor@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/viktorfreiman/smartthings-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
