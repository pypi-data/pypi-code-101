# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['rainflow']
extras_require = \
{':python_version < "3.8"': ['importlib_metadata']}

setup_kwargs = {
    'name': 'rainflow',
    'version': '3.1.0',
    'description': 'Implementation of ASTM E1049-85 rainflow cycle counting algorithm',
    'long_description': "Rainflow\n========\n\n[![Test rainflow](https://github.com/iamlikeme/rainflow/actions/workflows/tests.yml/badge.svg)](https://github.com/iamlikeme/rainflow/actions/workflows/tests.yml)\n\n`rainflow` is a Python implementation of the ASTM E1049-85 rainflow cycle counting\nalgorythm for fatigue analysis. Supports both Python 2 and 3.\n\nInstallation\n------------\n\n`rainflow` is available [on PyPI](https://pypi.org/project/rainflow/):\n\n```\npip install rainflow\n```\n\nand [on conda-forge](https://github.com/conda-forge/rainflow-feedstock):\n\n```\nconda install rainflow --channel conda-forge\n```\n\nUsage\n-----\n\nSee release notes in [`CHANGELOG.md`](CHANGELOG.md).\n\nLet's generate a sample time series.\nHere we simply generate a list of floats but `rainflow` works\nwith any sequence of numbers, including numpy arrays and pandas Series.\n\n```python\nfrom math import sin, cos\n\ntime = [4.0 * i / 200 for i in range(200 + 1)]\nsignal = [0.2 + 0.5 * sin(t) + 0.2 * cos(10*t) + 0.2 * sin(4*t) for t in time]\n```\n\nFunction `count_cycles` returns a sorted list of ranges and the corresponding\nnumber of cycles:\n\n```python\nimport rainflow\n\nrainflow.count_cycles(signal)\n# Output\n[(0.04258965150708488, 0.5),\n (0.10973439445727551, 1.0),\n (0.11294628078612906, 0.5),\n (0.2057106991158965, 1.0),\n (0.21467990941625242, 1.0),\n (0.4388985979776988, 1.0),\n (0.48305748051348263, 0.5),\n (0.5286423866535466, 0.5),\n (0.7809330293159786, 0.5),\n (1.4343610172143002, 0.5)]\n```\n\nCycle ranges can be binned or rounded to a specified number of digits\nusing optional arguments *binsize*, *nbins* or *ndigits*:\n\n```python\nrainflow.count_cycles(signal, binsize=0.5)\n# Output\n[(0.5, 5.5), (1.0, 1.0), (1.5, 0.5)]\n\nrainflow.count_cycles(signal, ndigits=1)\n# Output\n[(0.0, 0.5),\n (0.1, 1.5),\n (0.2, 2.0),\n (0.4, 1.0),\n (0.5, 1.0),\n (0.8, 0.5),\n (1.4, 0.5)]\n```\n\nFull information about each cycle, including mean value, can be obtained\nusing the `extract_cycles` function:\n\n```python\nfor rng, mean, count, i_start, i_end in rainflow.extract_cycles(signal): \n    print(rng, mean, count, i_start, i_end) \n# Output             \n0.04258965150708488 0.4212948257535425 0.5 0 3\n0.11294628078612906 0.38611651111402034 0.5 3 13\n...\n0.4388985979776988 0.18268137509849586 1.0 142 158\n1.4343610172143002 0.3478109852897205 0.5 94 200\n```\n\nRunning tests\n-------------\n\n```\npip install .[dev]\npytest\n```\n",
    'author': 'Piotr Janiszewski',
    'author_email': 'i.am.like.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/iamlikeme/rainflow',
    'package_dir': package_dir,
    'py_modules': modules,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
