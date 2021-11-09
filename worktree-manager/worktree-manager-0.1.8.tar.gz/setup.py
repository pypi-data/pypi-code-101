# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['worktree_manager']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0']

entry_points = \
{'console_scripts': ['work = worktree_manager.manager:cli']}

setup_kwargs = {
    'name': 'worktree-manager',
    'version': '0.1.8',
    'description': '',
    'long_description': None,
    'author': 'Tal Vintrob',
    'author_email': 'tvaintrob@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
