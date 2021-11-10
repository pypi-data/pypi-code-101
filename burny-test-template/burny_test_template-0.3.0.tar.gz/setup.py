# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['burny_test_template']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'burny-test-template',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'BurnySc2',
    'author_email': 'gamingburny@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
