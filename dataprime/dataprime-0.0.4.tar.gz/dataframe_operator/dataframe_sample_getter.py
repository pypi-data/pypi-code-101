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
from pandas import DataFrame
import math
import random


class DataFrameSampleGetter:
    """
    dataframe采样器
    处理：各种采样机制
    """

    def get_sampled_df(self, dataframe, **kwargs):

        sample_param = kwargs.get("sample")
        row_limit = sample_param.get("number")  # 采样数量,注意不是采样的间隔
        sample_type = sample_param.get("type")  # 采样类型
        if not sample_type or not row_limit or not isinstance(row_limit, int):
            return dataframe

        # 根据采样的类型执行对应的方法
        if sample_type == 'random':
            return self._process_random_sample(dataframe, row_limit)
        elif sample_type == 'equidistant':
            return self._process_equidistant_sample(dataframe, row_limit)

    @staticmethod
    def _process_random_sample(dataframe, row_limit):
        """
        执行随机采样
        """
        if isinstance(dataframe, DataFrame):
            length = math.ceil(len(dataframe) / row_limit)
            arr = []  # 被等距采样的行数
            for i in range(1, len(dataframe)):
                if i % length == 1:
                    print(i-length+1, i)
                    arr.append(random.randint(i-length+1, i))
            return dataframe.iloc[arr]
        return dataframe

    @staticmethod
    def _process_equidistant_sample(dataframe, row_limit):
        """
        执行等距采样
        """
        if isinstance(dataframe, DataFrame):
            length = math.ceil(len(dataframe) / row_limit)
            arr = []  # 被等距采样的行数
            for i in range(1, len(dataframe)):
                if i % length == 1:
                    arr.append(i-1)
            return dataframe.iloc[arr]
        return dataframe
