"""一些生成器方法，生成随机数，手机号，以及连续数字等"""
import random
import os
from faker import Factory
from time import time as ttm
from PIL import Image
import png
from concurrent.futures import ThreadPoolExecutor
from ..config import Config


fake = Factory().create('zh_CN')


def random_phone_number():
    """随机手机号"""
    return fake.phone_number()


def random_name():
    """随机姓名"""
    return fake.name()


def random_address():
    """随机地址"""
    return fake.address()


def random_email():
    """随机email"""
    return fake.email()


def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()


def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """

    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment

    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """

    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield random.choice(my_list)

    return choice_generator


def gen_16_randint(total=1, uniq_flag=1):
    """
    随机生成16位数字，跟当前时间戳有关(1毫秒100个数，如果重复，叠加头部标志）
    :param total: 随机数个数
    :param uniq_flag: 头部标志，内部调用
    :return: 返回列表
    """
    uniq_flag = 1 if not uniq_flag else int(uniq_flag)
    total = 1 if not total else int(total)
    # 每0.1ms生成10个数
    now_time = lambda: int(round(ttm() * 10000))
    num_list = ["{}{}{}".format(uniq_flag, now_time(), i) for i in range(10)]
    # 递归返回随机值
    if 0 < total < 10:
        num_list = random.sample(num_list, total)
    elif total > 10:
        num_list.extend(gen_16_randint(total - 10))
        # 递归去重
        unique_count = len(set(num_list))
        if unique_count != len(num_list):
            num_list = list(set(num_list))
            uniq_flag = uniq_flag + 1 if uniq_flag < 9 else 1
            num_list.extend(gen_16_randint(total - unique_count, uniq_flag))
    return num_list


def gen_17_randint(total=1, uniq_flag=1):
    """
    随机生成17位数字，跟当前时间戳有关(1毫秒1000个数，如果重复，叠加头部标志）
    :param total: 随机数个数
    :param uniq_flag: 头部标志，内部调用
    :return: 返回列表
    """
    uniq_flag = 1 if not uniq_flag else int(uniq_flag)
    total = 1 if not total else int(total)
    # 每0.1ms生成10个数
    now_time = lambda: int(round(ttm() * 10000))
    num_list = [int("{}{}{:02}".format(uniq_flag, now_time(), i)) for i in range(100)]
    # 递归返回随机值
    if 0 < total < 100:
        num_list = random.sample(num_list, total)
    elif total > 100:
        num_list.extend(gen_17_randint(total - 100))
        # 递归去重
        unique_count = len(set(num_list))
        if unique_count != len(num_list):
            num_list = list(set(num_list))
            uniq_flag = uniq_flag + 1 if uniq_flag < 9 else 1
            num_list.extend(gen_17_randint(total - unique_count, uniq_flag))
    return num_list


def gen_image(filename='default', size=(1280, 720), color=(255, 255, 255), format='JPEG'):
    """
    size: (1280, 720)
    color: (255, 255, 255)
    format: "PNG"
    """
    img = Image.new('RGB', size, color)
    img.save(filename, format)


def gen_png(width, hight, size, path=None):
    if width > 800 or hight > 800:
        raise ValueError("width or height max is 800")
    if not path:
        path = Config().DATA_PATH
    s = []
    for i in range(hight):
        s.append([])
        for j in range(width):
            s[i].append(0)

    palette = [(0x55, 0x55, 0x55), (0xff, 0x99, 0x99)]
    w = png.Writer(width, hight, palette=palette, bitdepth=1)
    filename = os.path.join(path, f'{width}x{hight}_{size}k.png')
    f = open(filename, 'wb')

    with ThreadPoolExecutor(max_workers=15) as executor:
        args = ((f, s) for i in range(size * 10))
        for result in executor.map(lambda p: w.write(*p), args):
            pass


if __name__ == '__main__':
    print(random_phone_number())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_str(min_chars=6, max_chars=8))
    id_gen = factory_generate_ids(starting_id=0, increment=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))

    # gen_image("10x10.png", (10, 10), (255, 255, 255), "PNG")
    # gen_png(800, 400, 100)
    # gen_png(800, 800, 100)
    # gen_png(79, 79, 1151)
    # gen_png(800, 400, 100)
    gen_image('1280x960_1M', (1280, 960))