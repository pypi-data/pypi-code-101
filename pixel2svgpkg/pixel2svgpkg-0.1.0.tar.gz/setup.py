# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixel2svgpkg']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0', 'svgwrite>=1.4.1,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'pixel2svgpkg',
    'version': '0.1.0',
    'description': 'A Python package/fork from the pixel2svg project by Florian Berger.',
    'long_description': "# pixel2svgpkg\n\n[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nA Python package/fork from the [pixel2svg](https://florian-berger.de/en/software/pixel2svg/) project by [Florian Berger](https://florian-berger.de/en/).\n\n## Development\n\n- `poetry install`\n- `poetry shell`\n\n## Tech Stack\n\n### Packaging and Development\n\n- [Poetry](https://python-poetry.org/)\n- [Mypy](http://mypy-lang.org/)\n- [isort](https://pycqa.github.io/isort/)\n- [Black](https://github.com/psf/black)\n- [Flake8](https://flake8.pycqa.org/)\n  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)\n  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)\n  - [pep8-naming](https://github.com/PyCQA/pep8-naming)\n  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)\n- [Bandit](https://bandit.readthedocs.io/)\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-pkg`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.\n\n## Notes\n\n- Poetry:\n  - `poetry --version`.\n  - [Licenses](https://python-poetry.org/docs/pyproject#license).\n  - [Exception: `No module named 'virtualenv.activation.nushell'`](https://github.com/python-poetry/poetry/issues/4515) issue. Run `poetry self update` to update Poetry (to version 1.1.11).\n- VS Code:\n  - [Different python.defaultInterpreterPath by workspace not being saved](https://github.com/microsoft/vscode-python/issues/12633#issuecomment-651853209) issue. Set `python.defaultInterpreterPath` instead of `python.pythonPath` in the `settings.json` file. More info [here](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter).\n- [ColorSpace](https://mycolor.space/gradient3) (3-Color-Gradient).\n- [Gremlins tracker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nhoizey.gremlins): to identify characters that can be harmful because they are invisible or look like legitimate ones.\n- [pixel2svg-fork](https://github.com/cyChop/pixel2svg-fork).\n",
    'author': 'João Palmeiro',
    'author_email': 'joaommpalmeiro@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joaopalmeiro/pixel2svgpkg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
