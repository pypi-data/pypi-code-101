# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dframeio', 'tests']

package_data = \
{'': ['*'],
 'tests': ['data/parquet/*',
           'data/parquet/multifile/*',
           'data/parquet/multifolder/gender=/*',
           'data/parquet/multifolder/gender=Female/*',
           'data/parquet/multifolder/gender=Male/*']}

install_requires = \
['lark-parser>=0.12.0,<0.13.0', 'pandas>=1.0.0,<2.0']

extras_require = \
{'parquet': ['pyarrow>=4.0,<7.0'],
 'postgres': ['psycopg>=3,<4'],
 'pyarrow': ['pyarrow>=4.0,<7.0']}

setup_kwargs = {
    'name': 'dframeio',
    'version': '0.3.0',
    'description': 'Read and write dataframes anywhere.',
    'long_description': '# dataframe-io\n\n[<img src="https://img.shields.io/pypi/v/dframeio.svg" alt="Release Status">](https://pypi.python.org/pypi/dframeio)\n[<img src="https://github.com/chr1st1ank/dataframe-io/actions/workflows/test.yml/badge.svg?branch=main" alt="CI Status">](https://github.com/chr1st1ank/dataframe-io/actions)\n[![codecov](https://codecov.io/gh/chr1st1ank/dataframe-io/branch/main/graph/badge.svg?token=4oBkRHXbfa)](https://codecov.io/gh/chr1st1ank/dataframe-io)\n\nRead and write dataframes from and to any storage.\n\n* Documentation: <https://chr1st1ank.github.io/dataframe-io/>\n* License: Apache-2.0\n* Status: Initial development\n\n## Features\n\nDataframes types supported:\n\n* pandas DataFrame\n* Python dictionary\n\nSupported storage backends:\n\n* Parquet files\n* PostgreSQL database\n\nMore backends will come. Open an [issue](https://github.com/chr1st1ank/dataframe-io/issues)\nif you are interested in a particular backend.\n\nImplementation status for reading data:\n\n| Storage       | Select columns | Filter rows | Max rows | Sampling | Drop duplicates |\n| ------------- | :------------: | :---------: | :------: | :------: | :-------------: |\n| Parquet files | ✔️              | ✔️           | ✔️        | ✔️        | ✔ ¹             |\n| PostgreSQL    | ✔️              | ✔️           | ✔️        | ✔️        | ✔️               |\n\n¹ only for pandas DataFrames\n\nImplementation status for writing data:\n\n| Storage       | write append | write replace |\n| ------------- | :----------: | :-----------: |\n| Parquet files | ✔️            | ✔️             |\n| PostgreSQL    | ✔️            | ✔️             |\n\n## Installation\n```\npip install dframeio\n\n# Including pyarrow to read/write parquet files:\npip install dframeio[parquet]\n\n# Including PostgreSQL support:\npip install dframeio[postgres]\n```\n\nShow installed backends:\n```\n>>> import dframeio\n>>> dframeio.backends\n[<class \'dframeio.parquet.ParquetBackend\'>]\n```\n',
    'author': 'Christian Krudewig',
    'author_email': 'chr1st1ank@krudewig-online.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chr1st1ank/dataframe-io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
