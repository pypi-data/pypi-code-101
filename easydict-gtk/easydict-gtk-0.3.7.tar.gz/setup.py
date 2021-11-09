# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easydict_gtk']

package_data = \
{'': ['*'], 'easydict_gtk': ['data/*', 'images/*', 'ui/*']}

install_requires = \
['PyGObject>=3.42.0,<4.0.0',
 'orjson>=3.6.4,<4.0.0',
 'pycairo>=1.20.1,<2.0.0',
 'tinydb>=4.5.2,<5.0.0']

entry_points = \
{'console_scripts': ['easydict-gtk = easydict_gtk.easydict:main']}

setup_kwargs = {
    'name': 'easydict-gtk',
    'version': '0.3.7',
    'description': 'The first open source translator which is completely open with dictionary data too.',
    'long_description': '# EasyDict\nThe first open source translator which is completely open with dictionary data too. The homepage is http://easydict.jiri.one. On this page you can also try the search results, which will be the same as in the app (however, the web application does not use TinyDB+orjson as a backend, but uses RethinkDB - the source data is the same). \n**The application is at an early stage of development, but the features and dictionaries that have already been implemented work very well.**\n\n## What is it\n\nEasyDict is a simple translator that will translate, typically, one word in one language into another language. This translator has several, sometimes unique, features. \n\n1. It is written in Python.\n2. It uses the fastest json implementation for storing dictionaries - [orjson](https://github.com/ijl/orjson) (own orjson storage for [TinyDB](https://tinydb.readthedocs.io)).\n3. The user interface is written in [PyGObject](https://pygobject.readthedocs.io) (GTK3.0).\n4. The application starts hidden in tray and tapping tray brings up the main application window - [xapp](https://github.com/linuxmint/xapp) library is used.\n5. If you have the main application window displayed, it is displayed on top and overlays all other windows. In this mode, the app monitors the clipboard and automatically translates the words you copy into it.\n6. You can use either a whole word search or a full-text.\n\n## Currently available dictionaries\nCurrently only Czech-English and English-Czech dictionaries are available. This dictionary data comes from the http://svobodneslovniky.cz project (the dictionary data is therefore governed by the GNU/FDL license).\n\nScreenshots\n---\n\n\n| Welcome Screen| Search Screen |\n| -------- | -------- |\n| ![](https://i.imgur.com/aTeNxq7.png)     | ![](https://i.imgur.com/tWvsQeQ.png)     |\n\nHow to install it and use it\n---\nBecause, the app is writen in Python, you can simply install from PyPi:\n`pip install easydict-gtk`\nand run it with:\n`easydict-gtk`\n\nDependencies:\n---\nEverything should be automatically installed by pip: tinydb, orjson, pycairo, PyGObject\n\nTo-Do-List\n---\n- [X] get the homepage https://easydict.jiri.one back online\n- [ ] create tests for backend\n- [ ] add the possibility to use other dictionaries\n- [ ] optimize the application for touch control so that it can be run on Phosh - https://puri.sm/projects/phosh/ using libhandy - https://gitlab.gnome.org/GNOME/libhandy\n- [X] ? maybe swith to poetry\n- [ ] create FlatPak package and publish it on FlatHub\n- [ ] create ArchLinux package an publish it on AUR\n- [ ] ...\n',
    'author': 'jiri.one',
    'author_email': 'nemec@jiri.one',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
