# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['many_requests_cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['mrc = many_requests_cli.main:app']}

setup_kwargs = {
    'name': 'many-requests-cli',
    'version': '0.1.2',
    'description': 'CLI app to send muliple requests to endpoint.',
    'long_description': "*Send many requests* 💣\n=======================   \n\nCLI app to send muliple requests to endpoint.\n\nUsage\n-----\nInstall the package:\n\n``pip install many-requests-cli``\nuse the command:\n``mrc --help``\n    \n*Disclaimer*\n------------\nI don't know what I am doing. Hope you know what you doing by using this! 🔬\n",
    'author': 'Yves Tumushimire',
    'author_email': 'ytumushimire@truststamp.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yvestumushimire/many_requests/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
