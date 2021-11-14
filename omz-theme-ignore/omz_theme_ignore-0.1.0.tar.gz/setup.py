# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omz_theme_ignore']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['omz_theme_ignore = omz_theme_ignore.main:main']}

setup_kwargs = {
    'name': 'omz-theme-ignore',
    'version': '0.1.0',
    'description': 'Easy add current random theme to ZSH_THEME_RANDOM_IGNORED section in .zshrc file.',
    'long_description': '# omz_ignore_theme\n\nAdd current RANDOM_THEME from oh-my-zsh to the .zshrc file to the ZSH_RANDOM_IGNORE_THEME section. Use via zsh alias via source:\n\n`alias it="python3 omz_theme_ignore/main.py $RANDOM_THEME"`\n\nor via package after installing via pip:\n\n`python3 -m pip install omz_theme_ignore`\n\n`alias it="omz_theme_ignore $RANDOM_THEME"`\n',
    'author': 'PaterIT',
    'author_email': 'paterit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/paterit/omz_ignore_theme',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
