# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyprojectify']

package_data = \
{'': ['*']}

install_requires = \
['Click>=8.0.3,<9.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyprojectify',
    'version': '0.3.1',
    'description': 'pyprojectify is a utility allowing python package authors/maintainers/packagers to painlessly migrate their package from setup.py to the new pyproject.toml.',
    'long_description': '============\npyprojectify\n============\n\n\n.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg\n        :target: https://GitHub.com/SekouDiaoNlp/pyprojectify/graphs/commit-activity\n        :alt: Package Maintenance Status\n\n.. image:: https://img.shields.io/badge/maintainer-SekouDiaoNlp-blue\n        :target: https://GitHub.com/SekouDiaoNlp/pyprojectify\n        :alt: Package Maintener\n\n.. image:: https://img.shields.io/github/checks-status/SekouDiaoNlp/mlconjug3/master?label=Build%20status%20on%20Windows%2C%20MacOs%20and%20Linux\n        :target: https://github.com/SekouDiaoNlp/pyprojectify/actions/workflows/main.yml\n        :alt: Build status on Windows, MacOs and Linux\n\n.. image:: https://img.shields.io/pypi/v/pyprojectify.svg\n        :target: https://pypi.python.org/pypi/pyprojectify\n        :alt: Pypi Python Package Index Status\n\n..\n    image:: https://anaconda.org/conda-forge/pyprojectify/badges/version.svg\n        :target: https://anaconda.org/conda-forge/pyprojectify\n        :alt: Anaconda Package Index Status\n\n.. image:: https://img.shields.io/pypi/pyversions/pyprojectify\n        :target: https://pypi.python.org/pypi/pyprojectify\n        :alt: Compatible Python versions\n\n..\n    image:: https://img.shields.io/conda/pn/conda-forge/pyprojectify?color=dark%20green&label=Supported%20platforms\n        :target: https://anaconda.org/conda-forge/pyprojectify\n        :alt: Supported platforms\n\n.. image:: https://readthedocs.org/projects/pyprojectify/badge/?version=latest\n        :target: https://pyprojectify.readthedocs.io/en/latest\n        :alt: Documentation Status\n\n.. image:: https://pyup.io/repos/github/SekouDiaoNlp/pyprojectify/shield.svg\n        :target: https://pyup.io/repos/github/SekouDiaoNlp/pyprojectify/\n        :alt: Dependencies status\n\n.. image:: https://codecov.io/gh/SekouDiaoNlp/pyprojectify/branch/master/graph/badge.svg?token=EiEXyUJGpF\n        :target: https://codecov.io/gh/SekouDiaoNlp/pyprojectify\n        :alt: Code Coverage Status\n\n.. image:: https://snyk-widget.herokuapp.com/badge/pip/pyprojectify/badge.svg\n        :target: https://snyk.io/test/github/SekouDiaoNlp/pyprojectify?targetFile=requirements.txt\n        :alt: Code Vulnerability Status\n\n.. image:: https://img.shields.io/pypi/dm/pyprojectify?label=PyPi%20Downloads\n        :target: https://pypi.org/project/pyprojectify/\n        :alt: PyPI Downloads\n\n..\n    image:: https://img.shields.io/conda/dn/conda-forge/pyprojectify?label=Anaconda%20Total%20Downloads\n        :target: https://anaconda.org/conda-forge/pyprojectify\n        :alt: Conda\n\n\n\n\n\n\npyprojectify is a utility allowing python package authors/maintainers/packagers to painlessly migrate their package from setup.py to the new pyproject.toml.\n\n\n* Free software: MIT license\n* Documentation: https://pyprojectify.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage\n',
    'author': 'Sekou Diao',
    'author_email': 'diao.sekou.nlp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
