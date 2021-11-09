# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ness']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=0.18.1']

setup_kwargs = {
    'name': 'ness',
    'version': '0.0.1',
    'description': 'A Python datalake client.',
    'long_description': '# Ness\n\n<p align="center">\n    <em>A Python datalake client.</em>\n</p>\n<p align="center">\n    <a href="https://github.com/postpayio/ness/actions">\n        <img src="https://github.com/postpayio/ness/actions/workflows/test-suite.yml/badge.svg" alt="Test">\n    </a>\n    <a href="https://codecov.io/gh/postpayio/ness">\n        <img src="https://img.shields.io/codecov/c/github/postpayio/ness?color=%2334D058" alt="Coverage">\n    </a>\n    <a href="https://pypi.org/project/ness">\n        <img src="https://img.shields.io/pypi/v/ness" alt="Package version">\n    </a>\n</p>\n\n## Requirements\n\n- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)\n\n## Installation\n\n### Using Conda:\n\n```sh\nconda install -c conda-forge pyarrow ness\n```\n\n### Using Pip:\n\n```sh\npip install pyarrow ness\n```\n\n## Quickstart\n\n```py\nimport ness\n\ndl = ness.dl(bucket="mybucket", name="mydatalake")\ndf = dl.read("mytable")\n```\n\n## Sync\n\n```py\n# Sync all tables\ndf = dl.sync()\n\n# Sync a single table\ndf = dl.sync("mytable")\n```\n\n## Format\n\nSpecify the input data source format, the default format is `parquet`:\n\n```py\nimport ness\n\ndl = ness.dl(bucket="mybucket", name="mydatalake", format="csv")\n```\n',
    'author': 'Dani',
    'author_email': 'dani@postpay.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/postpayio/ness',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
