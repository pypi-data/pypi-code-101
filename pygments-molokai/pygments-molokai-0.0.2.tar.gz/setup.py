# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygments_molokai']

package_data = \
{'': ['*']}

entry_points = \
{'pygments.styles': ['molokai = pygments_molokai.molokai:MolokaiStyle']}

setup_kwargs = {
    'name': 'pygments-molokai',
    'version': '0.0.2',
    'description': 'A Pygments style providing the Molokai colour scheme.',
    'long_description': "=======================\nPygments Molokai Plugin\n=======================\n\nThis Python package can be used to add the Molokai colour theme to Pygments.  It was generated from the `Vim Molokai plugin`_ using the `Vim Colorscheme Converter`_.  Once installed, a Pygments style named 'molokai' will become available.\n\n.. image:: https://raw.githubusercontent.com/gbpoole/gbpoole.github.io/main/assets/screen_shots/pygments_molokai_screen_shot.png\n  :alt: Pygments Molokai Screen Shot\n  :align: center\n\n.. _`Vim Molokai plugin`: https://github.com/tomasr/molokai\n\n.. _`Vim Colorscheme Converter`: https://github.com/honza/vim2pygments\n\nInstall\n=======\n\nWith Pygments installed, the Molokai style can be added as follows:\n\nUsing PyPI and pip\n------------------\n\nThe easiest way is to use 'pip':\n::\n\n    $ pip install pygments_molokai\n\n\nManual\n------\n\nFor those who want to work from code, you can install the Molokai theme manually.  First make sure that Poetry is installed (see `here`).  Then:\n::\n\n    $ git clone git://github.com/gbpoole/pygments-molokai.git\n    $ cd pygments-molokai\n    $ poetry install\n\n.. _here: https://python-poetry.org/docs/#installation\n\nUsage examples\n==============\n\nFrom Python:\n::\n\n    >>> from pygments.formatters import HtmlFormatter\n    >>> HtmlFormatter(style='molokai').style\n    <class 'pygments_style_molokai.MolokaiStyle'>\n\n\nor from the command line:\n::\n\n    pygmentize -g -O style=molokai <FILENAME>\n\nHelp\n====\n\nMore information about Pygment styles can be found at the `official Pygments documentation`_ page.\n\n.. _official Pygments documentation: https://pygments.org/docs/styles/\n\n",
    'author': 'Gregory Poole',
    'author_email': 'gbpoole@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gbpoole/pygments-molokai',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
