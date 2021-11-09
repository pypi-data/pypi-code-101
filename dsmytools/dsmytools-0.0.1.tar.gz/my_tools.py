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
