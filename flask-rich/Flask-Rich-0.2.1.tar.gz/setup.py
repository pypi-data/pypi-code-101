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
    'version': '0.2.1',
    'description': 'Rich implementation for Flask',
    'long_description': '# Flask Rich\n\nImplements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/). All features are toggleable, including:\n\n- Better logging\n- Colorful tracebacks\n\n## Usage\n\nImport the `RichApplication` class.\n\n```python\nfrom flask_rich import RichApplication\nfrom flask import Flask\n\nrich = RichApplication()\n\napp = Flask(__name__)\napp.config["RICH_EXAMPLE_SETTING"] = "value"\n\nrich.init_app(app)\n\n# Or\n# rich = RichApplication(app)\n```\n\n### Class options\n\n#### `RICH_LOGGING: bool = True`\n\nWhether to use [Rich\'s logging](https://rich.readthedocs.io/en/latest/logging.html) handler.\n\n#### `RICH_LOGGING_MARKUP: bool = True`\n\nWhether to allow [Rich\'s console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup) format in logging.\n\nAn example of console markup is `[blue]Hello[/blue], world!`.\n\n#### `RICH_TRACEBACK: bool = True`\n\nWhether to use [Rich\'s traceback](https://rich.readthedocs.io/en/latest/traceback.html) handler.\n\n#### `RICH_TRACEBACK_EXTRA_LINES: int = 1`\n\nWhen Rich prints the lines of code which raised the error, how many lines around it does it print as well. In the library it defaults to 3, but 1 is better for web applications.\n\n#### `RICH_TRACEBACK_SHOW_LOCALS: bool = False`\n\nWhether to print the local variables with traceback.\n\n## Contributing\n\nPRs are welcome! You can setup your own copy of the source code with:\n\n```shell\n# Git\ngit clone https://github.com/BD103/Flask-Rich.git\ncd Flask-Rich/\n\n# Poetry\npoetry lock\npoetry install\npoetry shell\n```\n\nYou will need [Poetry](https://python-poetry.org/) for managing dependencies.',
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
