# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apollo_fpga',
 'apollo_fpga.commands',
 'apollo_fpga.protocol',
 'apollo_fpga.support']

package_data = \
{'': ['*']}

install_requires = \
['pyusb>=1.1.1,<2.0.0', 'pyvcd>=0.2.4,<0.3.0']

entry_points = \
{'console_scripts': ['apollo = apollo_fpga.commands.cli:main']}

setup_kwargs = {
    'name': 'apollo-fpga',
    'version': '0.0.5',
    'description': 'host tools for Apollo FPGA debug controllers',
    'long_description': None,
    'author': 'Great Scott Gadgets',
    'author_email': 'info@greatscottgadgets.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
