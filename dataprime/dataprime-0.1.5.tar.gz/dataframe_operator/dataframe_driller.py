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
import pandas as pd
from pandas import DataFrame


class BaseDriller:

    def __init__(self,
                 dataframe: DataFrame,
                 dimensions: list("Dimension"),
                 drill_granularity_list: list,
                 drill_node_list: list
                 ):
        self.dataframe = dataframe
        self.dimensions = dimensions
        self.drill_granularity_list = drill_granularity_list
        self.drill_node_list = drill_node_list

    def get_drilled_dataframe(self):
        raise NotImplementedError


class DatetimeDriller(BaseDriller):
    """
    日期钻取
    执行过程：
    1、根据粒度信息，获取最细的粒度
    2、根据最细的粒度和最细粒度的上一个粒度的值，过滤dataframe
    3、根据最细粒度的格式，格式化日期字段，使得统一日期的数据能聚合。
    钻取的方式有：
            1、年-月-日
            2、年-日
            3、年-月
    返回：
        1、所有年 -> 某一年的所有月 -> 某一月的所有天
        2、所有年 -> 某一年的所有月日
        3、所有年 -> 某一年的所有月
    """
    drill_dimension_type = ['datetime']

    def __init__(self,
                 dataframe: DataFrame,
                 dimensions: list("Dimension"),
                 drill_granularity_list: list,
                 drill_node_list: list
                 ):
        """
        dataframe： Dataframe
        column: dataframe列名称
        drill_granularity_list: 钻取粒度list
        drill_node_list： 钻取粒度过滤值
        """
        super(DatetimeDriller, self).__init__(
            dataframe, dimensions, drill_granularity_list, drill_node_list)

    def _get_drill_dimension(self) -> "Dimension":
        """
        获取需要钻取的维度
        """
        for dimension in self.dimensions:
            if dimension["dtype"] in self.drill_dimension_type:
                return dimension
        raise ValueError("cannot found a drill dimension")

    def _get_minimum_granularity(self) -> tuple:
        """
        获取最小的粒度信息
        返回：
            tuple: granularity_index, granularity_name
        """
        # 如果没有上一层，返回粒度里面的第一个粒度
        if not self.drill_node_list:
            return 0, self.drill_granularity_list[0]['value'].lower()

        gran_index = 0
        for drill_node in self.drill_node_list:
            if drill_node['granularity']:
                gran_index += 1
        if gran_index < len(self.drill_granularity_list):
            return gran_index, self.drill_granularity_list[gran_index]['value'].lower()
        return -1, self.drill_granularity_list[-1]['value'].lower()

    def _filter_dataframe(self, column: str, mini_gran_tuple: tuple):
        """
        根据上一粒度值，过滤dataframe。
        存在的情况：
            1、年-月-日
            2、年-日
            3、年-月

        1、所有年 -> 某一年的所有月 -> 某一月的所有天
        2、所有年 -> 某一年的所有月日
        3、所有年 -> 某一年的所有月            
        """
        gran_index, mini_gran = mini_gran_tuple[0], mini_gran_tuple[1]
        # 最小粒度为年, 则不进行过滤
        if gran_index <= 0 and mini_gran == 'year':
            return self.dataframe

        date_filter_str = ""
        for drill_node in self.drill_node_list:
            if drill_node['granularity']:
                granularity = drill_node['granularity'].lower()
                granularity_value = drill_node['point']
                if granularity == 'year':
                    date_filter_str += granularity_value
                elif granularity == 'month':
                    date_filter_str += "-{}".format(granularity_value)
                elif granularity == 'day':
                    date_filter_str += "-{}".format(granularity_value)

        if date_filter_str:
            # 以时间列设置索引,再通过时间字符串进行过滤
            self.dataframe[column] = pd.to_datetime(self.dataframe[column])
            self.dataframe = self.dataframe.set_index(column)
            self.dataframe = self.dataframe.loc[date_filter_str].reset_index()

    def _format_datetime(self, column: str, mini_gran_tuple: tuple):
        """
        格式化钻取的维度，是否填空
        存在的情况：
            1、年-月-日
            2、年-日
            3、年-月

        1、所有年 -> 某一年的所有月 -> 某一月的所有天
        2、所有年 -> 某一年的所有月日
        3、所有年 -> 某一年的所有月             
        """
        gran_index, mini_gran = mini_gran_tuple[0], mini_gran_tuple[1]
        # 不需要过滤
        if gran_index <= 0 and mini_gran == 'year':
            self.dataframe[column] = self.dataframe[column].dt.strftime("%Y")
        # 处理年-> 日
        elif mini_gran == "day" and self.drill_granularity_list[gran_index - 1]['value'].lower() == "year":
            self.dataframe[column] = self.dataframe[column].dt.strftime(
                "%m-%d")
        # 处理年-> 月
        elif mini_gran == "month" and self.drill_granularity_list[gran_index - 1]['value'].lower() == "year":
            self.dataframe[column] = self.dataframe[column].dt.strftime("%m")
        elif mini_gran == "day":
            self.dataframe[column] = self.dataframe[column].dt.strftime("%d")

    def get_drilled_dataframe(self):
        """
        执行钻取
        """
        # 获取需要钻取的维度
        dimension = self._get_drill_dimension()
        column = dimension["column"]

        # 获取最小粒度
        mini_gran_tuple = self._get_minimum_granularity()

        # 执行数据过滤
        self._filter_dataframe(column, mini_gran_tuple)

        # 执行日期格式化
        self._format_datetime(column, mini_gran_tuple)

        return self.dataframe


class DataframeDriller:
    """
    基于dataframe的钻取实现
    """

    @staticmethod
    def get_drilled_dataframe(dataframe: DataFrame, **kwargs) -> DataFrame:
        drill_granularity_list = kwargs.get("drill_granularity_list")
        dimensions = kwargs.get('dimensions')
        if not (drill_granularity_list and dimensions):
            return dataframe
        drill_node_list = kwargs.get("drill_node_list")

        datetime_driller = DatetimeDriller(
            dataframe,
            dimensions,
            drill_granularity_list,
            drill_node_list
        )
        dataframe = datetime_driller.get_drilled_dataframe()
        return dataframe
