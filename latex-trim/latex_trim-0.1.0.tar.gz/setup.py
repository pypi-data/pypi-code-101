# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['latex_trim']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0', 'pdf2image>=1.16.0,<2.0.0']

entry_points = \
{'console_scripts': ['latex_trim = latex_trim.latex_trim:run']}

setup_kwargs = {
    'name': 'latex-trim',
    'version': '0.1.0',
    'description': 'Tool that allows you to include sub-selections of PDFs in latex documents.',
    'long_description': None,
    'author': 'Oliver Rausch',
    'author_email': 'oliverrausch99@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
