"""
@File  : constants.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/13
@Desc  :
"""
# -*- coding: utf-8 -*-

from smartDocx.constants import DocFontSize, DocFontFamily, DocAlignment, TableLandscapeAlignment, \
    TableVerticalAlignment, Orientation


# =========================
# =====  默认文本样式   =====
# =========================
class DocStylesBase(object):
    """文档样式基类"""

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _to_dict(self):
        """转字典"""
        styles = dict()
        for attr in dir(self):
            if attr.startswith('_'):
                continue
            value = getattr(self, attr)
            # 自定义的Enum类型,需转成实际数值
            if isinstance(value, (DocFontFamily, DocAlignment, TableLandscapeAlignment,
                                  TableVerticalAlignment, DocFontSize, Orientation)):
                value = value.value
            styles[attr] = value
        return styles

    def __iter__(self):
        for attr in self._to_dict():
            yield attr

    def __getitem__(self, item):
        return self._to_dict()[item]


class PageStyleBase(DocStylesBase):
    """页面样式基类"""

    def __init__(self,
                 page_width: (float, int) = 21.00,
                 page_height: (float, int) = 29.70,
                 left_margin: (int, float) = 3.17,
                 right_margin: (int, float) = 3.17,
                 top_margin: (int, float) = 2.54,
                 bottom_margin: (int, float) = 2.54,
                 orientation: Orientation = Orientation.portrait,
                 **kwargs):
        """
        :param page_width: 页面宽度
        :param page_height: 页面高度
        :param left_margin: 左边距cm
        :param right_margin: 右边距cm
        :param top_margin: 上边距cm
        :param bottom_margin: 底边距cm
        :param orientation: 纸张方向: 默认纵向portrait
        :param kwargs:
        """
        super(PageStyleBase, self).__init__(
            page_width=page_width,
            page_height=page_height,
            left_margin=left_margin,
            right_margin=right_margin,
            top_margin=top_margin,
            bottom_margin=bottom_margin,
            orientation=orientation,
            **kwargs)


class ParagraphStyleBase(DocStylesBase):
    """段落样式基类"""

    def __init__(self,
                 font_size=DocFontSize.SmallFour,
                 text_align=DocAlignment.justify,
                 font_weight=False,
                 color='#000000',
                 font_type=DocFontFamily.MSYH,
                 west_font_type=DocFontFamily.MSYH,
                 line_indent=True,
                 line_spacing=None,
                 style='Normal',
                 space_before=5,
                 space_after=5,
                 italic=False,
                 **kwargs):
        super(ParagraphStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            font_weight=font_weight,
            color=color,
            font_type=font_type,
            west_font_type=west_font_type,
            line_indent=line_indent,
            line_spacing=line_spacing,
            style=style,
            space_before=space_before,
            space_after=space_after,
            italic=italic,
            **kwargs)


class TitleStyleBase(DocStylesBase):
    """标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Four,
                 text_align=DocAlignment.justify,
                 font_weight=False,
                 color='#000000',
                 font_type=DocFontFamily.MSYH,
                 west_font_type=DocFontFamily.MSYH,
                 level=1,
                 line_indent=False,
                 line_spacing=None,
                 style='Normal',
                 space_before=5,
                 space_after=5,
                 italic=False,
                 underline=0,
                 **kwargs):
        """
        :param font_size: 字体大小
        :param text_align: 对齐模式
        :param font_weight: 字体粗细
        :param color: 字体颜色
        :param font_type: 中文字体类型
        :param west_font_type: 西文字体类型
        :param level: 标题等级
        :param line_indent: 首航缩进
        :param line_spacing: 行间距
        :param style: 字体类型
        :param space_before: 段前间距
        :param space_after: 段后间距
        :param italic: 是否斜体
        :param underline: 下划线
        :param kwargs:
        """
        super(TitleStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            font_weight=font_weight,
            color=color,
            font_type=font_type,
            west_font_type=west_font_type,
            level=level,
            line_indent=line_indent,
            line_spacing=line_spacing,
            style=style,
            space_before=space_before,
            space_after=space_after,
            italic=italic,
            underline=underline,
            **kwargs)


# 文章标题
class PaperTitleStyleBase(TitleStyleBase):
    """文章标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.SmallTwo,
                 text_align=DocAlignment.center,
                 font_weight=True,
                 level=0,
                 line_spacing=1.5,
                 space_before=10,
                 **kwargs):
        super(PaperTitleStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


class PaperSubTitleStyleBase(TitleStyleBase):
    """文章副标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.SmallFour,
                 text_align=DocAlignment.center,
                 font_weight=True,
                 level=0,
                 line_spacing=1.5,
                 space_before=10,
                 **kwargs):
        super(PaperSubTitleStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


# 正文
class ContentStyleBase(DocStylesBase):
    """正文样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Four,
                 text_align=DocAlignment.justify,
                 font_weight=False,
                 color='#000000',
                 font_type=DocFontFamily.MSYH,
                 west_font_type=DocFontFamily.MSYH,
                 line_indent=True,
                 line_spacing=1.5,
                 style='Normal',
                 space_before=5,
                 space_after=5,
                 italic=False,
                 paragraph_underline=None,
                 **kwargs):
        super(ContentStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            font_weight=font_weight,
            color=color,
            font_type=font_type,
            west_font_type=west_font_type,
            line_indent=line_indent,
            line_spacing=line_spacing,
            style=style,
            space_before=space_before,
            space_after=space_after,
            italic=italic,
            paragraph_underline=paragraph_underline,
            **kwargs)


class AbstractStyleBase(ContentStyleBase):
    """摘要样式基类"""

    def __init__(self,
                 font_size=DocFontSize.SmallFour,
                 font_weight=True,
                 font_type=DocFontFamily.KT,
                 west_font_type=DocFontFamily.MSYH,
                 line_spacing=1,
                 space_before=10,
                 space_after=30,
                 **kwargs):
        super(AbstractStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            font_type=font_type,
            west_font_type=west_font_type,
            line_spacing=line_spacing,
            space_before=space_before,
            space_after=space_after,
            **kwargs)


# 段落标题
class FirstTitleStyleBase(TitleStyleBase):
    """段落: 一级标题样式基类"""

    def __init__(self,
                 font_weight=True,
                 level=1,
                 line_spacing=1.5,
                 space_before=10,
                 **kwargs):
        super(FirstTitleStyleBase, self).__init__(
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


class SecondTitleStyleBase(TitleStyleBase):
    """段落: 二级级标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Four,
                 font_weight=True,
                 level=2,
                 line_spacing=1.5,
                 space_before=5,
                 **kwargs):
        super(SecondTitleStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


class ThirdTitleStyleBase(TitleStyleBase):
    """段落: 三级标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.SmallFour,
                 font_weight=True,
                 level=3,
                 line_spacing=1.5,
                 space_before=10,
                 **kwargs):
        super(ThirdTitleStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


class FourthTitleStyleBase(TitleStyleBase):
    """段落: 四级标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Five,
                 font_weight=True,
                 level=4,
                 line_spacing=1.5,
                 space_before=10,
                 **kwargs):
        super(FourthTitleStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            **kwargs)


class UnderlineTitleStyleBase(TitleStyleBase):
    """下划线标题(正文内容)"""

    def __init__(self,
                 font_size=DocFontSize.Five,
                 text_align=DocAlignment.justify,
                 color='#042D86',
                 font_weight=True,
                 line_indent=False,
                 line_spacing=1,
                 level=None,
                 space_before=10,
                 space_after=5,
                 paragraph_underline=None,
                 **kwargs):
        """
        :param font_size:
        :param text_align:
        :param color:
        :param font_weight:
        :param line_indent:
        :param line_spacing:
        :param level:
        :param space_before:
        :param space_after:
        :param paragraph_underline: 段落下划线样式
        :param kwargs:
        """
        if paragraph_underline is None:
            paragraph_underline = {
                "sz": 15,  # 粗细程度
                "color": "#042D86",  # 颜色
                "val": "single"  # 线条类型
            }
        super(UnderlineTitleStyleBase, self).__init__(
            font_size=font_size,
            text_align=text_align,
            color=color,
            font_weight=font_weight,
            line_indent=line_indent,
            line_spacing=line_spacing,
            level=level,
            space_before=space_before,
            space_after=space_after,
            paragraph_underline=paragraph_underline,
            **kwargs)


# 表格
class TableStyleBase(DocStylesBase):
    """表格样式基类"""

    def __init__(self,
                 alignment=TableLandscapeAlignment.center,
                 vertical_alignment=TableVerticalAlignment.center,
                 font_size=DocFontSize.Five,
                 font_type=DocFontFamily.MSYH,
                 west_font_type=DocFontFamily.MSYH,
                 font_weight=False,
                 color='#000000',
                 italic=False,
                 underline=0,
                 autofit=True,
                 background=None,
                 **kwargs):
        """

        :param alignment: 水平对齐方式
        :param vertical_alignment: 垂直对齐方式
        :param font_size:
        :param font_type:
        :param west_font_type:
        :param font_weight:
        :param color:
        :param italic:
        :param underline:
        :param autofit: 自动单元格宽度
        :param background: 单元格背景色
        :param kwargs:
        """
        super(TableStyleBase, self).__init__(
            alignment=alignment,
            vertical_alignment=vertical_alignment,
            font_size=font_size,
            font_type=font_type,
            west_font_type=west_font_type,
            font_weight=font_weight,
            color=color,
            italic=italic,
            underline=underline,
            autofit=autofit,
            background=background,
            **kwargs)


class TableTitleStyleBase(TitleStyleBase):
    """表格标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Five,
                 font_weight=True,
                 level=None,
                 line_spacing=1.5,
                 space_before=5,
                 space_after=0,
                 underline=0,
                 background=None,
                 **kwargs):
        super(TableTitleStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            space_after=space_after,
            underline=underline,
            background=background,
            **kwargs)


class TableHeadStyleBase(TitleStyleBase):
    """表格首部样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Five,
                 font_weight=True,
                 level=None,
                 line_spacing=1.5,
                 space_before=5,
                 space_after=0,
                 background=None,
                 **kwargs):
        super(TableHeadStyleBase, self).__init__(
            font_size=font_size,
            font_weight=font_weight,
            level=level,
            line_spacing=line_spacing,
            space_before=space_before,
            space_after=space_after,
            background=background,
            **kwargs)


class TableBodyStyleBase(TableStyleBase):
    """表格内容样式基类"""

    def __init__(self, **kwargs):
        super(TableBodyStyleBase, self).__init__(**kwargs)


# 图片
class PicTitleStyleBase(TitleStyleBase):
    """图片标题样式基类"""

    def __init__(self,
                 font_size=DocFontSize.Five,
                 level=None,
                 **kwargs):
        super(PicTitleStyleBase, self).__init__(
            font_size=font_size,
            level=level,
            **kwargs)


class PicImgStyleBase(DocStylesBase):
    """图片样式基类"""

    def __init__(self,
                 zom_rate=1,
                 alignment=DocAlignment.center,
                 **kwargs):
        """

        :param zom_rate: 缩放比例
        :param alignment: 对齐方式
        :param kwargs:
        """
        super(PicImgStyleBase, self).__init__(
            zom_rate=zom_rate,
            alignment=alignment,
            **kwargs)
