# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isabelle_client']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'isabelle-client',
    'version': '0.2.10',
    'description': 'A client to Isabelle proof assistant server',
    'long_description': "[![PyPI version](https://badge.fury.io/py/isabelle-client.svg)](https://badge.fury.io/py/isabelle-client) [![CircleCI](https://circleci.com/gh/inpefess/isabelle-client.svg?style=svg)](https://circleci.com/gh/inpefess/isabelle-client) [![Documentation Status](https://readthedocs.org/projects/isabelle-client/badge/?version=latest)](https://isabelle-client.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/inpefess/isabelle-client/branch/master/graph/badge.svg)](https://codecov.io/gh/inpefess/isabelle-client)\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/inpefess/isabelle-client/HEAD?labpath=example.ipynb)\n\n# Python client for Isabelle server\n\n`isabelle-client` is a TCP client for [Isabelle](https://isabelle.in.tum.de) server. For more information about the server see part 4 of [the Isabelle system manual](https://isabelle.in.tum.de/dist/Isabelle2021/doc/system.pdf).\n\n# How to Install\n\nThe best way to install this package is to use `pip`:\n\n```sh\npip install isabelle-client\n```\n\nOne can also download and run the client together with Isabelle in a Docker contanier:\n\n```sh\ndocker build -t isabelle-client https://github.com/inpefess/isabelle-client.git\ndocker run -it --rm -p 8888:8888 isabelle-client jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser\n```\n\n# How to use\n\nFollow the [usage example](https://isabelle-client.readthedocs.io/en/latest/usage-example.html#usage-example) from documentation, run the [script](https://github.com/inpefess/isabelle-client/blob/master/examples/example.py), or use `isabelle-client` from a [notebook](https://github.com/inpefess/isabelle-client/blob/master/examples/example.ipynb), e.g. with [Binder](https://mybinder.org/v2/gh/inpefess/isabelle-client/HEAD?labpath=example.ipynb).\n\n# How to Contribute\n\n[Pull requests](https://github.com/inpefess/isabelle-client/pulls) are welcome. To start:\n\n```sh\ngit clone https://github.com/inpefess/isabelle-client\ncd isabelle-client\n# activate python virtual environment with Python 3.6+\npip install -U pip\npip install -U setuptools wheel poetry\npoetry install\n# recommended but not necessary\npre-commit install\n```\n\nTo check the code quality before creating a pull request, one might run the script [show_report.sh](https://github.com/inpefess/isabelle-client/blob/master/show_report.sh). It locally does nearly the same as the CI pipeline after the PR is created.\n\n# Reporting issues or problems with the software\n\nQuestions and bug reports are welcome on [the tracker](https://github.com/inpefess/isabelle-client/issues). \n\n# More documentation\n\nMore documentation can be found [here](https://isabelle-client.readthedocs.io/en/latest).\n\n# Video example\n\n![video tutorial](https://github.com/inpefess/isabelle-client/blob/master/examples/tty.gif).\n\n# How to cite\n\nIf you're writing a research paper, you can cite Isabelle client (and Isabelle 2021) using the [following DOI](https://doi.org/10.1007/978-3-030-81097-9\\_20).\n",
    'author': 'Boris Shminke',
    'author_email': 'boris@shminke.ml',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/inpefess/isabelle-client',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
