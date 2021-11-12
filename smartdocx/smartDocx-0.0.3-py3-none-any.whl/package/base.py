"""
@File  : base.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/13
@Desc  : 自动化报告
"""
# -*- coding: utf-8 -*-

from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

from smartDocx.config import DocStylesBase
from smartDocx.constants import DEFAULT_WEST_FONT


class Base(object):
    """基类"""

    def __init__(self, content_type: str, config: (DocStylesBase, dict), *args, **kwargs):
        """

        :param content_type: 类型
        :param config: 配置
        :param args:
        :param kwargs:
        """
        self.type = content_type
        self.styles = config._to_dict() if isinstance(config, (DocStylesBase,)) else config
        self.args = args
        self.kwargs = kwargs

    def generate(self, *args, **kwargs):
        """生成文本"""
        raise Exception("子类需重写该方法")

    def _format(self, *args, **kwargs):
        """格式化"""
        pass

    # ==============
    # = 字体格式设置 =
    # ==============
    def _handle_font_weight(self, obj, value):
        """设置字体粗细"""
        if value is True:
            obj.bold = True
        else:
            obj.bold = False

    def _handle_font_size(self, obj, value):
        """设置字体大小"""
        if isinstance(value, (int, float)):
            obj.font.size = Pt(value)

    def _handle_color(self, obj, value):
        """设置字体颜色"""
        if isinstance(value, str):
            obj.font.color.rgb = self._handle_rgb_hex_str(rgb_hex_str=value)

    def _handle_font_type(self, obj, value):
        """设置字体类型"""
        if isinstance(value, str):
            # 西文字体
            obj.font.name = self.styles.get('west_font_type', DEFAULT_WEST_FONT)
            # 中文字体
            obj._element.rPr.rFonts.set(*(qn('w:eastAsia'), value))

    def _handle_italic(self, obj, value):
        """设置斜体"""
        if value is True:
            obj.font.italic = True
        else:
            obj.font.italic = False

    def _handle_underline(self, obj, value):
        """设置下划线"""
        if isinstance(value, int):
            obj.underline = value

    def _handle_rgb_hex_str(self, rgb_hex_str):
        """处理十六进制RGB值"""
        r = int(rgb_hex_str[1:3], 16)
        g = int(rgb_hex_str[3:5], 16)
        b = int(rgb_hex_str[5:], 16)
        return RGBColor(r, g, b)
