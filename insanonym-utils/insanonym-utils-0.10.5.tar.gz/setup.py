# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['insanonym_utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pdoc3>=0.9.2,<0.10.0',
 'pydantic>=1.8.1,<2.0.0',
 'pytest>=6.2.3,<7.0.0']

entry_points = \
{'console_scripts': ['anon = insanonym_utils.main:main']}

setup_kwargs = {
    'name': 'insanonym-utils',
    'version': '0.10.5',
    'description': 'Execute anonymization scripts over a table',
    'long_description': None,
    'author': 'Daniel Mathiot',
    'author_email': 'd.danymat@gmail.com',
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
