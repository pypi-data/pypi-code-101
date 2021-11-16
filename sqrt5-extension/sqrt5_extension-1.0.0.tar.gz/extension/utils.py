# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Sqrt5


import base64
import codecs
import copy
import cv2
import datetime
import hashlib
import json
import math
import numpy as np
import os
import pytz
import random
import re
import shutil
import sys
import time
import urllib.request
from PIL import Image
from io import BytesIO



class Timer:
    def __init__(self, cnt=1000):
        self.start_time = 0.0
        self.time_list = []
        self.cnt = cnt


    def tic(self):
        self.start_time = time.time()


    def toc(self, mode='time'):
        assert mode in ['time', 'avg time', 'fps', 'avg fps']
        self.time_list.append(time.time() - self.start_time)
        while len(self.time_list) > self.cnt:
            self.time_list.pop(0)
        if mode == 'time':
            return self.time_list[-1]
        elif mode == 'avg time':
            return sum(self.time_list) / len(self.time_list)
        elif mode == 'fps':
            return 1.0 / self.time_list[-1]
        elif mode == 'avg fps':
            return len(self.time_list) / sum(self.time_list)


    def clear(self):
        self.start_time = 0.0
        self.time_list.clear()
        self.cnt = 1000


class cache:
    def __init__(self, max_size=0):
        self.cache_list = []
        self.max_size = max_size


    def __len__(self):
        return len(self.cache_list)


    def __iter__(self):
        self.idx = 0
        return self


    def __next__(self):
        if self.idx >= len(self.cache_list):
            raise StopIteration
        cache = self.cache_list[self.idx]
        self.idx += 1
        return cache


    def pop(self, num=1):
        for _ in range(num):
            self.cache_list.pop(0)


    def add(self, elem):
        self.cache_list.append(elem)
        if self.max_size > 0 and len(self.cache_list) > self.max_size:
            self.cache_list.pop(0)


    def filter(self, func=lambda x: True):
        self.cache_list = list(filter(func, self.cache_list))


    def sort(self, key=lambda x: x, reverse=False):
        self.cache_list.sort(key=key, reverse=reverse)


    def copy(self):
        cache_copy = cache(max_size=self.max_size)
        # cache_copy.cache_list = self.cache_list
        cache_copy.cache_list = copy.copy(self.cache_list)
        return cache_copy


    def deepcopy(self):
        cache_copy = cache(max_size=self.max_size)
        cache_copy.cache_list = copy.deepcopy(self.cache_list)
        return cache_copy


    def clear(self):
        self.cache_list.clear()


    def __repr__(self):
        max_size = 'inf' if self.max_size == 0 else '%3d' % self.max_size
        return f'max size:{max_size}, cache list(size:{len(self.cache_list)}):{self.cache_list}'


def prob(p):
    """
    以概率p返回True

    :param p: 概率
    :returns: True or False
    """
    # [0, 1), so use <, not <=, p: 0 -> never, 1 -> always
    return True if random.uniform(0, 1) < p else False


def intRound(n):
    """
    返回n四舍五入后的整数

    :param n: 数
    :returns: int型整数
    """
    if type(n) == tuple:
        return tuple(map(lambda x:int(round(x)), n))
    elif type(n) == list:
        return list(map(lambda x:int(round(x)), n))
    return int(round(n))


def floatRound(n, precision=0.125):
    """
    返回1/part为精度的数字

    :param n: 数
    :param precision: 精度
    :returns: 以precision为精度的小数
    """
    if type(n) == tuple:
        return tuple(map(lambda x:float(intRound(float(x) / precision)) * float(precision), n))
    elif type(n) == list:
        return list(map(lambda x:float(intRound(float(x) / precision)) * float(precision), n))
    return float(intRound(float(n) / precision)) * float(precision)


def progressbar(cur, total, begin_time = 0, cur_time = 0, info = ''):
    """
    进度条

    :param cur: 当前索引
    :param total: 总数量
    :param begin_time: 开始时间
    :param cur_time: 当前时间
    :param info: 其他信息
    """
    text = '\r'
    if begin_time == 0 and cur_time == 0 or cur == 0:
        text += '[%-30s]\t%6.2f%%' % (
            '=' * int(math.floor(cur * 30 / total)),
            float(cur * 100) / total
        )
    else:
        text += '[%-30s]  %6.2f%%   COST: %.2fs   ETA: %.2fs   %s     ' % (
            '=' * int(math.floor(cur * 30 / total)),
            float(cur * 100) / total,
            (cur_time - begin_time),
            (cur_time - begin_time) * (total - cur) / cur,
            info
        )
    if cur == total:
        text += '\n'
    sys.stdout.write(text)
    sys.stdout.flush()
    return


def exchangePathSeparator(path):
    """
    按Linux/Unix/Windows修改目录路径的/和\\

    :param path: 目录路径
    :returns: 修改目录分隔符后的路径
    """
    parts = []
    d_pre = path
    while True:
        d, f = os.path.split(d_pre)
        parts.append(f)
        if d == d_pre:
            break
        d_pre = d
    parts.append(d_pre)
    path = os.path.join(*parts[::-1])
    return path


def listFileFromDirectory(
    directory,
    extension=[],
    abs_path=False,
    case_sensitive=False,
    only_file=False,
    only_dir=False,
    is_iter=False,
    is_sort=False
):
    """
    遍历目录中的所有文件

    :param directory: 目录路径
    :param extension: 扩展名
    :param case_sensitive: 是否区分大小写
    :param only_file: 是否只保留文件
    :param is_iter: 是否遍历子文件夹
    :returns: 包含路径的文件列表
    """
    assert os.path.exists(directory) and os.path.isdir(directory)
    assert not (only_file and only_dir)

    def listDir(directory, file_list, is_iter):
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if is_iter and os.path.isdir(file_path):
                listDir(file_path, file_list, is_iter)
            else:
                file_list.append(file_path)
                sys.stdout.write('\r已扫描%d个文件' % len(file_list))
                sys.stdout.flush()

    def endsInList(file_name, ext_list):
        if len(ext_list) == 0:
            return True
        for ext in ext_list:
            if file_name.endswith(ext):
                return True
        return False

    file_list_tmp = []
    listDir(directory, file_list_tmp, is_iter)
    sys.stdout.write('\n')

    file_list = []
    extension_tmp = [extension] if type(extension) == str else copy.deepcopy(extension)
    if not case_sensitive:
        extension_tmp = [ext.upper() for ext in extension_tmp]
    for file_name in file_list_tmp:
        file_name_tmp = file_name
        if not case_sensitive:
            file_name_tmp = file_name.upper()
        if endsInList(file_name_tmp, extension_tmp):
            if (only_file and os.path.isfile(file_name)) or \
                (only_dir and os.path.isdir(file_name)) or \
                    (not (only_file or only_dir)):
                if abs_path:
                    file_name = os.path.abspath(file_name)
                if os.path.isdir(file_name):
                    file_name = os.path.join(file_name, '')
                file_list.append(exchangePathSeparator(file_name))
    if is_sort:
        file_list.sort()
    return file_list


def splitPath(path, keep_sub=0, check_exists=False):
    """
    完全拆分路径

    :param path: 路径
    :param keep_sub: 保留子目录级数
    :param check_exists: 依据不带"/"或"\\"的path的实际属性判断是否是目录
    :returns: 目录名称 文件名称 文件扩展名 子目录
    """
    is_dir = False
    if path[-1] in ['/', '\\']:
        is_dir = True
    path = os.path.abspath(path)
    if check_exists:
        if os.path.exists(path):
            if os.path.isdir(path):
                is_dir = True
    if is_dir:
        path = os.path.join(path, '')
    directory_path, file_name_with_ext = os.path.split(path)
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    parent_directory_name_list = []
    directory_path_remain = directory_path
    for i in range(keep_sub):
        directory_path_remain, parent_directory_name = os.path.split(directory_path_remain)
        if parent_directory_name != '':
            parent_directory_name_list.append(parent_directory_name)
        else:
            break
    parent_directory_name = ''
    if len(parent_directory_name_list) > 0:
        parent_directory_name_list = parent_directory_name_list[::-1]
        parent_directory_name = parent_directory_name_list[0]
        for parent_directory_name_ in parent_directory_name_list[1:]:
            parent_directory_name = os.path.join(parent_directory_name, parent_directory_name_)
    return directory_path, file_name, file_ext, parent_directory_name


def replaceExt(file_path, ext, suffix=''):
    if not ext.startswith('.'):
        ext = '.' + ext
    file_path = os.path.splitext(file_path)[0] + suffix + ext
    return file_path


def checkDirectory(directory):
    """
    查看目录是否存在，不存在则创建

    :param directory: 目录路径
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return


def clearDirectory(directory):
    """
    清空目录，原理是删除整个目录再创建

    :param directory: 目录路径
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    return


def checkFileName(file_name):
    """
    校验文件名，如果存在则加入9位数字编号的后缀

    :param file_name: 文件名
    :returns: 新文件名
    """
    directory, file_name_without_path = os.path.split(file_name)
    file_name_without_path_ext, ext = os.path.splitext(file_name_without_path)
    checkDirectory(directory)
    cnt = 0
    while os.path.exists(file_name):
        file_name = os.path.join(
            directory, '%s_%09d%s' % (
                file_name_without_path_ext,
                cnt,
                ext
            )
        )
        cnt += 1
    return file_name


def getFileNameByTime(extension=''):
    """
    根据时间随机产生一个文件名

    :param extension: 扩展名
    :returns: 新文件名
    """
    return '%d%010d%s' % (int(time.time() * 1e10), int(random.random() * 1e10), extension)


def md5sum(file_name):
    """
    返回文件的MD5码

    :param file_name: 文件名
    :returns: 文件的MD5码
    """
    assert os.path.exists(file_name)
    with open(file_name, 'rb') as f:
        md5 = hashlib.md5(f.read()).hexdigest().upper()
    return md5


def splitList(sample_list, num_part=1, continuous=False):
    """
    分割列表

    :param sample_list: 待分割列表
    :param part_num: 分割份数
    :param continuous: 是否连续分割
    :returns: 分割后的列表组成的列表
    """
    assert num_part >= 1 and type(num_part) == int
    if num_part == 1:
        return [sample_list]
    sample_lists = []
    if continuous:
        idx_pre = 0
        for i in range(num_part):
            num = math.ceil((len(sample_list) - idx_pre) / (num_part - i))
            idx_now = idx_pre + num
            sample_lists.append(sample_list[idx_pre:idx_now])
            idx_pre = idx_now
    else:
        for i in range(num_part):
            sample_lists.append([])
        for loop, sample in enumerate(sample_list, 1):
            index = (loop - 1) % num_part
            sample_lists[index].append(sample)
            if loop % 10000 == 0:
                sys.stdout.write('\r已处理:%d     ' % loop)
        sys.stdout.write('\r已处理:%d     \n' % loop)
    return sample_lists


def readFile(file_name):
    """
    读取文件

    :param file_name: 文件名
    :returns: 每行内容组成的列表
    """
    line_list = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            for loop, line in enumerate(f, 1):
                line_list.append(line.strip())
                if loop % 10000 == 0:
                    sys.stdout.write('\r已处理:%d    ' % loop)
            sys.stdout.write('\r已处理:%d   \n' % loop)
    return line_list


def getRandomSamples(sample_list, num_samples):
    """
    从样本列表里随机获取样本，类似random.sample，但可以处理num_samples > len(sample_list)的情况

    :param sample_list: 样本列表
    :param num_samples: 样本数量
    :returns: 返回指定数量的样本列表，如果num_samples > len(sample_list)则某些元素将会等概率出现多次
    """
    return random.sample(math.ceil(num_samples / len(sample_list)) * sample_list, num_samples)


def sendData2Url(url, value, timeout=3):
    """
    给指定url发送数据value

    :param url: url地址
    :param value: 数据，一般是一个只具有简单数据类型的字典
    :param timeout: 超时等待时间，单位秒
    :returns: url返回值
    """
    data = json.dumps(value).encode('utf8')
    connect_time = time.time()
    request = urllib.request.Request(url, data, {'content-type': 'application/json'})
    response = urllib.request.urlopen(request, timeout=timeout)
    return response.read().decode('utf8')


def convertTimestamp(timestamp, decimal_digits=0, time_zone='Asia/Shanghai', time_format='%Y-%m-%d %H:%M:%S'):
    """
    转换时间戳为指定时区是定格式的时间

    :param timestamp: 时间戳
    :param decimal_digits: 保留小数位数
    :param time_zone: 时区，None使用机器时区
    :param time_format: 时间格式
    :returns: 指定时区是定格式的时间字符串
    """
    assert decimal_digits >= 0
    integer_part_str = ''
    decimal_part_str = ''
    decimal_digits = intRound(decimal_digits)
    integer_part = math.floor(timestamp)
    decimal_part = timestamp - integer_part
    if time_zone is None:
        integer_part_str = time.strftime(time_format, time.localtime(timestamp))
    else:
        integer_part_str = datetime.datetime.fromtimestamp(integer_part, pytz.timezone(time_zone)).strftime(time_format)
    decimal_part_str = '%d' % intRound(decimal_part * math.pow(10, decimal_digits))
    decimal_part_str = '0' * (decimal_digits - len(decimal_part_str)) + decimal_part_str
    return integer_part_str + '.' + decimal_part_str


def file2base64(file_name):
    """
    文件转为base64

    :param file_name: 文件名
    :returns: base64
    """
    with open(file_name, 'rb') as f:
        encoded = base64.b64encode(f.read())
    return str(encoded)[2:-1]


def base642file(base64_data, file_name):
    """
    base64转为文件

    :param base64_data base64字符串
    :param file_name: 文件名
    :returns: 文件名
    """
    byte_data = base64.b64decode(base64_data)
    with open(file_name, 'wb') as f:
        f.write(byte_data)
    return file_name


def image2base64(image):
    """
    Pillow Image转为base64

    :param file_name: Pillow Image
    :returns: base64
    """
    buffered = BytesIO()
    image.save(buffered, format='BMP')
    encoded = base64.b64encode(buffered.getvalue())
    # Pillow和OpenCV解析JPEG和BMP都略有不同，为了尽可能保持一致，可以使用Pillow->OpenCV后调用image2base64_cv，注意RGB和BGR转换
    # return image2base64_cv(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
    return str(encoded)[2:-1]


def base642image(base64_data):
    """
    base64转为Pillow Image

    :param base64_data base64字符串
    :returns: Pillow Image
    """
    base64_data = re.sub('^data:image/.+;base64,', '', base64_data)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    image = Image.open(image_data)
    # Pillow和OpenCV解析JPEG和BMP都略有不同，为了尽可能保持一致，可以使用base642image_cv后转Pillow，注意RGB和BGR转换
    # return Image.fromarray(cv2.cvtColor(base642image_cv(base64_data), cv2.COLOR_BGR2RGB))
    return image


def image2base64_cv(image):
    """
    OpenCV Image转为base64

    :param file_name: OpenCV Image
    :returns: base64
    """
    image = cv2.imencode('.bmp', image)[1]
    encoded = base64.b64encode(image)
    return str(encoded)[2:-1]


def base642image_cv(base64_data):
    """
    base64转为OpenCV Image

    :param base64_data base64字符串
    :returns: OpenCV Image
    """
    byte_data = base64.b64decode(base64_data)
    image_array = np.frombuffer(byte_data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image
