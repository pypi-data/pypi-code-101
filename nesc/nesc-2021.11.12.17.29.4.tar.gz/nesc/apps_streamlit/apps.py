#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : apps
# @Time         : 2021/11/12 下午3:18
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


import streamlit as st

from meutils.pipe import *
from meutils.request_utils.crawler import Crawler
from meutils.decorators.decorator import decorator
from meutils.notice.wecom import Wecom

from nesc.sim.simv2 import *


##################################################################
@st.experimental_singleton()
def lac_obj():
    Wecom().send_markdown('加载lac')

    from LAC import LAC

    lac = LAC(mode='lac')
    return lac


lac = lac_obj()


@st.experimental_singleton()
def s2v_obj(model_home):
    return Simbert2vec(model_home)


def download_excel(df, app_name, file_name='词根翻译结果.xlsx'):
    filename = f"{app_name}/{time.time()}.xlsx"
    df.to_excel(filename)

    with open(filename, 'rb') as f:
        data = f.read()

        st.download_button(
            label="下载🥺",
            data=data,
            file_name=file_name,
            mime='application/octet-stream',
        )

    st.dataframe(df.head(10), 4000, 3000)


##################################################################


@decorator
def app_info(f, desc='', *args, **kwargs):
    app_name = f.__name__
    Path(app_name).mkdir(exist_ok=True)

    st.markdown(f'##### {app_name}')
    st.markdown(f'**{desc}**')

    return f(*args, **kwargs)


@app_info()
def 爬虫工具():
    url = st.text_input('url', 'https://top.baidu.com/board?tab=realtime')
    xpath = st.text_input('xpath', '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[*]/div[2]/a/div[1]//text()')

    c = Crawler(url)
    st.json(c.xpath(xpath))


@app_info()
def 字段翻译():
    io = st.sidebar.file_uploader('上传词根字典（默认旧字典可上传更新）')
    targets = set(st.text_area('待翻译字段', '公募基金', height=300).strip().split('\n'))

    if io is None:
        io = '/root/model/bert/字段词根字典（征求意见稿）.xlsx'

    df = pd.read_excel(io)[['中文全称', '英文名称', '英文简称']]
    df['中文全称'] = df['中文全称'].str.split('/')
    df = df.explode('中文全称')

    # # 自定义分割词
    # lac.add_word(' '.join(df['中文全称'].to_list())) # 有bug，没区分出

    for w in set(df['中文全称'].append(pd.read_csv('/root/model/bert/words.txt', names=['w'])['w'].astype(str))):
        lac.add_word(w)

    is_run = st.button('开始🔥')

    if is_run:
        rst = []
        for t in targets:
            t_ = t
            t = lac.run(t)[0]

            英文名称 = []
            英文简称 = []
            for w in t:
                if w == t_:
                    continue
                df_r = df[df['中文全称'] == w]
                if len(df_r):
                    _ = df_r[:1].values[0]  # 日期', 'DATE', 'DT', 2

                    英文名称.append(_[1])
                    英文简称.append(_[2])
                else:
                    英文名称.append(w)
                    英文简称.append(w)

            rst.append([t_, t, ' '.join(英文名称), '_'.join(英文简称)])

        df_rst = pd.DataFrame(rst, columns=['中文字段', '分词', '英文名称', '英文简称'])

        download_excel(df_rst)


@app_info()
def 字段模糊匹配():
    topn = st.sidebar.slider('召回TopN', min_value=1, max_value=20, value=1)

    s2 = set(st.sidebar.text_area('目标字段', '治理数据', height=300).strip().split('\n'))
    s1 = set(st.text_area('待匹配字段', '数据治理', height=300).strip().split('\n'))

    is_run = st.button('开始🔥')
    if is_run:

        model_home = 'chinese_roformer-sim-char-ft_L-6_H-384_A-6'
        batch_size = 512

        def bert_vector(s1, s2, batch_size=batch_size, model_home='chinese_roformer-sim-char-ft_L-6_H-384_A-6'):
            w2v = get_vector_cache()
            s = (s1 | s2) - set(w2v)

            if s:
                s2v = s2v_obj(model_home)

                my_bar = st.progress(0)
                _iter = list(s) | xgroup(batch_size)
                with st.spinner("向量化 ..."):

                    for idx, ws in tqdm(enumerate(_iter, 1), '向量化'):
                        my_bar.progress(idx / len(_iter))
                        vs = s2v.encoder(ws, output_dim=None)
                        w2v.update(zip(ws, vs))  # 向量全集

                joblib.dump(w2v, 'cache.pkl')  # 更新cache

            return w2v

        w2v = bert_vector(s1, s2, batch_size, model_home)

        i2w_1, data1 = get_i2w_vecs(s1, w2v)
        i2w_2, data2 = get_i2w_vecs(s2, w2v)

        ann = ANN()
        ann.train(data2, metric=0)

        diss, idxs = ann.search(data1, topn)

        df_rst = get_rst(i2w_1, i2w_2, diss, idxs)
        df_rst.columns = ['target', 'recall', 'score']
        download_excel(df_rst)


@app_info()
def 数据分级预测():
    pass


@app_info()
def 数据分类预测():
    pass
