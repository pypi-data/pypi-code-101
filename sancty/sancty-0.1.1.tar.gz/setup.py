# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sancty', 'sancty.patch_blessed']

package_data = \
{'': ['*']}

install_requires = \
['blessed==1.19.0', 'cwcwidth>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'sancty',
    'version': '0.1.1',
    'description': 'Sancty is an extension to jquast/blessed for simple editor-like terminal apps',
    'long_description': '# Sancty\nSancty is an extension to jquast/blessed for simple editor-like terminal apps\n\n### Usage\n\nSancty has two major components, `Reader` (which follows the `ReaderProtocol`) and `Renderer` (which follows the `RendererProtocol`). As you are free to choose your own communication channel and event loop/threading architecture, these do not work out of the box. For implementations that work out of the box, take a look at `ProcessReader` and `ProcessRenderer`, which use standard `multiprocessing` classes to each run on their own thread. You can also spin up a basic editor by running `start_terminal()`.\n\nIf you don\'t want to customize the run architecture, but _do_ want to customize the `Reader` and `Renderer` classes, simply extend them (but be sure to still conform to their respective protocols) and pass the classes as variables to `start_terminal()`.\n\nYou can also pass a custom `replace_dict`, which is a dictionary of all possible `\\\\` commands. By default, the key swill correspond to strings that will be replaced by the value strings, but if the key is an integer, a custom `special_slash_fn` can also be passed to perform arbitrary transformations of the render array. Note that all negative numbers are reserved for this program.\n\n#### Default `\\\\` commands\n\n```python\ndefault_replace_dict = {\n    "clr": (-1, "Clears all text"),\n    "help": (-2, "Shows all slash commands"),\n}\n```',
    'author': 'Tip ten Brink',
    'author_email': '75669206+tiptenbrink@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
