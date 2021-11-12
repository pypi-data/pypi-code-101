#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : flask_demo
# @Time         : 2021/10/27 下午6:38
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


import os
import time
from flask import Flask

app = Flask(__name__)


# os.system(f"echo {time.ctime()} >> ./log/test.log")


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run('0.0.0.0', 8501)
