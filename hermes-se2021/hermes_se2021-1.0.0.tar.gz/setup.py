# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hermes']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'matplotlib', 'numpy', 'pandas', 'scikit-learn', 'uvicorn']

setup_kwargs = {
    'name': 'hermes-se2021',
    'version': '1.0.0',
    'description': 'A small tool for data collection and processing for SE2021 HSE SPb course',
    'long_description': None,
    'author': 'Jura Khudyakov',
    'author_email': 'catchitoo@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MariaChizhova/SE_2021',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
