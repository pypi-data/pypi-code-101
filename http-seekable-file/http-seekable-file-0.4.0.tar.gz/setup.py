# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['http_seekable_file']

package_data = \
{'': ['*']}

extras_require = \
{'async': ['aiohttp[speedups]>=3.6,<4.0',
           'asynciobase>=0.2.0,<0.3.0',
           'asyncio-rlock>=0.1.0,<0.2.0'],
 'sync': ['requests>=2.22,<3.0']}

setup_kwargs = {
    'name': 'http-seekable-file',
    'version': '0.4.0',
    'description': 'Provides file-like seekable interface for HTTP(S) URLs in sync and async fashion',
    'long_description': None,
    'author': 'JuniorJPDJ',
    'author_email': 'dev@juniorjpdj.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
