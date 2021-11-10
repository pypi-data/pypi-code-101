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

from dataprime_celery.tasks import filter_task


class AsyncDataPrime:

    @staticmethod
    def wrap_param(**kwargs):
        """使用pickle序列化参数供celery任务调用"""
        pickle_data = pickle.dumps(kwargs)
        base64_str = base64.b64encode(pickle_data).decode()
        return base64_str

    def async_filter(self, dataframe, filter_list):
        param = self.wrap_param(dataframe=dataframe, filter_list=filter_list)
        task_id = filter_task.delay(param)
        return task_id
