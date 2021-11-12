# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aio_cosmos']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0,<4.0.0']

setup_kwargs = {
    'name': 'aio-cosmos',
    'version': '0.1.0',
    'description': 'Ayncio Client for Azure Cosmos DB',
    'long_description': '# aio-cosmos\nAsyncio SDK for Azure Cosmos DB. This library is intended to be a very thin asyncio wrapper around the [Azure Comsos DB Rest API][1]. \nIt is not intended to have feature parity with the Microsoft Azure SDKs but to provide async versions of the most commonly used interfaces.\n\n[1]: (https://docs.microsoft.com/en-us/rest/api/cosmos-db/)\n\n## Feature Support\n### Databases\n✅ List\\\n✅ Create\\\n✅ Delete\n\n### Containers\n✅ Create\\\n✅ Delete\n\n### Documents\n✅ Create Single\\\n✅ Create Concurrent Multiple\\\n✅ Delete\\\n✅ Get\\\n✅ Query\n\n## Installation\n\n```shell\npip install aio-cosmos\n```\n\n',
    'author': 'Grant McDonald',
    'author_email': 'calmseasdev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/calmseas/aio-cosmos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
