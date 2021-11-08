# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sqlfmt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata']}

entry_points = \
{'console_scripts': ['sqlfmt = sqlfmt.cli:sqlfmt']}

setup_kwargs = {
    'name': 'shandy-sqlfmt',
    'version': '0.1.0a8',
    'description': 'sqlfmt is an opinionated CLI tool that formats your sql files',
    'long_description': '# sqlfmt\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n\nsqlfmt is an opinionated CLI tool that formats your dbt sql files. It is similar in nature to black, gofmt, \nand rustfmt.\n\nsqlfmt is not configurable, except for line length. It enforces a single style. sqlfmt maintains comments and some extra newlines, but largely ignores all indentation and line breaks in the input file.\n\nsqlfmt is not a linter. It does not parse your code; it just tokenizes it and tracks a small subset of tokens that impact formatting. This lets us "do one thing and do it well:" sqlfmt is very fast, and easier to extend than linters that need a full sql grammar.\n\nsqlfmt is designed to work with sql files that contain jinja tags and blocks. It formats the code that users look at, and therefore doesn\'t need to know anything about what happens after the templates are rendered.\n\n## Contributing\n\n### Setting up Your Dev Environment and Running Tests\n\n1. Install [Poetry](https://python-poetry.org/docs/#installation) if you don\'t have it already. You may also need or want pyenv, make, and gcc. A complete setup from a fresh install of Ubuntu can be found [here](https://github.com/tconbeer/linux_setup)\n1. Clone this repo into a directory (let\'s call it `sqlfmt`), then `cd sqlfmt`\n1. Use `poetry install` to install the project (editable) and its dependencies into a new virtual env\n1. Use `poetry shell` to spawn a subshell\n1. Type `make` to run all tests and linters, or run `pytest`, `black`, `flake8`, `isort`, and `mypy` individually.',
    'author': 'Ted Conbeer',
    'author_email': 'ted@shandy.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://sqlfmt.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
