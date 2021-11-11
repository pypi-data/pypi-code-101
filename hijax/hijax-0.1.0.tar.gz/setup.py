# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hijax', 'hijax.setup']

package_data = \
{'': ['*']}

install_requires = \
['black>=21.10b0,<22.0',
 'dm-haiku>=0.0.5,<0.0.6',
 'hydra-core>=1.1.1,<2.0.0',
 'jax>=0.2.24,<0.3.0',
 'mypy>=0.910,<0.911',
 'numpy>=1.21.4,<2.0.0',
 'optax>=0.0.9,<0.0.10',
 'torch>=1.10.0,<2.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'wandb>=0.12.6,<0.13.0']

setup_kwargs = {
    'name': 'hijax',
    'version': '0.1.0',
    'description': 'An experiment framework for Haiku and Jax',
    'long_description': None,
    'author': 'Angus Turner',
    'author_email': 'angusturner27@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
