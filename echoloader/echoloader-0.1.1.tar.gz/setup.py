# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['echoloader']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.4,<2.0.0',
 'opencv-python>=4.5.4,<5.0.0',
 'pycognito>=2021.3.1,<2022.0.0',
 'pydicom>=2.2.2,<3.0.0',
 'pynetdicom>=1.5.7,<2.0.0',
 'python-gdcm>=3.0.10,<4.0.0',
 'requests>=2.26.0,<3.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'watchdog>=2.1.5,<3.0.0']

entry_points = \
{'console_scripts': ['echoloader = echoloader.watcher:main']}

setup_kwargs = {
    'name': 'echoloader',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'mathias',
    'author_email': 'mathias@us2.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.5,<3.11',
}


setup(**setup_kwargs)
