# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['graia', 'graia.scheduler', 'graia.scheduler.saya']

package_data = \
{'': ['*']}

install_requires = \
['croniter>=1.0.0,<2.0.0', 'graia-broadcast>=0.12.1']

extras_require = \
{':python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'graia-scheduler',
    'version': '0.0.6',
    'description': 'a scheduler for graia framework',
    'long_description': None,
    'author': 'GreyElaina',
    'author_email': 'GreyElaina@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
