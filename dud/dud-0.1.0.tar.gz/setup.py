# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dud']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0.2,<3.0.0', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dud = dud.main:app']}

setup_kwargs = {
    'name': 'dud',
    'version': '0.1.0',
    'description': 'experimental static site generator in python',
    'long_description': None,
    'author': 'Amal Shaji',
    'author_email': '18011385+amalshaji@users.noreply.github.com',
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
