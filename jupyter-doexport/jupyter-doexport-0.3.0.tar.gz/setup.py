# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jupyter_doexport']

package_data = \
{'': ['*'],
 'jupyter_doexport': ['templates/dofile/*', 'templates/dofile_output/*']}

install_requires = \
['nbconvert>=6.3.0,<7.0.0']

setup_kwargs = {
    'name': 'jupyter-doexport',
    'version': '0.3.0',
    'description': 'A package to convert jupyter notebooks to Stata do-files',
    'long_description': None,
    'author': 'Aleksandr Michuda',
    'author_email': 'amichuda@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
