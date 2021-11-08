# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anime_cli', 'anime_cli.search']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'html5lib>=1.1,<2.0',
 'inquirerpy>=0.3.0,<0.4.0',
 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['anime-cli = anime_cli.__main__:main']}

setup_kwargs = {
    'name': 'anime-cli',
    'version': '0.3.3',
    'description': 'A python based anime cli, search, download watch animes. (Works on Windows too)',
    'long_description': "## Anime-cli\n\nA CLI for streaming, downloading anime shows.\nThe shows data is indexed through [GogoAnime](https://gogoanime.pe).\n\nPlease install [mpv video-player](https://mpv.io/installation/) for better experience and no ads.\n\nVersion 0.3.1+ works on android/Smart TV's see [usage instructions](#usage-android) below\n\nhttps://user-images.githubusercontent.com/81347541/137595104-0c0418e9-71b8-4c45-b507-78892cca961c.mp4\n\n### Usage\nIt's recommended to stream episodes using a video player (no ads)\nAlmost all video players all supported which can stream a m3u8 url. To achive this a proxy server is used.\n\nYou can install anime-cli from pip using\n```\npip install anime-cli\n```\nThen run using `python -m anime_cli` or simply `anime-cli`\n\nIf you want to help develop `anime-cli`. It is recommended that you clone the repo using and then install the dependencies\n```\ngit clone https://github.com/chirag-droid/anime-cli.git\npoetry install\n```\nand then to run, `poetry run anime-cli`\n\n### Usage Android\n- Download `Termux` from Fdroid\n- Download `mpv-player` from playstore\n\nIn termux install python using `pkg install python`\nFollow the same steps as above for downloading `anime-cli`\n\nWhen asked to enter the video-player change it to `xdg-open` which will automatically open `mpv-player`.\n\n### Motivation\n\nI recently found out about [ani-cli](https://github.com/pystardust/ani-cli), but it was not cross-platform because it was written in shell, so I decided to recreate that same thing in Python, hoping to make it cross-platform and possibly also have pretty UI.\n\n### TODO\n- [x] Stream on browser\n- [ ] Make streaming on browsers ad free\n- [x] Stream to video player like MPV\n- [ ] Ability to download the shows as mp4\n- [ ] Support for multiple mirrors\n",
    'author': 'Chirag Singla',
    'author_email': 'chirag.singla.pi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chirag-droid/anime-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
