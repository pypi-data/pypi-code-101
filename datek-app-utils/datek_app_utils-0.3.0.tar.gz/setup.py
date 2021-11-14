# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datek_app_utils', 'datek_app_utils.env_config']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'datek-app-utils',
    'version': '0.3.0',
    'description': 'Utilities for building applications',
    'long_description': '[![pipeline status](https://gitlab.com/DAtek/app-utils/badges/master/pipeline.svg)](https://gitlab.com/DAtek/app-utils/-/commits/master)\n[![coverage report](https://gitlab.com/DAtek/app-utils/badges/master/coverage.svg)](https://gitlab.com/DAtek/app-utils/-/commits/master)\n\n# Utilities for building applications.\n\n## Contains:\n- Config loading from environment\n- Bootstrap for logging\n\n## Examples: \n```python\nimport os\n\nfrom datek_app_utils.env_config.base import BaseConfig\n\nos.environ["COLOR"] = "RED"\nos.environ["TEMPERATURE"] = "50"\n\n\nclass Config(BaseConfig):\n    COLOR: str\n    TEMPERATURE: int\n\n\nassert Config.COLOR == "RED"\nassert Config.TEMPERATURE == 50\n```\n\nThe `Config` class casts the values automatically.\nMoreover, you can test whether all the variables have been set or not.\n\n```python\nimport os\n\nfrom datek_app_utils.env_config.base import BaseConfig\nfrom datek_app_utils.env_config.utils import validate_config\nfrom datek_app_utils.env_config.errors import ValidationError\n\nos.environ["COLOR"] = "RED"\n\n\nclass Config(BaseConfig):\n    COLOR: str\n    TEMPERATURE: int\n\n\ntry:\n    validate_config(Config)\nexcept ValidationError as error:\n    for attribute_error in error.errors:\n        print(attribute_error)\n\n```\nOutput:\n```\nTEMPERATURE: Not set. Required type: <class \'int\'>\n```',
    'author': 'Attila Dudas',
    'author_email': 'attila.dudas@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/DAtek/app-utils',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
