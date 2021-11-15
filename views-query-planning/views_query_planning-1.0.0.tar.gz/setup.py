# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['views_query_planning']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.27,<2.0.0', 'networkx>=2.6.3,<3.0.0']

setup_kwargs = {
    'name': 'views-query-planning',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'peder2911',
    'author_email': 'pglandsverk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
