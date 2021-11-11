# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylibvirt', 'pylibvirt.modules', 'pylibvirt.modules.devices']

package_data = \
{'': ['*'], 'pylibvirt': ['template/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click>=8.0.1,<9.0.0',
 'defusedxml>=0.7.1,<0.8.0',
 'libvirt-python>=7.5.0,<8.0.0',
 'rich>=10.6.0,<11.0.0']

entry_points = \
{'console_scripts': ['pylibvirt = pylibvirt.__main__:main']}

setup_kwargs = {
    'name': 'pylibvirt',
    'version': '0.0.7',
    'description': 'Python package to orchestrate libvirt API from yaml declaration file',
    'long_description': '##############\nPython Libvirt\n##############\n\n*****************\nWhat is pylibvirt\n*****************\n\nPylibvirt is a tools based on python-libvirt api.\nThe goal are to create virtual machines, networks, volumes and storage more easily\nusing yaml description file.\n\n\n***************************\nHow to create template file\n***************************\n\nThe template must contain at least the provider.\n\nAfter you can declare just what you need.\n\nIf you just want to create a Storage on your target you can just add storage element.\n\n**All properties used in the yaml are the same as those used in libvirt**\n\n\nProvider\n========\n\n**Currently the only tested provider is Qemu/Kvm**\n\n\nThe URI format is the same as libvirt api.\n\n.. code-block:: yaml\n\n    provider:\n        uri: qemu+ssh://root@ip/system\n\nnetwork\n========\n\n**Mode** *is the type of network, values can be nat, route, open, hostdev and False for\nisolated network*\n\n.. code-block:: yaml\n\n    network:\n        - network_name:\n              mode: nat\n              domain: network\n              ip4_cidr: ipv4_format_cidr\n              dhcp_start: first_ip_to_use\n              dhcp_stop: last_ip_to_use\n\nstorage\n========\n\nOnly *dir* storage have been tested\n\n.. code-block:: yaml\n\n    storage:\n        - storage_name:\n              pool_type: dir\n              path: storage_path\n\n\nvolume\n======\n\npool is the storage name declared in libvirt or previously in yaml.\n\nname is the end name set to the volume. It\'s this name that must used in domain section.\n\nThe _key_ has no effect you can set what you want.\n\nIf you want to clone an existing volume or a previouslly create volume you can\nuse the clone argument with the name of the volume. The two volumes must be in the same\npool.\n\n.. code-block:: yaml\n\n    volume:\n      - _key_:\n          disk_format: qcow2\n          capacity: 30\n          size_unit: G\n          pool: storage_name\n          name: volume_name\n\ndomain\n======\n\n_key_ is the name of the VM, choose what you want.\n\nExcept the following key [\'memory\', \'boot_order\', \'DiskDevice\', \'domain_type\',\n                    \'Feature\', \'Os\']\n\nall other key must be the name of a class in pylibvirt/modules/devices\n\nThe class is called dynamically with the parameters.\nExample if you want to add Rng module add an item call RngDevice (class in\npylibvirt/modules/devices/rng.py)\n\n.. code-block:: yaml\n\n    RngDevice:\n        - first_rng_device:\n            - arg_class: value\n        - second_rng_device\n            - model: virtio\n            - backend_model: random\n            - host_device: /dev/my_custom_random\n\n\n.. code-block:: yaml\n\n    domain:\n      - _key_:\n          boot_order:\n            - cdrom\n            - hd\n          memory:\n            mem_unit: G\n            max_memory: 4\n          Os:\n            arch: x86_64\n            machine: q35\n            os_type: hvm\n          Feature: # Features list: https://libvirt.org/formatdomain.html#hypervisor-features\n            - acpi\n            - kvm:\n                hidden:\n                  state: \'on\'\n                poll-control:\n                  state: \'on\'\n          CpuDevice:\n            cpu_model: host\n            model_args:\n              fallback: allow\n            vcpu: 2\n            vcpu_args:\n              placement: static\n          GraphicDevice:\n            - spice_server:\n                graphic_type: spice\n          VideoDevice:\n            - screen:\n                model_type: qxl\n                ram: 66500\n          DiskDevice:\n            - disk:\n                volume: debian-10-2.qcow2\n                driver: qemu\n                bus: scsi\n                pool: data\n            - cdrom:\n                volume: debian-10.10.0-amd64-netinst.iso\n                pool: data\n\n          NetworkInterfaceDevice:\n            - default:\n                net_interface: default\n                net_type: network\n                model: e1000e\n\n\n**************\nHow to install\n**************\n\nRequirements\n============\n\nYou need to install the following packages on your system to install python-libvirt in a virtualenv\n\nFedora\n----------\n\nRPM dependencies\n^^^^^^^^^^^^^^^^\n\n.. code-block:: bash\n\n   dnf install python3-devel pkgconfig libvirt-devel\n\n.. code-block:: bash\n\n   pip install pylibvirt\n\nDebian\n----------\nDEB dependencies\n^^^^^^^^^^^^^^^^\n\n.. code-block:: bash\n\n   apt install python3-dev pkg-config libvirt-dev\n\n.. code-block:: bash\n\n   pip install pylibvirt\n\n***********\nHow to use\n***********\n\nCli usage\n=========\n\n.. code-block:: bash\n\n    pylibvirt -t /path/to/template.yml\n\nUse in python code\n==================\n\nTo use pylibvirt in your python code you can do:\n\ncall manager and set file path\n\n.. code-block:: python\n\n    import pylibvirt\n    pylibvirt.Manager(template=\'path_to_file\')\n\n\nor call manager and directly pass template object\n\n.. code-block:: python\n\n    import pylibvirt\n    pylibvirt.Manager(template=[yaml object])\n\n\nCreate your external module\n===========================\n\nIf you want to create your own pylibvirt modules you must create a class that inherits from\n\n.. code-block:: python\n\n    from pylibvirt.modules.devices import Device\n\nand implement method *generate_data(self)*\n\nIn your setup.py you must register it\n\n.. code-block:: python\n\n    from setuptools import setup\n\n    setup(\n        name=\'cute_snek\',\n        entry_points={\n            \'pylibvirt_modules\': [\n                \'ClassName = ModuleName\',\n            ],\n        }\n    )\n\nIf you use poetry configure your toml like this\n\n.. code-block:: toml\n\n    [tool.poetry.plugins."pylibvirt_modules"]\n    ClassName = \'ModuleName\'\n\nYou can find example of modules in pylibvirt/modules/devices',
    'author': 'Sevolith',
    'author_email': 'contactsevolith@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/Sevolith/Python-Libvirt/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
