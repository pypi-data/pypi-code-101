# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cosmoglobe',
 'cosmoglobe.data',
 'cosmoglobe.h5',
 'cosmoglobe.plot',
 'cosmoglobe.sky',
 'cosmoglobe.sky.components']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2',
 'astropy>=4.3.1,<5.0.0',
 'click>=8.0.1',
 'cmasher>=1.6.2,<2.0.0',
 'h5py>=3.0.0',
 'healpy>=1.15.0,<2.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'numba>=0.54.0,<0.55.0',
 'numpy>=1.17.0,<1.21.0',
 'rich>=10.9.0,<11.0.0',
 'scipy>=1.6.0',
 'tqdm>=4.62.2,<5.0.0']

entry_points = \
{'console_scripts': ['cosmoglobe = cosmoglobe.__main__:cli']}

setup_kwargs = {
    'name': 'cosmoglobe',
    'version': '0.9.43',
    'description': 'A Python package for interfacing the Cosmoglobe Sky Model with commander3 outputs for the purpose of producing astrophysical sky maps.',
    'long_description': '\n\n# Cosmoglobe Sky Model\n[![Documentation Status](https://readthedocs.org/projects/cosmoglobe/badge/?version=latest)](https://cosmoglobe.readthedocs.io/en/latest/?badge=latest)\n[![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/)\n\n## Description\ncosmoglobe is a python package that interfaces the Cosmoglobe Sky Model with the commander3 outputs for the purpose of producing astrophyiscal sky maps.\n\nThe documentation can be found at [https://cosmoglobe.readthedocs.io](https://cosmoglobe.readthedocs.io/en/latest/).\n## Funding\n\nThis work has received funding from the European Union\'s Horizon 2020 research and innovation programme under grant agreements No 776282 (COMPET-4; BeyondPlanck), 772253 (ERC; bits2cosmology) and 819478 (ERC; Cosmoglobe).\n\n<p align="center">\n    <img src="./logo/LOGO_ERC-FLAG_EU_.jpg" height="200">\n    <img src="./logo/horizon2020_logo.jpg" height="200">\n</p>\n\n---\n\n## License\n\n[GNU GPLv3](https://github.com/Cosmoglobe/Commander/blob/master/COPYING)\n',
    'author': 'Metin San',
    'author_email': 'metinisan@gmail.com',
    'maintainer': 'Metin San',
    'maintainer_email': 'metinisan@gmail.com',
    'url': 'https://github.com/Cosmoglobe/Cosmoglobe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
