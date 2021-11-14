# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_demo_domroon']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'poetry-demo-domroon',
    'version': '0.1.2',
    'description': 'Test',
    'long_description': None,
    'author': 'Dominik Haeusser',
    'author_email': 'haeusser-dominik@web.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
