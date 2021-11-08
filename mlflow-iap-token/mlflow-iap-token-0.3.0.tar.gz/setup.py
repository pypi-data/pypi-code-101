# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_iap_token']

package_data = \
{'': ['*'], 'mlflow_iap_token': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

install_requires = \
['google-auth>=2.3.3,<3.0.0', 'mlflow-skinny>=1.21.0,<2.0.0']

entry_points = \
{'mlflow.request_header_provider': ['unused = '
                                    'mlflow_iap_token.iap_token:IdentityAwareProxyPluginRequestHeaderProvider']}

setup_kwargs = {
    'name': 'mlflow-iap-token',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Myung Kim',
    'author_email': 'agilemlops@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
