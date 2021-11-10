# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xiao_asgi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xiao-asgi',
    'version': '0.2.1',
    'description': 'A small ASGI framework.',
    'long_description': '# xiao asgi\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nxiao asgi is a small [ASGI](https://asgi.readthedocs.io/en/latest/) framework that can be used to create ASGI applications.\nIt is designed to be small in size, simple to use and have few dependencies.\nHTTP and WebSockets are both supported.\n\n## Installation\n\nxiao asgi can be installed into a Python environment by running `pip install xiao-asgi`.\n\n### Supported Python versions\n\nxiao asgi has been tested with the following versions of Python:\n\n* 3.10.0\n* 3.9.7\n\n## Documentation\n\nDocstrings are included in the project and more information can be found at the [Wiki](https://github.com/jonathanstaniforth/xiao-asgi/wiki) tab (work in progress).\n\n## Discussions\n\nHead over to the [Discussions](https://github.com/jonathanstaniforth/xiao-asgi/discussions) tab to start a conversation on xiao asgi.\n\n## Contributions\n\nThis project uses the [GitHub flow](https://guides.github.com/introduction/flow/) branching strategy.\n\n## License\n\nxiao asgi is open-sourced software licensed under the [MIT](https://opensource.org/licenses/MIT) license.\n',
    'author': 'Jonathan Staniforth',
    'author_email': 'jonathanstaniforth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/limber-project/limberframework',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
