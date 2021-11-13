# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyasn1_modules']

package_data = \
{'': ['*']}

install_requires = \
['pysnmp-pyasn1>=0.4.11,<0.5.0']

setup_kwargs = {
    'name': 'pysnmp-pyasn1-modules',
    'version': '0.2.9',
    'description': 'A collection of ASN.1-based protocols modules.',
    'long_description': '\nASN.1 modules for Python\n------------------------\n[![PyPI](https://img.shields.io/pypi/v/pyasn1-modules.svg?maxAge=2592000)](https://pypi.org/project/pyasn1-modules)\n[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1-modules.svg)](https://pypi.org/project/pyasn1-modules/)\n[![Build status](https://travis-ci.org/etingof/pyasn1-modules.svg?branch=master)](https://travis-ci.org/etingof/pyasn1-modules)\n[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pyasn1-modules.svg)](https://codecov.io/github/etingof/pyasn1-modules/)\n[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pyasn1-modules/master/LICENSE.txt)\n\nThe `pyasn1-modules` package contains a collection of\n[ASN.1](https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-X.208-198811-W!!PDF-E&type=items)\ndata structures expressed as Python classes based on [pyasn1](https://github.com/pysnmp/pyasn1)\ndata model.\n\nIf ASN.1 module you need is not present in this collection, try using\n[Asn1ate](https://github.com/kimgr/asn1ate) tool that compiles ASN.1 documents\ninto pyasn1 code.\n\nFeedback\n--------\n\nIf something does not work as expected, \n[open an issue](https://github.com/pysnmp/pyasn1-modules/issues) at GitHub\nor post your question [on Stack Overflow](https://stackoverflow.com/questions/ask)\n \nNew modules contributions are welcome via GitHub pull requests.\n\nCopyright (c) 2005-2020, [Ilya Etingof](mailto:etingof@gmail.com).\nAll rights reserved.\n',
    'author': 'rfaircloth-splunk',
    'author_email': 'rfaircloth@splunk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
