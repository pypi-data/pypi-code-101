# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crabber']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'python-crabber',
    'version': '1.1.1',
    'description': 'A Python client for the Crabber REST API.',
    'long_description': '# python-crabber\n\n[![PyPI version](https://img.shields.io/pypi/v/python-crabber)](https://pypi.org/project/python-crabber)\n[![ReadTheDocs](https://readthedocs.org/projects/python-crabber/badge/)](https://python-crabber.readthedocs.io/en/latest/)\n\nA Python client for the Crabber.net REST API.\n\n## Installation\n\n``` bash\npip install python-crabber\n```\n\n## Documentation\n\nYou can find the full documentation at\n[ReadTheDocs](https://python-crabber.readthedocs.io/en/latest/).\n\n## Usage\n\n``` python3\n>>> import crabber\n>>> help(crabber.API)\n```\n\nAuthentication is done with developer/api keys and access tokens. You can get\nboth of these at https://crabber.net/developer/. Only an API key is needed to\naccess Crabber\'s API. \n\n``` python3\n>>> api = crabber.API(api_key=YOUR_DEVELOPER_KEY)\n>>> jake = api.get_crab_by_username(\'jake\')\n>>> jake\n<Crab @jake [1]>\n>>> jake.display_name\n\'Jake L.\'\n```\n\nIf you want to make actions on a user\'s behalf you\'ll need to authenticate with\nan access token. Access tokens are tied to specific accounts, so if you create\nan access token while logged in as \'@thedude\' then all applications\nauthenticated with that access token will act as if they are logged in as\n\'@thedude\'. **This is why it is imperative that access tokens are kept private \nand not shared with *anyone*.**\n\n``` python3\n>>> jake = api.get_crab_by_username(\'jake\')\n>>> jake.follow()\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "/Users/jake/code/python-crabber/crabber/models.py", line 342, in follow\n    raise RequiresAuthenticationError(\ncrabber.exceptions.RequiresAuthenticationError: You are not properly authenticated for this request.\n>>> api.authenticate(YOUR_ACCESS_TOKEN)\n>>> jake.follow()\nTrue\n>>> api.get_current_user() in jake.followers\nTrue\n>>> api.post_molt(\'Hello, world!\')\n<Molt [683]>\n```\n\nIt is also possible to authenticate while intializing the API object rather than\nafterwards.\n\n``` python3\n>>> api = crabber.API(api_key=YOUR_DEVELOPER_KEY, access_token=YOUR_ACCESS_TOKEN)\n>>> api.get_current_user()\n<Crab @thedude [85]>\n```\n',
    'author': 'Jake Ledoux',
    'author_email': 'contactjakeledoux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/python-crabber',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
