# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eospyo', 'eospyo.contracts']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.19.0,<0.20.0', 'pydantic>=1.8.2,<2.0.0', 'ueosio>=0.2.5,<0.3.0']

setup_kwargs = {
    'name': 'eospyo',
    'version': '0.5.1',
    'description': 'Interact with EOSIO blockchain networks',
    'long_description': None,
    'author': 'Edson',
    'author_email': 'eospyo@facings.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
