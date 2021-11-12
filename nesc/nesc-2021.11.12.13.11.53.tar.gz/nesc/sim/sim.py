#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : sim_app
# @Time         : 2021/9/1 下午2:45
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *

from shutil import copyfile

from bertzoo.simbert2vec import Simbert2vec
from gensim.models import KeyedVectors

tqdm.pandas()

CACHE = 'cache.pkl'


def get_vector_cache(backup=False):
    p = Path(CACHE)  # p.read_text() windows有编码问题

    w2v = {}
    if p.is_file():
        if backup:
            copyfile(p, f"{p}.bak.{time.time()}")  # 备份cache

        w2v = joblib.load(CACHE)

    return w2v


def get_word_set(path):
    if Path(path).is_file():
        return set(pd.read_csv(path, names=['w']).w.astype(str).str.strip().str.replace('\t', '').str.replace(' ', ''))
    return {path}


def bert_vector(s1, s2, batch_size=3, model_home='chinese_roformer-sim-char-ft_L-6_H-384_A-6'):
    w2v = get_vector_cache()
    s = (s1 | s2) - set(w2v)

    if s:
        s2v = Simbert2vec(model_home)

        for ws in tqdm(list(s) | xgroup(batch_size), '向量化'):
            vs = s2v.encoder(ws, output_dim=None)
            w2v.update(zip(ws, vs))  # 向量全集

        joblib.dump(w2v, 'cache.pkl')  # 更新cache

    return w2v


def get_vector_from_w2v(s, w2v):
    s = list(s)
    v = operator.itemgetter(*s)(w2v)

    if len(s) > 1:
        return np.row_stack(v)
    else:
        return v.reshape(1, -1)


def main(target, file, topn=10, batch_size=512, model_home='chinese_roformer-sim-char-ft_L-6_H-384_A-6'):
    s1 = get_word_set(target)
    s2 = get_word_set(file)
    w2v = bert_vector(s1, s2, batch_size, model_home)

    v1 = get_vector_from_w2v(s1, w2v)
    v2 = get_vector_from_w2v(s2, w2v)

    wv = KeyedVectors(384)
    wv.add_vectors(list(s2), v2, replace=True)
    wv.init_sims(True)

    df_rsts = []
    for s, v in tqdm(zip(s1, v1), desc="向量匹配"):
        r2s = wv.similar_by_vector(v, topn=topn)
        df_rst = pd.DataFrame(r2s, columns=['recall', 'score'])
        df_rst.insert(0, 'target', s)
        df_rsts.append(df_rst)

    df = pd.concat(df_rsts, ignore_index=True)

    opath = Path(file).parent / 'recall.tsv'
    df.to_csv(opath, '\t', index=False, header=False)
    logger.info(f"输出路径：{opath}")

    if len(s1) == 1:
        df.columns = ['target', 'recall', 'score']
        tb = Besttable.draw_df(df)
        time.sleep(0.3)
        print(tb)

    return df
