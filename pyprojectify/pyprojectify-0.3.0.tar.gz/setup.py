# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyprojectify']

package_data = \
{'': ['*']}

install_requires = \
['Click>=8.0.3,<9.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyprojectify',
    'version': '0.3.0',
    'description': 'pyprojectify is a utility allowing python package authors/maintainers/packagers to painlessly migrate their package from setup.py to the new pyproject.toml.',
    'long_description': None,
    'author': 'Sekou Diao',
    'author_email': 'diao.sekou.nlp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
