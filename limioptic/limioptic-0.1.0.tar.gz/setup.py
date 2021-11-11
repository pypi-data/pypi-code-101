# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['limioptic']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.4,<6.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pyqtgraph>=0.12.3,<0.13.0',
 'scipy>=1.7.1,<2.0.0']

setup_kwargs = {
    'name': 'limioptic',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alexander M. Stolz',
    'author_email': 'alexander.stolz@dvs.ag',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
