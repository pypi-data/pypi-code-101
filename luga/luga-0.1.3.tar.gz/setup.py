# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['luga']

package_data = \
{'': ['*']}

install_requires = \
['fasttext>=0.9.2,<0.10.0', 'httpx>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'luga',
    'version': '0.1.3',
    'description': 'Sensing the language of the text using Machine Learning',
    'long_description': None,
    'author': 'Prayson W. Daniel',
    'author_email': 'praysonwilfred@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
