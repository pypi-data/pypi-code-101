# -*- coding: utf-8 -*-
import datetime
import time

"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""
DATE_PATTERN = "%Y-%m-%d"  # 日期默认格式
DATETIME_PATTERN = "%Y-%m-%d %H:%M:%S"  # 时间默认格式
START_TIME = " 00:00:00"
END_TIME = " 23:59:59"


def today():
    """拿到今天时间对象"""
    return datetime.datetime.today()


def now_stamp():
    """当前时间的时间戳"""
    stamp = int(time.time())
    return stamp


def now():
    return datetime.datetime.now()


def datetime_to_str(dt: datetime, pattern=DATETIME_PATTERN):
    """
    把时间对象格式化成字符串
    :param dt: 时间对象
    :param pattern:
    :return:
    """
    try:
        return dt.strftime(format=pattern)
    except:  # noqa
        return ""


def get_day_start_end(day, pattern=DATE_PATTERN):
    """获取某一天的开始和结束时间"""
    _start = datetime_to_str(day, pattern=pattern)
    start = _start + START_TIME
    end = _start + END_TIME
    return start, end


def yesterday_date():
    """获取昨天的日期"""
    return today() - oneday()


def get_yesterday_start_end(pattern=DATE_PATTERN):
    """
    获取昨天的开始和结束时间
    :return: ("2021-08-08 00:00:00", "2021-08-08 23:59:59")
    """
    return get_day_start_end(yesterday_date(), pattern)


def get_today_start_and_end(pattern=DATE_PATTERN):
    """
    获取今天的开始和结束时间
    :return: ("2021-08-08 00:00:00", "2021-08-08 23:59:59")
    """
    return get_day_start_end(today(), pattern)


def __gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day * i


def get_date_list(start: datetime, end: datetime, dt_str=False, pattern=DATE_PATTERN):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :param dt_str: 是否需要时间字符串 默认返回事件对象
    :param pattern: 格式化方式
    :return: ["2021-08-08", "2021-08-09", "2021-08-10", ...]
    """

    data = []
    for d in __gen_dates(start, (end - start).days):
        if dt_str:
            d = datetime_to_str(d, pattern=pattern)
        data.append(d)
    return data


def oneday():
    """获取一天的时间长度"""
    return datetime.timedelta(days=1)


def datetime_to_stamp(dt: datetime, pattern=DATETIME_PATTERN):
    """
    时间对象转时间戳
    :param dt: 时间对象
    :param pattern: 格式
    :return: 时间戳，单位：秒
    """
    if not dt:
        return 0
    time_tuples = time.strptime(datetime_to_str(dt, pattern), pattern)
    return int(time.mktime(time_tuples))


def datetime_str_to_stamp(dt: str, pattern=DATETIME_PATTERN):
    """
    时间字符串转时间戳
    :param dt: 时间字符串
    :param pattern: 格式
    :return: 时间戳，单位：秒
    """
    if not dt:
        return 0
    time_tuples = time.strptime(dt, pattern)
    return int(time.mktime(time_tuples))


def stamp_to_datetime(t):
    """
    时间戳转时间对象
    :param t: 时间戳单位：秒
    """
    if not t:
        return None
    return datetime.datetime.fromtimestamp(t)


def datetime_range(start, end, mode='day'):
    """
    :param start: 开始时间字符串  2019-01-01
    :param end: 结束时间字符串  2019-04-05
    :param mode: 划分间隔 (day，week， month，year)
    :return:[{'start': '2019-05-01', 'end': '2019-05-05'}]
    """
    result = []
    date_all = []
    date_list = []
    tmp = None
    try:
        start = datetime.datetime.strptime(start, '%Y-%m-%d')
        end = datetime.datetime.strptime(end, '%Y-%m-%d')
        if start > end:
            return []
        delta = end - start
        for i in range(delta.days + 1):
            day = start + datetime.timedelta(days=i)

            if mode == 'day':
                flag = day
            elif mode == 'week':
                flag = day - datetime.timedelta(days=day.weekday())
            elif mode == 'month':
                flag = (day.year, day.month)
            elif mode == 'year':
                flag = day.year
            else:
                return []

            if flag != tmp:
                if date_list:
                    date_all.append(date_list)
                date_list = [day]
                tmp = flag
            else:
                date_list.append(day)
        if date_list:
            date_all.append(date_list)

        for i in date_all:
            if mode == 'day':
                result.append({
                    'start': i[0].strftime('%Y-%m-%d'),
                    'end': '',
                })
            else:
                result.append({
                    'start': i[0].strftime('%Y-%m-%d'),
                    'end': i[-1].strftime('%Y-%m-%d'),
                })

    except:  # noqa
        return None
    return result


def str_to_datetime(dt_str, pattern=DATETIME_PATTERN):
    """
    字符串转时间对象
    :param dt_str: 字符串
    :param pattern: 格式
    :return:
    """
    try:
        dt = datetime.datetime.strptime(dt_str, pattern)
        return dt
    except:  # noqa
        return None


def get_remnant_s():
    """获取从现在开始到晚上12点还剩多少秒"""
    n = now()
    end = datetime_to_str(n, pattern=DATE_PATTERN) + END_TIME
    # 当前时间秒数
    return int((str_to_datetime(end) - n).total_seconds())


def get_now_hour_range():
    """
    获取当前时间所处小时起始范围
    :return: 时间对象元组
    """
    n = now()
    s = datetime.datetime(n.year, n.month, n.day, n.hour, 0, 0)
    e = datetime.datetime(n.year, n.month, n.day, n.hour, 59, 59)
    return s, e


def get_now_hour():
    """
    获取当前小时整点
    :return: 字符串
    """
    n = now()
    date = n.date().strftime(DATE_PATTERN)
    hour = n.hour
    date_str = '%s %s:00:00' % (date, hour)
    return date_str

if __name__ == '__main__':
    print(get_now_hour_range())