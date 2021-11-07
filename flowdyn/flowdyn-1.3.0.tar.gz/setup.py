# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowdyn', 'flowdyn.modelphy', 'flowdyn.solution']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.15,<2.0', 'pytest>=6.0,<7.0']

setup_kwargs = {
    'name': 'flowdyn',
    'version': '1.3.0',
    'description': 'Model of discretization of hyperbolic model, base is Finite Volume method',
    'long_description': 'flowdyn\n-----\n\n[![PyPi Version](https://img.shields.io/pypi/v/flowdyn.svg?style=flat)](https://pypi.org/project/flowdyn)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/flowdyn.svg?style=flat)](https://pypi.org/pypi/flowdyn/)\n[![Build Status](https://travis-ci.com/jgressier/flowdyn.svg?branch=master)](https://travis-ci.com/jgressier/flowdyn)\n[![Doc](https://readthedocs.org/projects/flowdyn/badge/?version=latest)](https://flowdyn.readthedocs.io/en/latest/)\n[![Slack](https://img.shields.io/static/v1?logo=slack&label=slack&message=contact&style=flat)](https://join.slack.com/t/isae-opendev/shared_invite/zt-obqywf6r-UUuHR4_hc5iTzyL5bFCwpw\n)\n\n[![GitHub stars](https://img.shields.io/github/stars/jgressier/flowdyn.svg?style=flat&logo=github&label=Stars&logoColor=white)](https://github.com/jgressier/flowdyn)\n[![PyPi downloads](https://img.shields.io/pypi/dm/flowdyn.svg?style=flat)](https://pypistats.org/packages/flowdyn)\n[![codecov](https://img.shields.io/codecov/c/github/jgressier/flowdyn.svg?style=flat)](https://codecov.io/gh/jgressier/flowdyn)\n[![lgtm](https://img.shields.io/lgtm/grade/python/github/jgressier/flowdyn.svg?style=flat)](https://lgtm.com/projects/g/jgressier/flowdyn/)\n\n### Documentation and examples\n\n* documentation of the [official release](https://flowdyn.readthedocs.io/en/latest/) or [development branch](https://flowdyn.readthedocs.io/en/develop/)\n* some [examples in the documentation](https://flowdyn.readthedocs.io/en/latest/examples) pages\n* some examples in the [github repository](https://github.com/jgressier/flowdyn/tree/master/validation)\n\n### Features\n\nCurrent version includes\n* 1D scalar models: linear convection, Burgers\n* 1D model: inviscid compressible flow (Euler), section law effects with source terms\n* 1st to 3rd order linear extrapolation, 2nd order MUSCL extrapolation\n* various centered or upwind/Riemann fluxes\n* explicit, runge-kutta and implicit integrators\n\n### Installation and usage\n\n    pip install flowdyn\n\n### Requirements\n\n* `numpy`\n* examples are plotted using [matplotlib](http://matplotlib.org)\n\n',
    'author': 'j.gressier',
    'author_email': 'jeremie.gressier@isae-supaero.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jgressier/flowdyn',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
