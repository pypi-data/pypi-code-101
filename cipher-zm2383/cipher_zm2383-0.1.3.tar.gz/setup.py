# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cipher_zm2383']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.4,<2.0.0']

setup_kwargs = {
    'name': 'cipher-zm2383',
    'version': '0.1.3',
    'description': 'hm07',
    'long_description': '# cipher_zm2383\n\nhm07\n\n## Installation\n\n```bash\n$ pip install cipher_zm2383\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`cipher_zm2383` was created by Zhenwei Ma. Zhenwei Ma retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.\n\n## Credits\n\n`cipher_zm2383` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Zhenwei Ma',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
