#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 21:53
# @Author : 心蓝
"""
日志处理器
"""
import logging


def get_logger(name='easytest', file=None, debug=False):
    if debug:
        # 如果开启了调试模式
        fmt = '%(levelname)s %(threadName)s %(asctime)s [%(filename)s-->line:%(lineno)d]:%(message)s'
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        fmt = '%(levelname)s %(asctime)s :%(message)s'
        file_level = logging.WARNING
        console_level = logging.INFO

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置等级
    # 3. 创建格式化器
    formatter = logging.Formatter(fmt=fmt)
    # 2. 创建日志处理器
    if file:
        file_handler = logging.FileHandler(filename=file, encoding='utf-8')
        file_handler.setLevel(file_level)  # 设置写入文件的日志等级
        # 4. 把格式化器添加到日志处理器上
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)  # 设置控制台输出日志的等级
    console_handler.setFormatter(formatter)
    # 5. 把日志处理器添加到日志器

    logger.addHandler(console_handler)
    return logger


# logger = get_logger(debug=True)

