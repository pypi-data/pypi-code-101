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
    'version': '0.1.1',
    'description': 'CLI app to send muliple requests to endpoint.',
    'long_description': None,
    'author': 'Yves Tumushimire',
    'author_email': 'ytumushimire@truststamp.net',
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
