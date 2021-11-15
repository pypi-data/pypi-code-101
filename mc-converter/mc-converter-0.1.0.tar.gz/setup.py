# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mc_converter', 'mc_converter.Helpers']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'murmurhash2>=0.2.9,<0.3.0',
 'pytoml>=0.1.21,<0.2.0',
 'tomli>=1.2.1,<2.0.0']

entry_points = \
{'console_scripts': ['mc-converter = mc_converter:main']}

setup_kwargs = {
    'name': 'mc-converter',
    'version': '0.1.0',
    'description': '',
    'long_description': "# modpack-converter\nConvert's one modpack format to another.\n\nMaybe I need to think of a better name...\n\n# How to Install\n\n## From PyPI\n```\npip install mc-converter\n```\n## From `.whl` file\nGo to Release page, download latest `.whl` file \\\n And install it via the following comand:\n ```\n pip install mc_converter_{version}.whl\n ```\n ",
    'author': 'RozeFound',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RozeFound/modpack-converter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
