# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['fee']
entry_points = \
{'console_scripts': ['fee = fee:main']}

setup_kwargs = {
    'name': 'fee',
    'version': '0.1.1',
    'description': 'Execute ELF files without dropping them on disk',
    'long_description': None,
    'author': 'Rasmus Moorats',
    'author_email': 'xx@nns.ee',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
