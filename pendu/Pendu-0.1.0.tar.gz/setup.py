# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pendu']

package_data = \
{'': ['*']}

install_requires = \
['art>=5.3,<6.0', 'termcolor>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'pendu',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'iHelperRepo',
    'author_email': '86736499+PetchouDev@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
