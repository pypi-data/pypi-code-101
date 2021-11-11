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


from dataframe_operator.operate_utils.col_generate.base_operate import SumOperate, AvgOperate, COUNT_COLOperate

OPERATE_CLASS_MAP = {
    "Sum": SumOperate,
    "Avg": AvgOperate,
    "COUNT_COL": COUNT_COLOperate,
}


class OperateContext:
    """
    操作上下文
    操作上下文由于需要动态加载算法，不能使用单例模式
    """

    @staticmethod
    def find_operation_and_process_operate(source_col_list, operate, new_column, dataframe):
        """
        上下文对外提供调用的主入口
        提示：
            显式生成列算法调用为动态加载
            隐式生成列算法调用为静态加载
        """
        operate_label = operate.get("value", None)
        # 显式生成列
        operator = OPERATE_CLASS_MAP.get(operate_label)

        if not operate_label or not operator:
            return dataframe

        return operator.process_operate(
            dataframe=dataframe,
            source_col_list=source_col_list,
            new_column=new_column
        )
