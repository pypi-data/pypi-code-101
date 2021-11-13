# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twspace_dl']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['twspace_dl = twspace_dl.__main__:main']}

setup_kwargs = {
    'name': 'twspace-dl',
    'version': '2021.11.13.0',
    'description': 'Twitter Space archive helper script',
    'long_description': '<div align="center">\n  <h1 id="twspace-dl">Twspace-dl</h1>\n  <p>\n    <a href="https://pypi.org/project/twspace-dl/">\n      <img src="https://img.shields.io/pypi/v/twspace-dl?style=for-the-badge" alt="PyPI">\n    </a>\n    <a href="https://pypi.org/project/twspace-dl/">\n      <img src="https://img.shields.io/pypi/dm/twspace-dl?label=DOWNLOADS%20%28PYPI%29&amp;style=for-the-badge" alt="PyPI DLs">\n    </a>\n    <a href="https://github.com/Ryu1845/twspace-dl/releases">\n      <img src="https://img.shields.io/github/downloads/Ryu1845/twspace-dl/total?label=DOWNLOADS%20%28GITHUB%29&amp;style=for-the-badge" alt="Github Releases DLs">\n    </a>\n  </p>\n  <p>A python script to download twitter spaces.</p>\n</div>\n\n## Requirements\n\nffmpeg\n\n## Install\n\n### From source\n```bash\ngit clone --depth 1 https://github.com/Ryu1845/twspace-dl\ncd twspace-dl\npip install .\n```\n\n### From PyPI\n```bash\npip install twspace-dl\n```\n\n## Usage\n```bash\ntwspace_dl -i space_url\n```\n\n## Features\nHere\'s the output of the help option\n```\nusage: twspace_dl [-h] [-t THREADS] [-v] [-s] [-k] [-i SPACE_URL] [-U USER_URL] [-d DYN_URL] [-f URL]\n                  [-o FORMAT_STR] [-m] [-p] [-u]\n\nScript designed to help download twitter spaces\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -t THREADS, --threads THREADS\n                        number of threads to run the script with(default with max)\n  -v, --verbose\n  -s, --skip-download\n  -k, --keep-files\n\ninput:\n  -i SPACE_URL, --input-url SPACE_URL\n  -U USER_URL, --user-url USER_URL\n  -d DYN_URL, --from-dynamic-url DYN_URL\n                        use the master url for the processes(useful for ended spaces)\n  -f URL, --from-master-url URL\n                        use the master url for the processes(useful for ended spaces)\n\noutput:\n  -o FORMAT_STR, --output FORMAT_STR\n  -m, --write-metadata  write the full metadata json to a file\n  -p, --write-playlist  write the m3u8 used to download the stream(e.g. if you want to use another downloader)\n  -u, --url             display the master url\n```\n\n## Format\nYou can use the following identifiers for the formatting\n```\n%(title)s\n%(id)s\n%(start_date)s\n%(creator_name)s\n%(creator_screen_name)s\n%(url)s\n```\nExample:\xa0`[%(creator_screen_name)s]-%(title)s|%(start_date)s`\n\n## Service\nThere\'s an example service file [there](https://github.com/Ryu1845/twspace-dl/blob/main/twspace-dl@.service)\nYou\'ll have to modify different stuff depending on how you installed or not the script.\n\nI\'d be very grateful if someone made a PR with a bash script automating those ;)\n\n### Cloned Repository\nIn that case, you\'ll have to modify the `WorkingDirectory` to where you cloned the repo.\n\n### Pip\n1. Change `WorkingDirectory` to where you want the spaces to be downloaded.\n2. Find where your executable is by running `which twspace_dl` in your terminal.\n3. Change the `/usr/bin/python twspace_dl` part to the path of your executable.\n\n\nNow to install the service, you can either install it as a user service(recommended if on your personal desktop), or as a normal service.\n\n### User\n1. Copy the file you modified earlier to `~/.config/systemd/user`(create the systemd directory if it doesn\'t exist).\n2. run\n\n``` bash\nsystemctl --user daemon-reload\nsystemctl --user start twspace-dl@USER_ID.service\n```\n`USER_ID` is the part after `https://twitter.com/` in the url of a twitter profile (i.e `https://twitter.com/USER_ID`)\n\nTo keep it working after restarts run:\n\n``` bash\nsystemctl --user enable twspace-dl@USER_ID.service\n```\n\n### System\n1. Copy the file you modified earlier to `/etc/systemd/system`.\n2. run\n\n``` bash\nsudo systemctl daemon-reload\nsudo systemctl start twspace-dl@USER_ID.service\n```\n`USER_ID` is the part after `https://twitter.com/` in the url of a twitter profile (i.e `https://twitter.com/USER_ID`)\n\nTo keep it working after restarts run:\n\n``` bash\nsudo systemctl enable twspace-dl@USER_ID.service\n```\n',
    'author': 'Ryu1845',
    'author_email': 'ryu@tpgjbo.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
