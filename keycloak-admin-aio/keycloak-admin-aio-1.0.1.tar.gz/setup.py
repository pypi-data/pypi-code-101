# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keycloak_admin_aio',
 'keycloak_admin_aio._resources',
 'keycloak_admin_aio._resources.admin_events',
 'keycloak_admin_aio._resources.authentication',
 'keycloak_admin_aio._resources.authentication.required_actions',
 'keycloak_admin_aio._resources.client_scopes',
 'keycloak_admin_aio._resources.client_scopes.by_id',
 'keycloak_admin_aio._resources.client_scopes.by_id.scope_mappings',
 'keycloak_admin_aio._resources.client_scopes.by_id.scope_mappings.realm',
 'keycloak_admin_aio._resources.clients',
 'keycloak_admin_aio._resources.clients.by_id',
 'keycloak_admin_aio._resources.clients.by_id.default_client_scopes',
 'keycloak_admin_aio._resources.clients.by_id.default_client_scopes.by_id',
 'keycloak_admin_aio._resources.groups',
 'keycloak_admin_aio._resources.groups.by_id',
 'keycloak_admin_aio._resources.groups.by_id.children',
 'keycloak_admin_aio._resources.groups.by_id.members',
 'keycloak_admin_aio._resources.roles',
 'keycloak_admin_aio._resources.roles.by_id',
 'keycloak_admin_aio._resources.roles.by_id.composites',
 'keycloak_admin_aio._resources.roles.by_name',
 'keycloak_admin_aio._resources.roles.by_name.composites',
 'keycloak_admin_aio._resources.users',
 'keycloak_admin_aio._resources.users.by_id',
 'keycloak_admin_aio._resources.users.by_id.execute_actions_email',
 'keycloak_admin_aio._resources.users.by_id.groups',
 'keycloak_admin_aio._resources.users.by_id.groups.by_id',
 'keycloak_admin_aio._resources.users.by_id.role_mappings',
 'keycloak_admin_aio._resources.users.by_id.role_mappings.realm',
 'keycloak_admin_aio.types']

package_data = \
{'': ['*'], 'keycloak_admin_aio': ['_lib/*']}

install_requires = \
['dacite>=1.6.0,<2.0.0', 'httpx>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'keycloak-admin-aio',
    'version': '1.0.1',
    'description': 'async keycloak admin api wrapper',
    'long_description': None,
    'author': 'Nicklas Sedlock',
    'author_email': 'nicklas@delphai.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/delphai/keycloak-admin-aio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
