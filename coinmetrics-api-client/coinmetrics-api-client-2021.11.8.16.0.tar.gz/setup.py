# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coinmetrics']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.6.0,<4.0.0', 'requests>=2.24.0,<3.0.0']

extras_require = \
{'pandas': ['pandas>=1.3.3,<2.0.0']}

entry_points = \
{'console_scripts': ['poetry = poetry.console:run']}

setup_kwargs = {
    'name': 'coinmetrics-api-client',
    'version': '2021.11.8.16.0',
    'description': 'Python client for Coin Metrics API v4.',
    'long_description': '# Coin Metrics Python API v4 client library\n\nThis is an official Python API client for Coin Metrics API v4.\n\n## Installation\nTo install the client you can run the following command:\n```\npip install coinmetrics-api-client\n```\n\n\n## Introduction\nYou can use this client for querying all kinds of data with your API.\n\nTo initialize the client you should use your API key, and the CoinMetricsClient class like the following.\n```\nfrom coinmetrics.api_client import CoinMetricsClient\n\nclient = CoinMetricsClient("<cm_api_key>")\n\n# or to use community API:\nclient = CoinMetricsClient()\n```\n\nAfter that you can use the client object for getting stuff like available markets:\n```\nprint(client.catalog_markets())\n```\n\nor to query all available assets along with what is available for those assets, like metrics, markets:\n\n```\nprint(client.catalog_assets())\n```\n\n\nyou can also use filters for the catalog endpoints like this:\n\n```\nprint(client.catalog_assets(assets=[\'btc\']))\n```\nin this case you would get all the information for btc only\n\nYou can use this client to connect to our API v4 and get catalog or timeseries data from python environment. It natively supports paging over the data so you can use it to iterate over timeseries entries seamlessly.\n\nThe client can be used to query both pro and community data.\n\n## Getting timeseries data\n\nFor getting timeseries data you want to use methods of the client class that start with `get_`.\n\nFor example if you want to get a bunch of market data trades for coinbase btc-usd pair you can run something similar to the following:\n\n```\nfor trade in client.get_market_trades(\n    markets=\'coinbase-btc-usd-spot\', \n    start_time=\'2020-01-01\', \n    end_time=\'2020-01-03\',\n    limit_per_market=10\n):\n    print(trade)\n```\n\nOr if you want to see daily btc asset metrics you can use something like this:\n\n```\nfor metric_data in client.get_asset_metrics(assets=\'btc\', \n                                            metrics=[\'ReferenceRateUSD\', \'BlkHgt\', \'AdrActCnt\',  \n                                                     \'AdrActRecCnt\', \'FlowOutBFXUSD\'], \n                                            frequency=\'1d\',\n                                            limit_per_asset=10):\n    print(metric_data)\n```\nThis will print you the requested metrics for all the days where we have any of the metrics present. \n\n\n### DataFrames \n_(New in >=`2021.9.30.14.30`)_\n\nTimeseries data can be transformed into a pandas dataframe by using the `to_dataframe()` method. The code snippet below shows how:\n```\nimport pandas as pd\nfrom coinmetrics.api_client import CoinMetricsClient\nfrom os import environ\n\nclient = CoinMetricsClient()\ntrades = client.get_market_trades(\n    markets=\'coinbase-btc-usd-spot\', \n    start_time=\'2021-09-19T00:00:00Z\', \n    limit_per_market=10\n)\ntrades_df = trades.to_dataframe()\nprint(trades_df.head())\n\n```\nIf you want to use dataframes, then you will need to install pandas\n\n**Notes**\n\n- This only works with requests that return the type `DataCollection`. Thus, `catalog` requests, which return lists cannot be returned as dataframes.\nPlease see the [API Client Spec](https://coinmetrics.github.io/api-client-python/site/api_client.html) for a full list\nof requests and their return types.\n- API restrictions apply. Some requests may return empty results due to limited access to the API from you API key.\n\n\n### Paging\nYou can make the datapoints to iterate from start or from end (default).\n\nfor that you should use a paging_from argument like the following:\n```\nfrom coinmetrics.api_client import CoinMetricsClient\nfrom coinmetrics.constants import PagingFrom\n\nclient = CoinMetricsClient()\n\nfor metric_data in client.get_asset_metrics(assets=\'btc\', metrics=[\'ReferenceRateUSD\'],\n                                            paging_from=PagingFrom.START):\n    print(metric_data)\n```\n\nPagingFrom.END: is available but it is also a default value also, so you might not want to set it.\n\n## Extended documentation\nFor more information about the available methods in the client please reference [API Client Spec](https://coinmetrics.github.io/api-client-python/site/api_client.html)\n',
    'author': 'Coin Metrics',
    'author_email': 'info@coinmetrics.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://coinmetrics.github.io/api-client-python/site/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
