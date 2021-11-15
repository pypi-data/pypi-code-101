# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataclass_builders']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dataclass-builders',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Bidimpata-Kerim Ntumba Tshimanga',
    'author_email': 'bk.tshimanga@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
