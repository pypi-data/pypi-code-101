# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tracerepo']

package_data = \
{'': ['*']}

install_requires = \
['fractopo>=0.1.0,<0.2.0',
 'json5>=0.9.6,<0.10.0',
 'nialog>=0.0.1,<0.0.2',
 'pandas',
 'pandera',
 'pydantic>=1.8.2,<2.0.0',
 'pyproj>=3.1,<3.2',
 'rich>=10.7.0,<11.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{'coverage': ['coverage>=5.0,<6.0', 'coverage-badge'],
 'docs': ['sphinx',
          'sphinx-rtd-theme',
          'nbsphinx',
          'sphinx-gallery',
          'sphinx-autodoc-typehints'],
 'format-lint': ['sphinx',
                 'pylint',
                 'rstcheck',
                 'black',
                 'black-nb',
                 'blacken-docs',
                 'blackdoc',
                 'isort'],
 'typecheck': ['mypy']}

entry_points = \
{'console_scripts': ['tracerepo = tracerepo.cli:app']}

setup_kwargs = {
    'name': 'tracerepo',
    'version': '0.0.4',
    'description': 'Fracture & lineament data management.',
    'long_description': 'Documentation\n=============\n\n|Documentation Status| |PyPI Status| |CI Test| |Coverage|\n\nRunning tests\n-------------\n\nTo run pytest in currently installed environment:\n\n.. code:: bash\n\n   poetry run pytest\n\nTo run full extensive test suite:\n\n.. code:: bash\n\n   poetry run invoke test\n\nFormatting and linting\n----------------------\n\nFormatting and linting is done with a single command. First formats,\nthen lints.\n\n.. code:: bash\n\n   poetry run invoke format-and-lint\n\nBuilding docs\n-------------\n\nDocs can be built locally to test that ``ReadTheDocs`` can also build them:\n\n.. code:: bash\n\n   poetry run invoke docs\n\nInvoke usage\n------------\n\nTo list all available commands from ``tasks.py``:\n\n.. code:: bash\n\n   poetry run invoke --list\n\nDevelopment\n~~~~~~~~~~~\n\nDevelopment dependencies include:\n\n   -  invoke\n   -  nox\n   -  copier\n   -  pytest\n   -  coverage\n   -  sphinx\n\nBig thanks to all maintainers of the above packages!\n\nLicense\n~~~~~~~\n\nCopyright © 2021, Nikolas Ovaskainen.\n\n\n.. |Documentation Status| image:: https://readthedocs.org/projects/tracerepo/badge/?version=latest\n   :target: https://tracerepo.readthedocs.io/en/latest/?badge=latest\n.. |PyPI Status| image:: https://img.shields.io/pypi/v/tracerepo.svg\n   :target: https://pypi.python.org/pypi/tracerepo\n.. |CI Test| image:: https://github.com/nialov/tracerepo/workflows/test-and-publish/badge.svg\n   :target: https://github.com/nialov/tracerepo/actions/workflows/test-and-publish.yaml?query=branch%3Amaster\n.. |Coverage| image:: https://raw.githubusercontent.com/nialov/tracerepo/master/docs_src/imgs/coverage.svg\n   :target: https://github.com/nialov/tracerepo/blob/master/docs_src/imgs/coverage.svg\n',
    'author': 'nialov',
    'author_email': 'nikolasovaskainen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nialov/tracerepo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
