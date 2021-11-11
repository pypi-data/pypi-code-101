# -*- coding: utf-8 -*-
"""
一些常见的工具函数
"""
import hashlib
import json
import random
import uuid


def md5(s: str):
    """
    计算字符串的md5
    """
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def generate_uuid():
    """
    随机生成32位的uuid 去掉 '-'
    :return:
    """
    return str(uuid.uuid4()).replace("-", "")


def rand_str(num=10):
    """
    随机生成一个指定长度的字符串
    :param num: 字符串长度
    :return: 字符串
    """
    return "".join(
        random.sample(
            "ABCDEFGHJKLMNPQRSTUVWXY"
            "0123456789"
            "ABCDEFGHJKLMNPQRSTUVWXY"
            "0123456789"
            "abcdefghjkmnpqrstuvwxy"
            "0123456789"
            "abcdefghjkmnpqrstuvwxy"
            "0123456789",
            num))  # noqa


def safe_id(value):
    """
    安全的将字符串转成int类型
    :param value: 字符串
    :return: int数字
    """
    try:
        return int(value)
    except:  # noqa
        return None


def dumps(d: dict):
    """
    字典转json字符串
    :param d: 字典
    :return: 字符串
    """
    return json.dumps(d, ensure_ascii=False)


def loads(source_str: str):
    """json字符串转字典 捕获异常
    """
    try:
        return json.loads(source_str)
    except:  # noqa
        return None


