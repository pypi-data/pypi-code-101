# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netts',
    'version': '0.1.0',
    'description': 'Not name squatting, to be released later this week.',
    'long_description': None,
    'author': 'Iain-S',
    'author_email': '25081046+Iain-S@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
