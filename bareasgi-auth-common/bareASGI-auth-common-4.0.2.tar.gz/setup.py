# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_auth_common']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.3,<3.0', 'bareasgi>=4.0,<5.0', 'bareclient>=5.0,<6.0']

setup_kwargs = {
    'name': 'bareasgi-auth-common',
    'version': '4.0.2',
    'description': '',
    'long_description': '# bareASGI-auth-common\n\nCommon code for authentication with bareASGI.',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareASGI-auth-common',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
