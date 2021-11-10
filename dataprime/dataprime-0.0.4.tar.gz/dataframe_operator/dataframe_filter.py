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
from dateutil.parser import parse


class DataFrameFilter:
    """过滤器实现类"""

    @staticmethod
    def _get_the_same_type_of_df_col(filter_list):
        """
        把前端传递的值转化为dataframe每一列的相同数据类型值,
        确保可以dataframe的操作可以正确执行
        """
        for filter_param in filter_list:
            value = filter_param["filter"]["value"]
            dtype = filter_param["dtype"]
            if dtype == "int":
                value = int(value)
            elif dtype == "float":
                value = float(value)
            elif dtype == "str":
                value = str(value)
            elif dtype == "datetime":
                value = parse(value)
            filter_param["filter"]["value"] = value

        return filter_list

    def get_filter_df(self, dataframe, **kwargs):
        """
        获取过滤数值后的dataframe
        """
        filter_list = kwargs.get("filter_list")
        if filter_list:
            # 类型转换
            same_type_filter_params = self._get_the_same_type_of_df_col(filter_list)
            for filter_dict in same_type_filter_params:
                dataframe = self._filter_data(filter_dict, dataframe)
        return dataframe

    @staticmethod
    def _filter_data(filter_dict, dataframe):
        """
        对数值进行过滤
        """
        data_filter = filter_dict.get("filter", None)
        condition = data_filter.get("condition", None)
        column = filter_dict.get("column", None)
        value = data_filter.get("value", None)
        data_max = data_filter.get("max", None)
        data_min = data_filter.get("min", None)

        # 等于
        if condition == 'equal':
            dataframe = dataframe[dataframe[column] == value]
        # 不等于
        elif condition == 'not_equal':
            dataframe = dataframe[dataframe[column] != value]
        # 大于
        elif condition == 'greater_than':
            dataframe = dataframe[dataframe[column] > value]
        # 大于等于
        elif condition == 'equal_greater_than':
            dataframe = dataframe[dataframe[column] >= value]
        # 小于
        elif condition == 'less_than':
            dataframe = dataframe[dataframe[column] < value]
        # 小于等于
        elif condition == 'equal_less_than':
            dataframe = dataframe[dataframe[column] <= value]
        # 区间内
        elif condition == 'in_between':
            dataframe = dataframe[(dataframe[column] < data_max) & (
                dataframe[column] > data_min)]
        # 区间外
        elif condition == 'out_between':
            dataframe = dataframe[(dataframe[column] > data_max) | (
                dataframe[column] < data_min)]
        # 包含
        elif condition == 'contains':
            dataframe = dataframe[dataframe[column].str.contains(value)]
        # 不包含
        elif condition == 'not_contains':
            dataframe = dataframe[dataframe[column].str.contains(
                value) == False]
        # 高于平均值
        elif condition == 'greater_than_average':
            dataframe = dataframe[dataframe[column] > dataframe[column].mean()]
        # 低于平均值
        elif condition == 'less_than_average':
            dataframe = dataframe[dataframe[column] < dataframe[column].mean()]

        return dataframe
