"""
Copyright (c) [Year] [name of copyright holder]
[Software Name] is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import base64
import pickle
from celery import shared_task

from dataframe_operator.dataframe_filter import DataFrameFilter


def decode_param(param_str):
    """解析参数字符串"""
    base64_str = base64.b64decode(param_str)
    param_dict = pickle.loads(base64_str)
    return param_dict


@shared_task
def filter_task(param):
    """filter任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    filter_list = param_dict["filter_list"]
    dataframe = DataFrameFilter().get_filter_df(dataframe, filter_list=filter_list)
    result = dataframe.to_json()
    return result
