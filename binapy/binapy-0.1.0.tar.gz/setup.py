# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binapy',
 'binapy.compression',
 'binapy.encoding',
 'binapy.hashing',
 'binapy.parsing',
 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'binapy',
    'version': '0.1.0',
    'description': 'Binary Data manipulation, for humans.',
    'long_description': '# BinaPy\n\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/binapy">\n    <img src="https://img.shields.io/pypi/v/binapy.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/guillp/binapy/actions">\n    <img src="https://github.com/guillp/binapy/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://binapy.readthedocs.io/en/latest/?badge=latest">\n    <img src="https://readthedocs.org/projects/binapy/badge/?version=latest" alt="Documentation Status">\n</a>\n\n<a href="https://pyup.io/repos/github/guillp/binapy/">\n<img src="https://pyup.io/repos/github/guillp/binapy/shield.svg" alt="Updates">\n</a>\n\n</p>\n\n\n**BinaPy** is a module that makes Binary Data manipulation simpler and easier than what is offered in the Python standard library.\n\nWith BinaPy, encoding or decoding data in a number of formats (base64, base64url, hex, url-encoding, etc.), compressing or decompressing (gzip), hashing (SHA1, SHA256, MD5, etc., with or without salt), is all a single method call away! And you can extend it with new formats and features.\n\n```python\nfrom binapy import BinaPy\n\nbp = BinaPy("Hello, World!").compress_gzip().encode_b64u()\nprint(bp)\n# b\'eJzzSM3JyddRCM8vyklRBAAfngRq\'\nbp.decode_b64u().decompress_gzip().decode()\n# "Hello, World!"\nisinstance(bp, bytes)\n# True\n```\n\n* Free software: MIT\n* Documentation: <https://binapy.readthedocs.io>\n\n## Features\n\n- Fluent interface, based on a `bytes` subclass\n- Provides a convenient interface over `hashlib`, `base64`, `gzip`, `urllib.parse`, `json` and more\n- Easy to extend with new formats\n\n## TODO\n\n- add more parsing formats like YAML\n- optionally use faster third-party modules when available\n\n## Credits\n\nThis package template was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Guillaume Pujol',
    'author_email': 'guill.p.linux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/guillp/binapy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
