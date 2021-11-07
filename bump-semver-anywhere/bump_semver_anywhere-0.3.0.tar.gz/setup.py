# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bump_semver_anywhere']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pytomlpp>=1.0.3,<2.0.0',
 'semver>=2.13.0,<3.0.0']

entry_points = \
{'console_scripts': ['bump_semver_anywhere = bump_semver_anywhere.cli:main']}

setup_kwargs = {
    'name': 'bump-semver-anywhere',
    'version': '0.3.0',
    'description': 'Bump your semantic version of any software using regex',
    'long_description': '# bump semver anywhere \n[![PyPI version](https://badge.fury.io/py/bump-semver-anywhere.svg)](https://badge.fury.io/py/bump-semver-anywhere)\n\nThis is a library intented to replace all semversion bumpers and finally be agnostic of the language / use case for your semantic versioning. This is achieved by providing the regex pattern to the place and filename of the string that contains the semantic version.\n\n## usage\n\n- install `pip install bump_semver_anywhere`\n- create a `bump_semver_anywhere.toml` in the root of your project (see _config example_) or run `bump_semver_anywhere init`\n- run `bump_semver_anywhere bump -p patch`\n\n```console\nHello there. Today I want to show you a library I have been working on. I was inspired by necessity of changing all the versions in every file: `pyproject.toml`, `__init__.py`, `docker-compose.yaml`, `package.json`, etc. I searched for packages that do this but either they are specific to the language (Python or Javascript) or I did not like the customization for it. At the end I decided to create `bump_semver_anywhere`. This is inspired in [bump2version](https://github.com/c4urself/bump2version/) but with a much simpler approach. It uses TOML for configuration.\n\n> This is a library intended to replace all semantic version bumpers and finally be agnostic of the language. This is achieved by providing the regex pattern to the place and filename of the string that contains the version.\n\nconfiguration example:\n```toml\n# bump_semver_anywhere.toml\n\n[general]\ncurrent_version = "0.1.2"\n\n[vcs]\ncommit = true\ncommit_msg = "release({part}): bump {current_version} -> {new_version}"\n\n[files]\n\n[files.python-module]\nfilename = "bump_semver_anywhere/__init__.py"\npattern = \'__version__ ?= ?"(.*?)"\'\n\n[files.python-pyproject]\nfilename = "pyproject.toml"\npattern = \'version ?= ?"(.*?)"\'\n```\n\nIt can be run as CLI `bump_semver_anywhere bump -p patch` or triggered via a Github action by commenting `/release patch`\n\n```console\n❯ python -m bump_semver_anywhere bump -p patch\n[-] Loading config from bump_semver_anywhere.toml and bumping patch\n[=] config loaded\n[ ] files to update\n • bump_semver_anywhere/__init__.py: 0.1.1\n • pyproject.toml: 0.1.1\n • bump_semver_anywhere.toml: 0.1.1\n[ ] VCS enabled with git\n[-] bumping patch version\n • bump_semver_anywhere/__init__.py -> 0.1.2\n • pyproject.toml -> 0.1.2\n • bump_semver_anywhere.toml -> 0.1.2\n[*] saving files to disk\n[*] staging\n[*] commiting: release(patch): bump 0.1.1 -> 0.1.2\nblack....................................................................Passed\nisort....................................................................Passed\nflake8...................................................................Passed\n[main 5092515] release(patch): bump 0.1.1 -> 0.1.2\n 3 files changed, 3 insertions(+), 3 deletions(-)\n[+] bye bye\n```\n\n\nPS: If you have any suggestions for changing the name to a much simpler one I will be grateful.\nPS2: I accept PR and any feedback.\n\n\n### cli\n\n```console\n❯ bump_semver_anywhere --help\nUsage: python -m bump_semver_anywhere [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  bump  Bump your semantic version of any software using regex\n  init  Initialize the config\n```\n\n```console\n❯ bump_semver_anywhere bump --help\nUsage: python -m bump_semver_anywhere bump [OPTIONS]\n\n  Bump your semantic version of any software using regex\n\nOptions:\n  -c, --config FILE               the config file  [default:\n                                  bump_semver_anywhere.toml]\n  -p, --part [major|minor|patch|prerelease]\n                                  the version part to bump  [required]\n  -n, --dry-run                   do not modify files\n  --help                          Show this message and exit.\n```\n\n```console\n❯ bump_semver_anywhere init --help\nUsage: python -m bump_semver_anywhere init [OPTIONS]\n\n  Initialize the config\n\nOptions:\n  -o, --output PATH  the output config file path  [default:\n                     bump_semver_anywhere.toml]\n  --help             Show this message and exit.\n```\n\n## config example\n\nThe following example will bump the version for docker and a python or javascript package.\n\n```toml\n# bump_semver_anywhere.toml\n\n[general]\ncurrent_version = "0.1.0"\n\n[vcs]\ncommit = true\ncommit_msg = "release({part}): bump {current_version} -> {new_version}"\n\n[files]\n\n[files.docker]\nfilename = "docker-compose.yaml"\npattern = \'image:.*?:(.*?)"\'\n\n[files.python-module]\nfilename = "__init__.py"\npattern = \'__version__ ?= ?"(.*?)"\'\n\n[files.python-pyproject]\nfilename = "pyproject.toml"\npattern = \'version ?= ?"(.*?)"\'\n\n[files.javascript]\nfilename = "package.json"\npattern = \'"version": ?"(.*?)"\'\n```\n\n## github action\n\nSee `.github/workflows/bump_semver_anywhere.yaml` to integrate the action to your repo.\n\nThe current behaviour is to comment `/release <part>` (e.g. `/release patch`) in a pull request. \nPer default it pushes the bump commit to the branch the PR points to. \nTherefore it should be commented after accepting the PR',
    'author': 'Ivan Gonzalez',
    'author_email': 'scratchmex@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/scratchmex/all-relative',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
