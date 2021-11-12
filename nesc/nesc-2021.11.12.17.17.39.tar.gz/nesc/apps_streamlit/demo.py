#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : demo
# @Time         : 2021/10/22 下午2:13
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


import streamlit  as st
from meutils.pipe import *


@st.experimental_memo(ttl=10)
def func():
    time.sleep(3)
    print(time.time())


#y
# @st.experimental_singleton()
# def func():
#     time.sleep(5)


func()


st.title('# DONE')



