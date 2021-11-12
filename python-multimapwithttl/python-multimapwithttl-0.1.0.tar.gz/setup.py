# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multimapwithttl', 'tests']

package_data = \
{'': ['*']}

extras_require = \
{':extra == "test"': ['fakeredis>=1.6.1,<2.0.0',
                      'pytest-freezegun>=0.4.2,<0.5.0',
                      'types-redis>=3.5.15,<4.0.0'],
 'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'python-multimapwithttl',
    'version': '0.1.0',
    'description': 'An implementation of multimap with per-item expiration backed up by Redis.',
    'long_description': "# MultiMapWithTTL\n\n\n[![pypi](https://img.shields.io/pypi/v/python-multimapwithttl.svg)](https://pypi.org/project/python-multimapwithttl/)\n[![python](https://img.shields.io/pypi/pyversions/python-multimapwithttl.svg)](https://pypi.org/project/python-multimapwithttl/)\n[![Build Status](https://github.com/loggi/python-multimapwithttl/actions/workflows/dev.yml/badge.svg)](https://github.com/loggi/python-multimapwithttl/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/loggi/python-multimapwithttl/branch/main/graphs/badge.svg)](https://codecov.io/github/loggi/python-multimapwithttl)\n\n\n\nAn implementation of multimap with per-item expiration backed up by Redis.\n\n\n* Documentation: <https://loggi.github.io/python-multimapwithttl>\n* GitHub: <https://github.com/loggi/python-multimapwithttl>\n* PyPI: <https://pypi.org/project/python-multimapwithttl/>\n* Free software: MIT\n\n\n## Description\n\nThis lib is based on: https://quickleft.com/blog/how-to-create-and-expire-list-items-in-redis/\nwithout the need for an extra job to delete old items.\n\nValues are internally stored on Redis using Sorted Sets :\n\n    key1: { (score1, value1), (score2, value2), ... }\n    key2: { (score3, value3), (score4, value4), ... }\n    ...\n\nWhere the `score` is the timestamp when the value was added.\nWe use the timestamp to filter expired values and when an insertion happens,\nwe opportunistically garbage collect expired values.\n\nThe key itself is set to expire through redis ttl mechanism together with the newest value.\nThese operations result in a simulated multimap with item expiration.\n\nYou can use to keep track of values associated to keys,\nwhen the value has a notion of expiration.\n\n```\n>>> s = MultiMapWithTTL(redis_client, 'multimap')\n>>> s.add('a', 1, 2, 3)\n>>> sorted(s.get('a'))\n[1, 2, 3]\n>>> s.add_many([('b', (4, 5, 6)), ('c', (7, 8, 9)), ])\n>>> sorted(sorted(values) for values in s.get_many('a', 'b', 'c')))\n[[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n```\n",
    'author': 'Fernando Macedo',
    'author_email': 'fgmacedo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/loggi/python-multimapwithttl',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
