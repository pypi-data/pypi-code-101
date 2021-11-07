# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sqlfmt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata']}

entry_points = \
{'console_scripts': ['sqlfmt = sqlfmt.cli:sqlfmt']}

setup_kwargs = {
    'name': 'shandy-sqlfmt',
    'version': '0.1.0a3',
    'description': 'sqlfmt is an opinionated CLI tool that formats your sql files',
    'long_description': None,
    'author': 'Ted Conbeer',
    'author_email': 'ted@shandy.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
