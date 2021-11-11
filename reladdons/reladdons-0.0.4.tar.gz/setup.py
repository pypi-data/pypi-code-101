# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['reladdons']
setup_kwargs = {
    'name': 'reladdons',
    'version': '0.0.4',
    'description': 'the 4 version',
    'long_description': None,
    'author': "D1ffic00lt's Community",
    'author_email': 'dm.filinov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
