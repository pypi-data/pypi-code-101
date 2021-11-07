# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cryptofeed_werks', 'cryptofeed_werks.exchanges', 'cryptofeed_werks.trades']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'cryptofeed>=1.9.3,<2.0.0',
 'numpy>=1.21.4,<2.0.0',
 'websockets>=9.1,<10.0']

extras_require = \
{'all': ['google-cloud-bigquery>=2.6.1,<3.0.0',
         'google-cloud-bigquery-storage>=2.1.0,<3.0.0',
         'google-cloud-pubsub>=2.8.0,<3.0.0',
         'google-cloud-firestore>=2.1.0,<3.0.0',
         'sentry-sdk>=1.0.0,<2.0.0'],
 'bigquery': ['google-cloud-bigquery>=2.6.1,<3.0.0',
              'google-cloud-bigquery-storage>=2.1.0,<3.0.0'],
 'firestore': ['google-cloud-firestore>=2.1.0,<3.0.0'],
 'sentry': ['sentry-sdk>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'cryptofeed-werks',
    'version': '0.1.0',
    'description': 'Pipeline for live data from cryptocurrency exchanges',
    'long_description': '# What?\n\nThis is the basis of a pipeline for live data from cryptocurrency exchanges. It normalizes [cryptofeed](https://github.com/bmoscon/cryptofeed) WebSocket messages, aggregates, and optionally publishes them to GCP Pub/Sub and/or Firestore.\n\n# How?\n\nSequences of trades that have equal symbol, timestamp, nanoseconds, and tick rule are aggregated. Aggregating trades in this way can increase information, as they are either orders of size or stop loss cascades.\n\nAs well, the number of messages can be reduced by 30-50%\n\nBy filtering aggregated messages, for example only emitting a meesage when `thresh_attr = "volume"` is greater than `thresh_value >= 1000`, the number of messages can be reduced more.\n\nExample\n-------\nThe following are two sequential aggregated trades by timestamp, nanoseconds, and tick rule.\n\nAs it was aggregated from 4 raw trades, the second trade has ticks 4.\n\n```python\n[\n    {\n        "timestamp": 1620000915.31424,\n        "price": "57064.01",\n        "volume": "566.6479018604",\n        "notional": "0.00993004",\n        "tickRule": -1,\n        "ticks": 1\n    },\n    {\n        "timestamp": 1620000915.885381,\n        "price": "57071.2",\n        "volume": "9376.6869202914",\n        "notional": "0.16429813",\n        "tickRule": 1,\n        "ticks": 4\n    }\n]\n```\n\nAn example filtered message, emitted because the second aggregated trade `thresh_attr = "volume"` exceeds `thresh_value >= 1000`\n\nInformation related to the first trade is aggregated with the second.\n\n```python\n[\n    {\n        "timestamp": 1620000915.885381,\n        "price": "57071.2",\n        "volume": "9376.6869202914",\n        "notional": "0.16429813",\n        "tickRule": 1,\n        "ticks": 4,\n        "high": \'57071.2\',\n        "low": \'57064.01\',\n        "totalBuyVolume": "9376.6869202914",\n        "totalVolume": "9943.3348221518",\n        "totalBuyNotional": "0.16429813",\n        "totalNotional": "0.17422817",\n        "totalBuyTicks": 4,\n        "totalTicks": 5\n    }\n]\n```\n\nFor 1m, 5m, 15m candles, there is an optional parameter `window_seconds`.  \n\nFor settings, see [demo.py](https://github.com/globophobe/cryptofeed-werks/blob/main/demo.py)\n\nSupported exchanges\n-------------------\n\n* Binance\n* Bitfinex\n* Bitflyer\n* BitMEX\n* Bybit\n* Coinbase Pro\n* Deribit\n* FTX\n* Upbit\n\nFuture plans\n------------\nOrder book aggregation, in the manner of [crypto-whale-watching-app](https://github.com/pmaji/crypto-whale-watching-app)\n',
    'author': 'Alex',
    'author_email': 'globophobe@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/globophobe/cryptofeed-werks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
