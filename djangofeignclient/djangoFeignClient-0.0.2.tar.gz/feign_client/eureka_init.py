#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------
    Author:     JiChao_Song
    Date  :     2021/11/10 19:32
    Desc  :
--------------------------------------
"""
from py_eureka_client import eureka_client


def eureka_init(eureka_server:str, app_name:str, port:int):
    eureka_client.init(eureka_server=eureka_server,
                       app_name=app_name,
                       # 当前组件的主机名，可选参数，如果不填写会自动计算一个，如果服务和 eureka 服务器部署在同一台机器，请必须填写，否则会计算出 127.0.0.1
                       instance_port = port,
                       # 调用其他服务时的高可用策略，可选，默认为随机
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)