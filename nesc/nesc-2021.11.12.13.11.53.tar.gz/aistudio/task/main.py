#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : demo.py
# @Time         : 2021/11/11 下午3:20
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *


path = 'hdfs://easyops-cluster/user/smartdata/hive_db/tmp.db/data_biz_date/biz=GuessYouLikeIt/date=20211011'

df = pd.read_csv(f'{path}/000000_0', header=None, error_bad_lines=False)


print(df.head())


# import pyarrow as pa
#
# hfs = pa.hdfs.HadoopFileSystem()
# path = hfs.ls("hdfs://user/smartdata/hive_db/")
# print(path)
