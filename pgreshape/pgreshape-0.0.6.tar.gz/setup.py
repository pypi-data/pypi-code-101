# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pgreshape']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.3.0,<0.4.0']

entry_points = \
{'console_scripts': ['pgreshape = pgreshape.main:main']}

setup_kwargs = {
    'name': 'pgreshape',
    'version': '0.0.6',
    'description': 'Embed the new column according to the desired position in any table in the postgresql database., using on CLI.',
    'long_description': '# reshape',
    'author': 'Rafael Fernando Garcia Sagastume',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafaelsagastume/reshape.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
