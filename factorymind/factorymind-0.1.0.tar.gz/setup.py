# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['factorymind']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.68.1,<0.69.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.3,<2.0.0',
 'pytest>=6.2.5,<7.0.0',
 'python-dotenv>=0.19.0,<0.20.0',
 'requests>=2.26.0,<3.0.0',
 'uvicorn>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'factorymind',
    'version': '0.1.0',
    'description': 'Python module `factorymind` for the FactoryMind platform',
    'long_description': None,
    'author': 'FactoryMind AS',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
