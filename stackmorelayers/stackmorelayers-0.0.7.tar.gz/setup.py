# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stackmorelayers']

package_data = \
{'': ['*']}

install_requires = \
['catboost>=1.0.3,<2.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'numpy>=1.21.4,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'scikit-learn>=1.0.1,<2.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'stackmorelayers',
    'version': '0.0.7',
    'description': 'My personal ML library',
    'long_description': None,
    'author': 'Andrew Sonin',
    'author_email': 'sonin.cel@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/andrewsonin/stackmorelayers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
