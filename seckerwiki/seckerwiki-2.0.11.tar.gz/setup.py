# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seckerwiki', 'seckerwiki.commands', 'seckerwiki.scripts']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'pdf2image>=1.16.0,<2.0.0',
 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['wiki = seckerwiki.wiki:main']}

setup_kwargs = {
    'name': 'seckerwiki',
    'version': '2.0.11',
    'description': 'A collection of scripts used to manage my personal Foam workspace',
    'long_description': '# Seckerwiki Scripts\n\nThis package is a CLI that helps me manage my markdown-based [Foam](https://foambubble.github.io/) workspace, or my "Personal Wiki".\nI store everything in my wiki, from journal entries to uni notes.\n\n## Installation\n\nVersion `1.x` had requirements for extra dependencies to get the lecture-to-markdown converter working properly. Since I no longer go to uni, I don\'t need those scripts anymore, so the installation is as simple as:\n\n```\npip3 install seckerwiki\n```\n\nOnce installed, run this command to generate the config files:\n\n```\nwiki setup\n```\n\n## Commands\n\n### Setup\n\nThis command does a couple of things:\n\n- Creates a `config.yml` file in `~/.config/seckerwiki`, which is used to configure some things in the repo.\n- Creates a `credentials` file in `~/.config/seckerwiki/`, which stores secrets.\n\nEdit the credentials file to add a secret passsword used for decrypting your Journal (see below).\n\n### log \n\nAlias for git log, with some pretty graph options.\n\n### status\n\nRuns `git status`. Basically just a convenience function, so you don\'t have to `cd` into a wiki dir.\n\n### commit \n\ndoes a git commit, generating a commit message. If there are a number of staged files, the commit header shows the top level folders instead.\n\nArgs:\n\n- `-y`: skip verification and commit\n- `-a`: also do `git add --all`\n\n### sync\n\nperform a `git pull` (rebase) then `git push`\n\n### journal\n\nI use my wiki to store encrypted journal entries.\n\nRun `wiki journal` to generate a new empty journal entry in the journal folder specified in the settings. `wiki journal --encrypt` replaces all the `.md` files with `.md.asc` files, encrypting the files with a symmetric key specified in the settings. `wiki journal --decrypt [filename]` decrypts a file in the encrypted journal directory and prints it to stdout.\n\n### toc\n\nGenerates a table of contents for other files/subfolders the markdown file is.\n\nAdd the following tags to the "contents/readme" page in each subfolder:\n\n```\n<!--BEGIN_TOC-->\n<!--END_TOC-->\n```\n\nThe script will replace the content between these two tags with the contents. For example:\n\n```\n<!--BEGIN_TOC-->\nPages:\n- [hardware](./hardware.md)\n- [iot-development](./iot-development.md)\n- [iot-platforms](./iot-platforms.md)\n- [platformio-esp32-notes](./platformio-esp32-notes.md)\n- [rtoses](./rtoses.md)\n\n<!--END_TOC-->\n```\n\n### stats\n\nPrints some cool stats about the wiki:\n\n- `commits made` - number of git commits since repo was created\n- `Number of notes` - number of markdown files in repo\n- `total lines` - non-empty lines in `.md` files\n- `largest files` - paths to the top 3 longest `.md` files\n\n\n## Developing\n\nI use [poetry](https://python-poetry.org/) for building/publishing the package. Read their docs.',
    'author': 'Benjamin Secker',
    'author_email': 'benjamin.secker@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bsecker/wiki/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
