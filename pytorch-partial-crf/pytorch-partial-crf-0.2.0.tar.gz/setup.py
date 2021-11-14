# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytorch_partial_crf']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6.2.5,<7.0.0', 'torch>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'pytorch-partial-crf',
    'version': '0.2.0',
    'description': '',
    'long_description': 'None',
    'author': 'Koga Kobayashi',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
