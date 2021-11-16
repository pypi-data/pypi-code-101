# -*- coding: utf-8 -*-
# @Time : 2021/11/16 4:49 下午
# @Author : Kane.Yan
# @File : test_case.py
import pytest


@pytest.mark.parametrize("user",["张三","李四"],ids=['张','李'])
def test_hook(user):
    print(user)