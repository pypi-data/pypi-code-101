# -*- coding: utf-8 -*-
"""
 * TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-蓝鲸 PaaS 平台(BlueKing-PaaS) available.
 * Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://opensource.org/licenses/MIT
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
"""
from bkapi_client_core.apigateway import APIGatewayClient, Operation, OperationGroup, bind_property


class Group(OperationGroup):
    # 申请网关API访问权限
    apply_permissions = bind_property(
        Operation, name="apply_permissions", method="POST",
        path="/api/v1/apis/{api_name}/permissions/apply/",
    )

    # 创建资源版本
    create_resource_version = bind_property(
        Operation, name="create_resource_version", method="POST",
        path="/api/v1/apis/{api_name}/resource_versions/",
    )

    # 获取网关公钥
    get_apigw_public_key = bind_property(
        Operation, name="get_apigw_public_key", method="GET",
        path="/api/v1/apis/{api_name}/public_key/",
    )

    # 获取网关最新版本
    get_latest_resource_version = bind_property(
        Operation, name="get_latest_resource_version", method="GET",
        path="/api/v1/apis/{api_name}/resource_versions/latest/",
    )

    # 网关为应用主动授权
    grant_permissions = bind_property(
        Operation, name="grant_permissions", method="POST",
        path="/api/v1/apis/{api_name}/permissions/grant/",
    )

    # 通过文档归档文件导入资源文档
    import_resource_docs_by_archive = bind_property(
        Operation, name="import_resource_docs_by_archive", method="POST",
        path="/api/v1/apis/{api_name}/resource-docs/import/by-archive/",
    )

    import_resource_docs_by_swagger = bind_property(
        Operation, name="import_resource_docs_by_swagger", method="POST",
        path="/api/v1/apis/{api_name}/resource-docs/import/by-swagger/",
    )

    # 发布版本
    release = bind_property(
        Operation, name="release", method="POST",
        path="/api/v1/apis/{api_name}/resource_versions/release/",
    )

    # 同步策略
    sync_access_strategy = bind_property(
        Operation, name="sync_access_strategy", method="POST",
        path="/api/v1/apis/{api_name}/access_strategies/sync/",
    )

    # 同步网关
    sync_api = bind_property(
        Operation, name="sync_api", method="POST",
        path="/api/v1/apis/{api_name}/sync/",
    )

    # 同步资源
    sync_resources = bind_property(
        Operation, name="sync_resources", method="POST",
        path="/api/v1/apis/{api_name}/resources/sync/",
    )

    # 同步环境
    sync_stage = bind_property(
        Operation, name="sync_stage", method="POST",
        path="/api/v1/apis/{api_name}/stages/sync/",
    )


class Client(APIGatewayClient):
    """bk-apigateway
    蓝鲸API网关
    """
    _api_name = "bk-apigateway"

    api = bind_property(Group, name="api")
