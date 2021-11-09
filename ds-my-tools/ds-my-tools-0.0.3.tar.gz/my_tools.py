import json


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
