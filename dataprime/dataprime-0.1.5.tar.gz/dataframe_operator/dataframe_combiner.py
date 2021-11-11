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
from numpy import float64


class DataFrameCombiner(object):
    """
    dataframe数据聚合器，聚合原本的dataframe中的重复列
    """
    aggregation_method = ['count', 'sum', 'mean',
                          'median', 'std', 'var',
                          'max', 'min']

    def _parse_aggregation(self, aggregation_list) -> dict:
        """
        解析度量的聚合方式的参数
        """
        aggregations = {}
        if not aggregation_list:
            return aggregations
        for each in aggregation_list:
            if 'aggregation_option' in each and each['aggregation_option']['value'] in self.aggregation_method:
                aggregations[each['column']] = each['aggregation_option']['value']

        return aggregations

    @staticmethod
    def _set_default_aggregation(dataframe: DataFrame, dimensions: list, aggregation: dict) -> dict:
        """
        设置默认的聚合，如果一个度量没有设置聚合方式， 默认求和。
        """
        # 获取除dimension外的所有column
        df_columns = set(dataframe.columns.to_list())
        seted_agg_column = set(aggregation.keys())
        not_set_agg_metrics = df_columns - set(dimensions) - seted_agg_column
        for agg in not_set_agg_metrics:
            aggregation[agg] = "sum"

        return aggregation

    @staticmethod
    def _make_sure_metric_is_numeric(dataframe, metrics):
        """
        确保聚合操作中的数据都是数值类型, 将其数据转换为metric中声明的数据
        """
        for metric in metrics:
            if not metric.get("column"):
                continue
            if metric["dtype"] == "decimal":
                dataframe[metric["column"]] = dataframe[metric["column"]].astype(float64)
        return dataframe

    def get_combined_dataframe(self, dataframe, **kwargs) -> DataFrame:
        """
        获取数据聚合后的dataframe, 顺便会加上一行新的
        """
        metrics = kwargs.get('metrics')
        dimensions = kwargs.get('dimensions')
        # todo 是否只允许传入一个维度?
        if not dimensions:
            return dataframe

        column_by = [dimension["column"] for dimension in dimensions]

        # 生成集合参数
        aggregation = self._parse_aggregation(kwargs.get("aggregation_list"))

        # 设置默认聚合参数
        aggregation = self._set_default_aggregation(dataframe, column_by, aggregation)

        # 转换数值类型
        dataframe = self._make_sure_metric_is_numeric(dataframe, metrics)

        # 执行聚合
        # as_index=False可以保持被用来分组的列在聚合后不被删除
        # sort默认为true会为分组后的数据排序
        # group_keys=False是为了保持列的顺序不变
        dataframe = dataframe.groupby(
            by=column_by,
            as_index=False,
            sort=False,
            group_keys=False
        ).agg(aggregation).reset_index(drop=True)

        return dataframe
