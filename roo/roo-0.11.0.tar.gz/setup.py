# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['roo',
 'roo.caches',
 'roo.cli',
 'roo.deptree',
 'roo.exporters',
 'roo.exporters.lock',
 'roo.files',
 'roo.parsers',
 'roo.semver',
 'roo.sources']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.13,<4.0.0',
 'atomicwrites>=1.4,<2.0',
 'beautifulsoup4>=4.8.2,<5.0.0',
 'click>=7.0,<8.0',
 'packaging>=20.1,<21.0',
 'requests>=2.22.0,<3.0.0',
 'rich>=2.2.3,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['roo = roo.cli.__main__:main']}

setup_kwargs = {
    'name': 'roo',
    'version': '0.11.0',
    'description': 'A package manager to handle R environments',
    'long_description': None,
    'author': 'Stefano Borini',
    'author_email': 'stefano.borini@astrazeneca.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
