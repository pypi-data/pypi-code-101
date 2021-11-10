# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cipher_yb2503']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cipher-yb2503',
    'version': '0.1.1',
    'description': 'We are adding cipher to the package',
    'long_description': '# cipher_yb2503\n\nWe are adding cipher to the package\n\n## Installation\n\n```bash\n$ pip install cipher_yb2503\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`cipher_yb2503` was created by Yunxin Bo. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`cipher_yb2503` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Yunxin Bo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/QMSS-G5072-2021/cipher_bo_yunxin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
