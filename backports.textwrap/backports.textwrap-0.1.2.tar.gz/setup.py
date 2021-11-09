# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['backports']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'backports.textwrap',
    'version': '0.1.2',
    'description': 'A backport of upcoming python/cpython#28136',
    'long_description': '# textwrap\nA backport of upcoming python/cpython#28136 with some additional fixes.\n\nMotivated due to jquast/blessed using textwrap, but this fails for zero-width characters. This allows setting text_len\nto, for example, wcswidth for more accuracy when word wrapping in the terminal.\n\nThis uses the backports package style, see https://pypi.python.org/pypi/backports.',
    'author': 'Tip ten Brink',
    'author_email': '75669206+tiptenbrink@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
