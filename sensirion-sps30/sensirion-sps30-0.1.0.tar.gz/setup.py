# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sensirion_sps30']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'sensirion-sps30',
    'version': '0.1.0',
    'description': 'Sensirion SPS30 Python library',
    'long_description': '# Sensirion SPS30 PM Sensor\n\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/MMartin09/sensirion-sps30/lint?style=flat-square)\n![GitHub](https://img.shields.io/github/license/MMartin09/sensirion-sps30)\n[![style black](https://img.shields.io/badge/Style-Black-black.svg?style=flat-square)](https://github.com/ambv/black)\n\n## Usage\n\nExample Python script to read and print a single measurement.\n\n```python\nfrom time import sleep\n\nfrom sensirion_sps30 import SPS30\n\nport: str = "COM3"\nsps30 = SPS30(port)\n\nsps30.start_measurement()\nsleep(5)\n\ndata = sps30.read_values()\nprint(data)\n\nsps30.stop_measurement()\n```',
    'author': 'MMartin09',
    'author_email': 'mmartin09@outlook.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mmartin09.github.io/pm-dashboard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
