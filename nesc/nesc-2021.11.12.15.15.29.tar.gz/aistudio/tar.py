#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : tar.py
# @Time         : 2021/10/29 上午8:30
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *

DIR = Path(__file__).absolute().parent

dirs = DIR.glob("*") | xfilter(Path.is_dir) | xlist

# import tarfile
for d in dirs:
    os.system(f"tar -cvf {d.name}.tar {d.name}")
