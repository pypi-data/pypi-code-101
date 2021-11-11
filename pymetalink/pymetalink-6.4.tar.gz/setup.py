# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metalink']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pymetalink = metalink.console:main']}

setup_kwargs = {
    'name': 'pymetalink',
    'version': '6.4',
    'description': 'A metalink library for Python',
    'long_description': None,
    'author': 'Neil McNab',
    'author_email': 'nabber00@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/metalink-dev/pymetalink',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
