# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['base', 'schemas']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.7.0,<0.8.0',
 'aiohttp[speedups]>=3.8.0,<4.0.0',
 'pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'timetables-lib',
    'version': '1.0.0',
    'description': 'Szkolny.eu Timetables Common Library',
    'long_description': '# Szkolny.eu Timetables Common Library\n\nThis is a common library used by all Timetables packages and containers.\n',
    'author': 'Kuba Szczodrzyński',
    'author_email': 'kuba@szczodrzynski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
