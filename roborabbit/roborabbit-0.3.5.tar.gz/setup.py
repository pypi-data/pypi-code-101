# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roborabbit']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'aio-pika>=6.8.0,<7.0.0', 'click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['roborabbit = roborabbit.main:main']}

setup_kwargs = {
    'name': 'roborabbit',
    'version': '0.3.5',
    'description': 'Set up your rabbit instance using a declarative yaml file.',
    'long_description': "# RoboRabbit\nRoboRabbit is a simple to use, opinionated, asynchronous abstraction over amqp/RabbitMQ (using aio_pika) and configuration CLI.\n\n\n## Features\n- Create/assert Queues, Exchanges, and Bindings on connection\n- Declarative Queue, Exchange, Binding, and Connection configuration using YAML\n- Very straight forward async message handling\n- Command line interface for bootstrapping rabbit from your roborabbit yaml config file.\n\n## Installation\n\n#### pip\n$ `pip install roborabbit`\n\n#### poetry\n$ `poetry add roborabbit`\n\n## Handle queue messages\n\nThe simplest worker possible. Connection information is in the `roborabbit.yaml` file. The method `run()` takes an dictionary with a key/value pair:\n- key: `queue` - string, the name of the queue to listen to\n- value: `handler` - function, the callback function messages will be sent to\n\n### Notes\n\n- Dead letter exchanges/queues are created and bound for you. (default is {queue_name}_dlq and {queue_name}_dlx)\n- Messages are `reject`ed and pushed into the dead letter queue when an exception is thrown.\n- Messages are `nack`ed and returned to queue when disconnected (asyncio.CancelledError).\n- Messages are `ack`ed automatically after the callback has run without exception.\n- Multiple queues can be listened to at the same time.\n- Connection is honored in the following order\n  - The `Connection()` class\n  - Connection parameters defined in your roborabbit.yaml file\n  - Environment variables (see environment variables section)\n  - Default RabbitMQ connection values\n\n### environment variables\n- `RABBIT_HOST` default 'localhost'\n- `RABBIT_USER` default 'guest'\n- `RABBIT_PASS` default 'guest'\n- `RABBIT_PORT` default 5432\n- `RABBIT_VIRTUALHOST` default '/'\n- `RABBIT_PREFETCH` default 10\n\n\n### Basic Example\n```py\nfrom roborabbit.roborabbit import RoboRabbit\nfrom pathlib import Path\n\nconfig_path = Path('roborabbit.yaml')\nrobo = RoboRabbit(config_path)\n\nasync def queue_handler(msg):\n    print(msg)  # your logic here\n\nawait robo.run({'queue_1', queue_handler})\n```\n\n### Explicit connection example\n\nIf you want control over the configuration, you can pass in the roborabbit connection object.\n\n```py\nfrom roborabbit.connection import Connection\nfrom roborabbit.roborabbit import RoboRabbit\nfrom pathlib import Path\n\nconfig_path = Path('roborabbit.yaml')\nconnection = Connection(\n    host='not.localhost.com',\n    username='bob',\n    password='pas123',\n    port=4499,\n    virtualhost='/')\n\nrobo = RoboRabbit(config_path, connection)\n\nasync def queue_handler(msg):\n    print(msg)  # your logic here\n\nasync def work():\n    await robo.run({'queue_1', queue_handler})\n```\n\n## Command\n\n`roborabbit --config path/to/roborabbit.yaml`\n\n### info\n\n```\nUsage: roborabbit [OPTIONS]\n\n  import yaml config file and creates a dictionary from it\n\nOptions:\n  --config TEXT       Path to rabbit config yaml file\n  --host TEXT         RabbitMQ host\n  --port TEXT         RabbitMQ port\n  --virtualhost TEXT  RabbitMQ virtualhost\n  --username TEXT     RabbitMQ username\n  --password TEXT     RabbitMQ password\n  --help              Show this message and exit.\n```\n\n## Override environment variables\n\n```\nRABBIT_USER=guest\nRABBIT_PASS=guest\nRABBIT_HOST=localhost\nRABBIT_PORT=5672\nRABBIT_VHOST=/\n```\n\n## Example yaml files\n\n### Simple declare queue, exchange, and bind\n\n```\nhost: localhost\nusername: guest\npassword: guest\nvirtualhost: /\nport: 5672\nexchanges:\n  - name: exchange_1\n    type: topic\nqueues:\n  - name: queue_1\nbindings:\n  - from:\n      type: exchange\n      name: exchange_1\n    to:\n      type: queue\n      name: queue_1\n    routing_keys:\n      - records.created\n```\n\n### Header exchange declaration and binding\n\n```\nhost: localhost\nusername: guest\npassword: guest\nvirtualhost: /\nport: 5672\nexchanges:\n  - name: exchange_2\n    type: headers\nqueues:\n  - name: queue_2\nbindings:\n  - from:\n      type: exchange\n      name: exchange_2\n    to:\n      type: queue\n      name: queue_1\n    bind_options:\n      - x-match: all\n        hw-action: header-value\n```\n\n## All Values Available\n\n```\n# Connection info\nhost: localhost\nusername: guest\npassword: guest\nvirtualhost: /\nport: 5672\n\n# Exchange declarations\nexchanges:\n  - name: string\n    type: topic|headers|direct|fanout # topic is default\n    durable: false # default\n    auto_delete: true # default\n\n# queue declarations\nqueues:\n  - name: string\n    type: quorum # Not required. This is the default and currently only option available (For us, all our queues are quorum. We manually create the queue that needs other requirements). MR welcome\n    dlq: string # default {queue_name}_dlq\n    dlx: string # default {queue_name}_dlx\n    durable: true # default\n    robust: true # default\n    auto_delete: false # default\n    exclusive: false # default\n    auto_delete_delay: 0 # default\n    arguments: # rabbit specific key/value pairs\n      key_1: value_1\n      key_2: value_2\n\n# bindings\nbindings:\n  - from:\n      type: exchange\n      name: string\n    to:\n      type: exchange|queue\n      name: string\n    routing_keys:\n      - record.created  # list of string, required, unless bind_options is defined\n    bind_options: # list of `x-match` and `header-key`, required if binding to a header exchange\n      - x-match: all|any # header type of matcher\n        header-key: string # header topic to be matched\n```\n\n## Planned features:\n- Simple message publishing\n- Expose the underlying channel so you can drop right into aio_pika if you want.\n",
    'author': 'Skyler Lewis',
    'author_email': 'skyler@hivewire.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alairock/roborabbit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
