# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zen_core',
 'zen_core.configuration',
 'zen_core.handlers',
 'zen_core.logging',
 'zen_core.parsing']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'github3.py>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'zen-core',
    'version': '0.2.1',
    'description': 'Github API zen core utilities',
    'long_description': None,
    'author': 'dragosdumitrache',
    'author_email': 'dragos@afterburner.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
