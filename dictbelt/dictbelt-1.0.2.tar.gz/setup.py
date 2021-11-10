# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dictbelt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dictbelt',
    'version': '1.0.2',
    'description': 'A batbelt utility for dictionaries',
    'long_description': 'DICTBELT\n========\n\nThe bat-belt for dictionaries!\n\nThis library contains a set of functions and wrapper to better deal with complex\nhierarchies of dictionaries (and lists).\n\nOf note is the `dic_walk()` function that allows traversing an entire `dict` and\n`list` tree.\n\n',
    'author': 'Steeleye',
    'author_email': 'python.devs@steel-eye.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Etenil/dictbelt',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
