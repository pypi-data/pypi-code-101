# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['isetool']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'requests>=2.26.0,<3.0.0', 'urllib3>=1.26.6,<2.0.0']

entry_points = \
{'console_scripts': ['isetool = isetool.cli:cli']}

setup_kwargs = {
    'name': 'isetool',
    'version': '1.0.1',
    'description': 'Command line for querying a Cisco ISE server',
    'long_description': '# isetool',
    'author': 'Rob Woodward',
    'author_email': 'rob@emailplus.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/robwdwd/isetool',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
