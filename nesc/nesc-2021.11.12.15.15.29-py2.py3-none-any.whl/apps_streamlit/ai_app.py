#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : ai_app
# @Time         : 2021/11/12 下午3:04
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :
import streamlit as st

from meutils.pipe import *

from nesc.apps_streamlit.apps import crawler_

st.sidebar.markdown('**🔥应用集成🔥**')

app_options = (
    '字段翻译', '数据分级预测', '字段模糊匹配', '爬虫工具', '企微机器人', 'OCR', 'Docs'
)
app_name = st.sidebar.selectbox('AI', app_options)
Path(app_name).mkdir(exist_ok=True)

if app_name == 'Docs':
    st.markdown('# 文档')

elif app_name == '字段模糊匹配':
    st.markdown(f'##### {app_name}')

elif app_name == '爬虫工具':
    crawler_.main()
