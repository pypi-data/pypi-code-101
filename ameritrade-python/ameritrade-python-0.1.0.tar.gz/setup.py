# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ameritrade']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.3,<4.0.0', 'dataclass-factory>=2.10,<3.0']

setup_kwargs = {
    'name': 'ameritrade-python',
    'version': '0.1.0',
    'description': 'A python wrapper for the Ameritrade API.',
    'long_description': None,
    'author': 'Kyler Roloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
