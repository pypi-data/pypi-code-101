# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scenic',
 'scenic.core',
 'scenic.domains',
 'scenic.domains.driving',
 'scenic.formats',
 'scenic.formats.opendrive',
 'scenic.simulators',
 'scenic.simulators.carla',
 'scenic.simulators.carla.utils',
 'scenic.simulators.gta',
 'scenic.simulators.lgsvl',
 'scenic.simulators.newtonian',
 'scenic.simulators.newtonian.utils',
 'scenic.simulators.utils',
 'scenic.simulators.webots',
 'scenic.simulators.webots.guideways',
 'scenic.simulators.webots.mars',
 'scenic.simulators.webots.road',
 'scenic.simulators.xplane',
 'scenic.syntax']

package_data = \
{'': ['*']}

install_requires = \
['antlr4-python3-runtime>=4.8,<4.9',
 'attrs>=19.3.0,<20.0.0',
 'decorator>=5.0.9,<6.0.0',
 'dotmap>=1.3.13,<2.0.0',
 'mapbox_earcut>=0.12.10,<0.13.0',
 'matplotlib>=3.2.1,<4.0.0',
 'numpy>=1.21.3,<2.0.0',
 'opencv-python>=4.5.4,<5.0.0',
 'pillow>=8.1.1,<9.0.0',
 'pygame>=2.0.1,<3.0.0',
 'pynverse>=0.1.4,<0.2.0',
 'scipy>=1.4.1,<2.0.0',
 'shapely>=1.7.0,<2.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['importlib_metadata>=3.7,<4.0'],
 'dev': ['pyproj>=3.0.0,<4.0.0',
         'pytest-randomly>=3.2.1,<4.0.0',
         'pytest>=6.0.0,<7.0.0',
         'sphinx>=3.3.0,<5',
         'tox>=3.14.0,<4.0.0',
         'sphinx_rtd_theme>=0.5.2,<0.6.0',
         'astor>=0.8.1,<0.9.0'],
 'guideways': ['pyproj>=3.0.0,<4.0.0'],
 'test': ['pytest-randomly>=3.2.1,<4.0.0', 'pytest>=6.0.0,<7.0.0']}

entry_points = \
{'console_scripts': ['scenic = scenic.__main__:dummy'],
 'pygments.lexers': ['scenic = scenic.syntax.pygment:ScenicLexer']}

setup_kwargs = {
    'name': 'scenic',
    'version': '2.1.0b1',
    'description': 'The Scenic scenario description language.',
    'long_description': '# Scenic\n\n[![Documentation Status](https://readthedocs.org/projects/scenic-lang/badge/?version=latest)](https://scenic-lang.readthedocs.io/en/latest/?badge=latest)\n[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n\nA compiler and scenario generator for the Scenic scenario description language.\nPlease see the [documentation](https://scenic-lang.readthedocs.io/) for installation instructions, as well as tutorials and other information about the Scenic language, its implementation, and its interfaces to various simulators.\n\nFor a description of the language and some of its applications, see [our preprint](https://arxiv.org/abs/2010.06580), which extends our [PLDI 2019 paper](https://arxiv.org/abs/1809.09310) (*note:* the syntax of Scenic has changed slightly since that paper, and many features such as support for dynamic scenarios have been added; these are described in the preprint).\nScenic was designed and implemented by Daniel J. Fremont, Edward Kim, Tommaso Dreossi, Shromona Ghosh, Xiangyu Yue, Alberto L. Sangiovanni-Vincentelli, and Sanjit A. Seshia.\n\nIf you have any problems using Scenic, please submit an issue to [our GitHub repository](https://github.com/BerkeleyLearnVerify/Scenic) or contact Daniel at <dfremont@ucsc.edu>.\n\nThe repository is organized as follows:\n\n* the _src/scenic_ directory contains the package proper;\n* the _examples_ directory has many examples of Scenic programs;\n* the _docs_ directory contains the sources for the documentation;\n* the _tests_ directory contains tests for the Scenic compiler.\n',
    'author': 'Daniel Fremont',
    'author_email': 'dfremont@ucsc.edu',
    'maintainer': 'Daniel Fremont',
    'maintainer_email': 'dfremont@ucsc.edu',
    'url': 'https://github.com/BerkeleyLearnVerify/Scenic',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
