"""
@File  : __init__.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/13
@Desc  : 
"""
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

__all__ = (
    'Paragraph',
    'Title',
    'Table',
    'Picture',
    'Chart',
    'Content',
    'SmartReportBase',
    'SmartReportDataBase',
    'put_paragraph_data',
    'handle_paragraph',
    'utils'
)

from .report import SmartReportBase, SmartReportDataBase
from .package.chart import Chart
from .package.content import Content
from .package.paragraph import Paragraph
from .package.picture import Picture
from .package.table import Table
from .package.title import Title
from .utils import put_paragraph_data, handle_paragraph
