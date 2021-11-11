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
from dataframe_operator.dataframe_col_generator import DataFrameColGenerator
from dataframe_operator.dataframe_combiner import DataFrameCombiner
from dataframe_operator.dataframe_driller import DataframeDriller
from dataframe_operator.dataframe_filter import DataFrameFilter
from dataframe_operator.dataframe_sample_getter import DataFrameSampleGetter
from dataframe_operator.dataframe_sort import DataFrameSort
from dataframe_operator.dataframe_topN import DataFrameTopN
from dataprime.init_celery import create_files


class DataPrime:

    def __init__(self, dataframe=None, **kwargs):
        self.dataframe = dataframe
        self.kwargs = kwargs
        self.celery_config = self.kwargs.get("celery")

        # dataframe过滤器
        self.df_filter = DataFrameFilter()

        # dataframe列生成器
        self.df_col_generator = DataFrameColGenerator()

        # dataframe聚合器
        self.df_combiner = DataFrameCombiner()

        # dataframe排序器
        self.df_sort = DataFrameSort()

        # dataframeTOPN
        self.df_topN = DataFrameTopN()

        # dataframe采样器
        self.dataframe_sample_getter = DataFrameSampleGetter()

        # dataframe钻取器
        self.dataframe_driller = DataframeDriller()

        # dataframe操作节点映射
        self.calculation_operators = {
            # 钻取
            "DRILLING": {
                "method": self.dataframe_driller.get_drilled_dataframe,
            },

            # 采样
            "SAMPLING": {
                "method": self.dataframe_sample_getter.get_sampled_df,
            },

            # 过滤
            "FILTER": {
                "method": self.df_filter.get_filter_df,
            },

            # 生成器
            "GENERATOR": {
                "method": self.df_col_generator.get_col_gen_df,
            },

            # 聚合
            "AGGREGATION": {
                "method": self.df_combiner.get_combined_dataframe,
            }
        }

    @staticmethod
    def init_celery():
        """创建celery相关工程目录"""
        create_files()

    def wrap_param(self, **kwargs):
        """使用pickle序列化参数供celery任务调用"""
        pickle_data = pickle.dumps(kwargs)
        base64_str = base64.b64encode(pickle_data).decode()
        return base64_str

    def filter(self, filter_list):
        """过滤"""
        self.dataframe = self.df_filter.get_filter_df(self.dataframe, filter_list=filter_list)
        return self

    def drill(self, drill_granularity_list, drill_node_list, dimensions):
        """钻取"""
        self.dataframe = self.dataframe_driller.get_drilled_dataframe(
            self.dataframe,
            drill_granularity_list=drill_granularity_list,
            drill_node_list=drill_node_list,
            dimensions=dimensions
        )
        return self

    def sample(self, number, type):
        """采样"""
        self.dataframe = self.dataframe_sample_getter.get_sampled_df(
            self.dataframe,
            sample={"number": number, "type": type}
        )
        return self

    def generate(self, generated_metric_list):
        """生成器"""
        self.dataframe = self.df_col_generator.get_col_gen_df(
            self.dataframe,
            generated_metric_list=generated_metric_list
        )
        return self

    def aggregate(self, metrics, dimensions, aggregation_list):
        """聚合"""
        self.dataframe = self.df_combiner.get_combined_dataframe(
            self.dataframe,
            metrics=metrics,
            dimensions=dimensions,
            aggregation_list=aggregation_list
        )
        return self

    def order_by(self, column, condition):
        """排序"""
        self.dataframe = self.df_sort.get_sort_df(
            self.dataframe,
            sort={"column": column, "condition": condition}
        )
        return self

    def top_n(self, column, condition, limit):
        """top N 根据某一字段排序,获取前n条"""
        self.dataframe = self.df_topN.get_topN_df(
            self.dataframe,
            topn={"column": column, "condition": condition, "limit": limit}
        )
        return self

    @staticmethod
    def fill_nan_to_none(dataframe):
        """
        空值填充为None，保证json序列化可以实现
        """
        dataframe = dataframe.where(dataframe.notnull(), None)
        return dataframe

    def process_df_operator(self):
        """
        根据不同参数调用不同操作类, 对dataframe进行处理
        """
        dataframe = self.fill_nan_to_none(self.dataframe)
        calculation_flow_nodes = self.kwargs.get('calculation_flow_nodes', [])

        # 遍历计算节点,依次处理
        for calculation_node in calculation_flow_nodes:
            cal_node = self.calculation_operators.get(calculation_node)
            if cal_node:
                dataframe = cal_node['method'](dataframe, **self.kwargs)

        # 排序
        dataframe = self.df_sort.get_sort_df(dataframe, **self.kwargs)

        # topN
        dataframe = self.df_topN.get_topN_df(dataframe, **self.kwargs)

        return dataframe

    def split_dataframe(self, dataframe):
        """将dataframe按照维度和度量拆分"""
        dimensions_data = [
            {
                "name": dimension["column"],
                "data": dataframe[dimension["column"]].to_list()
            } for dimension in self.kwargs["dimensions"]
        ]

        metrics_data = [
            {
                "name": metric["column"],
                "data": dataframe[metric["column"]].to_list()
            } for metric in self.kwargs["metrics"]
        ]
        return {
            "x_data_list": dimensions_data,
            "y_data_list": metrics_data
        }


if __name__ == '__main__':
    pass
