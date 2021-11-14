# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exc_fal']

package_data = \
{'': ['*']}

install_requires = \
['iaswn>=0.1.6,<0.2.0', 'rich>=10.13.0,<11.0.0']

setup_kwargs = {
    'name': 'exc-fal',
    'version': '0.1.7',
    'description': '',
    'long_description': None,
    'author': 'suizokukan',
    'author_email': 'suizokukan@orange.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
