# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smartthings_rest']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'smartthings-rest',
    'version': '0.1.2',
    'description': 'Smart and straightforward lib for controlling things with smartthings',
    'long_description': '# Smartthings-rest\n\nNOTE! work in progress\n\nSmart and straightforward lib for controlling things with <https://www.smartthings.com/>  \n\n- [Smartthings-rest](#smartthings-rest)\n- [simple json printout of all](#simple-json-printout-of-all)\n- [Turn device on](#turn-device-on)\n- [Turn device off](#turn-device-off)\n\n[Offical smartthings docs](https://developer-preview.smartthings.com/docs/getting-started/welcome)\n\n~~~py\n# simple json printout of all \nfrom smartthings_rest import SmartThings\n\nst = SmartThings(personal_access_token)\n\nprint(st.devices())\n\n~~~\n\n~~~sh\nexport PAT="your_pat"\npython3 hello_smartthings.py\n~~~\n\n~~~text\nUrls to add\n\nhttps://api.smartthings.com/v1/devices/deviceId/status\n\nhttps://api.smartthings.com/v1/devices/deviceId/components/main/capabilities/mediaInputSource/status\n\n---\n# Turn device on\nhttps://api.smartthings.com/v1/devices/deviceId/commands\n\n{\n    "commands": [\n        {\n            "component": "main",\n            "capability": "switch",\n            "command": "on"\n        }\n    ]\n}\n\n# Turn device off\nhttps://api.smartthings.com/v1/devices/deviceId/commands\n\n{\n    "commands": [\n        {\n            "component": "main",\n            "capability": "switch",\n            "command": "off"\n        }\n    ]\n}\n\nhttps://api.smartthings.com/v1/capabilities\n\nhttps://api.smartthings.com/v1/capabilities/switch/1\n\n~~~\n',
    'author': 'Viktor Freiman',
    'author_email': 'freiman.viktor@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/viktorfreiman/smartthings-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
