#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : simapp
# @Time         : 2021/10/12 下午8:29
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


from st_utils import *
import streamlit as st

st.markdown(
    """
    # 字段名检索
    实现方式：simbert + ann
    """
)
st.sidebar.select_slider('select_slider', ['nlp','ocr', 'tab'])


text = st.sidebar.text_input('字段', value="东北证券")  # st.text_area('xx', value="小米\n苹果")
topn = st.sidebar.slider('召回数', value=20, min_value=1, max_value=100)
