# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hass_auth_synology']

package_data = \
{'': ['*']}

install_requires = \
['homeassistant>=2021.11.2,<2022.0.0']

entry_points = \
{'console_scripts': ['hass-auth-synology = hass_auth_synology.install:cli']}

setup_kwargs = {
    'name': 'hass-auth-synology',
    'version': '0.2.0',
    'description': 'Synology authentication provider for Home Assistant',
    'long_description': None,
    'author': 'Sam Debruyn',
    'author_email': 'sam@debruyn.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
