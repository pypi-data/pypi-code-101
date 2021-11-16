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
from .resources import CollectionsAPI

# 判断是否在Django环境下，如果在Django环境下，默认从settings中读取配置信息，否则，使用默认配置
# 客户端可采用import后再修改的方式来改变配置
try:
    from django.conf import settings

    APP_CODE = settings.APP_CODE
    SECRET_KEY = settings.SECRET_KEY
except Exception:
    APP_CODE = None
    SECRET_KEY = None

try:
    from bkapi_client_core.config import settings

    HOST = settings.get("BK_API_URL_TMPL", "")
except ImportError:
    HOST = ""

AVAILABLE_COLLECTIONS = {
    "api": CollectionsAPI,
}
