# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ns_poet', 'ns_poet.package_targets']

package_data = \
{'': ['*']}

install_requires = \
['astor>=0.8.1,<0.9.0',
 'click>=8.0.3,<9.0.0',
 'networkx<2.6',
 'setuptools>=58.5.3,<59.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['nspoet = ns_poet.cli:cli']}

setup_kwargs = {
    'name': 'ns-poet',
    'version': '0.2.0',
    'description': 'Autogenerate Poetry package manifests in a monorepo',
    'long_description': '# ns-poet\n[![](https://img.shields.io/pypi/v/ns_poet.svg)](https://pypi.org/pypi/ns_poet/) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n\nAutogenerate Poetry package manifests in a monorepo\n\nFeatures:\n\n- <!-- list of features -->\n\nTable of Contents:\n\n- [Installation](#installation)\n- [Guide](#guide)\n- [Development](#development)\n\n## Installation\n\nns-poet requires Python 3.6 or above.\n\n```bash\npip install ns-poet\n# or\npoetry add ns-poet\n```\n\n## Guide\n\n<!-- Subsections explaining how to use the package -->\n\n## Development\n\nTo develop ns-poet, install dependencies and enable the pre-commit hook:\n\n```bash\npip install pre-commit poetry\npoetry install\npre-commit install -t pre-commit -t pre-push\n```\n\nTo run tests:\n\n```bash\npoetry run pytest\n```\n',
    'author': 'Jonathan Drake',
    'author_email': 'jdrake@narrativescience.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NarrativeScience/ns-poet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.5,<4.0.0',
}


setup(**setup_kwargs)
