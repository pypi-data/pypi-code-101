# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ci_plumber', 'ci_plumber.docs', 'ci_plumber.helpers', 'ci_plumber.templates']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.20,<4.0.0',
 'framework-detector>=0.2.1,<0.3.0',
 'importlib-metadata>=4.6.3,<5.0.0',
 'openshift>=0.12.1,<0.13.0',
 'python-gitlab>=2.10.0,<3.0.0',
 'rich>=10.7.0,<11.0.0',
 'typer[all]>=0.3.2,<0.4.0',
 'types-requests>=2.25.2,<3.0.0']

extras_require = \
{'all': ['ci-plumber-openshift>=0.3.1,<0.4.0',
         'ci-plumber-gitlab>=0.1.3,<0.2.0',
         'ci-plumber-azure>=0.2.3,<0.3.0']}

entry_points = \
{'console_scripts': ['ci-plumber = ci_plumber.main:app']}

setup_kwargs = {
    'name': 'ci-plumber',
    'version': '1.4.2',
    'description': 'Plumb together different CI/CD services',
    'long_description': '# CI Plumber\n\n[![CodeFactor](https://www.codefactor.io/repository/github/pbexe/ci-plumber/badge)](https://www.codefactor.io/repository/github/pbexe/ci-plumber) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ci-plumber) ![PyPI](https://img.shields.io/pypi/v/ci-plumber) ![PyPI - Downloads](https://img.shields.io/pypi/dm/ci-plumber) [![python-app](https://github.com/pbexe/ci-plumber/actions/workflows/python-app.yml/badge.svg)](https://github.com/pbexe/ci-plumber/actions/workflows/python-app.yml) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5545987.svg)](https://doi.org/10.5281/zenodo.5545987)\n\n\nA tool to create and configure all of the stages of a CI/CD pipeline.\n\nCurrent integrations:\n- Gitlab\n- Gitlab pipelines\n- Azure App Service\n- Azure Image Registry\n- Azure MariaDB\n- Openshift\n- Openshift MariaDB\n\nFull documentation is available [here](https://milesbudden.com/ci-plumber/).\n\n## Installation\n\n```sh\npip install ci-plumber[all]\n```\n\n### Requirements\n\n- `oc` CLI tool\n- `az` CLI tool\n\n## Usage\n\n### GitLab\n```sh\n# Initialise the project\nci-plumber gitlab init\n```\n\n### OpenShift\n\n```sh\n# Deploy from the current docker registry to OpenShift\nci-plumber openshift deploy\n\n# Create a new DB and store the credentials in maria.env\nci-plumber openshift create-db\n```\n\n### Azure\n\n```sh\n# Log in to Azure\nci-plumber azure login\n\n# List your Azure subscriptions\nci-plumber azure list-subscriptions\n\n# Set the subscription to use\nci-plumber azure set-default-subscription\n\n# Create a docker registry\nci-plumber azure create-registry\n\n# Trigger a build and push\ngit add .\ngit commit -m "Added Azure CI file"\ngit tag -a v1.0.0 -m "Version 1.0.0"\ngit push --follow-tags\n\n# Deploy to Azure\nci-plumber azure create-app\n\n# Create a database and store the credentials in maria.env\nci-plumber azure create-db\n```\n\n## Developing\n\n### Installation\n```sh\n# Install dependencies\n$ poetry install\n$ poetry shell\n\n# Install git hooks\n$ pre-commit install\n$ pre-commit autoupdate\n$ pre-commit run --all-files\n\n# Symlink the plugins back to the main project\n$ ln -s ./plugins/example/ci_plumber_example/ ./ci_plumber_example\n$ ln -s ./plugins/gitlab/ci_plumber_gitlab/ ./ci_plumber_gitlab\n$ ln -s ./plugins/openshift/ci_plumber_openshift/ ./ci_plumber_openshift\n$ ln -s ./plugins/azure/ci_plumber_azure/ ./ci_plumber_azure\n```\n\n### Features\n\n- Runs checks on commit\n    - Flake8\n    - Black\n    - pre-commit-hooks checks\n    - mypy\n    - isort\n- Installable as a script\n',
    'author': 'Miles Budden',
    'author_email': 'git@miles.so',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pbexe/ci-plumber',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
