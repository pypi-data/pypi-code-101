# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cipher_yw3760']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'cipher-yw3760',
    'version': '0.1.0',
    'description': 'an example python package written by Yu Wang for MDS Fall 2021',
    'long_description': '# cipher_yw3760\n\nan example python package written by Yu Wang for MDS Fall 2021\n\n## Installation\n\n```bash\n$ pip install cipher_yw3760\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`cipher_yw3760` was created by YU WANG. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`cipher_yw3760` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'YU WANG',
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
