# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chkapi']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20.0,<0.21.0',
 'textual-inputs>=0.1.2,<0.2.0',
 'textual>=0.1.12,<0.2.0']

entry_points = \
{'console_scripts': ['chkapi = chkapi.app:main']}

setup_kwargs = {
    'name': 'chkapi',
    'version': '0.2.0',
    'description': 'Console based app for browsing API',
    'long_description': '# API Checker\nSimple app for browsing api.\n\n## Usage\n```\npip install chkapi\n\nchkapi [url]\n```\n\nYou can check all features from scenarios: https://github.com/climbus/chkapi/tree/main/features\n\n## From source\n```\ngit clone https://github.com/climbus/chkapi.git\ncd chkapi\npoetry install\npoetry shell\npython -m rest_checker.app\n```\n\n\n',
    'author': 'Jarosław Kulesza',
    'author_email': 'climbus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/climbus/chkapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
