# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['viecpro_vis', 'viecpro_vis.migrations']

package_data = \
{'': ['*'],
 'viecpro_vis': ['static/vis/css/*', 'static/vis/js/*', 'templates/*']}

install_requires = \
['apis-core>=0.16.33,<0.17.0']

setup_kwargs = {
    'name': 'viecpro-vis',
    'version': '0.1.5',
    'description': 'Django-App providing visualisations for the APIS-VieCPro instance.',
    'long_description': None,
    'author': 'Gregor Pirgie',
    'author_email': 'gregor.pirgie@univie.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
