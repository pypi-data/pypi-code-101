# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_imports', 'py_imports.base']

package_data = \
{'': ['*']}

install_requires = \
['pyflakes==2.4.0']

setup_kwargs = {
    'name': 'py-imports',
    'version': '1.0.0',
    'description': 'Python Toolkit to imports introspection',
    'long_description': '\n![Py-Imports](https://github.com/AndresBena19/py-imports/blob/develop/img/icon-import-py.png?raw=true )\n<p align="center">\n    <em>Parse imports from .py file in a flexible way</em>\n</p>\n<p align="center">\n<a href="https://github.com/andresbena19/py-imports/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">\n    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">\n</a>\n<a href="https://codecov.io/gh/andresbena19/py-imports" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/andresbena19/py-imports" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/py-imports" target="_blank">\n    <img src="https://img.shields.io/pypi/v/py-imports?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/py-imports" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/py_imports.svg?color=%2334D058" alt="Supported Python versions">\n</a>\n</p>\n\n\n---\n\n**Source Code**: <a href="https://github.com/andresbena19/py-imports" target="_blank"> https://github.com/andresbena19/py-imports\n</a>\n## Requirements\n\nPython 3.7+\n\npy-imports stands on the shoulders of giants:\n\n* <a href="https://docs.python.org/3/library/ast.html" class="external-link" target="_blank">ast — Abstract Syntax Trees</a> to traverse python code.\n\n## Installation\n\n<div class="termy">\n\n```console\n$ pip install py-imports\n\n---> 100%\n\nAll it\'s ready to begin \n```\n\n</div>\n\n## Example\n\n### Introspect it\n\n* Create a file `main.py` with:\n\n```Python\nfrom py_imports.manager import PyImports\n\nmyself = "main.py"\n\n# Let\'s introspect myself\nwith PyImports() as manager:\n    manager.get_imports(myself)\n    imports = manager.imports_resume()\n\n\n# Now you have access to the imports used in each file \nprint(imports)\n{\n \'main.py\': <py_imports.base.models.ImportsCollectionFile object at 0x10b889220>\n}\n\n# Get details about the absolute, relative and standard imports in the file\ncollector_object = imports.get(myself)\nabsolute_imports = collector_object.absolute_imports\nrelative_imports = collector_object.relative_imports\nimports = collector_object.imports\n\n# It\'s obvious that in this file there are just one absolute import\n#  --- from py_imports.manager import PyImports ---\n# If we introspect the object, we will get the next\n\nfirst_import = absolute_imports[0]\nfirst_import.childs -> [\'PyImports\']\nfirst_import.parent -> \'py_imports.manager\'\nfirst_import.statement -> \'from py_imports.manager import PyImports\'\nfirst_import.level -> 0\nfirst_import.line -> 1\n\n# Now you know more about you...\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Andres',
    'author_email': 'andresbenavides404@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AndresBena19/py-imports.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
