# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gadd']

package_data = \
{'': ['*']}

install_requires = \
['autoflake>=1.4,<2.0',
 'black>=21.10,<22.0',
 'flake8>=4.0,<5.0',
 'gitpython>=3.1,<4.0',
 'isort>=5.10,<6.0',
 'pylint>=2.11,<3.0',
 'vulture>=2.3,<3.0']

setup_kwargs = {
    'name': 'gadd',
    'version': '0.1.0',
    'description': 'Sort imports, remove unused imports, run Black, flake8, pylint, vulture in one go for al staged .py files',
    'long_description': '# gadd\nVery opinionated formatting python files after git add\n\n# Intent\nI needed a small tool to reformat and lint all the staged `.py` files according to the specific rules. I wanted it to be able to `pip` install it and available in the `PATH`. It is called `gadd` because you run it after `git add` command.\nIt will do:\n* Remove unused imports\n* Sort imports\n* Reformat with [`Black`](https://github.com/psf/black)\n* Run [`flake8`](https://github.com/PyCQA/pylint) and [`pylint`](https://github.com/PyCQA/flake8) linters\n* Search for deadcode with [`vulture`](https://github.com/jendrikseipp/vulture)\n\nObeys `.flake8`, `.pylintrc` and `whitelist.py` config files in the current directory.\n\n# Tutorial\nThis is quick tutorial on hoe to create `pip` installable Python CLI tool.\n\n* create a repository with the following file structure: \n```bash\nuser@computer gadd % exa -T .\n.\n├── gadd\n│  ├── __init__.py\n│  └── gadd.py\n├── LICENSE\n├── README.md\n└── test\n   ├── __init__.py\n   └── test_gadd.py\n```\n\n# Publish to `pip` with [`poetry`](https://python-poetry.org)\nMake it pip installable with CLI command.\n\nMake and publish `pip` package with `poetry`:\n\n* Install `poetry`. I would highly recommend to install it with `pipx`\n\n```\ncd gadd\npipx install poetry\npoetry init\n```\n* Modify `pyproject.toml` file:\n```toml\n [tool.poetry]\nname = "gadd"\nversion = "0.1.0"\ndescription = "Sort imports, remove unused imports, run Black, flake8, pylint, vulture in one go for al staged .py files"\nauthors = ["Almaz Kunpeissov <hello@akun.dev>"]\nkeywords = ["Black", "Sort imports", "analysis", "automation", "autopep8", "code", "flake8", "formatter", "gofmt", "lint", "linter", "pyfmt", "pylint", "python", "remove unused imports", "rustfmt", "static", "vulture", "yapf"]\nreadme = "README.md"\nlicense = "MIT"\nhomepage = "https://github.com/almazkun/gadd"\nrepository = "https://github.com/almazkun/gadd"\ndocumentation = "https://github.com/almazkun/gadd"\ninclude = [\n    "LICENSE",\n]\nclassifiers = [\n    "Topic :: Software Development :: Libraries :: Python Modules",\n    "Topic :: Software Development :: Quality Assurance",\n    "Topic :: Software Development :: Debuggers",\n]\n\n[tool.poetry.dependencies]\npython = "^3.6"\nautoflake = "^1.4"\nblack = "^21.10"\nflake8 =  "^4.0"\ngitpython = "^3.1"\nisort =  "^5.10"\npylint = "^2.11"\nvulture = "^2.3"\n\n[tool.poetry.dev-dependencies]\n\n[build-system]\nrequires = ["poetry-core>=1.0.0"]\nbuild-backend = "poetry.core.masonry.api"\n```\n\n\n\n# TODO\n* [ ] load from `.conf` file\n* [ ] publish to pip\n* [ ] make it `async`\n* [ ] ',
    'author': 'Almaz Kunpeissov',
    'author_email': 'hello@akun.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/almazkun/gadd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
