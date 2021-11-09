# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dropdown']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0.0,<4.0.0', 'djangorestframework>=3.11.0,<4.0.0']

setup_kwargs = {
    'name': 'drf-dropdown',
    'version': '0.3.2',
    'description': 'Dropdown population implementation for Django REST Framework',
    'long_description': "# drf-dropdown\n\n![GitHub](https://img.shields.io/github/license/earthpyy/drf-dropdown)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/earthpyy/drf-dropdown/CI)\n![PyPI](https://img.shields.io/pypi/v/drf-dropdown)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drf-dropdown)\n![Django Version](https://img.shields.io/badge/django-3.0%20%7C%203.1%20%7C%203.2-blue)\n![Django REST Version](https://img.shields.io/badge/djangorestframework-3.11%20%7C%203.12-blue)\n![Pre-commit Enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)\n\nDropdown population implementation for Django REST Framework\n\n## Usage\n\n### Add `DropdownView` to API URL\n\n```python\n# urls.py\nimport dropdown\n\nurlpatterns = [\n    ...\n    path('dropdown/', dropdown.DropdownView.as_view(), name='dropdown'),\n]\n```\n\n### Define new dropdown\n\n```python\n# someapp/dropdown.py\nimport dropdown\n\n@dropdown.register\ndef users(query='', **kwargs):\n    return dropdown.from_model(User, label_field='email')\n```\n\n## Development\n\n### Set Up\n\n```bash\nmake setup\n```\n",
    'author': 'Preeti Yuankrathok',
    'author_email': 'preetisatit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/earthpyy/drf-dropdown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
