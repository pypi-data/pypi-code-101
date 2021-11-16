# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wstompy', 'wstompy.protocol', 'wstompy.tests', 'wstompy.tests.protocol']

package_data = \
{'': ['*']}

install_requires = \
['websocket-client>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'wstompy',
    'version': '0.1.0',
    'description': 'Using a transport agnostic protocol and websocket-client to speak STOMP over websocket.',
    'long_description': "# wstompy\nUsing a transport agnostic protocol and websocket-client to speak STOMP over websocket.\n\n## Features\n\n### Yes\n* [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html)\n* Websocket with SSL/TLS(wss://) from websocket-client\n* Verbose socket logging thanks to websocket-client `websocket.enableTrace(True)` \n* Custom headers for transport and protocol\n\n### No\n* A non-websocket client\n\n### No, until added\n* STOMP versions before 1.2 \n* Data Classes/Models\n* Ready for production\n\n## Instructions\n\n### Install\n`pip install wstompy`\n\n### Usage\n```python\nimport websocket\nfrom wstompy.connection import WebSocketStompClient\n\nwebsocket.enableTrace(True)\n\naccess_token = 'tokentokentoken'\nhost = 'localhost'\nurl = f'ws://{host}:8080/ws/websocket'\nclient = WebSocketStompClient(\n    header_host=host,\n    socket_url=url,\n    custom_headers={'Authorization': f'Bearer {access_token}'},\n    subprotocols=['v12.stomp']\n)\nclient.run_forever(suppress_origin=True)\n```\n\n### Collaboration\n* Submit polite and/or well-written tickets for issues.\n* Fork and submit PRs referencing issues.\n* Uses poetry because they were early with pyproject.toml implementation which is neater when publishing.\n* Testing, feedback and reporting on usage with different server implementations.\n* Code is expected to have been run through black before commits, see Makefile.\n\n## Family, extended relatives and inspirations\n* [stomp.py](https://github.com/jasonrbriggs/stomp.py) - tried but its run loop was too sticky using dunders, preventing an easy merge with websocket-client's run loop.\n* [stomper](https://github.com/oisinmulvihill/stomper) - didn't have STOMP 1.2 implemented and I figured it was just as easy to reimplement to have the possibility of adding custom headers.\n* [stompest](https://github.com/nikipore/stompest) - didn't try it, but has async support in its packaged client. \n\n## Developing\n* `flake8 wstompy/` config in .flake8 until they support pyproject.toml\n* `mypy wstompy/` config in pyproject.toml\n* `black wstompy/` config in pyproject.toml\n\n## Notes\n* This has initially been implemented using [Spring Framework's STOMP server](https://spring.io/guides/gs/messaging-stomp-websocket/) with and without SockJS.\n",
    'author': 'Henrik Lindgren',
    'author_email': 'henriklindgren@users.noreply.github.com',
    'maintainer': 'Henrik Lindgren',
    'maintainer_email': 'henriklindgren@users.noreply.github.com',
    'url': 'https://github.com/henriklindgren/wstompy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
