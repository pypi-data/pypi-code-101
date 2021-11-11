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


class SumOperate:
    """
    若干列进行加法运算
    """
    label = 'SUM'

    @staticmethod
    def process_operate(dataframe, source_col_list, new_column):
        i = 0
        for col in source_col_list:
            p_col = col.get('column', None)
            if i == 0:
                dataframe[new_column] = dataframe[p_col]
            else:
                dataframe[new_column] += dataframe[p_col]
            i += 1
        return dataframe


class AvgOperate:
    """
    若干列进行求均值
    """
    label = 'AVG'

    @staticmethod
    def process_operate(dataframe, source_col_list, new_column):
        i = 0
        for col in source_col_list:
            p_col = col.get('column', None)
            if i == 0:
                dataframe[new_column] = dataframe[p_col]
            else:
                dataframe[new_column] += dataframe[p_col]
            i += 1
        dataframe[new_column] = dataframe[new_column] / i
        return dataframe


class COUNT_COLOperate:
    """
    在每一行后面添加1,用于计数
    """
    label = 'COUNT_COL'

    @staticmethod
    def process_operate(dataframe, new_column, **kwargs):
        dataframe[new_column] = 1
        return dataframe
