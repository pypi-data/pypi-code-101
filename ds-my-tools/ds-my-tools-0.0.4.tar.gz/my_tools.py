import json
import sys
from win32com.client import Dispatch
import fitz # pip install pymupdf
import os
import requests
import base64


# 读取json
def read_json(path):
    """
    读取json文件
    :param path:json文件路径
    :return: [a,b,c]   a:成功失败状态,b:返回的数据,c:错误信息
    """
    try:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
            return [True, data, 'utf-8']
        except UnicodeDecodeError:
            with open(path, 'r', encoding='gbk') as f:
                data = json.loads(f.read())
            return [True, data, 'gbk']
    except Exception as e:
        return [False, str(e), 'error']


# 写入数据
def write_dict_to_json(dict_data, path, mode="w", encoding="utf-8"):
    """
    写入dict数据到文件中
    :param encoding: 编码
    :param mode: 模式
    :param dict_data: 需要写入的数据
    :param path: 文件路径
    :return: [a,b,c]   a:成功失败状态,b:编码或错误信息,c:模式
    """
    try:
        with open(path, mode, encoding=encoding) as f:
            f.write(json.dumps(dict_data, ensure_ascii=False, indent=4))
        return [True, encoding, mode]
    except Exception as e:
        return [False, str(e), mode]


# 过滤所有的标点符号
def filter_punctuation(string):
    """
    过滤所有的标点符号
    :param string: 字符串
    :return: 返回过滤后的字符串
    """
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~！（）-【】{}；：‘“、，《》/？@#￥%……&*——~·'''
    for i in punctuation:
        string = string.replace(i, '')
    return string


# 给定两个列表判断两个列表的差部分
def diff_list(list1, list2):
    """
    给定两个列表判断第一个列表不在第二个列表中的部分
    :param list1: 列表1
    :param list2: 列表2
    :return: 差部分
    """
    return list(set(list1).difference(set(list2)))


# 给定两个列表判断两个列表的交集部分
def intersection_list(list1, list2):
    """
    给定两个列表判断两个列表的相同部分
    :param list1: 列表1
    :param list2: 列表2
    :return: 交集部分
    """
    return list(set(list1).intersection(set(list2)))


# word_to_pdf
def word_to_pdf(word_file, pdf_file):
    """
    将word文件转换成pdf文件
    :param pdf_file:
    :param word_file: word文件
    :return:
    """
    # 获取word格式处理对象
    word = Dispatch('Word.Application')
    # 以Doc对象打开文件
    doc_ = word.Documents.Open(word_file)
    # 另存为pdf文件
    doc_.SaveAs(pdf_file, FileFormat=17)
    # 关闭doc对象
    doc_.Close()
    # 退出word对象
    word.Quit()


# pdf_to_png
def pdf_to_png(_pdf, _save_dir):
    _doc = fitz.open(_pdf)
    for pg in range(_doc.pageCount):
        page = _doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # save_dir = pdf.replace('.pdf', '')
        if not os.path.exists(_save_dir):
            os.mkdir(_save_dir)
        pm.writePNG(os.path.join(_save_dir, '%s.png' % pg))
