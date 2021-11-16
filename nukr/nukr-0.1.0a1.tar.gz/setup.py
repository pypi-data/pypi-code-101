# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nukr']

package_data = \
{'': ['*']}

install_requires = \
['click-sources>=0.1.0-alpha.1,<0.2.0',
 'click>=8.0.3,<9.0.0',
 'dateparser>=1.1.0,<2.0.0',
 'praw>=7.5.0,<8.0.0',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'nukr',
    'version': '0.1.0a1',
    'description': '',
    'long_description': None,
    'author': '0',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
