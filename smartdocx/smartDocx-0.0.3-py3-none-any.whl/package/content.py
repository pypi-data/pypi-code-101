"""
@File  : content.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/16
@Desc  : 
"""
# -*- coding: utf-8 -*-
from smartDocx.config import DocStylesBase
from smartDocx.package.paragraph import Paragraph


class Content(Paragraph):
    """正文内容"""

    def __init__(self, config: DocStylesBase, content_type='CONTENT'):
        super(Content, self).__init__(config=config, content_type=content_type)
