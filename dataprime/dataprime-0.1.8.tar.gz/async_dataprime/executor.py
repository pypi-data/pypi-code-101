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

from dataprime_celery.tasks import filter_task, aggregate_task, sort_task, top_n_task, sample_task, generate_task


class AsyncDataPrime:
    """异步任务调用类"""

    @staticmethod
    def wrap_param(**kwargs):
        """使用pickle序列化参数供celery任务调用"""
        pickle_data = pickle.dumps(kwargs)
        base64_str = base64.b64encode(pickle_data).decode()
        return base64_str

    def filter(self, dataframe, filter_list):
        """异步过滤"""
        param = self.wrap_param(
            dataframe=dataframe,
            filter_list=filter_list
        )
        return filter_task.delay(param)

    def generate(self, dataframe, generated_metric_list):
        """异步生成"""
        param = self.wrap_param(
            dataframe=dataframe,
            generated_metric_list=generated_metric_list,
        )
        return generate_task.delay(param)

    def aggregate(self, dataframe, metrics, dimensions, aggregation_list):
        """异步聚合"""
        param = self.wrap_param(
            dataframe=dataframe,
            metrics=metrics,
            dimensions=dimensions,
            aggregation_list=aggregation_list,
        )
        return aggregate_task.delay(param)

    def sort(self, dataframe, sort):
        """异步排序"""
        param = self.wrap_param(
            dataframe=dataframe,
            sort=sort
        )
        return sort_task.delay(param)

    def top_n(self, dataframe, topn):
        """异步排序"""
        param = self.wrap_param(
            dataframe=dataframe,
            topn=topn
        )
        return top_n_task.delay(param)

    def sample(self, dataframe, sample):
        """异步排序"""
        param = self.wrap_param(
            dataframe=dataframe,
            sample=sample
        )
        return sample_task.delay(param)