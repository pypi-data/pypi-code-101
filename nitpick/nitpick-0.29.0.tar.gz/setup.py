# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nitpick', 'nitpick.plugins', 'nitpick.style', 'nitpick.style.fetchers']

package_data = \
{'': ['*']}

install_requires = \
['ConfigUpdater',
 'attrs',
 'autorepr',
 'cachy',
 'click',
 'dictdiffer',
 'flake8>=3.0.0',
 'identify',
 'jmespath',
 'loguru',
 'marshmallow-polyfield>=5.10,<6.0',
 'marshmallow>=3.0.0b10',
 'more-itertools',
 'pluggy',
 'pydantic',
 'python-slugify',
 'requests',
 'ruamel.yaml',
 'sortedcontainers',
 'toml',
 'tomlkit']

extras_require = \
{':python_version >= "3.6" and python_version < "3.9"': ['importlib-resources'],
 'doc': ['sphinx', 'sphinx_rtd_theme', 'sphobjinv'],
 'lint': ['pylint'],
 'test': ['pytest',
          'pytest-cov',
          'testfixtures',
          'freezegun',
          'responses',
          'pytest-testmon',
          'pytest-watch',
          'pytest-socket']}

entry_points = \
{'console_scripts': ['nitpick = nitpick.cli:nitpick_cli'],
 'flake8.extension': ['NIP = nitpick.flake8:NitpickFlake8Extension'],
 'nitpick': ['ini = nitpick.plugins.ini',
             'json = nitpick.plugins.json',
             'pre_commit = nitpick.plugins.pre_commit',
             'text = nitpick.plugins.text',
             'toml = nitpick.plugins.toml']}

setup_kwargs = {
    'name': 'nitpick',
    'version': '0.29.0',
    'description': 'Enforce the same settings across multiple language-independent projects',
    'long_description': 'Nitpick\n=======\n\n|PyPI|\n|GitHub Actions Python Workflow|\n|Documentation Status|\n|Coveralls|\n|Maintainability|\n|Test Coverage|\n|Supported Python versions|\n|Project License|\n|Code style: black|\n|Renovate|\n|semantic-release|\n|pre-commit.ci status|\n|FOSSA Status|\n\nCommand-line tool and `flake8 <https://github.com/PyCQA/flake8>`__\nplugin to enforce the same settings across multiple language-independent\nprojects.\n\nUseful if you maintain multiple projects and are tired of\ncopying/pasting the same INI/TOML/YAML/JSON keys and values over and\nover, in all of them.\n\nThe CLI now has a ``nitpick fix`` command that modifies configuration\nfiles directly (pretty much like\n`black <https://github.com/psf/black>`__ and\n`isort <https://github.com/PyCQA/isort>`__ do with Python files).\nSee the `CLI docs for more\ninfo <https://nitpick.rtfd.io/en/latest/cli.html>`__.\n\nMany more features are planned for the future, check `the\nroadmap <https://github.com/andreoliwa/nitpick/projects/1>`__.\n\nStyle file\n----------\n\nA "nitpick code style" is a `TOML <https://github.com/toml-lang/toml>`__\nfile with the settings that should be present in config files from other\ntools.\n\nExample of a style:\n\n.. code-block:: toml\n\n    ["pyproject.toml".tool.black]\n    line-length = 120\n\n    ["pyproject.toml".tool.poetry.dev-dependencies]\n    pylint = "*"\n\n    ["setup.cfg".flake8]\n    ignore = "D107,D202,D203,D401"\n    max-line-length = 120\n    inline-quotes = "double"\n\n    ["setup.cfg".isort]\n    line_length = 120\n    multi_line_output = 3\n    include_trailing_comma = true\n    force_grid_wrap = 0\n    combine_as_imports = true\n\nThis style will assert that:\n\n-  ... `black <https://github.com/psf/black>`__,\n   `isort <https://github.com/PyCQA/isort>`__ and\n   `flake8 <https://github.com/PyCQA/flake8>`__ have a line length of\n   120;\n-  ... `flake8 <https://github.com/PyCQA/flake8>`__ and\n   `isort <https://github.com/PyCQA/isort>`__ are configured as above in\n   ``setup.cfg``;\n-  ... `Pylint <https://www.pylint.org>`__ is present as a\n   `Poetry <https://github.com/python-poetry/poetry>`__ dev dependency\n   in ``pyproject.toml``.\n\nSupported file types\n--------------------\n\nThese are the file types currently handled by Nitpick.\n\n-  Some files are only being checked and have to be modified manually;\n-  Some files can already be fixed automatically (with the\n   ``nitpick fix`` command);\n-  Others are still under construction; the ticket numbers are shown in\n   the table (upvote the ticket with 👍🏻 if you would like to prioritise\n   development).\n\nImplemented\n~~~~~~~~~~~\n\n.. auto-generated-start-implemented\n.. list-table::\n   :header-rows: 1\n\n   * - File type\n     - ``nitpick check``\n     - ``nitpick fix``\n   * - `Any INI file <https://nitpick.rtfd.io/en/latest/plugins.html#ini-files>`_\n     - ✅\n     - ✅\n   * - `Any JSON file <https://nitpick.rtfd.io/en/latest/plugins.html#json-files>`_\n     - ✅\n     - `#358 <https://github.com/andreoliwa/nitpick/issues/358>`_ 🚧\n   * - `Any text file <https://nitpick.rtfd.io/en/latest/plugins.html#text-files>`_\n     - ✅\n     - ❌\n   * - `Any TOML file <https://nitpick.rtfd.io/en/latest/plugins.html#toml-files>`_\n     - ✅\n     - ✅\n   * - `.editorconfig <https://nitpick.rtfd.io/en/latest/examples.html#example-editorconfig>`_\n     - ✅\n     - ✅\n   * - `package.json <https://nitpick.rtfd.io/en/latest/examples.html#example-package-json>`_\n     - ✅\n     - `#358 <https://github.com/andreoliwa/nitpick/issues/358>`_ 🚧\n   * - `.pre-commit-config.yaml <https://nitpick.rtfd.io/en/latest/plugins.html#pre-commit-config-yaml>`_\n     - ✅\n     - `#282 <https://github.com/andreoliwa/nitpick/issues/282>`_ 🚧\n   * - `.pylintrc <https://nitpick.rtfd.io/en/latest/plugins.html#ini-files>`_\n     - ✅\n     - ✅\n   * - `pyproject.toml <https://nitpick.rtfd.io/en/latest/plugins.html#toml-files>`_\n     - ✅\n     - ✅\n   * - `requirements.txt <https://nitpick.rtfd.io/en/latest/plugins.html#text-files>`_\n     - ✅\n     - ❌\n   * - `setup.cfg <https://nitpick.rtfd.io/en/latest/plugins.html#ini-files>`_\n     - ✅\n     - ✅\n.. auto-generated-end-implemented\n\nPlanned\n~~~~~~~\n\n.. auto-generated-start-planned\n.. list-table::\n   :header-rows: 1\n\n   * - File type\n     - ``nitpick check``\n     - ``nitpick fix``\n   * - Any Markdown file\n     - `#280 <https://github.com/andreoliwa/nitpick/issues/280>`_ 🚧\n     - ❓\n   * - Any Terraform file\n     - `#318 <https://github.com/andreoliwa/nitpick/issues/318>`_ 🚧\n     - ❓\n   * - Dockerfile\n     - `#272 <https://github.com/andreoliwa/nitpick/issues/272>`_ 🚧\n     - `#272 <https://github.com/andreoliwa/nitpick/issues/272>`_ 🚧\n   * - .dockerignore\n     - `#8 <https://github.com/andreoliwa/nitpick/issues/8>`_ 🚧\n     - `#8 <https://github.com/andreoliwa/nitpick/issues/8>`_ 🚧\n   * - .gitignore\n     - `#8 <https://github.com/andreoliwa/nitpick/issues/8>`_ 🚧\n     - `#8 <https://github.com/andreoliwa/nitpick/issues/8>`_ 🚧\n   * - Jenkinsfile\n     - `#278 <https://github.com/andreoliwa/nitpick/issues/278>`_ 🚧\n     - ❓\n   * - Makefile\n     - `#277 <https://github.com/andreoliwa/nitpick/issues/277>`_ 🚧\n     - ❓\n   * - .travis.yml\n     - `#15 <https://github.com/andreoliwa/nitpick/issues/15>`_ 🚧\n     - `#15 <https://github.com/andreoliwa/nitpick/issues/15>`_ 🚧\n.. auto-generated-end-planned\n\nQuickstart\n----------\n\nInstall\n~~~~~~~\n\nInstall in an isolated global environment with\n`pipx <https://github.com/pipxproject/pipx>`__::\n\n    # Latest PyPI release\n    pipx install nitpick\n\n    # Development branch from GitHub\n    pipx install git+https://github.com/andreoliwa/nitpick\n\nOn macOS/Linux, install with\n`Homebrew <https://github.com/Homebrew/brew>`__::\n\n    # Latest PyPI release\n    brew install andreoliwa/formulae/nitpick\n\n    # Development branch from GitHub\n    brew install andreoliwa/formulae/nitpick --HEAD\n\nOn Arch Linux, install with yay::\n\n    yay -Syu nitpick\n\nAdd to your project with\n`Poetry <https://github.com/python-poetry/poetry>`__::\n\n    poetry add --dev nitpick\n\nOr install it with pip::\n\n    pip install -U nitpick\n\nRun\n~~~\n\nTo fix and modify your files directly::\n\n    nitpick fix\n\nTo check for errors only::\n\n    nitpick check\n\nNitpick is also a ``flake8`` plugin, so you can run this on a project\nwith at least one Python (``.py``) file::\n\n    flake8 .\n\nNitpick will download and use the opinionated `default style\nfile <https://github.com/andreoliwa/nitpick/blob/v0.29.0/nitpick-style.toml>`__.\n\nYou can use it as a template to configure your own style.\n\nRun as a pre-commit hook\n~~~~~~~~~~~~~~~~~~~~~~~~\n\nIf you use `pre-commit <https://pre-commit.com/>`__ on your project, add\nthis to the ``.pre-commit-config.yaml`` in your repository::\n\n    repos:\n      - repo: https://github.com/andreoliwa/nitpick\n        rev: v0.29.0\n        hooks:\n          - id: nitpick\n\nThere are 3 available hook IDs: ``nitpick``, ``nitpick-fix``, ``nitpick-check``.\n\nMore information\n----------------\n\nNitpick is being used by projects such as:\n\n-  `wemake-services/wemake-python-styleguide <https://github.com/wemake-services/wemake-python-styleguide>`__\n-  `dry-python/returns <https://github.com/dry-python/returns>`__\n-  `sobolevn/django-split-settings <https://github.com/sobolevn/django-split-settings>`__\n-  `catalyst-team/catalyst <https://github.com/catalyst-team/catalyst>`__\n-  `alan-turing-institute/AutSPACEs <https://github.com/alan-turing-institute/AutSPACEs>`__\n-  `pytest-dev/pytest-mimesis <https://github.com/pytest-dev/pytest-mimesis>`__\n\nFor more details on styles and which configuration files are currently\nsupported, `see the full documentation <https://nitpick.rtfd.io/>`__.\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/nitpick.svg\n   :target: https://pypi.org/project/nitpick\n.. |GitHub Actions Python Workflow| image:: https://github.com/andreoliwa/nitpick/workflows/Python/badge.svg\n.. |Documentation Status| image:: https://readthedocs.org/projects/nitpick/badge/?version=latest\n   :target: https://nitpick.rtfd.io/en/latest/?badge=latest\n.. |Coveralls| image:: https://coveralls.io/repos/github/andreoliwa/nitpick/badge.svg\n   :target: https://coveralls.io/github/andreoliwa/nitpick\n.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/61e0cdc48e24e76a0460/maintainability\n   :target: https://codeclimate.com/github/andreoliwa/nitpick\n.. |Test Coverage| image:: https://api.codeclimate.com/v1/badges/61e0cdc48e24e76a0460/test_coverage\n   :target: https://codeclimate.com/github/andreoliwa/nitpick\n.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/nitpick.svg\n   :target: https://pypi.org/project/nitpick/\n.. |Project License| image:: https://img.shields.io/pypi/l/nitpick.svg\n   :target: https://pypi.org/project/nitpick/\n.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n.. |Renovate| image:: https://img.shields.io/badge/renovate-enabled-brightgreen.svg\n   :target: https://renovatebot.com/\n.. |semantic-release| image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg\n   :target: https://github.com/semantic-release/semantic-release\n.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/andreoliwa/nitpick/develop.svg\n   :target: https://results.pre-commit.ci/latest/github/andreoliwa/nitpick/develop\n.. |FOSSA Status| image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2Fandreoliwa%2Fnitpick.svg?type=shield\n   :target: https://app.fossa.com/projects/git%2Bgithub.com%2Fandreoliwa%2Fnitpick?ref=badge_shield\n\nContributing\n------------\n\nYour help is very much appreciated.\n\nThere are many possibilities for new features in this project, and not enough time or hands to work on them.\n\nIf you want to contribute with the project, set up your development environment following the steps on the `contribution guidelines <https://nitpick.rtfd.io/en/latest/contributing.html>`_ and send your pull request.\n',
    'author': 'W. Augusto Andreoli',
    'author_email': 'andreoliwa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/andreoliwa/nitpick',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
