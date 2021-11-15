# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['modelator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'modelator',
    'version': '0.0.1',
    'description': 'Python bindings of Modelator',
    'long_description': None,
    'author': 'Ranadeep Biswas',
    'author_email': 'mail@rnbguy.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
