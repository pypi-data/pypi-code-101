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
from . import conf
from .base import RequestAPI


class CollectionsAPI(object):
    def __init__(self, client):
        self.client = client
        self.host = "" or conf.HOST.format(api_name="bk-apigateway")

        self.sync_api = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/sync/")

        self.sync_stage = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/stages/sync/")

        self.sync_resources = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/resources/sync/")

        self.create_resource_version = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/resource_versions/")

        self.sync_access_strategy = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/access_strategies/sync/")

        self.apply_permissions = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/permissions/apply/")

        self.get_apigw_public_key = RequestAPI(client=self.client, method="GET", host=self.host, path="/api/v1/apis/{api_name}/public_key/")

        self.get_latest_resource_version = RequestAPI(client=self.client, method="GET", host=self.host, path="/api/v1/apis/{api_name}/resource_versions/latest/")

        self.release = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/resource_versions/release/")

        self.grant_permissions = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/permissions/grant/")

        self.import_resource_docs_by_archive = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/resource-docs/import/by-archive/")

        self.import_resource_docs_by_swagger = RequestAPI(client=self.client, method="POST", host=self.host, path="/api/v1/apis/{api_name}/resource-docs/import/by-swagger/")
