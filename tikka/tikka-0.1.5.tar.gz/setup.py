# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tikka',
 'tikka.adapters',
 'tikka.data',
 'tikka.domains',
 'tikka.gui',
 'tikka.gui.images',
 'tikka.gui.menus',
 'tikka.gui.tabs',
 'tikka.gui.widgets',
 'tikka.gui.windows',
 'tikka.libs']

package_data = \
{'': ['*'],
 'tikka': ['assets/*',
           'assets/migrations/*',
           'locales/en_US/*',
           'locales/en_US/LC_MESSAGES/*',
           'locales/fr_FR/*',
           'locales/fr_FR/LC_MESSAGES/*'],
 'tikka.gui.images': ['files/*']}

install_requires = \
['duniterpy==1.0.0rc1',
 'markdown>=3.3.3,<4.0.0',
 'mnemonic>=0.19,<0.20',
 'tkinterhtml>=0.7,<0.8',
 'wxPython==4.1.1',
 'yoyo-migrations>=7.3.1,<8.0.0']

entry_points = \
{'console_scripts': ['tikka = tikka.__main__:main']}

setup_kwargs = {
    'name': 'tikka',
    'version': '0.1.5',
    'description': 'Tikka is a fast and light Python/Tk client to manage your Ğ1 accounts',
    'long_description': None,
    'author': 'Vincent Texier',
    'author_email': 'vit@free.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
