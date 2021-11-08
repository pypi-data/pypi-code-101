"""
一些支持方法，比如加密等
❗️ 注意：基础脚本【config， support】，不能import更高级的脚本如logger， Sql
"""
import hashlib
from socket import socket, AF_INET, SOCK_STREAM
from zipfile import ZipFile
from os import path, listdir
import importlib
import types
import json


class EncryptError(Exception):
    pass


def sign(sign_dict, private_key=None, encrypt_way='MD5'):
    """传入待签名的字典，返回签名后字符串
    1.字典排序
    2.拼接，用&连接，最后拼接上私钥
    3.MD5加密"""
    dict_keys = sorted(sign_dict.keys())

    string = ''
    for key in dict_keys:
        if sign_dict[key] is None:
            pass
        else:
            string += '{0}={1}&'.format(key, sign_dict[key])
    string = string[0:len(string) - 1].replace(' ', '')

    return encrypt(string, salt=private_key, encrypt_way=encrypt_way)


def encrypt(string, salt='', encrypt_way='MD5'):
    u"""根据输入的string与加密盐，按照encrypt方式进行加密，并返回加密后的字符串"""
    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way.upper() == 'SHA1':
        hash_string = hashlib.sha1()
    else:
        raise EncryptError('请输入正确的加密方式，目前仅支持 MD5 或 SHA1')

    hash_string.update(string.encode())
    return hash_string.hexdigest()


def unzip(abs_file, ext_path):
    zip_file = ZipFile(abs_file)
    for name in zip_file.namelist():
        zip_file.extract(name, ext_path)
    zip_file.close()


def get_suffix_list(file_path, suffix=".pkl"):
    """
    递归遍历指定目录，获取指定后缀的文件
    :param file_path: 目录或文件（如果是文件，则返回[file_path]）
    :param suffix: 后缀名
    :return: suffix_list = [ file1.suffix, file2.suffix, ]
    """
    suffix_list = []

    if path.isdir(file_path):
        for fi in listdir(file_path):
            fi_abspath = path.join(file_path, fi)
            if path.isfile(fi_abspath) and fi_abspath.endswith(suffix):
                suffix_list.append(fi_abspath)
            elif path.isdir(fi_abspath):
                suffix_list.extend(get_suffix_list(fi_abspath))

    elif path.isfile(file_path) and file_path.endswith(suffix):
        suffix_list = [file_path]

    return suffix_list


def socket_open(ip, port):
    # 检查IP和端口是否可连接
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)

        print("服务器连接成功")
        return True
    except:
        print("服务器连接失败")
        return False


def get_access_dir(dir_info, default_dir):
    # 从命令行读取测试数据路径，并检查路径是否存在
    while True:
        access_data_dir = str(input("请输入{}路径(默认当前目录下{}，输入0跳过)：".format(dir_info, default_dir)))
        if access_data_dir == "0":
            break

        if not access_data_dir:
            access_data_dir = default_dir
        else:
            access_data_dir = path.abspath(access_data_dir)

        if not path.exists(access_data_dir):
            print("路径不存在，重新输入")
        else:
            break

    return access_data_dir


def to_list(data):
    # ensure the value list is this format: [value]
    if not data:
        value_list = [None]
    elif isinstance(data, list):
        value_list = data
    else:
        value_list = [data]
    return value_list


def eval_param(data: str):
    """
    data = "${get_hash('79x79_999k')}"  -->  return get_hash('79x79_999k')
    default module is test_common.argv_read, can auto import function get_hash from file test_common/common_argv.py
    if data = "${utils.support.get_hash()}", will import get_hash from file utils/support.py
    """
    if isinstance(data, str) and data.startswith("${") and data.endswith("}"):
        data = data.lstrip("${").rstrip("}")

        func_dir = data.split("(")[0]
        func_name = func_dir.split(".")[-1]
        param = data.strip(func_dir).strip("(").strip(")")
        param_list = [i.strip() for i in param.split(",")]
        # print(f"analysis param:\t{param}")

        if func_dir == func_name:
            module = "common_argv"
        else:
            module = func_dir.replace(f".{func_name}", "")
        try:
            module = importlib.import_module(module)
            module = importlib.reload(module)
    
            for name, item in vars(module).items():
                if isinstance(item, types.FunctionType) and name == func_name:
                    data = item(*param_list) if param else item()
                    break
        except ModuleNotFoundError as e:
            raise e
    return data


def rec_merge(d1, d2):
    """
    递归合并字典（最小单元key的value以d2为准）
    :param d1: {"a": {"c": 2, "d": 1}, "b": 2}
    :param d2: {"a": {"c": 1, "f": {"zzz": 2}}, "c": 3, }
    :return: {'a': {'c': 1, 'd': 1, 'f': {'zzz': 2}}, 'b': 2, 'c': 3}
    """
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1 == d2:
            return d1
        else:
            for key, value in d2.items():
                if key not in d1:
                    d1[key] = value
                else:
                    if isinstance(d1[key], dict) and isinstance(value, dict):
                        rec_merge(d1[key], value)
                    else:
                        d1[key] = value
            return d1
    else:
        return None


if __name__ == '__main__':
    print(encrypt('Crowd@ad123', '', 'MD5'))
    zjk = {'ZJK': 'YES', 'OK': '365  DAYS', 'WHO': 'EVERYONE', 'WHERE': 'SEA', 'DAYS': 'SOME', 'PASS': None}
    print(sign(zjk, private_key='张'))
    print(eval_param("${tests.SPDL.cms.image_svc.get_hash(79x79_999k)}"))
    print(get_suffix_list("/", ".txt"))
    de = {'DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_invalid': {'case_status': 'failed', 'steps': [{'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}, {'name': 'List Demo InValid', 'case_status': 'broken'}]}, 'DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid': {'case_status': 'failed', 'steps': [{'name': 'List Demo Valid', 'case_status': 'broken'}, {'name': 'List Demo Valid', 'case_status': 'broken'}, {'name': 'List Demo Valid', 'case_status': 'broken'}, {'name': 'List Demo Valid', 'case_status': 'broken'}]}}

    sr = {'DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_invalid': {'case_id': 1}}
    rec_merge(de, sr)
    print(de)
