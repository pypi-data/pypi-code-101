# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kebab', 'kebab.cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'deprecation>=2.1.0,<3.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pyyaml>=5.3.1,<6.0.0']

extras_require = \
{'ali': ['oss2>=2.11.0,<3.0.0'],
 'aws': ['boto3>=1.13.12,<2.0.0'],
 'k8s': ['kubernetes>=12.0.0a1,<13.0.0']}

entry_points = \
{'console_scripts': ['kebab = kebab.cli:run']}

setup_kwargs = {
    'name': 'pykebab',
    'version': '0.5.0',
    'description': '',
    'long_description': None,
    'author': 'Yangming Huang',
    'author_email': 'leonmax@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
