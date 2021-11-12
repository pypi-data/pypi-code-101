# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jirajumper', 'jirajumper.cache', 'jirajumper.commands', 'jirajumper.fields']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=1.11.1,<2.0.0',
 'click<8.0.0',
 'documented>=0.1.1,<0.2.0',
 'graphviz>=0.18,<0.19',
 'jira>=3.1.1,<4.0.0',
 'more-itertools>=8.10.0,<9.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'rich>=10.12.0,<11.0.0',
 'stringcase>=1.2.0,<2.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['jj = jirajumper:app']}

setup_kwargs = {
    'name': 'jirajumper',
    'version': '0.1.6',
    'description': 'Yet another JIRA issue manager CLI with emphasis on task chains.',
    'long_description': '# jeeves-jira\n\n[![Build Status](https://github.com/jeeves-sh/jeeves-jira/workflows/test/badge.svg?branch=master&event=push)](https://github.com/jeeves-sh/jeeves-jira/actions?query=workflow%3Atest)\n[![codecov](https://codecov.io/gh/jeeves-sh/jeeves-jira/branch/master/graph/badge.svg)](https://codecov.io/gh/jeeves-sh/jeeves-jira)\n[![Python Version](https://img.shields.io/pypi/pyversions/jeeves-jira.svg)](https://pypi.org/project/jeeves-jira/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nYet another JIRA issue manager CLI with emphasis on task chains.\n\n\n## Features\n\n- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)\n- Add yours!\n\n\n## Installation\n\n```bash\npip install jirajumper\n```\n\n\n## License\n\n[MIT](https://github.com/jeeves-sh/jeeves-jira/blob/master/LICENSE)\n\n\n## Credits\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [86ec1f15472f7c9f634cdbaa0d33eddf166888b2](https://github.com/wemake-services/wemake-python-package/tree/86ec1f15472f7c9f634cdbaa0d33eddf166888b2). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/86ec1f15472f7c9f634cdbaa0d33eddf166888b2...master) since then.\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anatoly-scherbakov/jirajumper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
