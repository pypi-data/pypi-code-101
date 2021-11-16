# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smb']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3', 'numpy>=1.21.4', 'torch>=1.10.0', 'torchvision>=0.11.1']

setup_kwargs = {
    'name': 'smb-optimizer',
    'version': '0.1.0',
    'description': 'Implementation for Pytorch of the method described in our paper "Bolstering Stochastic Gradient Descent with Model Building", S. Ilker Birbil, Ozgur Martin, Gonenc Onay, Figen Oztoprak, 2021 (see https://arxiv.org/abs/2111.07058)',
    'long_description': None,
    'author': 'Ilker BIRBIL',
    'author_email': 's.i.birbil@uva.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
