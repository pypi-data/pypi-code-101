# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oofd_kz_parser']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'html5lib>=1.1,<2.0',
 'pydantic>=1.8.2,<2.0.0',
 'pyzbar>=0.1.8,<0.2.0',
 'selenium>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'oofd-kz-parser',
    'version': '0.1.1',
    'description': 'Parse tickets from consumer.oofd.kz',
    'long_description': None,
    'author': 'Kirill Olar',
    'author_email': 'kirill.olar26@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skroll182/oofd-kz-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
