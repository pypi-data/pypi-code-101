# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['netdevsnmp',
 'netdevsnmp.hostinfo',
 'netdevsnmp.oids',
 'netdevsnmp.vendors',
 'netdevsnmp.vendors.airespace',
 'netdevsnmp.vendors.alcatel',
 'netdevsnmp.vendors.arbor',
 'netdevsnmp.vendors.arista',
 'netdevsnmp.vendors.cisco',
 'netdevsnmp.vendors.ericsson',
 'netdevsnmp.vendors.extreme',
 'netdevsnmp.vendors.hpe',
 'netdevsnmp.vendors.huawei',
 'netdevsnmp.vendors.juniper',
 'netdevsnmp.vendors.metamako',
 'netdevsnmp.vendors.synology']

package_data = \
{'': ['*']}

install_requires = \
['pysnmp>=4.3.1']

setup_kwargs = {
    'name': 'netdevsnmp',
    'version': '1.0.0',
    'description': 'A wrapper module for pysnmp to get device information',
    'long_description': 'NetDevSNMP\n==========\n\nNetdevsnmp is based on Nelsnmp and is a wrapper around pysnmp to make it easier to use SNMP against network equipment.\n',
    'author': 'Rob Woodward',
    'author_email': 'rob@emailplus.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/robwdwd/netdevsnmp',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
