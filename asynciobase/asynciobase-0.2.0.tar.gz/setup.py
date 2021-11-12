# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asynciobase']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'asynciobase',
    'version': '0.2.0',
    'description': 'Base class for every async file-like, similar to io.IOBase for sync file-like',
    'long_description': None,
    'author': 'JuniorJPDJ',
    'author_email': 'dev@juniorjpdj.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
