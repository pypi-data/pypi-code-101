#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : simple_web
# @Time         : 2021/10/26 下午7:13
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  : tar -cvf [目标文件名].tar [原文件名/目录名]

from meutils.pipe import *
from meutils.db import DB
from appzoo import App

# redis
ips = "10.211.96.32:7000,10.211.96.32:7001,10.211.96.33:7000,10.211.96.33:7001,10.211.96.34:7000,10.211.96.34:7001".split(
    ',')
password = "PzGgrUK#eE*U305O"
rc = DB().redis(ips, password)


class Params(BaseConfig):
    userId: str = 13009109939
    mobileNo: str = 13009109939
    fundAccount: str = None
    deviceID: str = None
    scenesId: str = None
    source: str = None
    appVersion: str = None  # 客户端版本号
    riskLevel: str = None  # 客户风险等级
    topN: int = 3


class Item(BaseConfig):
    itemId: str = None
    traceId: str = None
    code1: str = None
    code2: str = None


def func(**kwargs):
    p = Params.parse_obj(kwargs.get('request', {}))

    items = ['03:000001', '39:000003', '39:000004']  # 'register_corp_code:product_code'  公司代码:商品代码
    if p.mobileNo:
        _ = rc.get(f'rec:gyl:{p.mobileNo}')
        if _:
            items = _.split(',')

    items = [Item(code1=item.split(':')[0], code2=item.split(':')[1]) for item in items]

    return np.random.choice(items, p.topN).tolist()


app = App()
app.add_route('/rec', func, method='POST', code=200, info='ok', result_key='data')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8501)
