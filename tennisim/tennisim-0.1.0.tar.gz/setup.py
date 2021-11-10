# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tennisim']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tennisim',
    'version': '0.1.0',
    'description': 'Simple pure python functions for simulating tennis matches',
    'long_description': '# tennisim\nSmall package to simulate tennis points, games, sets and matches\n',
    'author': 'mjam03',
    'author_email': 'markjamison03@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mjam03/tennisim',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
