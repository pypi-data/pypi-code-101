# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyasn1',
 'pyasn1.codec',
 'pyasn1.codec.ber',
 'pyasn1.codec.cer',
 'pyasn1.codec.der',
 'pyasn1.codec.native',
 'pyasn1.compat',
 'pyasn1.type']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysnmp-pyasn1',
    'version': '0.4.9',
    'description': 'ASN.1 types and codecs',
    'long_description': None,
    'author': 'rfaircloth-splunk',
    'author_email': 'rfaircloth@splunk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pysnmp/pyasn1',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
