# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['knex']

package_data = \
{'': ['*']}

install_requires = \
['macaddr>=2.1,<3.0', 'regex>=2021.8.28,<2022.0.0', 'textfsm>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'knex',
    'version': '0.5.0',
    'description': 'Python library for building composable text parsers',
    'long_description': '# KNEX\n\nPython library for creating chainable data transformers.\n\n## Installation\n\n`pip install knex`\n\n## Usage\n\n```python\n>>> from knex.parsers import *\n>>>\n>>> input_data = """\n... Interface             IP-Address      OK?    Method Status          Protocol\n... GigabitEthernet0/1    unassigned      YES    unset  up              up\n... GigabitEthernet0/2    192.168.190.235 YES    unset  up              up\n... GigabitEthernet0/3    unassigned      YES    unset  up              up\n... GigabitEthernet0/4    192.168.191.2   YES    unset  up              up\n... TenGigabitEthernet2/1 unassigned      YES    unset  up              up\n... Virtual36             unassigned      YES    unset  up              up\n... """\n>>>\n>>> pattern = r"\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b"\n>>>\n>>> end = (\n                Start(input_data)\n                > RegexExtractAll(pattern)\n                > GetIndex(0)\n                > Concat("", "/24")\n                > IpNetwork()\n             )\n>>>\n>>> print(end.result)\n192.168.190.0/24\n>>> print(json.dumps(end.history, indent=4))\n[\n    {\n        "parser": "RegexExtractAll",\n        "input": "...omitted for brevity...",\n        "args": {\n            "pattern": "\\\\b\\\\d{1,3}\\\\.\\\\d{1,3}\\\\.\\\\d{1,3}\\\\.\\\\d{1,3}\\\\b"\n        },\n        "error": false,\n        "output": [\n            "192.168.190.235",\n            "192.168.191.2"\n        ]\n    },\n    {\n        "parser": "GetIndex",\n        "input": [\n            "192.168.190.235",\n            "192.168.191.2"\n        ],\n        "args": {\n            "idx": 0\n        },\n        "error": false,\n        "output": "192.168.190.235"\n    },\n    {\n        "parser": "Concat",\n        "input": "192.168.190.235",\n        "args": {\n            "prefix": "",\n            "suffix": "/24"\n        },\n        "error": false,\n        "output": "192.168.190.235/24"\n    },\n    {\n        "parser": "IpNetwork",\n        "input": "192.168.190.235/24",\n        "args": {},\n        "error": false,\n        "output": "192.168.190.0/24"\n    }\n]\n>>>\n\n```\n',
    'author': 'Clay Curtis',
    'author_email': 'clay584@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://clay584.github.io/knex/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
