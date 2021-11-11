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


class DataFrameSort:
    """
    排序器实现类
    """
    def get_sort_df(self, dataframe, **kwargs):
        """
        获取排序后的dataframe
        """
        sort = kwargs.get("sort", None)
        if sort:
            dataframe = self._sort_data(sort, dataframe)
        return dataframe

    @staticmethod
    def _sort_data(sort_dict, dataframe):
        """
        对数值进行过滤
        """
        condition = sort_dict.get("condition", None)
        column = sort_dict.get("column", None)

        # 升序排序
        if condition == 'asc':
            dataframe = dataframe.sort_values(by=[column])
        # 降序排序
        if condition == 'desc':
            dataframe = dataframe.sort_values(by=[column], ascending=False)
        return dataframe
