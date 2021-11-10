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
from dataframe_operator.operate_utils.col_generate.operate_context import OperateContext


class DataFrameColGenerator:
    """
    生成器实现类
    """
    def get_col_gen_df(self, dataframe, **kwargs):
        """
        生成器处理参数返回df
        """
        # 处理用户显式生成的列generate_metric_list
        generated_metric_list = kwargs.get("generated_metric_list", None)
        if generated_metric_list:
            for generated_metric in generated_metric_list:
                if generated_metric:
                    dataframe = self._process_generate_col(dataframe, generated_metric)

        return dataframe

    @staticmethod
    def _process_generate_col(dataframe, metrics_to_generate):
        """
        调用算法生成一列
        """
        new_column = metrics_to_generate.get("column", None)
        source_col_list = metrics_to_generate.get("source_col_list", None)
        operate = metrics_to_generate.get("operate", None)

        if operate and new_column:
            opr_context = OperateContext()
            dataframe = opr_context.find_operation_and_process_operate(
                source_col_list, operate, new_column, dataframe
            )

        return dataframe
