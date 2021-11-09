# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nytxw_puz']

package_data = \
{'': ['*']}

modules = \
['nytxw_gen']
install_requires = \
['colorlog>=6.6.0,<7.0.0', 'pendulum>=2.1.2,<3.0.0', 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['nytxw_gen = utils.nytxw_gen:main',
                     'nytxw_puz = nytxw_puz.main:main']}

setup_kwargs = {
    'name': 'nytxw-puz-cli',
    'version': '1.0.0',
    'description': 'CLI tool to convert NY Times crosswords into Across Lite files (.puz)',
    'long_description': '# NY Times Crossword to Puz\n\nCLI tool to convert NY Times crosswords into Across Lite files (.puz).\n\nThis is a fork of [nytxw_puz](https://github.com/Q726kbXuN/nytxw_puz) with some major differences:\n\n  * No browser installations are required. Authentication is performed by the program itself.\n  * Targeted for headless deployments and thus is non-interactive.\n  * Supports batch downloading with rate limiting and timeout.\n\n## Usage\n\n```bash\npip install nytxw_puz_cli\nnytxw_puz --help\n```\n\n### Credentials\n\nThe program expects a JSON credentials file to be passed via the `--credentials` flag. The expected format of the JSON is simple and as follows:\n\n```json\n{"email": "user@domain.com", "password": "my-password"}\n```\n\n### Example Using Flags\n\nA simple example downloading a single crossword:\n\n```bash\nnytxw_puz --credentials my-creds.creds --urls https://www.nytimes.com/crosswords/game/daily/2020/12/31 --filenames ~/puzzles/2020/12/31.puz\n```\n\n### Example Using stdin\n\nA full example of a run using cookie import/export and input of `URL,FILENAME` entries named `tasks.csv` via stdin:\n\n```bash\nnytxw_puz --credentials my-creds.creds --import-cookies mycookies.cookies --export-cookies mycookies.cookies -v < tasks.csv\n```\n\n### `nytxw_gen`\n\n`nytxw_gen` is a small tool to help generate date ranges of crossword puzzles in CSV format to pass into `nytxw_puz`. For example:\n\n```bash\nnytxw_gen --start 2012-07-18 --end 2014-12-31 --path-format "~/puzzles/<year>/<month>/<day>.puz" > puzzles-to-download.csv \n```\n\n\n## Development\n\n### Getting Started\n\nThis repository uses [poetry](https://python-poetry.org/) to manage dependencies and environments. To get started quickly, run:\n\n```bash\ncd nytxw_puz_cli\npoetry install\n```\n\n### Code Style\n\nFor Python, the repository uses the default settings of the [**Black code formatter**](https://black.readthedocs.io/).\n\nConformance can be enforced by using `black` as follows:\n\n```bash\nblack <file-name>\n```\n',
    'author': 'Chris Tam',
    'author_email': 'ohgodtamit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GodTamIt/nytxw_puz_cli',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
