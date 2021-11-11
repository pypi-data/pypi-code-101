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

from dataframe_operator.dataframe_col_generator import DataFrameColGenerator
from dataframe_operator.dataframe_combiner import DataFrameCombiner
from dataframe_operator.dataframe_filter import DataFrameFilter
from dataframe_operator.dataframe_sample_getter import DataFrameSampleGetter
from dataframe_operator.dataframe_sort import DataFrameSort
from dataframe_operator.dataframe_topN import DataFrameTopN


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


@shared_task
def generate_task(param):
    """generate任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    generated_metric_list = param_dict["generated_metric_list"]
    dataframe = DataFrameColGenerator().get_col_gen_df(dataframe, generated_metric_list=generated_metric_list)
    result = dataframe.to_json()
    return result


@shared_task
def aggregate_task(param):
    """aggreate任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    metrics = param_dict["metrics"]
    dimensions = param_dict["dimensions"]
    aggregation_list = param_dict["aggregation_list"]
    dataframe = DataFrameCombiner().get_combined_dataframe(
        dataframe,
        metrics=metrics,
        dimensions=dimensions,
        aggregation_list=aggregation_list
    )
    result = dataframe.to_json()
    return result


@shared_task
def sort_task(param):
    """sort任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    sort = param_dict["sort"]
    dataframe = DataFrameSort().get_sort_df(
        dataframe,
        sort=sort
    )
    result = dataframe.to_json()
    return result


@shared_task
def top_n_task(param):
    """top N任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    topn = param_dict["topn"]
    dataframe = DataFrameTopN().get_topN_df(
        dataframe,
        topn=topn
    )
    result = dataframe.to_json()
    return result


@shared_task
def sample_task(param):
    """sample任务"""
    param_dict = decode_param(param)
    dataframe = param_dict["dataframe"]
    sample = param_dict["sample"]
    dataframe = DataFrameSampleGetter().get_sampled_df(
        dataframe,
        sample=sample
    )
    result = dataframe.to_json()
    return result

