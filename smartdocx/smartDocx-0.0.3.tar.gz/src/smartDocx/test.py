# """
# @File  : test.py
# @IDE   : PyCharm
# @Author: Sanbom
# @Date  : 2021/7/13
# @Desc  :
# """
# # -*- coding: utf-8 -*-
#
# from kits.smart_report.package.content import Content
# from kits.smart_report.package.paragraph import Paragraph
# from kits.smart_report.package.table import Table
# from kits.smart_report.package.title import Title
# from kits.smart_report.report import SmartReportDataBase, SmartReportBase
# from kits.smart_report.utils import put_paragraph_data, handle_paragraph
#
#
# class SmartReportData(SmartReportDataBase):
#     """智能报告数据"""
#
#     def __init__(self, sql_client=None, neo4j_client=None, es_client=None, *args,
#                  **kwargs):
#         super(SmartReportData, self).__init__(sql_client, neo4j_client, es_client, *args,
#                                               **kwargs)
#
#     @put_paragraph_data
#     def chapter_01_paragraph_01(self):
#         """章节01"""
#         return dict(a='{}_a'.format('chapter_01'))
#
#     @put_paragraph_data
#     def chapter_01_01_paragraph_01(self):
#         """章节1.1"""
#         data = dict(
#             a='{}_a'.format('chapter_01_0a=1'),
#             columns=['市级责任单位', '工单批次', '事项批次'],
#             data=[
#                 ['上海市房屋管理局', 796, 613],
#                 ['上海市交通委员会', 294, 239],
#                 ['上海市住房和城乡建设管理委员会', 96, 85],
#                 ['上海市城市管', 67, 54],
#                 ['上海市绿化和市容管理局(上海市林业局)', 42, 38],
#                 ['上海市公积金管理中心', 19, 9],
#                 ['上海市水务局（上海市海洋局）', 7, 6],
#             ],
#             table_title='表xxx 表格标题'
#         )
#         return data
#
#     @put_paragraph_data
#     def chapter_01_01_01_paragraph_01(self):
#         """章节1.1.1"""
#         data = dict(
#             a='{}_a'.format('chapter_01_01_01'),
#             chart_01=dict(
#                 xaxis=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
#                 yaxis=[
#                     [5, 20, 36, 10, 75, 90],
#                     [15, 6, 45, 20, 35, 66]
#                 ],
#                 legend=['商家A', '商家B']
#             )
#         )
#         return data
#
#     @put_paragraph_data
#     def chapter_01_01_01_01_paragraph_01(self):
#         """章节1.1.1.1"""
#         return dict(a='{}_a'.format('chapter_01_01_01_01'))
#
#     @put_paragraph_data
#     def chapter_01_02_paragraph_01(self):
#         """章节1.2"""
#         data = dict(
#             columns=['责任单位', '信访事项', '批次'],
#             data=[
#                 ['崇明区', '城乡建设 - 住房保障与房地产 - 房地产开发管理 ', 174],
#                 ['浦东新区', '城乡建设 - 住房保障与房地产 - 物业服务', 84],
#                 ['黄浦区', '城乡建设 - 国有土地上房屋征收与补偿 - 安置补偿', 63],
#                 ['浦东新区', '城乡建设 - 住房保障与房地产 - 房地产开发管理', 52],
#             ],
#             table_title='表xxx 表格标题'
#         )
#         return data
#
#     @put_paragraph_data
#     def chapter_02_paragraph_01(self):
#         """章节2"""
#         return dict(a='{}_a'.format('chapter_02'))
#
#     @put_paragraph_data
#     def chapter_03_paragraph_01(self):
#         """章节3"""
#         return dict(a='{}_a'.format('chapter_03'))
#
#
# class SmartReport(SmartReportBase):
#     """智能报告"""
#
#     def __init__(self, filename: str, data: dict, *args, template: str = None, **kwargs):
#         super(SmartReport, self).__init__(filename, data, *args, template=template, **kwargs)
#
#     def handle_paper_heading(self):
#         """文章标题"""
#         title = Content(config=self.title_level_0_style)
#         title.generate(doc_obj=self.doc_obj, text='自动化测试报告')
#
#     def handle_paper_subheading(self):
#         """文章副标题"""
#         paragraph = Paragraph(config=self.paper_subheading_style)
#         paragraph.generate(doc_obj=self.doc_obj, text='时间范围: 2021年1月7日 --- 2021年2月7日')
#
#     def handle_abstract(self):
#         """文章摘要"""
#         content = Content(config=self.abstract)
#         text = "[本分析报告所指的信访数据以国家信访系统上海分系统登记的来信、来访、网信为依据，涵盖建设交通系统" \
#                "市级党政机关、委属事业单位、代管的中央在沪单位。市住建委、市交通委、市水务局、市绿化市容局、市房管" \
#                "局、市城管执法局、市公积金中心为上海市信访办管理系统中独立承办的责任单位。市建设交通党委代管的中央在" \
#                "沪单位由市住建委代为转交，由具体单位承办。]"
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01(self):
#         """章节1"""
#         p_title = Title(config=self.title_level_1_style)
#         text = "一、总体情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01(self):
#         """章节1.1 标题"""
#         p_title = Title(config=self.title_level_2_style)
#         text = "1.1 情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01_paragraph_01(self):
#         """章节1.1 段落01"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "新华社北京7月13日电 中国共产党成立100周年庆祝活动总结会议13日上午在京举行。中共中央总书记、国家主席、" \
#                "中央军委主席习近平在人民大会堂亲切会见庆祝活动筹办工作各方面代表，向他们表示衷心感谢和诚挚问候，对他们的辛" \
#                "勤工作和优异成绩给予充分肯定，勉励大家奋发进取、再创佳绩。{a}".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#         table = Table(config=self.table_body_style)
#         table.generate(doc_obj=self.doc_obj, columns=chapter_data.get('columns'), data=chapter_data.get('data'),
#                        table_title=chapter_data.get('table_title'), table_title_style=self.table_title_style)
#
#     @handle_paragraph
#     def chapter_01_01_01(self):
#         """章节1.1.1 标题"""
#         p_title = Title(config=self.title_level_3_style)
#         text = "1.1.1 总体情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01_01_paragraph_01(self):
#         """章节1.1.1 段落1"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "新华社北京7月13日电 中国共产党成立100周年庆祝活动总结会议13日上午在京举行。中共中央总书记、国家主席、" \
#                "中央军委主席习近平在人民大会堂亲切会见庆祝活动筹办工作各方面代表，向他们表示衷心感谢和诚挚问候，对他们的辛" \
#                "勤工作和优异成绩给予充分肯定，勉励大家奋发进取、再创佳绩。{a}".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01_01_01(self):
#         """章节1.1.1.1"""
#         p_title = Title(config=self.title_level_4_style)
#         text = "1.1.1.1 四级标题"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01_01_01_paragraph_01(self):
#         """章节1.1.1.1 段落01"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "四级标题测试内容。{a}".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_02(self):
#         """章节01.02 标题"""
#         p_title = Title(config=self.title_level_2_style)
#         text = "1.2 总体情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_02_paragraph_01(self):
#         """章节01.02 段落1"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "新华社北京7月13日电 中国共产党成立100周年庆祝活动总结会议13日上午在京举行。中共中央总书记、国家主席、" \
#                "中央军委主席习近平在人民大会堂亲切会见庆祝活动筹办工作各方面代表，向他们表示衷心感谢和诚挚问候，对他们的辛" \
#                "勤工作和优异成绩给予充分肯定，勉励大家奋发进取、再创佳绩。".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#         chapter_data['columns'] = ['t1', 't2', 't3', 't4', 't5', 't6']
#         chapter_data['data'] = [
#             ['测试', 'c1', 'c2', 0, 0, 0],
#             ['测试', 'c1', 'c2', 0, 0, 0],
#             ['测试', 'c1', 'c3', 0, 0, 0],
#             ['测试1', 'c1', 'c2', 0, 0, 0],
#             ['测试1', 'c3', 'c2', 0, 0, 0],
#         ]
#         table = Table(config=self.table_body_style)
#         table.generate(doc_obj=self.doc_obj, columns=chapter_data.get('columns'), data=chapter_data.get('data'),
#                        table_title=chapter_data.get('table_title'), table_title_style=self.table_title_style,
#                        built_table_color_style='Medium Shading 1 Accent 1', max_merge_col_index=2)
#         self.page_break()
#
#     @handle_paragraph
#     def chapter_02(self):
#         """章节02 标题"""
#         p_title = Title(config=self.title_level_1_style)
#         text = "二、情况1"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_02_paragraph_01(self):
#         """章节02 段落01"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "中共中央政治局常委李克强、汪洋、赵乐际、韩正参加会见。中共中央政治局常委王沪宁参加会见并在总结会议上讲话。{a}".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_03(self):
#         """章节03 标题"""
#         p_title = Title(config=self.title_level_1_style)
#         text = "三、情况2"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_03_paragraph_01(self):
#         """章节03 段落1"""
#         chapter_data = self.get_paragraph_data()
#         content = Content(config=self.content_style)
#         text = "13日上午，人民大会堂北大厅灯光璀璨、气氛热烈。11时许，习近平等来到这里，全场响起热烈掌声" \
#                "。习近平等走到代表们中间，同大家亲切交流并合影留念。{a}".format(**chapter_data)
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#
# if __name__ == '__main__':
#     # 从文件创建文档对象
#     file = '/Users/sanbom/Desktop/需求调查样例V0.7.1.docx'
#     # # template =None
#     # template = '/Users/sanbom/Storage/MyCode/kits/smart_report/template/demo.docx'
#     template = '/Users/sanbom/Storage/MyCode/kits/smart_report/template/需求调查.docx'
#     # # template = '/Users/sanbom/Storage/MyCode/kits/smart_report/template/table_styles.docx'
#     # template = '/Users/sanbom/Storage/MyCode/kits/smart_report/template/xxx.docx'
#     data = SmartReportData().data
#     print(data)
#     report = SmartReport(filename=file, data=data, template=template)
#     report.generate()
#
#
# from kits.smart_report import SmartReportBase, Content, Paragraph, handle_paragraph, Title
#
#
# class SmartReport(SmartReportBase):
#     """智能报告"""
#
#     def __init__(self, filename: str, data: dict, *args, template: str = None, **kwargs):
#         super(SmartReport, self).__init__(filename, data, *args, template=template, **kwargs)
#
#     def handle_paper_heading(self):
#         """文章标题"""
#         title = Content(config=self.title_level_0_style)
#         title.generate(doc_obj=self.doc_obj, text='自动化测试报告')
#
#     def handle_paper_subheading(self):
#         """文章副标题"""
#         paragraph = Paragraph(config=self.paper_subheading_style)
#         paragraph.generate(doc_obj=self.doc_obj, text='时间范围: 2021年1月7日 --- 2021年2月7日')
#
#     def handle_abstract(self):
#         """文章摘要"""
#         content = Content(config=self.abstract)
#         text = "[本分析报告所指的信访数据以国家信访系统上海分系统登记的来信、来访、网信为依据，涵盖建设交通系统" \
#                "市级党政机关、委属事业单位、代管的中央在沪单位。市住建委、市交通委、市水务局、市绿化市容局、市房管" \
#                "局、市城管执法局、市公积金中心为上海市信访办管理系统中独立承办的责任单位。市建设交通党委代管的中央在" \
#                "沪单位由市住建委代为转交，由具体单位承办。]"
#         content.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01(self):
#         """章节1"""
#         p_title = Title(config=self.title_level_1_style)
#         text = "一、总体情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)
#
#     @handle_paragraph
#     def chapter_01_01(self):
#         """章节1.1 标题"""
#         p_title = Title(config=self.title_level_2_style)
#         text = "1.1 情况"
#         p_title.generate(doc_obj=self.doc_obj, text=text)

from kits.smart_report import SmartReportBase, Content
from kits.smart_report.config import ContentStyleBase

report = SmartReportBase(filename='test.docx', data=dict())
doc_obj = report.doc_obj
content = Content(config=ContentStyleBase())
content.generate(doc_obj, text="自动化报告,从空白文件创建!")
report.generate()
