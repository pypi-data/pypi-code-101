# coding: utf-8

# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.42.0-8746aaa4-20211102-213344
 
"""
The Data Virtualization REST API connects to your service, so you can manage your virtual
data, data sources, and user roles.

API Version: 1.6.0
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DataVirtualizationV1(BaseService):
    """The Data Virtualization V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'data_virtualization'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DataVirtualizationV1':
        """
        Return a new client for the Data Virtualization service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Data Virtualization service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Data sources
    #########################


    def list_datasource_connections(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get data source connections.

        Gets all data source connections that are connected to the service.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DatasourceConnectionsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_datasource_connections')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/datasource/connections'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def add_datasource_connection(self,
        datasource_type: str,
        name: str,
        origin_country: str,
        properties: 'PostDatasourceConnectionParametersProperties',
        *,
        asset_category: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add data source connection.

        Adds a data source connection to the Data Virtualization service.

        :param str datasource_type: The type of data source that you want to add.
        :param str name: The name of data source.
        :param str origin_country: The location of data source that you want to
               add.
        :param PostDatasourceConnectionParametersProperties properties:
        :param str asset_category: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PostDatasourceConnection` object
        """

        if datasource_type is None:
            raise ValueError('datasource_type must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if origin_country is None:
            raise ValueError('origin_country must be provided')
        if properties is None:
            raise ValueError('properties must be provided')
        properties = convert_model(properties)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_datasource_connection')
        headers.update(sdk_headers)

        data = {
            'datasource_type': datasource_type,
            'name': name,
            'origin_country': origin_country,
            'properties': properties,
            'asset_category': asset_category
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/datasource/connections'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_datasource_connection(self,
        connection_id: str,
        *,
        cid: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete data source connection.

        Deletes a data source connection from the Data Virtualization service.

        :param str connection_id: The connection identifier for the platform..
        :param str cid: (optional) The identifier of the connection for the Data
               Virtualization..
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if connection_id is None:
            raise ValueError('connection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_datasource_connection')
        headers.update(sdk_headers)

        params = {
            'cid': cid
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['connection_id']
        path_param_values = self.encode_path_vars(connection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/datasource/connections/{connection_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_object_store_connections_v2(self,
        *,
        jwt_auth_user_payload: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Gets object store connection details.

        :param str jwt_auth_user_payload: (optional) Supplied by proxy.  Do NOT add
               your own value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ObjStoreConnectionResponseV2` object
        """

        headers = {
            'jwt-auth-user-payload': jwt_auth_user_payload
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_object_store_connections_v2')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/datasource/objectstore_connections'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Users
    #########################


    def grant_user_to_virtual_table(self,
        table_name: str,
        table_schema: str,
        authid: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Grant user access.

        Grants a user access to a specific virtualized table.

        :param str table_name: The name of the virtualized table.
        :param str table_schema: The schema of the virtualized table.
        :param str authid: The identifier of the authorization, if grant access to
               all users, the value is PUBLIC, othervise the value is the data
               virtualization username.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if table_name is None:
            raise ValueError('table_name must be provided')
        if table_schema is None:
            raise ValueError('table_schema must be provided')
        if authid is None:
            raise ValueError('authid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='grant_user_to_virtual_table')
        headers.update(sdk_headers)

        data = {
            'table_name': table_name,
            'table_schema': table_schema,
            'authid': authid
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/privileges/users'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def revoke_user_from_object(self,
        authid: str,
        table_name: str,
        table_schema: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Revoke user acccess.

        Revokes user access to the virtualized table.

        :param str authid: The Data Virtualization user name, if the value is
               PUBLIC, it means revoke access privilege from all Data Virtualization
               users.
        :param str table_name: The virtualized table's name.
        :param str table_schema: The virtualized table's schema name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if authid is None:
            raise ValueError('authid must be provided')
        if table_name is None:
            raise ValueError('table_name must be provided')
        if table_schema is None:
            raise ValueError('table_schema must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='revoke_user_from_object')
        headers.update(sdk_headers)

        params = {
            'table_name': table_name,
            'table_schema': table_schema
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['authid']
        path_param_values = self.encode_path_vars(authid)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/privileges/users/{authid}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Roles
    #########################


    def grant_roles_to_virtualized_table(self,
        table_name: str,
        table_schema: str,
        *,
        role_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Grant user role.

        Grants a user role access to a specific virtualized table.

        :param str table_name: The name of the virtualized table.
        :param str table_schema: The schema of the virtualized table.
        :param str role_name: (optional) The identifier of the authorization, if
               grant access to all users, the value is PUBLIC, othervise the value is the
               data virtualization username.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if table_name is None:
            raise ValueError('table_name must be provided')
        if table_schema is None:
            raise ValueError('table_schema must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='grant_roles_to_virtualized_table')
        headers.update(sdk_headers)

        data = {
            'table_name': table_name,
            'table_schema': table_schema,
            'role_name': role_name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/privileges/roles'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def dvaas_revoke_role_from_table(self,
        role_name: str,
        table_name: str,
        table_schema: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete role.

        Revokes roles for a virtualized table.

        :param str role_name: The Data Virtualization role type. Values can be
               DV_ADMIN, DV_ENGINEER, DV_STEWARD, or DV_WORKER, which correspond to
               MANAGER, ENGINEER, STEWARD, and USER roles in the user interface.
        :param str table_name: The virtualized table's name.
        :param str table_schema: The virtualized table's schema name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if role_name is None:
            raise ValueError('role_name must be provided')
        if table_name is None:
            raise ValueError('table_name must be provided')
        if table_schema is None:
            raise ValueError('table_schema must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='dvaas_revoke_role_from_table')
        headers.update(sdk_headers)

        params = {
            'table_name': table_name,
            'table_schema': table_schema
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['role_name']
        path_param_values = self.encode_path_vars(role_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/privileges/roles/{role_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def list_tables_for_role(self,
        rolename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get virtualized tables by role.

        Retrieves the list of virtualized tables that have a specific role.

        :param str rolename: Data Virtualization has four roles: MANAGER, STEWARD,
               ENGINEER and USER The value of rolename should be one of them.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TablesForRoleResponse` object
        """

        if rolename is None:
            raise ValueError('rolename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_tables_for_role')
        headers.update(sdk_headers)

        params = {
            'rolename': rolename
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/privileges/tables'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Securities
    #########################


    def turn_on_policy_v2(self,
        status: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Turn policy enforcement status on or off.

        Turns policy enforcement status on or off.

        :param str status: Set the status of policy enforcement.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TurnOnPolicyV2Response` object
        """

        if status is None:
            raise ValueError('status must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='turn_on_policy_v2')
        headers.update(sdk_headers)

        params = {
            'status': status
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/security/policy/status'
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def check_policy_status_v2(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get policy enforcement status.

        Get policy enforcement status, return enabled or disabled.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CheckPolicyStatusV2Response` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='check_policy_status_v2')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/security/policy/status'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Virtualization
    #########################


    def dvaas_virtualize_table(self,
        source_name: str,
        source_table_def: List['VirtualizeTableParameterSourceTableDefItem'],
        sources: List[str],
        virtual_name: str,
        virtual_schema: str,
        virtual_table_def: List['VirtualizeTableParameterVirtualTableDefItem'],
        *,
        is_included_columns: str = None,
        replace: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Virtualize table.

        Transforms a given data source table into a virtualized table.

        :param str source_name: The name of the source table.
        :param List[VirtualizeTableParameterSourceTableDefItem] source_table_def:
        :param List[str] sources:
        :param str virtual_name: The name of the table that will be virtualized.
        :param str virtual_schema: The schema of the table that will be
               virtualized.
        :param List[VirtualizeTableParameterVirtualTableDefItem] virtual_table_def:
        :param str is_included_columns: (optional) The columns that are included in
               the source table.
        :param bool replace: (optional) Determines whether to replace columns in
               the virtualized table.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `VirtualizeTableResponse` object
        """

        if source_name is None:
            raise ValueError('source_name must be provided')
        if source_table_def is None:
            raise ValueError('source_table_def must be provided')
        if sources is None:
            raise ValueError('sources must be provided')
        if virtual_name is None:
            raise ValueError('virtual_name must be provided')
        if virtual_schema is None:
            raise ValueError('virtual_schema must be provided')
        if virtual_table_def is None:
            raise ValueError('virtual_table_def must be provided')
        source_table_def = [convert_model(x) for x in source_table_def]
        virtual_table_def = [convert_model(x) for x in virtual_table_def]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='dvaas_virtualize_table')
        headers.update(sdk_headers)

        data = {
            'source_name': source_name,
            'source_table_def': source_table_def,
            'sources': sources,
            'virtual_name': virtual_name,
            'virtual_schema': virtual_schema,
            'virtual_table_def': virtual_table_def,
            'is_included_columns': is_included_columns,
            'replace': replace
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/virtualization/tables'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_table(self,
        virtual_schema: str,
        virtual_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete virtualized table.

        Removes the specified virtualized table. You must specify the schema and table
        name.

        :param str virtual_schema: The schema of virtualized table to be deleted.
        :param str virtual_name: The name of virtualized table to be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if virtual_schema is None:
            raise ValueError('virtual_schema must be provided')
        if virtual_name is None:
            raise ValueError('virtual_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_table')
        headers.update(sdk_headers)

        params = {
            'virtual_schema': virtual_schema
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['virtual_name']
        path_param_values = self.encode_path_vars(virtual_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/virtualization/tables/{virtual_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def virtualize_cos_v2(self,
        url: str,
        virtual_name: str,
        virtual_schema: str,
        virtual_table_def: List['VirtualizeCosV2RequestVirtualTableDefItem'],
        *,
        is_replace: bool = None,
        options: str = None,
        jwt_auth_user_payload: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a remote table for the ORC or Parquet file on a cloud object store (COS).

        Create a remote table for the ORC or Parquet file on a cloud object store (COS).

        :param str url: the file path with bucket name.
        :param str virtual_name: the virtual table name.
        :param str virtual_schema: the virtual table schema.
        :param List[VirtualizeCosV2RequestVirtualTableDefItem] virtual_table_def:
        :param bool is_replace: (optional) if repalce the existing one when create
               the virtual table.
        :param str options: (optional) the options used to virtualize file.
        :param str jwt_auth_user_payload: (optional) Supplied by proxy.  Do NOT add
               your own value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SuccessResponse` object
        """

        if url is None:
            raise ValueError('url must be provided')
        if virtual_name is None:
            raise ValueError('virtual_name must be provided')
        if virtual_schema is None:
            raise ValueError('virtual_schema must be provided')
        if virtual_table_def is None:
            raise ValueError('virtual_table_def must be provided')
        virtual_table_def = [convert_model(x) for x in virtual_table_def]
        headers = {
            'jwt-auth-user-payload': jwt_auth_user_payload
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='virtualize_cos_v2')
        headers.update(sdk_headers)

        data = {
            'url': url,
            'virtual_name': virtual_name,
            'virtual_schema': virtual_schema,
            'virtual_table_def': virtual_table_def,
            'is_replace': is_replace,
            'options': options
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/virtualization/cloud_object_storages'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Primary catalog
    #########################


    def get_primary_catalog(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get primary catalog ID.

        Gets the primary catalog ID from the DVSYS.INSTANCE_INFO table.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PrimaryCatalogInfo` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_primary_catalog')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/catalog/primary'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def post_primary_catalog(self,
        guid: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Add primary catalog.

        Inserts primary catalog ID into table DVSYS.INSTANCE_INFO.

        :param str guid:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PostPrimaryCatalog` object
        """

        if guid is None:
            raise ValueError('guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_primary_catalog')
        headers.update(sdk_headers)

        data = {
            'guid': guid
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/catalog/primary'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_primary_catalog(self,
        guid: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete primary catalog.

        Delete primary catalog item in the DVSYS.INSTANCE_INFO table.

        :param str guid: The Data Virtualization user name, if the value is PUBLIC,
               it means revoke access privilege from all Data Virtualization users.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if guid is None:
            raise ValueError('guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_primary_catalog')
        headers.update(sdk_headers)

        params = {
            'guid': guid
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/catalog/primary'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Publish objects
    #########################


    def publish_assets(self,
        catalog_id: str,
        allow_duplicates: bool,
        assets: List['PostPrimaryCatalogParametersAssetsItem'],
        **kwargs
    ) -> DetailedResponse:
        """
        Publish virtual tables to a catalog.

        Publishes virtual tables to a catalog.

        :param str catalog_id:
        :param bool allow_duplicates: The type of data source that you want to add.
        :param List[PostPrimaryCatalogParametersAssetsItem] assets:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CatalogPublishResponse` object
        """

        if catalog_id is None:
            raise ValueError('catalog_id must be provided')
        if allow_duplicates is None:
            raise ValueError('allow_duplicates must be provided')
        if assets is None:
            raise ValueError('assets must be provided')
        assets = [convert_model(x) for x in assets]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='publish_assets')
        headers.update(sdk_headers)

        data = {
            'catalog_id': catalog_id,
            'allow_duplicates': allow_duplicates,
            'assets': assets
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/integration/catalog/publish'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Caches
    #########################


    def get_caches_list(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List caches.

        List all active, inactive and deleted caches in Data Virtualization.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CacheListResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_caches_list')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/caching/caches'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_cache(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List a cache.

        List a specific cache in Data Virtualization.

        :param str id: The ID of the cache to be listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CacheResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_cache')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/caching/caches/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_cache_storage_detail(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Fetch the cache storage.

        Fetch the total cache storage and used capacities for active and inactive caches
        in Data Virtualization.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StorageDetails` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_cache_storage_detail')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/caching/storage'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class CacheListResponse():
    """
    CacheListResponse.

    :attr List[CacheListResponseCachesItem] caches: (optional)
    """

    def __init__(self,
                 *,
                 caches: List['CacheListResponseCachesItem'] = None) -> None:
        """
        Initialize a CacheListResponse object.

        :param List[CacheListResponseCachesItem] caches: (optional)
        """
        self.caches = caches

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CacheListResponse':
        """Initialize a CacheListResponse object from a json dictionary."""
        args = {}
        if 'caches' in _dict:
            args['caches'] = [CacheListResponseCachesItem.from_dict(x) for x in _dict.get('caches')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CacheListResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'caches') and self.caches is not None:
            _dict['caches'] = [x.to_dict() for x in self.caches]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CacheListResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CacheListResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CacheListResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CacheListResponseCachesItem():
    """
    CacheListResponseCachesItem.

    :attr str name: (optional) The name of this cache.
    :attr str id: (optional) The unique ID of this cache.
    :attr str query: (optional) The query that defines this cache.
    :attr str owner_id: (optional) Owner ID of this cache.
    :attr str type: (optional) Type of the cache - User-defined (U), Recommended
          (R).
    :attr str created_timestamp: (optional) Database timestamp at the time of cache
          creation.
    :attr str last_modified_timestamp: (optional) Database timestamp when this cache
          was last modified (state change).
    :attr str last_refresh_timestamp: (optional) Database timestamp when this cache
          was last refreshed.
    :attr str last_used_timestamp: (optional) Database timestamp when this cache was
          last used.
    :attr str state: (optional) State of this cache - one of
          Enabled,Disabled,Deleted,Failed,Populating,Activating,Enabling,Disabling,Refreshing,Deleting.
    :attr int size: (optional) Size of this cache (in KB).
    :attr int cardinality: (optional) Cardinality (number of rows) of this cache.
    :attr int time_taken_for_refresh: (optional) Time taken to refresh this cache
          most recently (in milliseconds).
    :attr int refresh_count: (optional) Number of times this cache has been
          refreshed since creation.
    :attr int hit_count: (optional) Hit Count of the cache (number of times this
          cache was used).
    :attr str refresh_schedule: (optional) Encoded cron-style representation of the
          cache refresh schedule.
    :attr str refresh_schedule_desc: (optional) Human-readable description of the
          cache refresh schedule.
    :attr str status_msg: (optional) Status message indicating the most recent
          error/issue with the cache, if any.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 id: str = None,
                 query: str = None,
                 owner_id: str = None,
                 type: str = None,
                 created_timestamp: str = None,
                 last_modified_timestamp: str = None,
                 last_refresh_timestamp: str = None,
                 last_used_timestamp: str = None,
                 state: str = None,
                 size: int = None,
                 cardinality: int = None,
                 time_taken_for_refresh: int = None,
                 refresh_count: int = None,
                 hit_count: int = None,
                 refresh_schedule: str = None,
                 refresh_schedule_desc: str = None,
                 status_msg: str = None) -> None:
        """
        Initialize a CacheListResponseCachesItem object.

        :param str name: (optional) The name of this cache.
        :param str id: (optional) The unique ID of this cache.
        :param str query: (optional) The query that defines this cache.
        :param str owner_id: (optional) Owner ID of this cache.
        :param str type: (optional) Type of the cache - User-defined (U),
               Recommended (R).
        :param str created_timestamp: (optional) Database timestamp at the time of
               cache creation.
        :param str last_modified_timestamp: (optional) Database timestamp when this
               cache was last modified (state change).
        :param str last_refresh_timestamp: (optional) Database timestamp when this
               cache was last refreshed.
        :param str last_used_timestamp: (optional) Database timestamp when this
               cache was last used.
        :param str state: (optional) State of this cache - one of
               Enabled,Disabled,Deleted,Failed,Populating,Activating,Enabling,Disabling,Refreshing,Deleting.
        :param int size: (optional) Size of this cache (in KB).
        :param int cardinality: (optional) Cardinality (number of rows) of this
               cache.
        :param int time_taken_for_refresh: (optional) Time taken to refresh this
               cache most recently (in milliseconds).
        :param int refresh_count: (optional) Number of times this cache has been
               refreshed since creation.
        :param int hit_count: (optional) Hit Count of the cache (number of times
               this cache was used).
        :param str refresh_schedule: (optional) Encoded cron-style representation
               of the cache refresh schedule.
        :param str refresh_schedule_desc: (optional) Human-readable description of
               the cache refresh schedule.
        :param str status_msg: (optional) Status message indicating the most recent
               error/issue with the cache, if any.
        """
        self.name = name
        self.id = id
        self.query = query
        self.owner_id = owner_id
        self.type = type
        self.created_timestamp = created_timestamp
        self.last_modified_timestamp = last_modified_timestamp
        self.last_refresh_timestamp = last_refresh_timestamp
        self.last_used_timestamp = last_used_timestamp
        self.state = state
        self.size = size
        self.cardinality = cardinality
        self.time_taken_for_refresh = time_taken_for_refresh
        self.refresh_count = refresh_count
        self.hit_count = hit_count
        self.refresh_schedule = refresh_schedule
        self.refresh_schedule_desc = refresh_schedule_desc
        self.status_msg = status_msg

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CacheListResponseCachesItem':
        """Initialize a CacheListResponseCachesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'query' in _dict:
            args['query'] = _dict.get('query')
        if 'owner_id' in _dict:
            args['owner_id'] = _dict.get('owner_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'created_timestamp' in _dict:
            args['created_timestamp'] = _dict.get('created_timestamp')
        if 'last_modified_timestamp' in _dict:
            args['last_modified_timestamp'] = _dict.get('last_modified_timestamp')
        if 'last_refresh_timestamp' in _dict:
            args['last_refresh_timestamp'] = _dict.get('last_refresh_timestamp')
        if 'last_used_timestamp' in _dict:
            args['last_used_timestamp'] = _dict.get('last_used_timestamp')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'cardinality' in _dict:
            args['cardinality'] = _dict.get('cardinality')
        if 'time_taken_for_refresh' in _dict:
            args['time_taken_for_refresh'] = _dict.get('time_taken_for_refresh')
        if 'refresh_count' in _dict:
            args['refresh_count'] = _dict.get('refresh_count')
        if 'hit_count' in _dict:
            args['hit_count'] = _dict.get('hit_count')
        if 'refresh_schedule' in _dict:
            args['refresh_schedule'] = _dict.get('refresh_schedule')
        if 'refresh_schedule_desc' in _dict:
            args['refresh_schedule_desc'] = _dict.get('refresh_schedule_desc')
        if 'status_msg' in _dict:
            args['status_msg'] = _dict.get('status_msg')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CacheListResponseCachesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'owner_id') and self.owner_id is not None:
            _dict['owner_id'] = self.owner_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'created_timestamp') and self.created_timestamp is not None:
            _dict['created_timestamp'] = self.created_timestamp
        if hasattr(self, 'last_modified_timestamp') and self.last_modified_timestamp is not None:
            _dict['last_modified_timestamp'] = self.last_modified_timestamp
        if hasattr(self, 'last_refresh_timestamp') and self.last_refresh_timestamp is not None:
            _dict['last_refresh_timestamp'] = self.last_refresh_timestamp
        if hasattr(self, 'last_used_timestamp') and self.last_used_timestamp is not None:
            _dict['last_used_timestamp'] = self.last_used_timestamp
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'cardinality') and self.cardinality is not None:
            _dict['cardinality'] = self.cardinality
        if hasattr(self, 'time_taken_for_refresh') and self.time_taken_for_refresh is not None:
            _dict['time_taken_for_refresh'] = self.time_taken_for_refresh
        if hasattr(self, 'refresh_count') and self.refresh_count is not None:
            _dict['refresh_count'] = self.refresh_count
        if hasattr(self, 'hit_count') and self.hit_count is not None:
            _dict['hit_count'] = self.hit_count
        if hasattr(self, 'refresh_schedule') and self.refresh_schedule is not None:
            _dict['refresh_schedule'] = self.refresh_schedule
        if hasattr(self, 'refresh_schedule_desc') and self.refresh_schedule_desc is not None:
            _dict['refresh_schedule_desc'] = self.refresh_schedule_desc
        if hasattr(self, 'status_msg') and self.status_msg is not None:
            _dict['status_msg'] = self.status_msg
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CacheListResponseCachesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CacheListResponseCachesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CacheListResponseCachesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CacheResponse():
    """
    CacheResponse.

    :attr str name: (optional) The name of this cache.
    :attr str id: (optional) The unique ID of this cache.
    :attr str query: (optional) The query that defines this cache.
    :attr str owner_id: (optional) Owner ID of this cache.
    :attr str type: (optional) Type of the cache - User-defined (U), Recommended
          (R).
    :attr str created_timestamp: (optional) Database timestamp at the time of cache
          creation.
    :attr str last_modified_timestamp: (optional) Database timestamp when this cache
          was last modified (state change).
    :attr str last_refresh_timestamp: (optional) Database timestamp when this cache
          was last refreshed.
    :attr str last_used_timestamp: (optional) Database timestamp when this cache was
          last used.
    :attr str state: (optional) State of this cache - one of
          Enabled,Disabled,Deleted,Failed,Populating,Activating,Enabling,Disabling,Refreshing,Deleting.
    :attr int size: (optional) Size of this cache (in KB).
    :attr int cardinality: (optional) Cardinality (number of rows) of this cache.
    :attr int time_taken_for_refresh: (optional) Time taken to refresh this cache
          most recently (in milliseconds).
    :attr int refresh_count: (optional) Number of times this cache has been
          refreshed since creation.
    :attr int hit_count: (optional) Hit Count of the cache (number of times this
          cache was used).
    :attr str refresh_schedule: (optional) Encoded cron-style representation of the
          cache refresh schedule.
    :attr str refresh_schedule_desc: (optional) Human-readable description of the
          cache refresh schedule.
    :attr str status_msg: (optional) Status message indicating the most recent
          error/issue with the cache, if any.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 id: str = None,
                 query: str = None,
                 owner_id: str = None,
                 type: str = None,
                 created_timestamp: str = None,
                 last_modified_timestamp: str = None,
                 last_refresh_timestamp: str = None,
                 last_used_timestamp: str = None,
                 state: str = None,
                 size: int = None,
                 cardinality: int = None,
                 time_taken_for_refresh: int = None,
                 refresh_count: int = None,
                 hit_count: int = None,
                 refresh_schedule: str = None,
                 refresh_schedule_desc: str = None,
                 status_msg: str = None) -> None:
        """
        Initialize a CacheResponse object.

        :param str name: (optional) The name of this cache.
        :param str id: (optional) The unique ID of this cache.
        :param str query: (optional) The query that defines this cache.
        :param str owner_id: (optional) Owner ID of this cache.
        :param str type: (optional) Type of the cache - User-defined (U),
               Recommended (R).
        :param str created_timestamp: (optional) Database timestamp at the time of
               cache creation.
        :param str last_modified_timestamp: (optional) Database timestamp when this
               cache was last modified (state change).
        :param str last_refresh_timestamp: (optional) Database timestamp when this
               cache was last refreshed.
        :param str last_used_timestamp: (optional) Database timestamp when this
               cache was last used.
        :param str state: (optional) State of this cache - one of
               Enabled,Disabled,Deleted,Failed,Populating,Activating,Enabling,Disabling,Refreshing,Deleting.
        :param int size: (optional) Size of this cache (in KB).
        :param int cardinality: (optional) Cardinality (number of rows) of this
               cache.
        :param int time_taken_for_refresh: (optional) Time taken to refresh this
               cache most recently (in milliseconds).
        :param int refresh_count: (optional) Number of times this cache has been
               refreshed since creation.
        :param int hit_count: (optional) Hit Count of the cache (number of times
               this cache was used).
        :param str refresh_schedule: (optional) Encoded cron-style representation
               of the cache refresh schedule.
        :param str refresh_schedule_desc: (optional) Human-readable description of
               the cache refresh schedule.
        :param str status_msg: (optional) Status message indicating the most recent
               error/issue with the cache, if any.
        """
        self.name = name
        self.id = id
        self.query = query
        self.owner_id = owner_id
        self.type = type
        self.created_timestamp = created_timestamp
        self.last_modified_timestamp = last_modified_timestamp
        self.last_refresh_timestamp = last_refresh_timestamp
        self.last_used_timestamp = last_used_timestamp
        self.state = state
        self.size = size
        self.cardinality = cardinality
        self.time_taken_for_refresh = time_taken_for_refresh
        self.refresh_count = refresh_count
        self.hit_count = hit_count
        self.refresh_schedule = refresh_schedule
        self.refresh_schedule_desc = refresh_schedule_desc
        self.status_msg = status_msg

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CacheResponse':
        """Initialize a CacheResponse object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'query' in _dict:
            args['query'] = _dict.get('query')
        if 'owner_id' in _dict:
            args['owner_id'] = _dict.get('owner_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'created_timestamp' in _dict:
            args['created_timestamp'] = _dict.get('created_timestamp')
        if 'last_modified_timestamp' in _dict:
            args['last_modified_timestamp'] = _dict.get('last_modified_timestamp')
        if 'last_refresh_timestamp' in _dict:
            args['last_refresh_timestamp'] = _dict.get('last_refresh_timestamp')
        if 'last_used_timestamp' in _dict:
            args['last_used_timestamp'] = _dict.get('last_used_timestamp')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'cardinality' in _dict:
            args['cardinality'] = _dict.get('cardinality')
        if 'time_taken_for_refresh' in _dict:
            args['time_taken_for_refresh'] = _dict.get('time_taken_for_refresh')
        if 'refresh_count' in _dict:
            args['refresh_count'] = _dict.get('refresh_count')
        if 'hit_count' in _dict:
            args['hit_count'] = _dict.get('hit_count')
        if 'refresh_schedule' in _dict:
            args['refresh_schedule'] = _dict.get('refresh_schedule')
        if 'refresh_schedule_desc' in _dict:
            args['refresh_schedule_desc'] = _dict.get('refresh_schedule_desc')
        if 'status_msg' in _dict:
            args['status_msg'] = _dict.get('status_msg')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CacheResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'owner_id') and self.owner_id is not None:
            _dict['owner_id'] = self.owner_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'created_timestamp') and self.created_timestamp is not None:
            _dict['created_timestamp'] = self.created_timestamp
        if hasattr(self, 'last_modified_timestamp') and self.last_modified_timestamp is not None:
            _dict['last_modified_timestamp'] = self.last_modified_timestamp
        if hasattr(self, 'last_refresh_timestamp') and self.last_refresh_timestamp is not None:
            _dict['last_refresh_timestamp'] = self.last_refresh_timestamp
        if hasattr(self, 'last_used_timestamp') and self.last_used_timestamp is not None:
            _dict['last_used_timestamp'] = self.last_used_timestamp
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'cardinality') and self.cardinality is not None:
            _dict['cardinality'] = self.cardinality
        if hasattr(self, 'time_taken_for_refresh') and self.time_taken_for_refresh is not None:
            _dict['time_taken_for_refresh'] = self.time_taken_for_refresh
        if hasattr(self, 'refresh_count') and self.refresh_count is not None:
            _dict['refresh_count'] = self.refresh_count
        if hasattr(self, 'hit_count') and self.hit_count is not None:
            _dict['hit_count'] = self.hit_count
        if hasattr(self, 'refresh_schedule') and self.refresh_schedule is not None:
            _dict['refresh_schedule'] = self.refresh_schedule
        if hasattr(self, 'refresh_schedule_desc') and self.refresh_schedule_desc is not None:
            _dict['refresh_schedule_desc'] = self.refresh_schedule_desc
        if hasattr(self, 'status_msg') and self.status_msg is not None:
            _dict['status_msg'] = self.status_msg
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CacheResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CacheResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CacheResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CatalogPublishResponseDuplicateAssetsItem():
    """
    CatalogPublishResponseDuplicateAssetsItem.

    :attr str schema_name: (optional)
    :attr str table_name: (optional)
    """

    def __init__(self,
                 *,
                 schema_name: str = None,
                 table_name: str = None) -> None:
        """
        Initialize a CatalogPublishResponseDuplicateAssetsItem object.

        :param str schema_name: (optional)
        :param str table_name: (optional)
        """
        self.schema_name = schema_name
        self.table_name = table_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogPublishResponseDuplicateAssetsItem':
        """Initialize a CatalogPublishResponseDuplicateAssetsItem object from a json dictionary."""
        args = {}
        if 'schema_name' in _dict:
            args['schema_name'] = _dict.get('schema_name')
        if 'table_name' in _dict:
            args['table_name'] = _dict.get('table_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogPublishResponseDuplicateAssetsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_name') and self.schema_name is not None:
            _dict['schema_name'] = self.schema_name
        if hasattr(self, 'table_name') and self.table_name is not None:
            _dict['table_name'] = self.table_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogPublishResponseDuplicateAssetsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogPublishResponseDuplicateAssetsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogPublishResponseDuplicateAssetsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CatalogPublishResponseFailedAssetsItem():
    """
    CatalogPublishResponseFailedAssetsItem.

    :attr str error_msg: (optional)
    :attr str schema_name: (optional)
    :attr str table_name: (optional)
    """

    def __init__(self,
                 *,
                 error_msg: str = None,
                 schema_name: str = None,
                 table_name: str = None) -> None:
        """
        Initialize a CatalogPublishResponseFailedAssetsItem object.

        :param str error_msg: (optional)
        :param str schema_name: (optional)
        :param str table_name: (optional)
        """
        self.error_msg = error_msg
        self.schema_name = schema_name
        self.table_name = table_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogPublishResponseFailedAssetsItem':
        """Initialize a CatalogPublishResponseFailedAssetsItem object from a json dictionary."""
        args = {}
        if 'error_msg' in _dict:
            args['error_msg'] = _dict.get('error_msg')
        if 'schema_name' in _dict:
            args['schema_name'] = _dict.get('schema_name')
        if 'table_name' in _dict:
            args['table_name'] = _dict.get('table_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogPublishResponseFailedAssetsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error_msg') and self.error_msg is not None:
            _dict['error_msg'] = self.error_msg
        if hasattr(self, 'schema_name') and self.schema_name is not None:
            _dict['schema_name'] = self.schema_name
        if hasattr(self, 'table_name') and self.table_name is not None:
            _dict['table_name'] = self.table_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogPublishResponseFailedAssetsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogPublishResponseFailedAssetsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogPublishResponseFailedAssetsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CatalogPublishResponsePublishedAssetsItem():
    """
    CatalogPublishResponsePublishedAssetsItem.

    :attr str schema_name: (optional)
    :attr str table_name: (optional)
    :attr str wkc_asset_id: (optional)
    """

    def __init__(self,
                 *,
                 schema_name: str = None,
                 table_name: str = None,
                 wkc_asset_id: str = None) -> None:
        """
        Initialize a CatalogPublishResponsePublishedAssetsItem object.

        :param str schema_name: (optional)
        :param str table_name: (optional)
        :param str wkc_asset_id: (optional)
        """
        self.schema_name = schema_name
        self.table_name = table_name
        self.wkc_asset_id = wkc_asset_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogPublishResponsePublishedAssetsItem':
        """Initialize a CatalogPublishResponsePublishedAssetsItem object from a json dictionary."""
        args = {}
        if 'schema_name' in _dict:
            args['schema_name'] = _dict.get('schema_name')
        if 'table_name' in _dict:
            args['table_name'] = _dict.get('table_name')
        if 'wkc_asset_id' in _dict:
            args['wkc_asset_id'] = _dict.get('wkc_asset_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogPublishResponsePublishedAssetsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_name') and self.schema_name is not None:
            _dict['schema_name'] = self.schema_name
        if hasattr(self, 'table_name') and self.table_name is not None:
            _dict['table_name'] = self.table_name
        if hasattr(self, 'wkc_asset_id') and self.wkc_asset_id is not None:
            _dict['wkc_asset_id'] = self.wkc_asset_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogPublishResponsePublishedAssetsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogPublishResponsePublishedAssetsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogPublishResponsePublishedAssetsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CheckPolicyStatusV2Response():
    """
    CheckPolicyStatusV2Response.

    :attr str status:
    """

    def __init__(self,
                 status: str) -> None:
        """
        Initialize a CheckPolicyStatusV2Response object.

        :param str status:
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CheckPolicyStatusV2Response':
        """Initialize a CheckPolicyStatusV2Response object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in CheckPolicyStatusV2Response JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CheckPolicyStatusV2Response object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CheckPolicyStatusV2Response object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CheckPolicyStatusV2Response') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CheckPolicyStatusV2Response') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatasourceConnectionsList():
    """
    DatasourceConnectionsList.

    :attr List[DatasourceConnectionsListDatasourceConnectionsItem]
          datasource_connections: (optional)
    """

    def __init__(self,
                 *,
                 datasource_connections: List['DatasourceConnectionsListDatasourceConnectionsItem'] = None) -> None:
        """
        Initialize a DatasourceConnectionsList object.

        :param List[DatasourceConnectionsListDatasourceConnectionsItem]
               datasource_connections: (optional)
        """
        self.datasource_connections = datasource_connections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatasourceConnectionsList':
        """Initialize a DatasourceConnectionsList object from a json dictionary."""
        args = {}
        if 'datasource_connections' in _dict:
            args['datasource_connections'] = [DatasourceConnectionsListDatasourceConnectionsItem.from_dict(x) for x in _dict.get('datasource_connections')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatasourceConnectionsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'datasource_connections') and self.datasource_connections is not None:
            _dict['datasource_connections'] = [x.to_dict() for x in self.datasource_connections]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatasourceConnectionsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatasourceConnectionsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatasourceConnectionsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatasourceConnectionsListDatasourceConnectionsItem():
    """
    DatasourceConnectionsListDatasourceConnectionsItem.

    :attr str node_name: (optional) The name of the node that a datasource
          connection associates.
    :attr str node_description: (optional) The description of the node that a
          datasource connection associates.
    :attr str agent_class: (optional) The type of connector, for example, H stands
          for Hosted, ie running within the cluster, F means Fenced Mode Process, ie
          direct within Data Virtualization instance.
    :attr str hostname: (optional) The hostname or IP address that is used to access
          the connection.
    :attr str port: (optional) The port number that is used to access the
          connection.
    :attr str os_user: (optional)
    :attr str is_docker: (optional) Determines whether the data source uses Docker.
    :attr str dscount: (optional) The number of data sources.
    :attr List[DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem]
          data_sources: (optional)
    """

    def __init__(self,
                 *,
                 node_name: str = None,
                 node_description: str = None,
                 agent_class: str = None,
                 hostname: str = None,
                 port: str = None,
                 os_user: str = None,
                 is_docker: str = None,
                 dscount: str = None,
                 data_sources: List['DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem'] = None) -> None:
        """
        Initialize a DatasourceConnectionsListDatasourceConnectionsItem object.

        :param str node_name: (optional) The name of the node that a datasource
               connection associates.
        :param str node_description: (optional) The description of the node that a
               datasource connection associates.
        :param str agent_class: (optional) The type of connector, for example, H
               stands for Hosted, ie running within the cluster, F means Fenced Mode
               Process, ie direct within Data Virtualization instance.
        :param str hostname: (optional) The hostname or IP address that is used to
               access the connection.
        :param str port: (optional) The port number that is used to access the
               connection.
        :param str os_user: (optional)
        :param str is_docker: (optional) Determines whether the data source uses
               Docker.
        :param str dscount: (optional) The number of data sources.
        :param
               List[DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem]
               data_sources: (optional)
        """
        self.node_name = node_name
        self.node_description = node_description
        self.agent_class = agent_class
        self.hostname = hostname
        self.port = port
        self.os_user = os_user
        self.is_docker = is_docker
        self.dscount = dscount
        self.data_sources = data_sources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatasourceConnectionsListDatasourceConnectionsItem':
        """Initialize a DatasourceConnectionsListDatasourceConnectionsItem object from a json dictionary."""
        args = {}
        if 'node_name' in _dict:
            args['node_name'] = _dict.get('node_name')
        if 'node_description' in _dict:
            args['node_description'] = _dict.get('node_description')
        if 'agent_class' in _dict:
            args['agent_class'] = _dict.get('agent_class')
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'os_user' in _dict:
            args['os_user'] = _dict.get('os_user')
        if 'is_docker' in _dict:
            args['is_docker'] = _dict.get('is_docker')
        if 'dscount' in _dict:
            args['dscount'] = _dict.get('dscount')
        if 'data_sources' in _dict:
            args['data_sources'] = [DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem.from_dict(x) for x in _dict.get('data_sources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatasourceConnectionsListDatasourceConnectionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'node_name') and self.node_name is not None:
            _dict['node_name'] = self.node_name
        if hasattr(self, 'node_description') and self.node_description is not None:
            _dict['node_description'] = self.node_description
        if hasattr(self, 'agent_class') and self.agent_class is not None:
            _dict['agent_class'] = self.agent_class
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'os_user') and self.os_user is not None:
            _dict['os_user'] = self.os_user
        if hasattr(self, 'is_docker') and self.is_docker is not None:
            _dict['is_docker'] = self.is_docker
        if hasattr(self, 'dscount') and self.dscount is not None:
            _dict['dscount'] = self.dscount
        if hasattr(self, 'data_sources') and self.data_sources is not None:
            _dict['data_sources'] = [x.to_dict() for x in self.data_sources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatasourceConnectionsListDatasourceConnectionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatasourceConnectionsListDatasourceConnectionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatasourceConnectionsListDatasourceConnectionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem():
    """
    DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem.

    :attr str cid: (optional) The identifier of the connection for the Data
          Virtualization.
    :attr str dbname: (optional) The name of the database.
    :attr str connection_id: (optional) The connection identifier for the platform.
    :attr str srchostname: (optional) The hostname or IP address of the data source.
    :attr str srcport: (optional) The port number of the data source.
    :attr str srctype: (optional) The type of the data source.
    :attr str usr: (optional) The user that has access to the data source.
    :attr str uri: (optional) The URI of the data source.
    :attr str status: (optional) The status of the data source.
    :attr str connection_name: (optional) The name of the connection.
    """

    def __init__(self,
                 *,
                 cid: str = None,
                 dbname: str = None,
                 connection_id: str = None,
                 srchostname: str = None,
                 srcport: str = None,
                 srctype: str = None,
                 usr: str = None,
                 uri: str = None,
                 status: str = None,
                 connection_name: str = None) -> None:
        """
        Initialize a DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem object.

        :param str cid: (optional) The identifier of the connection for the Data
               Virtualization.
        :param str dbname: (optional) The name of the database.
        :param str connection_id: (optional) The connection identifier for the
               platform.
        :param str srchostname: (optional) The hostname or IP address of the data
               source.
        :param str srcport: (optional) The port number of the data source.
        :param str srctype: (optional) The type of the data source.
        :param str usr: (optional) The user that has access to the data source.
        :param str uri: (optional) The URI of the data source.
        :param str status: (optional) The status of the data source.
        :param str connection_name: (optional) The name of the connection.
        """
        self.cid = cid
        self.dbname = dbname
        self.connection_id = connection_id
        self.srchostname = srchostname
        self.srcport = srcport
        self.srctype = srctype
        self.usr = usr
        self.uri = uri
        self.status = status
        self.connection_name = connection_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem':
        """Initialize a DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem object from a json dictionary."""
        args = {}
        if 'cid' in _dict:
            args['cid'] = _dict.get('cid')
        if 'dbname' in _dict:
            args['dbname'] = _dict.get('dbname')
        if 'connection_id' in _dict:
            args['connection_id'] = _dict.get('connection_id')
        if 'srchostname' in _dict:
            args['srchostname'] = _dict.get('srchostname')
        if 'srcport' in _dict:
            args['srcport'] = _dict.get('srcport')
        if 'srctype' in _dict:
            args['srctype'] = _dict.get('srctype')
        if 'usr' in _dict:
            args['usr'] = _dict.get('usr')
        if 'uri' in _dict:
            args['uri'] = _dict.get('uri')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'connection_name' in _dict:
            args['connection_name'] = _dict.get('connection_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cid') and self.cid is not None:
            _dict['cid'] = self.cid
        if hasattr(self, 'dbname') and self.dbname is not None:
            _dict['dbname'] = self.dbname
        if hasattr(self, 'connection_id') and self.connection_id is not None:
            _dict['connection_id'] = self.connection_id
        if hasattr(self, 'srchostname') and self.srchostname is not None:
            _dict['srchostname'] = self.srchostname
        if hasattr(self, 'srcport') and self.srcport is not None:
            _dict['srcport'] = self.srcport
        if hasattr(self, 'srctype') and self.srctype is not None:
            _dict['srctype'] = self.srctype
        if hasattr(self, 'usr') and self.usr is not None:
            _dict['usr'] = self.usr
        if hasattr(self, 'uri') and self.uri is not None:
            _dict['uri'] = self.uri
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'connection_name') and self.connection_name is not None:
            _dict['connection_name'] = self.connection_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjStoreConnectionResponseV2CosConnectionsItem():
    """
    ObjStoreConnectionResponseV2CosConnectionsItem.

    :attr str bucket_name: (optional)
    :attr str ccid: (optional)
    :attr str cid: (optional)
    :attr str endpoint: (optional)
    :attr bool removed: (optional)
    :attr str service_type: (optional)
    :attr str status: (optional)
    """

    def __init__(self,
                 *,
                 bucket_name: str = None,
                 ccid: str = None,
                 cid: str = None,
                 endpoint: str = None,
                 removed: bool = None,
                 service_type: str = None,
                 status: str = None) -> None:
        """
        Initialize a ObjStoreConnectionResponseV2CosConnectionsItem object.

        :param str bucket_name: (optional)
        :param str ccid: (optional)
        :param str cid: (optional)
        :param str endpoint: (optional)
        :param bool removed: (optional)
        :param str service_type: (optional)
        :param str status: (optional)
        """
        self.bucket_name = bucket_name
        self.ccid = ccid
        self.cid = cid
        self.endpoint = endpoint
        self.removed = removed
        self.service_type = service_type
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjStoreConnectionResponseV2CosConnectionsItem':
        """Initialize a ObjStoreConnectionResponseV2CosConnectionsItem object from a json dictionary."""
        args = {}
        if 'bucket_name' in _dict:
            args['bucket_name'] = _dict.get('bucket_name')
        if 'ccid' in _dict:
            args['ccid'] = _dict.get('ccid')
        if 'cid' in _dict:
            args['cid'] = _dict.get('cid')
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'removed' in _dict:
            args['removed'] = _dict.get('removed')
        if 'service_type' in _dict:
            args['service_type'] = _dict.get('service_type')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjStoreConnectionResponseV2CosConnectionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bucket_name') and self.bucket_name is not None:
            _dict['bucket_name'] = self.bucket_name
        if hasattr(self, 'ccid') and self.ccid is not None:
            _dict['ccid'] = self.ccid
        if hasattr(self, 'cid') and self.cid is not None:
            _dict['cid'] = self.cid
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'removed') and self.removed is not None:
            _dict['removed'] = self.removed
        if hasattr(self, 'service_type') and self.service_type is not None:
            _dict['service_type'] = self.service_type
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjStoreConnectionResponseV2CosConnectionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjStoreConnectionResponseV2CosConnectionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjStoreConnectionResponseV2CosConnectionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostDatasourceConnection():
    """
    PostDatasourceConnection.

    :attr str connection_id: The identifier of data source connection.
    :attr str datasource_type: The type of data source that you want to add.
    :attr str name: The name of data source.
    """

    def __init__(self,
                 connection_id: str,
                 datasource_type: str,
                 name: str) -> None:
        """
        Initialize a PostDatasourceConnection object.

        :param str connection_id: The identifier of data source connection.
        :param str datasource_type: The type of data source that you want to add.
        :param str name: The name of data source.
        """
        self.connection_id = connection_id
        self.datasource_type = datasource_type
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostDatasourceConnection':
        """Initialize a PostDatasourceConnection object from a json dictionary."""
        args = {}
        if 'connection_id' in _dict:
            args['connection_id'] = _dict.get('connection_id')
        else:
            raise ValueError('Required property \'connection_id\' not present in PostDatasourceConnection JSON')
        if 'datasource_type' in _dict:
            args['datasource_type'] = _dict.get('datasource_type')
        else:
            raise ValueError('Required property \'datasource_type\' not present in PostDatasourceConnection JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in PostDatasourceConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostDatasourceConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'connection_id') and self.connection_id is not None:
            _dict['connection_id'] = self.connection_id
        if hasattr(self, 'datasource_type') and self.datasource_type is not None:
            _dict['datasource_type'] = self.datasource_type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostDatasourceConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostDatasourceConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostDatasourceConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostDatasourceConnectionParametersProperties():
    """
    PostDatasourceConnectionParametersProperties.

    :attr str access_token: (optional)
    :attr str account_name: (optional)
    :attr str api_key: (optional)
    :attr str auth_type: (optional)
    :attr str client_id: (optional)
    :attr str client_secret: (optional)
    :attr str collection: (optional)
    :attr str credentials: (optional)
    :attr str database: (optional)
    :attr str host: (optional)
    :attr str http_path: (optional)
    :attr str jar_uris: (optional)
    :attr str jdbc_driver: (optional)
    :attr str jdbc_url: (optional)
    :attr str password: (optional)
    :attr str port: (optional)
    :attr str project_id: (optional)
    :attr str properties: (optional)
    :attr str refresh_token: (optional)
    :attr str role: (optional)
    :attr str sap_gateway_url: (optional)
    :attr str server: (optional)
    :attr str service_name: (optional)
    :attr str sid: (optional)
    :attr str ssl: (optional)
    :attr str ssl_certificate: (optional)
    :attr str ssl_certificate_host: (optional)
    :attr str ssl_certificate_validation: (optional)
    :attr str username: (optional)
    :attr str warehouse: (optional)
    """

    def __init__(self,
                 *,
                 access_token: str = None,
                 account_name: str = None,
                 api_key: str = None,
                 auth_type: str = None,
                 client_id: str = None,
                 client_secret: str = None,
                 collection: str = None,
                 credentials: str = None,
                 database: str = None,
                 host: str = None,
                 http_path: str = None,
                 jar_uris: str = None,
                 jdbc_driver: str = None,
                 jdbc_url: str = None,
                 password: str = None,
                 port: str = None,
                 project_id: str = None,
                 properties: str = None,
                 refresh_token: str = None,
                 role: str = None,
                 sap_gateway_url: str = None,
                 server: str = None,
                 service_name: str = None,
                 sid: str = None,
                 ssl: str = None,
                 ssl_certificate: str = None,
                 ssl_certificate_host: str = None,
                 ssl_certificate_validation: str = None,
                 username: str = None,
                 warehouse: str = None) -> None:
        """
        Initialize a PostDatasourceConnectionParametersProperties object.

        :param str access_token: (optional)
        :param str account_name: (optional)
        :param str api_key: (optional)
        :param str auth_type: (optional)
        :param str client_id: (optional)
        :param str client_secret: (optional)
        :param str collection: (optional)
        :param str credentials: (optional)
        :param str database: (optional)
        :param str host: (optional)
        :param str http_path: (optional)
        :param str jar_uris: (optional)
        :param str jdbc_driver: (optional)
        :param str jdbc_url: (optional)
        :param str password: (optional)
        :param str port: (optional)
        :param str project_id: (optional)
        :param str properties: (optional)
        :param str refresh_token: (optional)
        :param str role: (optional)
        :param str sap_gateway_url: (optional)
        :param str server: (optional)
        :param str service_name: (optional)
        :param str sid: (optional)
        :param str ssl: (optional)
        :param str ssl_certificate: (optional)
        :param str ssl_certificate_host: (optional)
        :param str ssl_certificate_validation: (optional)
        :param str username: (optional)
        :param str warehouse: (optional)
        """
        self.access_token = access_token
        self.account_name = account_name
        self.api_key = api_key
        self.auth_type = auth_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.collection = collection
        self.credentials = credentials
        self.database = database
        self.host = host
        self.http_path = http_path
        self.jar_uris = jar_uris
        self.jdbc_driver = jdbc_driver
        self.jdbc_url = jdbc_url
        self.password = password
        self.port = port
        self.project_id = project_id
        self.properties = properties
        self.refresh_token = refresh_token
        self.role = role
        self.sap_gateway_url = sap_gateway_url
        self.server = server
        self.service_name = service_name
        self.sid = sid
        self.ssl = ssl
        self.ssl_certificate = ssl_certificate
        self.ssl_certificate_host = ssl_certificate_host
        self.ssl_certificate_validation = ssl_certificate_validation
        self.username = username
        self.warehouse = warehouse

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostDatasourceConnectionParametersProperties':
        """Initialize a PostDatasourceConnectionParametersProperties object from a json dictionary."""
        args = {}
        if 'access_token' in _dict:
            args['access_token'] = _dict.get('access_token')
        if 'account_name' in _dict:
            args['account_name'] = _dict.get('account_name')
        if 'api_key' in _dict:
            args['api_key'] = _dict.get('api_key')
        if 'auth_type' in _dict:
            args['auth_type'] = _dict.get('auth_type')
        if 'client_id' in _dict:
            args['client_id'] = _dict.get('client_id')
        if 'client_secret' in _dict:
            args['client_secret'] = _dict.get('client_secret')
        if 'collection' in _dict:
            args['collection'] = _dict.get('collection')
        if 'credentials' in _dict:
            args['credentials'] = _dict.get('credentials')
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'http_path' in _dict:
            args['http_path'] = _dict.get('http_path')
        if 'jar_uris' in _dict:
            args['jar_uris'] = _dict.get('jar_uris')
        if 'jdbc_driver' in _dict:
            args['jdbc_driver'] = _dict.get('jdbc_driver')
        if 'jdbc_url' in _dict:
            args['jdbc_url'] = _dict.get('jdbc_url')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        if 'properties' in _dict:
            args['properties'] = _dict.get('properties')
        if 'refresh_token' in _dict:
            args['refresh_token'] = _dict.get('refresh_token')
        if 'role' in _dict:
            args['role'] = _dict.get('role')
        if 'sap_gateway_url' in _dict:
            args['sap_gateway_url'] = _dict.get('sap_gateway_url')
        if 'server' in _dict:
            args['server'] = _dict.get('server')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'sid' in _dict:
            args['sid'] = _dict.get('sid')
        if 'ssl' in _dict:
            args['ssl'] = _dict.get('ssl')
        if 'ssl_certificate' in _dict:
            args['ssl_certificate'] = _dict.get('ssl_certificate')
        if 'ssl_certificate_host' in _dict:
            args['ssl_certificate_host'] = _dict.get('ssl_certificate_host')
        if 'ssl_certificate_validation' in _dict:
            args['ssl_certificate_validation'] = _dict.get('ssl_certificate_validation')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'warehouse' in _dict:
            args['warehouse'] = _dict.get('warehouse')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostDatasourceConnectionParametersProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_token') and self.access_token is not None:
            _dict['access_token'] = self.access_token
        if hasattr(self, 'account_name') and self.account_name is not None:
            _dict['account_name'] = self.account_name
        if hasattr(self, 'api_key') and self.api_key is not None:
            _dict['api_key'] = self.api_key
        if hasattr(self, 'auth_type') and self.auth_type is not None:
            _dict['auth_type'] = self.auth_type
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'client_secret') and self.client_secret is not None:
            _dict['client_secret'] = self.client_secret
        if hasattr(self, 'collection') and self.collection is not None:
            _dict['collection'] = self.collection
        if hasattr(self, 'credentials') and self.credentials is not None:
            _dict['credentials'] = self.credentials
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'http_path') and self.http_path is not None:
            _dict['http_path'] = self.http_path
        if hasattr(self, 'jar_uris') and self.jar_uris is not None:
            _dict['jar_uris'] = self.jar_uris
        if hasattr(self, 'jdbc_driver') and self.jdbc_driver is not None:
            _dict['jdbc_driver'] = self.jdbc_driver
        if hasattr(self, 'jdbc_url') and self.jdbc_url is not None:
            _dict['jdbc_url'] = self.jdbc_url
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = self.properties
        if hasattr(self, 'refresh_token') and self.refresh_token is not None:
            _dict['refresh_token'] = self.refresh_token
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        if hasattr(self, 'sap_gateway_url') and self.sap_gateway_url is not None:
            _dict['sap_gateway_url'] = self.sap_gateway_url
        if hasattr(self, 'server') and self.server is not None:
            _dict['server'] = self.server
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'sid') and self.sid is not None:
            _dict['sid'] = self.sid
        if hasattr(self, 'ssl') and self.ssl is not None:
            _dict['ssl'] = self.ssl
        if hasattr(self, 'ssl_certificate') and self.ssl_certificate is not None:
            _dict['ssl_certificate'] = self.ssl_certificate
        if hasattr(self, 'ssl_certificate_host') and self.ssl_certificate_host is not None:
            _dict['ssl_certificate_host'] = self.ssl_certificate_host
        if hasattr(self, 'ssl_certificate_validation') and self.ssl_certificate_validation is not None:
            _dict['ssl_certificate_validation'] = self.ssl_certificate_validation
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'warehouse') and self.warehouse is not None:
            _dict['warehouse'] = self.warehouse
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostDatasourceConnectionParametersProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostDatasourceConnectionParametersProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostDatasourceConnectionParametersProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostPrimaryCatalogParametersAssetsItem():
    """
    PostPrimaryCatalogParametersAssetsItem.

    :attr str schema:
    :attr str table:
    """

    def __init__(self,
                 schema: str,
                 table: str) -> None:
        """
        Initialize a PostPrimaryCatalogParametersAssetsItem object.

        :param str schema:
        :param str table:
        """
        self.schema = schema
        self.table = table

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostPrimaryCatalogParametersAssetsItem':
        """Initialize a PostPrimaryCatalogParametersAssetsItem object from a json dictionary."""
        args = {}
        if 'schema' in _dict:
            args['schema'] = _dict.get('schema')
        else:
            raise ValueError('Required property \'schema\' not present in PostPrimaryCatalogParametersAssetsItem JSON')
        if 'table' in _dict:
            args['table'] = _dict.get('table')
        else:
            raise ValueError('Required property \'table\' not present in PostPrimaryCatalogParametersAssetsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostPrimaryCatalogParametersAssetsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema') and self.schema is not None:
            _dict['schema'] = self.schema
        if hasattr(self, 'table') and self.table is not None:
            _dict['table'] = self.table
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostPrimaryCatalogParametersAssetsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostPrimaryCatalogParametersAssetsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostPrimaryCatalogParametersAssetsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PrimaryCatalogInfoEntity():
    """
    PrimaryCatalogInfoEntity.

    :attr bool auto_profiling: (optional)
    :attr str bss_account_id: (optional)
    :attr int capacity_limit: (optional)
    :attr str description: (optional)
    :attr str generator: (optional)
    :attr bool is_governed: (optional)
    :attr str name: (optional)
    """

    def __init__(self,
                 *,
                 auto_profiling: bool = None,
                 bss_account_id: str = None,
                 capacity_limit: int = None,
                 description: str = None,
                 generator: str = None,
                 is_governed: bool = None,
                 name: str = None) -> None:
        """
        Initialize a PrimaryCatalogInfoEntity object.

        :param bool auto_profiling: (optional)
        :param str bss_account_id: (optional)
        :param int capacity_limit: (optional)
        :param str description: (optional)
        :param str generator: (optional)
        :param bool is_governed: (optional)
        :param str name: (optional)
        """
        self.auto_profiling = auto_profiling
        self.bss_account_id = bss_account_id
        self.capacity_limit = capacity_limit
        self.description = description
        self.generator = generator
        self.is_governed = is_governed
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrimaryCatalogInfoEntity':
        """Initialize a PrimaryCatalogInfoEntity object from a json dictionary."""
        args = {}
        if 'auto_profiling' in _dict:
            args['auto_profiling'] = _dict.get('auto_profiling')
        if 'bss_account_id' in _dict:
            args['bss_account_id'] = _dict.get('bss_account_id')
        if 'capacity_limit' in _dict:
            args['capacity_limit'] = _dict.get('capacity_limit')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'generator' in _dict:
            args['generator'] = _dict.get('generator')
        if 'is_governed' in _dict:
            args['is_governed'] = _dict.get('is_governed')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrimaryCatalogInfoEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'auto_profiling') and self.auto_profiling is not None:
            _dict['auto_profiling'] = self.auto_profiling
        if hasattr(self, 'bss_account_id') and self.bss_account_id is not None:
            _dict['bss_account_id'] = self.bss_account_id
        if hasattr(self, 'capacity_limit') and self.capacity_limit is not None:
            _dict['capacity_limit'] = self.capacity_limit
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'generator') and self.generator is not None:
            _dict['generator'] = self.generator
        if hasattr(self, 'is_governed') and self.is_governed is not None:
            _dict['is_governed'] = self.is_governed
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrimaryCatalogInfoEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrimaryCatalogInfoEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrimaryCatalogInfoEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PrimaryCatalogInfoMetadata():
    """
    PrimaryCatalogInfoMetadata.

    :attr str create_time: (optional)
    :attr str creator_id: (optional)
    :attr str guid: (optional)
    :attr str url: (optional)
    """

    def __init__(self,
                 *,
                 create_time: str = None,
                 creator_id: str = None,
                 guid: str = None,
                 url: str = None) -> None:
        """
        Initialize a PrimaryCatalogInfoMetadata object.

        :param str create_time: (optional)
        :param str creator_id: (optional)
        :param str guid: (optional)
        :param str url: (optional)
        """
        self.create_time = create_time
        self.creator_id = creator_id
        self.guid = guid
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrimaryCatalogInfoMetadata':
        """Initialize a PrimaryCatalogInfoMetadata object from a json dictionary."""
        args = {}
        if 'create_time' in _dict:
            args['create_time'] = _dict.get('create_time')
        if 'creator_id' in _dict:
            args['creator_id'] = _dict.get('creator_id')
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrimaryCatalogInfoMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = self.create_time
        if hasattr(self, 'creator_id') and self.creator_id is not None:
            _dict['creator_id'] = self.creator_id
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrimaryCatalogInfoMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrimaryCatalogInfoMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrimaryCatalogInfoMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class StorageDetails():
    """
    StorageDetails.

    :attr str total_size: (optional) Total cache storage size.
    :attr StorageDetailsEnabled enabled: (optional) Storage details of active
          caches.
    :attr StorageDetailsDisabled disabled: (optional) Storage details of inactive
          caches.
    """

    def __init__(self,
                 *,
                 total_size: str = None,
                 enabled: 'StorageDetailsEnabled' = None,
                 disabled: 'StorageDetailsDisabled' = None) -> None:
        """
        Initialize a StorageDetails object.

        :param str total_size: (optional) Total cache storage size.
        :param StorageDetailsEnabled enabled: (optional) Storage details of active
               caches.
        :param StorageDetailsDisabled disabled: (optional) Storage details of
               inactive caches.
        """
        self.total_size = total_size
        self.enabled = enabled
        self.disabled = disabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StorageDetails':
        """Initialize a StorageDetails object from a json dictionary."""
        args = {}
        if 'total_size' in _dict:
            args['total_size'] = _dict.get('total_size')
        if 'enabled' in _dict:
            args['enabled'] = StorageDetailsEnabled.from_dict(_dict.get('enabled'))
        if 'disabled' in _dict:
            args['disabled'] = StorageDetailsDisabled.from_dict(_dict.get('disabled'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StorageDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_size') and self.total_size is not None:
            _dict['total_size'] = self.total_size
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StorageDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StorageDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StorageDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class StorageDetailsDisabled():
    """
    Storage details of inactive caches.

    :attr int size: (optional) Total size of all inactive caches (in KB).
    :attr int count: (optional) Number of inactive caches.
    """

    def __init__(self,
                 *,
                 size: int = None,
                 count: int = None) -> None:
        """
        Initialize a StorageDetailsDisabled object.

        :param int size: (optional) Total size of all inactive caches (in KB).
        :param int count: (optional) Number of inactive caches.
        """
        self.size = size
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StorageDetailsDisabled':
        """Initialize a StorageDetailsDisabled object from a json dictionary."""
        args = {}
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StorageDetailsDisabled object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StorageDetailsDisabled object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StorageDetailsDisabled') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StorageDetailsDisabled') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class StorageDetailsEnabled():
    """
    Storage details of active caches.

    :attr int size: (optional) Total size of all active caches (in KB).
    :attr int count: (optional) Number of active caches.
    """

    def __init__(self,
                 *,
                 size: int = None,
                 count: int = None) -> None:
        """
        Initialize a StorageDetailsEnabled object.

        :param int size: (optional) Total size of all active caches (in KB).
        :param int count: (optional) Number of active caches.
        """
        self.size = size
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StorageDetailsEnabled':
        """Initialize a StorageDetailsEnabled object from a json dictionary."""
        args = {}
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StorageDetailsEnabled object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StorageDetailsEnabled object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StorageDetailsEnabled') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StorageDetailsEnabled') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TablesForRoleResponse():
    """
    TablesForRoleResponse.

    :attr List[TablesForRoleResponseObjectsItem] objects: (optional)
    """

    def __init__(self,
                 *,
                 objects: List['TablesForRoleResponseObjectsItem'] = None) -> None:
        """
        Initialize a TablesForRoleResponse object.

        :param List[TablesForRoleResponseObjectsItem] objects: (optional)
        """
        self.objects = objects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TablesForRoleResponse':
        """Initialize a TablesForRoleResponse object from a json dictionary."""
        args = {}
        if 'objects' in _dict:
            args['objects'] = [TablesForRoleResponseObjectsItem.from_dict(x) for x in _dict.get('objects')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TablesForRoleResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = [x.to_dict() for x in self.objects]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TablesForRoleResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TablesForRoleResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TablesForRoleResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TablesForRoleResponseObjectsItem():
    """
    TablesForRoleResponseObjectsItem.

    :attr str table_name: (optional) The virtualized table name that is granted
          access to role ROLENAME.
    :attr str table_schema: (optional) The SCHEMA of virtualized table that is
          granted access to role ROLENAME.
    """

    def __init__(self,
                 *,
                 table_name: str = None,
                 table_schema: str = None) -> None:
        """
        Initialize a TablesForRoleResponseObjectsItem object.

        :param str table_name: (optional) The virtualized table name that is
               granted access to role ROLENAME.
        :param str table_schema: (optional) The SCHEMA of virtualized table that is
               granted access to role ROLENAME.
        """
        self.table_name = table_name
        self.table_schema = table_schema

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TablesForRoleResponseObjectsItem':
        """Initialize a TablesForRoleResponseObjectsItem object from a json dictionary."""
        args = {}
        if 'table_name' in _dict:
            args['table_name'] = _dict.get('table_name')
        if 'table_schema' in _dict:
            args['table_schema'] = _dict.get('table_schema')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TablesForRoleResponseObjectsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'table_name') and self.table_name is not None:
            _dict['table_name'] = self.table_name
        if hasattr(self, 'table_schema') and self.table_schema is not None:
            _dict['table_schema'] = self.table_schema
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TablesForRoleResponseObjectsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TablesForRoleResponseObjectsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TablesForRoleResponseObjectsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TurnOnPolicyV2Response():
    """
    TurnOnPolicyV2Response.

    :attr str status:
    """

    def __init__(self,
                 status: str) -> None:
        """
        Initialize a TurnOnPolicyV2Response object.

        :param str status:
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnOnPolicyV2Response':
        """Initialize a TurnOnPolicyV2Response object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in TurnOnPolicyV2Response JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnOnPolicyV2Response object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnOnPolicyV2Response object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnOnPolicyV2Response') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnOnPolicyV2Response') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VirtualizeCosV2RequestVirtualTableDefItem():
    """
    VirtualizeCosV2RequestVirtualTableDefItem.

    :attr str column_name:
    :attr str column_type:
    """

    def __init__(self,
                 column_name: str,
                 column_type: str) -> None:
        """
        Initialize a VirtualizeCosV2RequestVirtualTableDefItem object.

        :param str column_name:
        :param str column_type:
        """
        self.column_name = column_name
        self.column_type = column_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VirtualizeCosV2RequestVirtualTableDefItem':
        """Initialize a VirtualizeCosV2RequestVirtualTableDefItem object from a json dictionary."""
        args = {}
        if 'column_name' in _dict:
            args['column_name'] = _dict.get('column_name')
        else:
            raise ValueError('Required property \'column_name\' not present in VirtualizeCosV2RequestVirtualTableDefItem JSON')
        if 'column_type' in _dict:
            args['column_type'] = _dict.get('column_type')
        else:
            raise ValueError('Required property \'column_type\' not present in VirtualizeCosV2RequestVirtualTableDefItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VirtualizeCosV2RequestVirtualTableDefItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'column_name') and self.column_name is not None:
            _dict['column_name'] = self.column_name
        if hasattr(self, 'column_type') and self.column_type is not None:
            _dict['column_type'] = self.column_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VirtualizeCosV2RequestVirtualTableDefItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VirtualizeCosV2RequestVirtualTableDefItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VirtualizeCosV2RequestVirtualTableDefItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VirtualizeTableParameterSourceTableDefItem():
    """
    VirtualizeTableParameterSourceTableDefItem.

    :attr str column_name: The name of the column.
    :attr str column_type: The type of the column.
    """

    def __init__(self,
                 column_name: str,
                 column_type: str) -> None:
        """
        Initialize a VirtualizeTableParameterSourceTableDefItem object.

        :param str column_name: The name of the column.
        :param str column_type: The type of the column.
        """
        self.column_name = column_name
        self.column_type = column_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VirtualizeTableParameterSourceTableDefItem':
        """Initialize a VirtualizeTableParameterSourceTableDefItem object from a json dictionary."""
        args = {}
        if 'column_name' in _dict:
            args['column_name'] = _dict.get('column_name')
        else:
            raise ValueError('Required property \'column_name\' not present in VirtualizeTableParameterSourceTableDefItem JSON')
        if 'column_type' in _dict:
            args['column_type'] = _dict.get('column_type')
        else:
            raise ValueError('Required property \'column_type\' not present in VirtualizeTableParameterSourceTableDefItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VirtualizeTableParameterSourceTableDefItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'column_name') and self.column_name is not None:
            _dict['column_name'] = self.column_name
        if hasattr(self, 'column_type') and self.column_type is not None:
            _dict['column_type'] = self.column_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VirtualizeTableParameterSourceTableDefItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VirtualizeTableParameterSourceTableDefItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VirtualizeTableParameterSourceTableDefItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VirtualizeTableParameterVirtualTableDefItem():
    """
    VirtualizeTableParameterVirtualTableDefItem.

    :attr str column_name: The name of the column.
    :attr str column_type: The type of the column.
    """

    def __init__(self,
                 column_name: str,
                 column_type: str) -> None:
        """
        Initialize a VirtualizeTableParameterVirtualTableDefItem object.

        :param str column_name: The name of the column.
        :param str column_type: The type of the column.
        """
        self.column_name = column_name
        self.column_type = column_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VirtualizeTableParameterVirtualTableDefItem':
        """Initialize a VirtualizeTableParameterVirtualTableDefItem object from a json dictionary."""
        args = {}
        if 'column_name' in _dict:
            args['column_name'] = _dict.get('column_name')
        else:
            raise ValueError('Required property \'column_name\' not present in VirtualizeTableParameterVirtualTableDefItem JSON')
        if 'column_type' in _dict:
            args['column_type'] = _dict.get('column_type')
        else:
            raise ValueError('Required property \'column_type\' not present in VirtualizeTableParameterVirtualTableDefItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VirtualizeTableParameterVirtualTableDefItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'column_name') and self.column_name is not None:
            _dict['column_name'] = self.column_name
        if hasattr(self, 'column_type') and self.column_type is not None:
            _dict['column_type'] = self.column_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VirtualizeTableParameterVirtualTableDefItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VirtualizeTableParameterVirtualTableDefItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VirtualizeTableParameterVirtualTableDefItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VirtualizeTableResponse():
    """
    VirtualizeTableResponse.

    :attr str table_name: The name of the table that is virtualized.
    :attr str schema_name: The schema of the table that is virtualized.
    """

    def __init__(self,
                 table_name: str,
                 schema_name: str) -> None:
        """
        Initialize a VirtualizeTableResponse object.

        :param str table_name: The name of the table that is virtualized.
        :param str schema_name: The schema of the table that is virtualized.
        """
        self.table_name = table_name
        self.schema_name = schema_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VirtualizeTableResponse':
        """Initialize a VirtualizeTableResponse object from a json dictionary."""
        args = {}
        if 'table_name' in _dict:
            args['table_name'] = _dict.get('table_name')
        else:
            raise ValueError('Required property \'table_name\' not present in VirtualizeTableResponse JSON')
        if 'schema_name' in _dict:
            args['schema_name'] = _dict.get('schema_name')
        else:
            raise ValueError('Required property \'schema_name\' not present in VirtualizeTableResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VirtualizeTableResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'table_name') and self.table_name is not None:
            _dict['table_name'] = self.table_name
        if hasattr(self, 'schema_name') and self.schema_name is not None:
            _dict['schema_name'] = self.schema_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VirtualizeTableResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VirtualizeTableResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VirtualizeTableResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CatalogPublishResponse():
    """
    CatalogPublishResponse.

    :attr List[CatalogPublishResponseDuplicateAssetsItem] duplicate_assets:
          (optional)
    :attr List[CatalogPublishResponseFailedAssetsItem] failed_assets: (optional)
    :attr List[CatalogPublishResponsePublishedAssetsItem] published_assets:
          (optional)
    """

    def __init__(self,
                 *,
                 duplicate_assets: List['CatalogPublishResponseDuplicateAssetsItem'] = None,
                 failed_assets: List['CatalogPublishResponseFailedAssetsItem'] = None,
                 published_assets: List['CatalogPublishResponsePublishedAssetsItem'] = None) -> None:
        """
        Initialize a CatalogPublishResponse object.

        :param List[CatalogPublishResponseDuplicateAssetsItem] duplicate_assets:
               (optional)
        :param List[CatalogPublishResponseFailedAssetsItem] failed_assets:
               (optional)
        :param List[CatalogPublishResponsePublishedAssetsItem] published_assets:
               (optional)
        """
        self.duplicate_assets = duplicate_assets
        self.failed_assets = failed_assets
        self.published_assets = published_assets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogPublishResponse':
        """Initialize a CatalogPublishResponse object from a json dictionary."""
        args = {}
        if 'duplicate_assets' in _dict:
            args['duplicate_assets'] = [CatalogPublishResponseDuplicateAssetsItem.from_dict(x) for x in _dict.get('duplicate_assets')]
        if 'failed_assets' in _dict:
            args['failed_assets'] = [CatalogPublishResponseFailedAssetsItem.from_dict(x) for x in _dict.get('failed_assets')]
        if 'published_assets' in _dict:
            args['published_assets'] = [CatalogPublishResponsePublishedAssetsItem.from_dict(x) for x in _dict.get('published_assets')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogPublishResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'duplicate_assets') and self.duplicate_assets is not None:
            _dict['duplicate_assets'] = [x.to_dict() for x in self.duplicate_assets]
        if hasattr(self, 'failed_assets') and self.failed_assets is not None:
            _dict['failed_assets'] = [x.to_dict() for x in self.failed_assets]
        if hasattr(self, 'published_assets') and self.published_assets is not None:
            _dict['published_assets'] = [x.to_dict() for x in self.published_assets]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogPublishResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogPublishResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogPublishResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjStoreConnectionResponseV2():
    """
    ObjStoreConnectionResponseV2.

    :attr List[ObjStoreConnectionResponseV2CosConnectionsItem] cos_connections:
          (optional)
    """

    def __init__(self,
                 *,
                 cos_connections: List['ObjStoreConnectionResponseV2CosConnectionsItem'] = None) -> None:
        """
        Initialize a ObjStoreConnectionResponseV2 object.

        :param List[ObjStoreConnectionResponseV2CosConnectionsItem]
               cos_connections: (optional)
        """
        self.cos_connections = cos_connections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjStoreConnectionResponseV2':
        """Initialize a ObjStoreConnectionResponseV2 object from a json dictionary."""
        args = {}
        if 'cos_connections' in _dict:
            args['cos_connections'] = [ObjStoreConnectionResponseV2CosConnectionsItem.from_dict(x) for x in _dict.get('cos_connections')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjStoreConnectionResponseV2 object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cos_connections') and self.cos_connections is not None:
            _dict['cos_connections'] = [x.to_dict() for x in self.cos_connections]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjStoreConnectionResponseV2 object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjStoreConnectionResponseV2') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjStoreConnectionResponseV2') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostPrimaryCatalog():
    """
    PostPrimaryCatalog.

    :attr str guid:
    :attr str name:
    :attr str description:
    """

    def __init__(self,
                 guid: str,
                 name: str,
                 description: str) -> None:
        """
        Initialize a PostPrimaryCatalog object.

        :param str guid:
        :param str name:
        :param str description:
        """
        self.guid = guid
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostPrimaryCatalog':
        """Initialize a PostPrimaryCatalog object from a json dictionary."""
        args = {}
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        else:
            raise ValueError('Required property \'guid\' not present in PostPrimaryCatalog JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in PostPrimaryCatalog JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in PostPrimaryCatalog JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostPrimaryCatalog object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostPrimaryCatalog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostPrimaryCatalog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostPrimaryCatalog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PrimaryCatalogInfo():
    """
    PrimaryCatalogInfo.

    :attr PrimaryCatalogInfoEntity entity: (optional)
    :attr str href: (optional)
    :attr PrimaryCatalogInfoMetadata metadata: (optional)
    """

    def __init__(self,
                 *,
                 entity: 'PrimaryCatalogInfoEntity' = None,
                 href: str = None,
                 metadata: 'PrimaryCatalogInfoMetadata' = None) -> None:
        """
        Initialize a PrimaryCatalogInfo object.

        :param PrimaryCatalogInfoEntity entity: (optional)
        :param str href: (optional)
        :param PrimaryCatalogInfoMetadata metadata: (optional)
        """
        self.entity = entity
        self.href = href
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrimaryCatalogInfo':
        """Initialize a PrimaryCatalogInfo object from a json dictionary."""
        args = {}
        if 'entity' in _dict:
            args['entity'] = PrimaryCatalogInfoEntity.from_dict(_dict.get('entity'))
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'metadata' in _dict:
            args['metadata'] = PrimaryCatalogInfoMetadata.from_dict(_dict.get('metadata'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrimaryCatalogInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity.to_dict()
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrimaryCatalogInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrimaryCatalogInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrimaryCatalogInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SuccessResponse():
    """
    SuccessResponse.

    :attr str message:
    """

    def __init__(self,
                 message: str) -> None:
        """
        Initialize a SuccessResponse object.

        :param str message:
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SuccessResponse':
        """Initialize a SuccessResponse object from a json dictionary."""
        args = {}
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in SuccessResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SuccessResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SuccessResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SuccessResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SuccessResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
