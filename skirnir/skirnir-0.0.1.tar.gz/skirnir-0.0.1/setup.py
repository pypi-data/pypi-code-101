# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['skirnir']

package_data = \
{'': ['*']}

extras_require = \
{'docs': ['sphinx<4',
          'sphinx-rtd-theme>=0.5.2,<0.6.0',
          'sphinx-autodoc-typehints>=1.12.0,<2.0.0']}

setup_kwargs = {
    'name': 'skirnir',
    'version': '0.0.1',
    'description': 'A system so send an route alerts',
    'long_description': '# Skirnir\n',
    'author': 'Eduard Thamm',
    'author_email': 'eduard.thamm@thammit.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/edthamm/skirnir',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
