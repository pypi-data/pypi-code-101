# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hookup']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hookup',
    'version': '0.1.1',
    'description': 'Watch attributes on a class and trigger a callback on change',
    'long_description': 'Hookup is a Python decorator to monitor one or more attributes on a given object, and trigger a callback function to be called when the attribute(s) value changes.\n\nExample:\n\n```python\nfrom hookup import hookup\n\n@hookup(attrs=["version"], callback="update_version")\nclass Software:\n    def __init__(self):\n        version = 1\n\n    def update_version(self):\n        # This is the callback function that will be called when the attribute\'s value changes\n        with open("version.txt") as _file:\n            _file.write(self.version)\n\nsoftware = Software()\nsoftware.version=2\n```\n\n# Installation\n\nTo install Hookup, simply:\n\n```\n$ pip install hookup\n```\n\n# Usage\n\nHookup is designed to be used as a decorator on a class:\n\n```python\n@hookup(attrs=["version"], callback="update_version")\nclass Software:\n```\n\nYou must pass in the two required arguments:\n1. `attrs` - a List of attributes that will be watched for changes\n2. `callback` - a function belonging to the class used as a callback\n\nUpon the value of any watched attribute (`attrs`) changing from one value to another, the callback function will be executed.\n\nThe callback function will be called with no additional parameters. For example, the following would both be valid callbacks:\n\n```python\ndef callback(self):\n```\n\n```python\ndef callback(self, option="default"):\n```\n\n\n# Contributing\n\n1. Check for open issues or open a new issue to kick off discussion\n2. Fork the repository on Github, create a branch and make your code changes\n3. Write a test which shows that the bug was fixed, or that the new feature works as expected\n4. Send a PR with a clear description of the change\n\n\n# Changelog\n\n## 0.1.1 (2021-11-10)\n\n* Initial release\n',
    'author': 'Shaun S',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shaunrs/python-hookup',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
