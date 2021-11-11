# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zen', 'zen.commands', 'zen.main']

package_data = \
{'': ['*']}

install_requires = \
['fuzzyfinder>=2.1.0,<3.0.0',
 'fuzzysearch>=0.7.3,<0.8.0',
 'simple-term-menu>=1.4.1,<2.0.0',
 'zen-core==0.2.0']

entry_points = \
{'console_scripts': ['zen = zen.main.zen:main']}

setup_kwargs = {
    'name': 'zen-git',
    'version': '0.1.3',
    'description': 'A git CLI utility tool',
    'long_description': '# Github Zen utility tools\n\nThis is a simple project aimed at improving command-line developer workflow with git.\n',
    'author': 'Dragos Dumitrache',
    'author_email': 'dragos@afterburner.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
