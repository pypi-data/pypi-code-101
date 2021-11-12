"""
@File  : echart.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/16
@Desc  : 
"""
# -*- coding: utf-8 -*-
import datetime
import os

from pyecharts.faker import _Faker
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

from smartDocx.constants import TMP_DIR


class Chart(object):
    """
    echarts图表
        该类仅实现生成图片功能(该类的render方法),其余配置请参考官方文档。


        # 参考文档及链接
        1.pyecharts
            官网文档: https://pyecharts.org/#/zh-cn/intro
            官方示例: https://gallery.pyecharts.org/#/README
        2.echarts
            官方文档: https://echarts.apache.org/zh/feature.html
            官方示例: https://echarts.apache.org/examples/zh/index.html

    """

    def __init__(self, tmp_dir: str = None):
        """
        :param tmp_dir:
        """
        if tmp_dir:
            if os.path.exists(tmp_dir):
                raise FileNotFoundError
        else:
            self.tmp_dir = TMP_DIR  # 临时文件夹
        self.picture_type = 'png'  # 图片类型
        self.pic_path = None  # 图片绝对路径
        self.chart_obj = None  # 原始pyecharts的图对象
        self._faker = _Faker

    def demo(self):
        """样例"""
        # self.chart_obj = Bar()

    @staticmethod
    def get_map_max_value(array, count: int = 5):
        """
        获取地区图例最大值
        @param array: 数组
        @param count: 均分数量
        """
        max_value = max(array)
        if max_value <= 10:
            return 10
        avg = max_value // count
        while avg * count * 0.8 <= max_value:
            if avg % 5 == 0 and (max_value <= avg * count):
                break
            avg += 1
        return avg * count

    def render(self, del_html=True):
        """
        渲染html,获取图片路径
            需要提前安装好node,实现html文件的截图;
        :param del_html: 是否删除html文件,默认删除,防止垃圾文件占用磁盘空间
        :return:
        """
        if not self.chart_obj:
            raise ValueError('chart_obj为None')
        html_path = self._get_path(prefix='html', file_type='html')
        pic_path = self._get_path(prefix='pic', file_type=self.picture_type)
        self.chart_obj.render(html_path)
        make_snapshot(snapshot, html_path, pic_path)
        if del_html:
            self.remove(html_path)
        return pic_path

    def _get_path(self, prefix, file_type):
        """
        获取路径
            临时文件夹tmp中存放pyecharts渲染生成的html和图片文件;
        :param prefix: 前缀
        :param file_type: 文件类型
        :return:
        """
        params = {
            'current': datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
            'prefix': prefix,
            'file_type': file_type
        }
        picture_path = os.path.join(self.tmp_dir, '{prefix}_{current}.{file_type}'.format(**params))
        return picture_path.replace('\\', '/')

    @staticmethod
    def remove(file_path):
        """
        删除文件
            html转图片后,删除原html文件
        :param file_path: 文件绝对路径
        :return:
        """
        try:
            os.remove(file_path)
        except Exception as e:
            print(e)
