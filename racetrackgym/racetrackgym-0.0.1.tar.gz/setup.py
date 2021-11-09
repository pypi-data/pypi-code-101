# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['racetrackgym', 'racetrackgym.maps.templates']

package_data = \
{'': ['*'],
 'racetrackgym': ['maps/*',
                  'maps/barto-big_scales/*',
                  'maps/barto-small_scales/*',
                  'maps/corner/*',
                  'maps/diverse/*',
                  'maps/nook/*',
                  'maps/potentials/*',
                  'maps/ring/*',
                  'maps/river/*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0',
 'argparse>=1.4.0,<2.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'numpy>=1.21.4,<2.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'rlmate>=0.0.9,<0.0.10']

setup_kwargs = {
    'name': 'racetrackgym',
    'version': '0.0.1',
    'description': 'tba',
    'long_description': '# racetrack\n\n',
    'author': 'Timo P. Gros',
    'author_email': 'timopgros@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
