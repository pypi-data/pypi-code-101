# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdw_api']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'pandas>=1.3.4,<2.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'sdw-api',
    'version': '0.1.0',
    'description': "Allows downloading data from the ECB's Statistical Data Warehouse (SDW)",
    'long_description': '# SDW_API',
    'author': 'Max',
    'author_email': 'maximilian.schroder@bi.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MaximilianSchroeder/SDW_API',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
