# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_iap_token']

package_data = \
{'': ['*'], 'mlflow_iap_token': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

entry_points = \
{'mlflow.request_header_provider': ['unused = '
                                    'mlflow_iap_token.iap_token:IdentityAwareProxyPluginRequestHeaderProvider']}

setup_kwargs = {
    'name': 'mlflow-iap-token',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Myung Kim',
    'author_email': 'agilemlops@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
