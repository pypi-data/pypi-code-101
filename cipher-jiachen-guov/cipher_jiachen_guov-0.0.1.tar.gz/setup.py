# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cipher_jiachen_guov']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.4,<2.0.0', 'pytest>=6.2.5,<7.0.0']

setup_kwargs = {
    'name': 'cipher-jiachen-guov',
    'version': '0.0.1',
    'description': 'good',
    'long_description': None,
    'author': 'Jiachen Guo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.12,<4.0.0',
}


setup(**setup_kwargs)
