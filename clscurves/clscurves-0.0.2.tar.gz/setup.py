# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clscurves', 'clscurves.plotter', 'clscurves.tests']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.2,<4.0.0',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'scipy>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'clscurves',
    'version': '0.0.2',
    'description': 'Compute and plot bootstrapped performance curves for classification problems.',
    'long_description': '# classification-curves',
    'author': 'Christopher Bryant',
    'author_email': 'cbryant@berkeley.edu',
    'maintainer': 'Christopher Bryant',
    'maintainer_email': 'cbryant@berkeley.edu',
    'url': 'https://github.com/chrismbryant/classification-curves',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
