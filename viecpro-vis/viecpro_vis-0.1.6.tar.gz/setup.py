# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['viecpro_vis', 'viecpro_vis.migrations']

package_data = \
{'': ['*'],
 'viecpro_vis': ['static/vis/css/*', 'static/vis/js/*', 'templates/*']}

setup_kwargs = {
    'name': 'viecpro-vis',
    'version': '0.1.6',
    'description': 'Django-App providing visualisations for the APIS-VieCPro instance.',
    'long_description': None,
    'author': 'Gregor Pirgie',
    'author_email': 'gregor.pirgie@univie.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
