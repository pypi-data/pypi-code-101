# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbt_coverage']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dbt-coverage = dbt_coverage.__init__:app']}

setup_kwargs = {
    'name': 'dbt-coverage',
    'version': '0.1.0',
    'description': 'A package for computing coverage of dbt-managed data warehouses',
    'long_description': None,
    'author': 'Andrej Švec',
    'author_email': 'asvec@slido.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
