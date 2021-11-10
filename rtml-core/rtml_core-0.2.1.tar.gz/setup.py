# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtml_core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rtml-core',
    'version': '0.2.1',
    'description': 'Resource tagging markup language.',
    'long_description': None,
    'author': 'DeadUnderscoreMeme',
    'author_email': 'deadunderscorememe@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
