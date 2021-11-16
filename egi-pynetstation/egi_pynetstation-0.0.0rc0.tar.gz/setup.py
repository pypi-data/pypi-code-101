# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['egi_pynetstation', 'egi_pynetstation.tests']

package_data = \
{'': ['*']}

install_requires = \
['ntplib>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'egi-pynetstation',
    'version': '0.0.0rc0',
    'description': 'Magstim-EGI EEG amplifier NetStation API',
    'long_description': None,
    'author': 'Joshua Teves',
    'author_email': 'joshua.teves@nih.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
