# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ameritrade']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.3,<4.0.0', 'dataclass-factory>=2.10,<3.0']

setup_kwargs = {
    'name': 'ameritrade-python',
    'version': '0.1.1',
    'description': 'A python wrapper for the Ameritrade API.',
    'long_description': '# ameritrade-python\nThis is a simple and lightweight async api wrapper for Ameritrade\'s API.\n\nThe official docs for the Ameritrade API can be found [here](https://developer.tdameritrade.com/apis).\n\nSimple usage using an existing refresh token:\n```python\nimport asyncio\nfrom os import environ\nfrom ameritrade import auth, stock\n\ntest_redirect_uri = environ.get("callback_url")\nconsumer_key = environ.get("consumer_key")\nrefresh_token = environ.get("refresh_token")\n\ntest_auth = auth.Auth(redirect_uri=test_redirect_uri, consumer_key=consumer_key, refresh_token=refresh_token)\n\nasync def main():\n    """Gets new tokens, then gets a single stock quote for \'KO\'/coca-cola."""\n    await test_auth.refresh_token_auth()  # Gets fresh tokens\n\n    test_stock = stock.Stock(auth_class=test_auth, symbol="ko")  # creates stock object for KO\n    await test_stock.get_quote()  # Makes the quote request\n    print(test_stock.quote)\n\n\nloop = asyncio.get_event_loop()  # Creates the event loop\nloop.run_until_complete(main())  # Runs the event loop\n```\n\n## Environment\nI suggest utilizing a .env file to store private/sensitive information.  \nIf you are not providing a refresh token, it is recommended that you use auth.Auth.manual_auth() in order to use\nAmeritrade\'s front end auth tools, you can follow the on-screen instructions for this.\n\nYou may choose to save your refresh token in a secure location/format, if using a previous refresh token, you only\nneed to provide these to your auth class:\n- consumer_key\n- refresh_token\n\n## Developemnt\nInstall dependencies with poetry `poetry install`.  \n\n### Building Locally\n`poetry build`\n',
    'author': 'Kyler Roloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fisher60/ameritrade-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
