# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyninjotiff', 'pyninjotiff.tests']

package_data = \
{'': ['*']}

install_requires = \
['dask[array]>=2021.9.1,<2022.0.0',
 'numpy>=1.6',
 'pyproj>=3.2.1,<4.0.0',
 'pyresample>=1.21.1,<2.0.0',
 'trollimage>=1.15.1,<2.0.0',
 'xarray>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'pyninjotiff',
    'version': '0.4.0',
    'description': 'Python Ninjo TIFF writing library',
    'long_description': None,
    'author': 'Martin Raspaud',
    'author_email': 'martin.raspaud@smhi.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
