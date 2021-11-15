# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_auth_server']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.3,<3.0',
 'bareasgi-auth-common>=4.0,<5.0',
 'bareasgi-cors>=4.1,<5.0',
 'bareasgi>=4.0,<5.0',
 'bareclient>=5.0,<6.0']

setup_kwargs = {
    'name': 'bareasgi-auth-server',
    'version': '4.0.1',
    'description': 'Authentication server for bareASGI',
    'long_description': '# bareASGI-auth-server\n\nAn example authentication server.\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareASGI-auth-server',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
