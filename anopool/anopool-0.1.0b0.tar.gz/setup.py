# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anopool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'anopool',
    'version': '0.1.0b0',
    'description': 'Generic thread-safe sync and async object pools.',
    'long_description': 'AnoPool\n=======\n\n|PyPI| |Build Status|\n\n``anopool`` is a generic thread-safe sync and async object pool implementation.\nbecause I got tired of writing the same code over and over again.\n\nInstall\n-------\n\n.. code:: bash\n\n   pip install anopool\n\nUsage\n-----\n\n.. code:: python\n\n   #TODO\n\nLicense\n-------\n\nMIT License\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/anopool.svg\n   :target: https://pypi.python.org/pypi/anopool\n.. |Build Status| image:: https://travis-ci.org/willtrnr/anopool.svg?branch=master\n   :target: https://travis-ci.org/willtrnr/anopool\n',
    'author': 'William Turner',
    'author_email': 'william.turner@aero.bombardier.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/willtrnr/anopool',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
