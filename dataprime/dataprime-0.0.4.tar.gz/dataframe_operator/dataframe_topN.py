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


class DataFrameTopN:
    """
    TopN实现类
    """
    def get_topN_df(self, dataframe, **kwargs):
        """
        获取topn后的dataframe
        """
        topn = kwargs.get("topn")
        if topn:
            dataframe = self._topn_data(topn, dataframe)
        return dataframe

    @staticmethod
    def _topn_data(topn_dict, dataframe):
        """
        获取topN
        """
        condition = topn_dict.get("condition")
        column = topn_dict.get("column")
        value = topn_dict.get("limit")

        # 排序前#项
        if condition == 'desc' and value:
            dataframe = dataframe.nlargest(value, column)
        # 排序后#项
        if condition == 'asc' and value:
            dataframe = dataframe.nsmallest(value, column)
        return dataframe
