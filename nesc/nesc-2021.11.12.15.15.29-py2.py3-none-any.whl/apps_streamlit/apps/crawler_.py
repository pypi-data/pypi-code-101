#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : crawler
# @Time         : 2021/11/12 下午3:05
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


from meutils.request_utils.crawler import Crawler


def main():
    url = st.text_input('url', 'https://top.baidu.com/board?tab=realtime')
    xpath = st.text_input('xpath', '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[*]/div[2]/a/div[1]//text()')

    c = Crawler(url)
    st.json(c.xpath(xpath))
