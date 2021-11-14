# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autobright']

package_data = \
{'': ['*']}

install_requires = \
['altair>=4.1.0,<5.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'streamlit>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['autobright = autobright.__main__:main']}

setup_kwargs = {
    'name': 'autobright',
    'version': '0.1.0',
    'description': 'Automatically adjust display brightness with external sensor',
    'long_description': None,
    'author': 'Martin Ueding',
    'author_email': 'mu@martin-ueding.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
