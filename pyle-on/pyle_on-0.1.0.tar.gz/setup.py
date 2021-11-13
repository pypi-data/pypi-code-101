# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyle_on']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyle-on',
    'version': '0.1.0',
    'description': 'Command-line tool to manage to-dos when things keep piling on',
    'long_description': '# pyle-on\nCommand-line friendly to-do list app for when things keep piling on\n',
    'author': 'Dhananjay Jindal',
    'author_email': 'djindal211@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DJ73/pyle-on',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
