# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lefi',
 'lefi.exts',
 'lefi.exts.commands',
 'lefi.exts.commands.core',
 'lefi.objects',
 'lefi.utils',
 'lefi.ws']

package_data = \
{'': ['*']}

install_requires = \
['PyNaCl>=1.4.0,<2.0.0', 'aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'lefi',
    'version': '0.2.3',
    'description': 'A discord API wrapper focused on clean code, and usability',
    'long_description': '# Lefi\n[![Documentation Status](https://readthedocs.org/projects/lefi/badge/?version=latest)](https://lefi.readthedocs.io/en/latest/?badge=latest)\n![Pytests](https://github.com/an-dyy/Lefi/actions/workflows/run-pytest.yml/badge.svg?event=push)\n![Mypy](https://github.com/an-dyy/Lefi/actions/workflows/mypy.yml/badge.svg?event=push)\n[![PyPI version](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.python.org/pypi/lefi/)\n[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/QPFXzFbqrK)\n\n\nA discord API wrapper focused on clean code, and usability\n\n## Installation\n\n1. Poetry\n\n   ```\n   poetry add lefi\n   ```\n\n2. Pip\n   ```\n   pip install lefi\n   ```\n\n## Example(s)\n[Here!](examples/)\n\n## Documentation\n[Here!](https://lefi.readthedocs.io/en/latest/)\n\n## Contributing\n1. If you plan on contributing please open an issue beforehand\n2. Fork the repo, and setup the poetry env (with dev dependencies)\n3. Install pre-commit hooks (*makes it a lot easier for me*)\n    ```\n    pre-commit install\n    ```\n\n## Join the discord!\n- [Discord](https://discord.gg/QPFXzFbqrK)\n\n## Notable contributors\n\n- [blanketsucks](https://github.com/blanketsucks) - collaborator\n- [an-dyy](https://github.com/an-dyy) - creator and maintainer\n\n',
    'author': 'an-dyy',
    'author_email': 'andy.development@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/an-dyy/Lefi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
