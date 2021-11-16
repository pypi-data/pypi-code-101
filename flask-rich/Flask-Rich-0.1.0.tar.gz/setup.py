# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flask_rich']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0.2,<3.0.0', 'rich>=10.13.0,<11.0.0']

setup_kwargs = {
    'name': 'flask-rich',
    'version': '0.1.0',
    'description': 'Rich implementation for Flask',
    'long_description': "# Flask Rich\n\nImplements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/). All features are toggleable, including:\n\n- Better logging\n\n## Usage\n\nImport the `RichApplication` class.\n\n```python\nfrom flask_rich import RichApplication\nfrom flask import Flask\n\nrich = RichApplication()\n\napp = Flask(__name__)\nrich.init_app(app)\n\n# Or\n# rich = RichApplication(app)\n```\n\n### Class options\n\n#### `app = None`\n\nThe Flask app that is used. It is optional, but you need to call `RichApplication.init_app(app)` later to enabled to library.\n\napp=None, enable_logging: bool=True, logging_markup: bool=True\n\n#### `enable_logging: bool = True`\n\nWhether to use [Rich's logging](https://rich.readthedocs.io/en/latest/logging.html) handler.\n\n#### `logging_markup: bool = True`\n\nWhether to allow [Rich's console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup) format in logging.\n\nAn example of console markup is `[blue]Hello[/blue], world!`.\n\n## Contributing\n\nPRs are welcome! You can setup your own copy of the source code with:\n\n```shell\n# Git\ngit clone https://github.com/BD103/Flask-Rich.git\ncd Flask-Rich/\n\n# Poetry\npoetry lock\npoetry install\npoetry shell\n```\n\nYou will need [Poetry](https://python-poetry.org/) for managing dependencies.",
    'author': 'BD103',
    'author_email': 'dont@stalk.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BD103/Flask-Rich',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
