# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chainsail_helpers',
 'chainsail_helpers.pdf',
 'chainsail_helpers.pdf.pymc3',
 'chainsail_helpers.pdf.stan']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.2,<2.0.0']

extras_require = \
{'pymc3': ['pymc3>=3.11.4,<4.0.0'], 'stan': ['requests>=2.26.0,<3.0.0']}

setup_kwargs = {
    'name': 'chainsail-helpers',
    'version': '0.1.0',
    'description': 'Probability distribution interfaces, examples, and utilities for the Chainsail sampling service',
    'long_description': "# Chainsail PDF interfaces and utilities\n\nThis small package complements the [Chainsail](https://chainsail.io) sampling service. It\n- defines the general interface for objects representing Chainsail-consumable probability distributions,\n- provides implementations thereof for popular probabilistic programming languages,\n- and contains a few helper scripts for post-processing.\n\n## Installation\nThis package requires a few Python dependencies.\nBest use [Poetry](https://python-poetry.org) to install them and develop your own probability density implementation: run\n```bash\n$ poetry install\n$ poetry shell\n```\nand you will be dropped into a virtual environment with these dependencies installed.\nIf you'd like implement a probability density using [Stan](https://mc-stan.org) or [PyMC3](https://docs.pymc.io), install the corresponding extra dependencies like so: `poetry install --extras pymc3` and similarly for `stan`. \nWhen using Chainsail, this package will be automatically installed, so no need to add it to the list of dependencies in the job submission form.\n\n## Contributing\nContributions, for example PDF implementations for other probabilistic programming languages, are highly welcome!\nJust open a pull request and we'll be happy to work with you to make Chainsail even more useful.\n\n## License\n&copy; 2021 [Tweag](https://tweag.io). `chainsail_helpers` is open-source software and licensed under the [MIT license](https://opensource.org/licenses/MIT).\n",
    'author': 'Simeon Carstens',
    'author_email': 'simeon.carstens@tweag.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tweag/chainsail-resources',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
