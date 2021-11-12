"""
@File  : title.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/13
@Desc  : 
"""

# -*- coding: utf-8 -*-
from docx import Document
from docx.document import Document as DocObject

from smartDocx.config import DocStylesBase
from smartDocx.package.paragraph import Paragraph


class Title(Paragraph):
    """标题"""

    def __init__(self, config: DocStylesBase, content_type='TITLE'):
        super(Title, self).__init__(config=config, content_type=content_type)

    def generate(self, doc_obj: DocObject, text: str, *args, **kwargs):
        """生成标题"""
        title = doc_obj.add_heading(level=self.styles['level'])  # 添加新段落
        run_obj = title.add_run(text=text)  # 新段落添加文本
        self._format(title, run_obj)

    def _format(self, title, run_obj):
        """格式化"""
        self._format_paragraph(title)  # 新段落格式化
        self._format_font(run_obj=run_obj)  # 字体格式化
