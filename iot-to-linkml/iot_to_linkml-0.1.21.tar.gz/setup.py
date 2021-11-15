# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iot_to_linkml']

package_data = \
{'': ['*']}

install_requires = \
['click',
 'google-api-python-client>=2.30.0,<3.0.0',
 'google-auth-oauthlib>=0.4.6,<0.5.0',
 'linkml-runtime>=1.1.6,<2.0.0',
 'linkml>=1.1.12,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'pyaml>=21.10.1,<22.0.0']

entry_points = \
{'console_scripts': ['becli = iot_to_linkml.becli:make_iot_yaml']}

setup_kwargs = {
    'name': 'iot-to-linkml',
    'version': '0.1.21',
    'description': 'see https://github.com/microbiomedata/IoT_to_linkml',
    'long_description': None,
    'author': 'Mark A. Miller',
    'author_email': 'mamillerpa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
