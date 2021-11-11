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
    'version': '2021.11.11.1',
    'description': 'Twitter Space archive helper script',
    'long_description': "# Twspace-dl\n\nA python script to download twitter space.\n\n## Install\n\n### From source\n```bash\ngit clone --depth 1 https://github.com/Ryu1845/twspace-dl\ncd twspace-dl\npip install .\n```\n\n### From PyPI\n```bash\npip install twspace-dl\n```\n\n## Usage\n```bash\ntwspace_dl -i space_url\n```\n\n## Features\nHere's the output of the help option\n```\nusage: twspace_dl [-h] [-t THREADS] [-v] [-s] [-k] [-i SPACE_URL] [-d DYN_URL] [-f URL] [-o FORMAT_STR] [-m] [-p] [-u]\n\nScript designed to help download twitter spaces\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -t THREADS, --threads THREADS\n                        number of threads to run the script with(default with max)\n  -v, --verbose\n  -s, --skip-download\n  -k, --keep-files\n\ninput:\n  -i SPACE_URL, --input-url SPACE_URL\n  -d DYN_URL, --from-dynamic-url DYN_URL\n                        use the master url for the processes(useful for ended spaces)\n  -f URL, --from-master-url URL\n                        use the master url for the processes(useful for ended spaces)\n\noutput:\n  -o FORMAT_STR, --output FORMAT_STR\n  -m, --write-metadata  write the full metadata json to a file\n  -p, --write-playlist  write the m3u8 used to download the stream(e.g. if you want to use another downloader)\n  -u, --url             display the master url\n```\n\n## Format\nYou can use the following identifiers for the formatting\n```\n%(title)s\n%(id)s\n%(start_date)s\n%(creator_name)s\n%(creator_screen_name)s\n%(url)s\n```\nExample:\xa0`[%(creator_screen_name)s]-%(title)s|%(start_date)s`\n",
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
