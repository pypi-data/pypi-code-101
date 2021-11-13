# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bot_exts', 'bot_exts.cogs']

package_data = \
{'': ['*']}

install_requires = \
['nextcord>=2.0.0-alpha.3,<3.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'tortoise-orm>=0.17.8,<0.18.0']

setup_kwargs = {
    'name': 'bot-exts',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'TrixiS',
    'author_email': 'oficialmorozov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
