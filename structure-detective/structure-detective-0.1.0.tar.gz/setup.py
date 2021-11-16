# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['structure_detective',
 'structure_detective.de',
 'structure_detective.en',
 'structure_detective.es']

package_data = \
{'': ['*']}

install_requires = \
['spacy>=3.2.0,<4.0.0']

setup_kwargs = {
    'name': 'structure-detective',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
