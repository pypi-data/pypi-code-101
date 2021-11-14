# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gitjirabot']

package_data = \
{'': ['*']}

install_requires = \
['atlassian-python-api>=3.14.1,<4.0.0', 'python-gitlab>=2.10.1,<3.0.0']

entry_points = \
{'console_scripts': ['gitjirabot = gitjirabot.cli:main']}

setup_kwargs = {
    'name': 'gitjirabot',
    'version': '0.1.5',
    'description': 'Git Jira integrations bot for automating complex tasks',
    'long_description': '# GitJiraBot\n\n[![pipeline status](https://gitlab.com/mikeramsey/gitjirabot/badges/main/pipeline.svg)](https://gitlab.com/mikeramsey/gitjirabot/pipelines)\n[![coverage report](https://gitlab.com/mikeramsey/gitjirabot/badges/main/coverage.svg)](https://gitlab.com/mikeramsey/gitjirabot/commits/master)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mikeramsey.gitlab.io/gitjirabot/)\n[![pypi version](https://img.shields.io/pypi/v/gitjirabot.svg)](https://pypi.org/project/gitjirabot/)\n[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/gitjirabot/community)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nGit Jira integrations bot for automating complex tasks\n\n## Requirements\n\nGitJiraBot requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.12\n\n# make it available globally\npyenv global system 3.6.12\n```\n</details>\n\n## Installation\n\nWith `pip`:\n```bash\npython3.6 -m pip install gitjirabot\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npython3.6 -m pip install --user pipx\n\npipx install --python python3.6 gitjirabot\n```\n',
    'author': 'Michael Ramsey',
    'author_email': 'mike@hackerdise.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mikeramsey/gitjirabot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
