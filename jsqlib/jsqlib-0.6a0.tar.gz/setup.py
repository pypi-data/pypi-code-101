# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsqlib', 'jsqlib.helpers']

package_data = \
{'': ['*']}

install_requires = \
['jsonschema>=4.0,<5.0', 'python-box>=5.4,<6.0', 'sqlfluff>=0.6,<0.7']

setup_kwargs = {
    'name': 'jsqlib',
    'version': '0.6a0',
    'description': 'JSON to SQL query generator',
    'long_description': '# jsqlib\n> JSON to SQL query generator.\n\n[![pipeline status](https://gitlab.com/ru-r5/jsqlib/badges/master/pipeline.svg)](https://gitlab.com/ru-r5/jsqlib/-/commits/master)\n[![PyPI version](https://badge.fury.io/py/jsqlib.png)](https://badge.fury.io/py/jsqlib)\n\nBuilds SQL queries from pre-designed JSON structures.\n\n![](jsqlib.png)\n\n## Installation\n\nOS X & Linux & Windows:\n\n```sh\npip install jsqlib\n```\n\n## Usage example\n\n```python\nfrom jsqlib import Query\n\njson = """{\n  "query": {\n    "select": [\n      {\n        "eval": 1\n      }\n    ]\n  }\n}\n"""\n\nquery = Query(json)\nassert query.sql == \'select 1\'\n\nschema = \'{}\'\nquery = Query(json, schema=schema)  # optional schema to validate the query\nquery.validate()  # explicit query validation\n```\n\n## Development setup\n- coverage\n\n```sh\n$ poetry run pytest --cov\n```\n\n- format\n\n```sh\n$ poetry run black jsqlib -S\n```\n\n- lint\n\n```sh\n$ poetry run flakehell lint\n```\n\n- type checking\n\n```sh\n$ poetry run pyre\n```\n\n## Release History\n- 0.6a0\n  - CHANGE: validating the rendered json query against the provided schema without any changes (#26)\n- 0.5a0\n  - FIX: local variable \'data\' referenced before assignment in Builder._update (#18)\n  - ADD: support for a \'name\' attribute in JSON \'select\' definition (#20)\n  - ADD: validating JSON query against a schema if any (#19)\n- 0.4a0\n  - FIX: `order by` implicit `asc` construct (#16)\n  - CHANGE: library no longer modifies the original json query (#15)\n  - ADD: `__version__` package attribute (#14)\n- 0.3a0\n  - ADD: `not like`, `delete` `using` constructs (#12, #13)\n- 0.2a0\n  - ADD: dialect based stringification (#11)\n  - ADD: custom builder support (#10)\n- 0.1a0\n  - initial alpha-release\n- 0.0.1\n  - wip\n\n## Meta\n\npymancer@gmail.com ([Polyanalitika LLC](https://polyanalitika.ru))  \n[https://gitlab.com/ru-r5/jsqlib](https://gitlab.com/ru-r5/jsqlib)\n\n## License\n\nThis Source Code Form is subject to the terms of the Mozilla Public  \nLicense, v. 2.0. If a copy of the MPL was not distributed with this  \nfile, You can obtain one at https://mozilla.org/MPL/2.0/.  \n\n## Contributing\n\n1. Fork it (<https://gitlab.com/ru-r5/jsqlib/fork>)\n2. Create your feature branch (`git checkout -b feature/foo`)\n3. Commit your changes (`git commit -am \'Add some foo\'`)\n4. Push to the branch (`git push origin feature/foo`)\n5. Create a new Pull Request\n',
    'author': 'pymancer',
    'author_email': 'pymancer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/ru-r5/jsqlib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
