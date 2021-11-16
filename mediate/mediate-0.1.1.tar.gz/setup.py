# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mediate']

package_data = \
{'': ['*']}

install_requires = \
['registrate>=0.1.3,<0.2.0']

setup_kwargs = {
    'name': 'mediate',
    'version': '0.1.1',
    'description': 'Middleware for every occasion',
    'long_description': None,
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
