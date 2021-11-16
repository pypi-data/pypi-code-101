# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Sqrt5



def getName2IdDict(label_file):
    """
    获取码表字典

    :param label_file: 标签文件，一行一个标签
    :returns: 返回名字为key值，类别编号为value值的字典
    """
    name2id = {}
    with open(label_file, 'r', encoding='utf-8') as f:
        for loop, line in enumerate(f):
            elems = line.strip('\n')
            name2id[elems] = loop
    return name2id


def getId2NameDict(label_file):
    """
    获取码表字典

    :param label_file: 标签文件，一行一个标签
    :returns: 返回类别编号为key值，名字为value值的字典
    """
    id2name = {}
    with open(label_file, 'r', encoding='utf-8') as f:
        for loop, line in enumerate(f):
            elems = line.strip('\n')
            id2name[loop] = elems
    return id2name


def swapDict(code_dict):
    """
    交换字典

    :param code_dict: 待交换字典
    :returns: 返原value值为key值，原key值为value值的字典
    """
    output_dict = {}
    for k, v in code_dict.items():
        if v not in output_dict:
            output_dict[v] = k
        else:
            return
    return output_dict
