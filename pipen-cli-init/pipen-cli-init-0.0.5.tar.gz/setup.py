# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipen_cli_init']

package_data = \
{'': ['*'], 'pipen_cli_init': ['templates/*']}

install_requires = \
['cmdy>=0.4,<0.5',
 'liquidpy>=0.7,<0.8',
 'pipen>=0.2,<0.3',
 'poetry>=1,<2',
 'toml>=0.10,<0.11']

entry_points = \
{'pipen_cli': ['cli-init = pipen_cli_init:PipenCliInit']}

setup_kwargs = {
    'name': 'pipen-cli-init',
    'version': '0.0.5',
    'description': 'A pipen cli plugin to create a pipen project (pipeline)',
    'long_description': None,
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
