# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zerochan']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'zerochan',
    'version': '0.5.0',
    'description': 'Python library and download cli util for https://www.zerochan.net',
    'long_description': '# Zerochan\n\nLibrary for Zerochan.net with pics parsing and downloader included!\n\n## Features\n* CLI utility for pics downloading from zerochan.net\n* Library for create custom downloader (you can write own) or data analyze.\n* Strong typed!\n\n## Installation:\n\n### Using pip\n`pip install zerochan`\n### Using poetry\n`poetry add zerochan`\n\n## Using as downloader tool:\n\nAfter install you can call zerochan by command `python -m zerochan`\n\n\n## Using as library: \n\nFirst, you should create `Zerochan` instance:\n```python\nfrom zerochan import ZeroChan\n\nzerochan_instance = ZeroChan()\n```\n\nNow, you can set some args for request\n\n```python\nfrom zerochan import ZeroChan, PictureSize, SortBy\n\nzerochan = ZeroChan()\n\nzerochan.search("Spain")  # Set title to search\nzerochan.size(PictureSize.BIGGER_AND_BETTER) # Set quality and pic size\nzerochan.sort(SortBy.POPULAR) # Set sorting (now only popular)\nzerochan.page(1) # Page to parse\nzerochan.authorize("hjsaf7afkjsaf78", "127364") # Authorize by z_hash and z_id in cookies\n```\n\n...or set args like this:\n\n```python\nzerochan.search("Spain")\\\n    .size(PictureSize.BIGGER_AND_BETTER)\\\n    .sort(SortBy.POPULAR)\n```\n\nAfter all settings, you should call `.pics()` to get pics:\n\n```python\ndata = zerochan.pics()\nfor img in data.images:\n    print(img.url)\n```',
    'author': 'kiriharu',
    'author_email': 'kiriharu@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kiriharu/zerochan',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
