# coding=utf8
import shutil
from os import path


def copy_history(report, result):
    start_path = path.join(report, 'history')
    end_path = path.join(result, 'history')
    if path.exists(end_path):
        shutil.rmtree(end_path)
    try:
        shutil.copytree(start_path, end_path)
        print("复制上一运行结果成功！")
    except FileNotFoundError:
        print("allure没有历史数据可复制！")
