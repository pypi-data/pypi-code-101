# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proto-stubs']

package_data = \
{'': ['*'],
 'proto-stubs': ['marshal/*', 'marshal/collections/*', 'marshal/rules/*']}

install_requires = \
['proto-plus>=1.18.0,<2.0.0', 'types-protobuf>=3.17.4,<4.0.0']

setup_kwargs = {
    'name': 'generic-proto-plus-stubs',
    'version': '0.1.1.post1',
    'description': 'Manually updated type stubs for proto-plus with some generics',
    'long_description': 'O           \n[![PyPI version](https://badge.fury.io/py/generic-proto-plus-stubs.svg)](https://badge.fury.io/py/generic-proto-plus-stubs)\n\nThis package provides type stubs for the [proto-plus](https://pypi.org/project/proto-plus/) package with \nsome use of generics. \n\n**This is in no way affiliated with Google.**\n\n**This is basically just a fork of [henribru/proto-plus-stubs](https://github.com/henribru/proto-plus-stubs)\nwith some manually added code to make use of pythons generics**\n\nThe stubs were created automatically by [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html).\n## Installation\n```shell script\n$ pip install generic-proto-stubs\n```\n',
    'author': 'Maximilian Schmidt',
    'author_email': 'landlaeufer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/saggitar/generic-proto-plus-stubs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
