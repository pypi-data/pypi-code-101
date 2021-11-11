# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['settings_doc']

package_data = \
{'': ['*'], 'settings_doc': ['templates/*']}

install_requires = \
['Jinja2>=3.0.2,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['settings-doc = settings_doc.main:app']}

setup_kwargs = {
    'name': 'settings-doc',
    'version': '0.4.0',
    'description': 'A command line tool for generating Markdown documentation and .env files from pydantic BaseSettings.',
    'long_description': '<h1 align="center" style="border-bottom: none;">:gear::memo:&nbsp;&nbsp; Settings DocGen &nbsp;&nbsp;:memo::gear:</h1>\n<h3 align="center">A command line tool for generating Markdown documentation and .env files from <a href="https://pydantic-docs.helpmanual.io/usage/settings">pydantic.BaseSettings</a>.</h3>\n\n<p align="center">\n    <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/radeklat/settings-doc">\n    <img alt="Codecov" src="https://img.shields.io/codecov/c/github/radeklat/settings-doc">\n    <img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/radeklat/settings-doc">\n    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/2021">\n    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/radeklat/settings-doc">\n    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/settings-doc">\n    <img alt="PyPI - License" src="https://img.shields.io/pypi/l/settings-doc">\n    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/settings-doc">\n</p>\n\n# Installation\n\n```\npip install settings-doc\n```\n\n# TODOs\n\n- Improve this README\n  - Add usage instructions\n  - Add features overview\n- Add an update flag to update existing documents between two marks\n',
    'author': 'Radek Lát',
    'author_email': 'radek.lat@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/radeklat/settings-doc',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
