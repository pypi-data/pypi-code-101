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
    'version': '0.3.5',
    'description': 'A package to convert jupyter notebooks to Stata do-files',
    'long_description': '======================\nStata Do File Exporter\n======================\n\n\nStata Do File Exporter provides a context menu and template for exporting a jupyter notebook with Stata kernel, to a do-file with all markdown and code ready to be executed at the Stata GUI or console.\n\nTo install the exporter, write:\n\n``pip install jupyter-doexport``\n\nYour jupyter notebook should not be available for export from the  ``File ->  Download as`` menu.\n\nCurrently, translation of stata_kernel magics are not supported.\n\nThanks also to\n--------------\n\nKyle Barron for an amazing Stata kernel implementation.\nYou can see how to install it `here <https://kylebarron.github.io/stata_kernel/>`_.\n\n\n\n',
    'author': 'Aleksandr Michuda',
    'author_email': 'amichuda@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/amichuda/jupyter-doexport',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
