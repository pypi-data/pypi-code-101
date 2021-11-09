# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bakkes_rcon', 'examples', 'tests', 'tests.bakkes_rcon']

package_data = \
{'': ['*']}

modules = \
['LICENSE', 'CHANGELOG']
install_requires = \
['websockets>=10.0,<11.0']

setup_kwargs = {
    'name': 'bakkes-rcon',
    'version': '0.0.1',
    'description': 'Tools for interacting with BakkesMod over its websocket RCON',
    'long_description': '# bakkes-rcon\n\nClient for interacting with [BakkesMod](https://bakkesmod.com/) over its websocket RCON.\n\n\n# Installation\n\n```shell\npip install bakkes-rcon\n```\n\n\n# Usage\n\n```python\nimport asyncio\nfrom bakkes_rcon import BakkesRconClient\n\nasync def main():\n    # By default, connects to ws://127.0.0.1:9002, with password "password"\n    async with BakkesRconClient() as client:\n        inventory = await client.get_inventory()\n        for item in inventory:\n            print(item)\n\nasyncio.run(main())\n```\n',
    'author': 'Zach "theY4Kman" Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/theY4Kman/bakkes-rcon',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
