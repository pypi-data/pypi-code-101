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
import json
import logging

from .client import RequestAPIClient
from .conf import APP_CODE, SECRET_KEY
from .exceptions import APIException

logger = logging.getLogger(__name__)

__all__ = [
    "get_client_by_request",
    "get_client_by_user",
]


HEADER_BK_AUTHORIZATION = "X-Bkapi-Authorization"


def get_client_by_request(request, stage="prod", common_args=None, headers={}):
    """根据当前请求返回一个client
    :param request: 一个django request实例
    :param stage: 请求环境，默认为prod
    :param common_args: 公共请求参数
    :param headers: 头部信息
    :returns: 一个初始化好的APIClint对象
    """
    is_authenticated = request.user.is_authenticated
    if callable(is_authenticated):
        is_authenticated = is_authenticated()
    if is_authenticated:
        try:
            from bkoauth import get_access_token

            access_token = get_access_token(request)
            headers.update(
                {
                    HEADER_BK_AUTHORIZATION: json.dumps({"access_token": access_token.access_token}),
                }
            )
        except Exception:
            pass
    else:
        raise APIException(u"用户未通过验证")

    return RequestAPIClient(
        app_code=APP_CODE, app_secret=SECRET_KEY, headers=headers, common_args=common_args, stage=stage
    )


def get_client_by_user(user, stage="prod", common_args=None, headers={}):
    """根据user实例返回一个client
    :param user: 用户
    :param stage: 请求环境，默认为prod
    :param common_args: 公共请求参数
    :param headers: 头部信息
    :returns: 一个初始化好的APIClint对象
    """
    if hasattr(user, "username"):
        user = user.username
    try:
        from bkoauth import get_access_token_by_user

        access_token = get_access_token_by_user(user)
        headers.update(
            {
                HEADER_BK_AUTHORIZATION: json.dumps({"access_token": access_token.access_token}),
            }
        )
    except Exception:
        pass

    return RequestAPIClient(
        app_code=APP_CODE, app_secret=SECRET_KEY, headers=headers, common_args=common_args, stage=stage
    )
