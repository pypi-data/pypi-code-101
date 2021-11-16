# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dvnv', 'dvnv.scripts.all', 'dvnv.scripts.python', 'dvnv.scripts.vim']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'rich>=10.12.0,<11.0.0']

entry_points = \
{'console_scripts': ['dvnv = dvnv.__main__:run_dvnv']}

setup_kwargs = {
    'name': 'dvnv',
    'version': '0.4.1',
    'description': 'Automate the creation of development environments',
    'long_description': None,
    'author': 'sudo-julia',
    'author_email': 'jlearning@tuta.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
