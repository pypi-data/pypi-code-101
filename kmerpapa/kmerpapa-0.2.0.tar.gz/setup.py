# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kmerpapa', 'kmerpapa.algorithms']

package_data = \
{'': ['*']}

install_requires = \
['numba>=0.54.1,<0.55.0', 'numpy>=1.17,<1.21', 'scipy>=1.7.1,<2.0.0']

entry_points = \
{'console_scripts': ['kmerpapa = kmerpapa.cli:main']}

setup_kwargs = {
    'name': 'kmerpapa',
    'version': '0.2.0',
    'description': 'Tool to calculate a k-mer pattern partition from position specific k-mer counts.',
    'long_description': '# kmerPaPa\n\nTool to calculate a "k-mer pattern partition" from position specific k-mer counts. This can for instance be used to train a mutation rate model.\n\n## Requirements\n\nkmerPaPa requires Python 3.7 or above.\n\n## Installation\n\n\n## Usage\nIf we want to train a mutation rate model then the input data should specifiy the number of times each k-mer is observed mutated and unmutated. One option is to have one file with the mutated k-mer counts (positive) and one file with the count of k-mers in the whole genome (background).  We can then run kmerpapa like this:\n```\nkmerpapa --positive test_data/mutated_5mers.txt --background test_data/background_5mers.txt --penalty_values 3 5 7\n```\nThe above command will first use cross validation to find the best penalty value between the values 3,5 and 7. Then it will find the optimal k-mer patter partiton using that penalty value.\nIf both a list of penalty values and a list of pseudo-counts are specified then all combinations of values will be tested during cross validation:\n```\nkmerpapa --positive test_data/mutated_5mers.txt --background test_data/background_5mers.txt --penalty_values 3 5 6 --pseudo_counts 0.5 1 10\n```',
    'author': 'Søren Besenbacher',
    'author_email': 'besenbacher@clin.au.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/besenbacher/kmerpapa',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
