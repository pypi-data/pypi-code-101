# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webhook_gateway', 'webhook_gateway.routes', 'webhook_gateway.routes.rules']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'dependency-injector>=4.37.0,<5.0.0',
 'fastapi>=0.70.0,<0.71.0',
 'jsonpath-ng>=1.5.3,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'uvicorn>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'webhook-gateway',
    'version': '0.1.0',
    'description': 'A configurable webhook gateway. Routes HTTP webhooks from any source, to any HTTP REST/JSON destination !',
    'long_description': None,
    'author': 'Léo GATELLIER',
    'author_email': 'github@leogatellier.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
