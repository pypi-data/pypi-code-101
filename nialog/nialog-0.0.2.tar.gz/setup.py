# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nialog']

package_data = \
{'': ['*']}

install_requires = \
['python-json-logger>=2.0.2,<3.0.0']

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

setup_kwargs = {
    'name': 'nialog',
    'version': '0.0.2',
    'description': 'JSON logging setup for Python.',
    'long_description': 'Documentation\n=============\n\n|Documentation Status| |PyPI Status| |CI Test| |Coverage|\n\nIntroduction\n------------\n\nSimple package/script to setup ``JSON`` logging for a Python app or script.\nUses `python-json-logger <https://github.com/madzak/python-json-logger>`__ and\nis mostly just a wrapper around it. Instead of adding this script to every\nPython module that I/you create you can just add this as a dependency and call:\n\n.. code:: python\n\n   from nialog import setup_module_logging, LoggingLevel\n\n   # Default logging level is WARNING\n   setup_module_logging()\n\n   # LoggingLevel has enums for default logging module levels\n   # Can be used with e.g. typer as command-line inputs\n   LoggingLevel.DEBUG.value == "DEBUG"  # = True\n\nRunning tests\n-------------\n\nTo run pytest in currently installed environment:\n\n.. code:: bash\n\n   poetry run pytest\n\nTo run test suite best suited for before pushing to e.g. GitHub.\n\n.. code:: bash\n\n   poetry run invoke prepush\n\nTo run full extensive test suite:\n\n.. code:: bash\n\n   poetry run invoke test\n\nFormatting and linting\n----------------------\n\nFormatting and linting is done with a single command. First formats,\nthen lints.\n\n.. code:: bash\n\n   poetry run invoke format-and-lint\n\nBuilding docs\n-------------\n\nDocs can be built locally to test that ``ReadTheDocs`` can also build them:\n\n.. code:: bash\n\n   poetry run invoke docs\n\nInvoke usage\n------------\n\nTo list all available commands from ``tasks.py``:\n\n.. code:: bash\n\n   poetry run invoke --list\n\nDevelopment\n~~~~~~~~~~~\n\nDevelopment dependencies include:\n\n   -  invoke\n   -  nox\n   -  copier\n   -  pytest\n   -  coverage\n   -  sphinx\n\nBig thanks to all maintainers of the above packages!\n\nLicense\n~~~~~~~\n\nCopyright © 2021, Nikolas Ovaskainen.\n\n\n.. |Documentation Status| image:: https://readthedocs.org/projects/nialog/badge/?version=latest\n   :target: https://nialog.readthedocs.io/en/latest/?badge=latest\n.. |PyPI Status| image:: https://img.shields.io/pypi/v/nialog.svg\n   :target: https://pypi.python.org/pypi/nialog\n.. |CI Test| image:: https://github.com/nialov/nialog/workflows/test-and-publish/badge.svg\n   :target: https://github.com/nialov/nialog/actions/workflows/test-and-publish.yaml?query=branch%3Amaster\n.. |Coverage| image:: https://raw.githubusercontent.com/nialov/nialog/master/docs_src/imgs/coverage.svg\n   :target: https://github.com/nialov/nialog/blob/master/docs_src/imgs/coverage.svg\n',
    'author': 'nialov',
    'author_email': 'nikolasovaskainen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nialov/nialog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
