# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dgad', 'dgad.app', 'dgad.grpc', 'dgad.models']

package_data = \
{'': ['*'], 'dgad.grpc': ['protos/*']}

install_requires = \
['grpcio>=1.34,<2.0',
 'keras-tcn>=3.2.1,<4.0.0',
 'numpy>=1.19.5,<2.0.0',
 'pandas>=1.1.5,<2.0.0',
 'pip>=21.1.2,<22.0.0',
 'redis>=3.5.3,<4.0.0',
 'tensorflow-cpu>=2.6.0,<3.0.0',
 'tldextract>=3.1.0,<4.0.0']

entry_points = \
{'console_scripts': ['dgad = dgad.app.cli:main']}

setup_kwargs = {
    'name': 'dgad',
    'version': '3.1.0',
    'description': '',
    'long_description': None,
    'author': 'Federico Falconieri',
    'author_email': 'federico.falconieri@tno.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
