# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openapy']

package_data = \
{'': ['*']}

install_requires = \
['single-source>=0.2.0,<0.3.0']

entry_points = \
{'console_scripts': ['pypj = openapy.main:main']}

setup_kwargs = {
    'name': 'openapy',
    'version': '0.1.0',
    'description': '',
    'long_description': '# openapy\n\n`openapy` adds CI/CD capability to [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator)\n',
    'author': 'edge-minato',
    'author_email': 'edge.minato@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/edge-minato/openapy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
