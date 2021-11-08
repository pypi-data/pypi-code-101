# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['chkdns', 'chkdns.whatsmydns']

package_data = \
{'': ['*']}

install_requires = \
['asyncio>=3.4.3,<4.0.0',
 'click>=8.0.3,<9.0.0',
 'httpx>=0.20.0,<0.21.0',
 'mypy>=0.910,<0.911',
 'rich>=10.13.0,<11.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['chkdns = chkdns.app:cli']}

setup_kwargs = {
    'name': 'chkdns',
    'version': '0.1.0',
    'description': 'A tool to check global dns propagation',
    'long_description': None,
    'author': 'Craig Gumbley',
    'author_email': 'craiggumbley@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chelnak/chkdns',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
