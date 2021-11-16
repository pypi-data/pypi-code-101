# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sancty', 'sancty.patch_blessed']

package_data = \
{'': ['*']}

install_requires = \
['blessed @ git+https://github.com/tiptenbrink/blessed@master',
 'cwcwidth>=0.1.5,<0.2.0',
 'numpy>=1.21.4,<2.0.0']

setup_kwargs = {
    'name': 'sancty',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Tip ten Brink',
    'author_email': '75669206+tiptenbrink@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
