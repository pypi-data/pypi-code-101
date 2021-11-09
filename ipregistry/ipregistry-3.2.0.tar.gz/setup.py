# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipregistry']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=4.2.4,<5.0.0', 'requests>=2.26.0,<3.0.0', 'six>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'ipregistry',
    'version': '3.2.0',
    'description': 'Official Python library for Ipregistry',
    'long_description': '[<img src="https://cdn.ipregistry.co/icons/icon-72x72.png" alt="Ipregistry" width="64"/>](https://ipregistry.co/) \n# Ipregistry Python Client Library\n\n[![License](http://img.shields.io/:license-apache-blue.svg)](LICENSE)\n[![Actions Status](https://github.com/ipregistry/ipregistry-python/workflows/Tests/badge.svg)](https://github.com/ipregistry/ipregistry-python/actions)\n[![PyPI](https://img.shields.io/pypi/v/ipregistry)](https://pypi.org/project/ipregistry/)\n\nThis is the official Python client library for the [Ipregistry](https://ipregistry.co) IP geolocation and threat data API, \nallowing you to lookup your own IP address or specified ones. Responses return multiple data points including carrier, \ncompany, currency, location, timezone, threat information, and more.\n\nStarting version 3 of the library, support for Python 2 has been dropped and the library requires Python 3.6+.\n\n## Getting Started\n\nYou\'ll need an Ipregistry API key, which you can get along with 100,000 free lookups by signing up for a free account at [https://ipregistry.co](https://ipregistry.co).\n\n### Installation\n\n```\npip install ipregistry\n```\n\n### Quick Start\n\n#### Single IP Lookup\n\n```python\nfrom ipregistry import IpregistryClient\n\nclient = IpregistryClient("YOUR_API_KEY")\nipInfo = client.lookup("54.85.132.205")\nprint(ipInfo)\n```\n\n#### Batch IP Lookup\n\n```python\nfrom ipregistry import IpregistryClient\n\nclient = IpregistryClient("YOUR_API_KEY")\nresults = client.lookup(["54.85.132.205", "8.8.8.8", "2001:67c:2e8:22::c100:68b"])\nfor ipInfo in results:\n    print(ipInfo)\n```\n\n#### Origin IP Lookup\n\n```python\nfrom ipregistry import IpregistryClient\n\nclient = IpregistryClient("YOUR_API_KEY")\nipInfo = client.lookup()\nprint(ipInfo)\n```\n\nMore advanced examples are available in the [samples](https://github.com/ipregistry/ipregistry-python/tree/master/samples) \nfolder.\n\n### Caching\n\nThis Ipregistry client library has built-in support for in-memory caching. By default caching is disabled. \nBelow are examples to enable and configure a caching strategy. Once enabled, default cache strategy is to memoize up to \n2048 lookups for at most 10min. You can change preferences as follows:\n\n#### Enabling caching\n\nEnable caching by passing an instance of `InMemoryCache`:\n\n```python\nfrom ipregistry import InMemoryCache, IpregistryClient\n\nclient = IpregistryClient("YOUR_API_KEY", cache=InMemoryCache(maxsize=2048, ttl=600))\n```\n\n#### Disabling caching\n\nDisable caching by passing an instance of `NoCache`:\n\n```python\nfrom ipregistry import IpregistryClient, NoCache\n\nclient = IpregistryClient("YOUR_API_KEY", cache=NoCache())\n```\n\n### Errors\n\nAll Ipregistry exceptions inherit `IpregistryError` class.\n\nMain subtypes are `ApiError` and `ClientError`.\n\nErrors of type _ApiError_ include a code field that maps to the one described in the [Ipregistry documentation](https://ipregistry.co/docs/errors).\n\n### Filtering bots\n\nYou might want to prevent Ipregistry API requests for crawlers or bots browsing your pages.\n\nA manner to proceed is to identify bots using the `User-Agent` header. \nTo ease this process, the library includes a utility method:\n\n```python\nfrom ipregistry import UserAgent\n\nisBot = UserAgent.isBot(\'YOUR_USER_AGENT_HEADER_VALUE_HERE\')\n```\n\n## Other Libraries\n\nThere are official Ipregistry client libraries available for many languages including \n[Java](https://github.com/ipregistry/ipregistry-java), \n[Javascript](https://github.com/ipregistry/ipregistry-javascript), and more.\n\nAre you looking for an official client with a programming language or framework we do not support yet? \n[let us know](mailto:support@ipregistry.co).\n',
    'author': 'Ipregistry Team',
    'author_email': 'support@ipregistry.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://ipregistry.co',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
