# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymultimonitor',
 'pymultimonitor.cinterface',
 'pymultimonitor.cinterface.constants',
 'pymultimonitor.cinterface.functions',
 'pymultimonitor.cinterface.functions.winuser',
 'pymultimonitor.cinterface.structures',
 'pymultimonitor.cinterface.structures.displaydevicesreference',
 'pymultimonitor.cinterface.structures.displaydevicesreference.wingdi',
 'pymultimonitor.cinterface.structures.monitorconfiguration',
 'pymultimonitor.cinterface.structures.monitorconfiguration.physicalmonitorenumerationapi',
 'pymultimonitor.core',
 'pymultimonitor.output']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pymultimonitor',
    'version': '0.2.0',
    'description': '',
    'long_description': "# PyMultiMonitor\n\nThis module can be used to interact with Windows Display. Currently, it supports:\n\n- Getting and setting current display topology (i.e. CLONE, EXTERNAL, INTERNAL, EXTENDED)\n- Getting display name\n- Getting and setting current display brightness\n\n## Example\n\n### Getting current display topology\n\n```python\n>>> from pymultimonitor.core.DisplayTopology import DisplayTopology\n>>> from pymultimonitor.cinterface.constants import DisplayConfigTopology\n>>> dt = DisplayTopology()\n>>> dt.get_display_topology()\n< DisplayConfigTopology.DISPLAYCONFIG_TOPOLOGY_EXTEND: 4 >\n>>> dt.get_display_topology() == DisplayConfigTopology.DISPLAYCONFIG_TOPOLOGY_EXTEND\nTrue\n```\n\n### Setting display topology\n\n```python\n>>> from pymultimonitor.core.DisplayTopology import DisplayTopology\n>>> from pymultimonitor.cinterface.constants import DisplayConfigTopology\n>>> dt = DisplayTopology()\n>>> dt.set_topology_extend()\n>>> dt.get_display_topology() == DisplayConfigTopology.DISPLAYCONFIG_TOPOLOGY_EXTEND\nTrue\n>>> dt.set_topology_external()\n>>> dt.get_display_topology() == DisplayConfigTopology.DISPLAYCONFIG_TOPOLOGY_EXTERNAL\nTrue\n```\n\n### Getting current display device friendly name\n\n```python\n>>> from pymultimonitor.core.DisplayInfo import DisplayInfo\n>>> di = DisplayInfo()\n>>> di.get_display_names()\n{'\\\\\\\\.\\\\DISPLAY1': 'LG ULTRAWIDE'}\n```\n\n### Getting and setting current display brightness for a particular monitor\n\n```python\n>>> from pymultimonitor.core.DisplayMonitors import DisplayMonitors\n>>> dm = DisplayMonitors()\n>>> physical_monitors = dm.get_physical_monitor_handles()\n>>> physical_monitors\n[PhysicalMonitor(hPhysicalMonitor=1, szPhysicalMonitorDescription='Generic PnP Monitor')]\n>>> from pymultimonitor.core.DisplayBrightness import DisplayBrightness\n>>> db = DisplayBrightness()\n>>> db.get_display_brightness_for_monitor(physical_monitors[0])\nBrightness(minimum=0, current=20, maximum=100)\n>>> db.set_display_brightness_for_monitor(physical_monitors[0], 50)\n```",
    'author': 'debakarr',
    'author_email': 'debakar.roy@intel.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Dibakarroy1997/pymultimonitor',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
