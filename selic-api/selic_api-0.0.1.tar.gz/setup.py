# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['selic_api']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.2,<3.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'selic-api',
    'version': '0.0.1',
    'description': 'API para obtenção dos dados da SELIC.',
    'long_description': None,
    'author': 'João Marcelo',
    'author_email': 'joaomarceloav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
