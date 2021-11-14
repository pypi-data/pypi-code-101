# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['burgeon']

package_data = \
{'': ['*']}

install_requires = \
['watchgod>=0.7,<0.8']

setup_kwargs = {
    'name': 'burgeon',
    'version': '0.1.1',
    'description': '',
    'long_description': 'Burgeon - Python Code Reloading\n-------------------------------\n\nThis project exposes one function -- `with_reloading` -- which is used to run a\nsingle callable. This callable gets run in a separate thread which gets\nrestarted whenever a Python source file from the current working directory down\nchanges. This improves the development cycle by removing the need to manually\nrestart long running services whenever its source code changes.\n\n> Burgeon: To grow or develop rapidly; expand or proliferate.\n\nExample Usage\n=============\n\n.. code-block:: python\n\n    from burgeon import with_reloading\n\n\n    def my_function():\n        while True:\n            print("hello")\n\n    with_reloading(func)\n\nThe function above demonstrates a minimal example of using `with_reloading`.\nOnce the code is executed, any changes to the file (that get saved) will notify\n`burgeon` to restart the thread running the function and execute the new\nchanges.\n\nAcknowledgements\n================\n\nThis implementation of Python file reloading uses watchgod and is heavily based\noff the `BaseReload` class in the `uvicorn`_ repository. For context, this is\nhow uvicorn implements its own development server reloading. This project\nsimplifies the implementation and exposes the reloading functionality via a\nsimple and opinionated interface.\n\n.. _uvicorn: https://github.com/encode/uvicorn',
    'author': 'Uriel Mandujano',
    'author_email': 'uriel.mandujano14@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
