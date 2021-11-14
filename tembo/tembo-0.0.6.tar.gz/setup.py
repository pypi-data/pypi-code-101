# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tembo', 'tembo.cli', 'tembo.journal', 'tembo.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.2,<4.0.0',
 'click>=8.0.3,<9.0.0',
 'panaetius>=2.3.2,<3.0.0',
 'pendulum>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['tembo = tembo.cli.cli:main']}

setup_kwargs = {
    'name': 'tembo',
    'version': '0.0.6',
    'description': 'A simple folder organiser for your work notes.',
    'long_description': '# Tembo\n\n<center>\n    <img\n        src="https://raw.githubusercontent.com/tembo-pages/tembo-core/main/assets/tembo_logo.png"\n        width="200px"\n    />\n</center>\n\nA simple folder organiser for your work notes.\n',
    'author': 'dtomlinson',
    'author_email': 'dtomlinson@panaetius.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tembo-pages.github.io/tembo-core/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
