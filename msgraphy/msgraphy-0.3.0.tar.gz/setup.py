# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msgraphy',
 'msgraphy.auth',
 'msgraphy.client',
 'msgraphy.data',
 'msgraphy.domains',
 'msgraphy.sharepoint_classic']

package_data = \
{'': ['*']}

install_requires = \
['msal>=1.10.0,<2.0.0', 'pyhumps>=3.0.2,<4.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'msgraphy',
    'version': '0.3.0',
    'description': 'An API generator for the MS Graph API',
    'long_description': None,
    'author': 'Kaj Siebert',
    'author_email': 'kaj@k-si.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
