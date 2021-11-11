# -*- coding: utf-8 -*
from pyhive import hive
import requests
import json
import re
import sys
import datetime
import calendar

# 设置周一为一周第一天
calendar.setfirstweekday(firstweekday=6)

def run_hive(sql,host1,host2,port,username,message,url):
    try:
        sqls='''set hive.tez.auto.reducer.parallelism=true;
        set hive.exec.reducers.max=99;
        set hive.merge.tezfiles=true;
        set hive.merge.smallfiles.avgsize=32000000;
        set hive.merge.size.per.task=128000000;
        set tez.queue.name=analyst;'''+sql
        sqllist = [j for j in sqls.split(';') if j != '']
        res=[]
        conn = hive.connect(host=host1,port=port,username=username)
        cursor = conn.cursor()
        for i in sqllist:
            cursor.execute(i)
            try:
                res = cursor.fetchall()
            except:
                pass
            conn.commit()
        conn.close()
        return res
    except:
        try:
            conn = hive.connect(host=host2,port=port,username=username)
            cursor = conn.cursor()
            for i in sqllist:
                cursor.execute(i)
                try:
                    res = cursor.fetchall()
                except:
                    pass
                conn.commit()
            conn.close()
            return res
        except Exception as e:
            try:
                error='告警消息: '+message+'\n'+i+'\n'+re.match(r'.* (FAILED:.*)',str(e)).group(1)
            except:
                error='告警消息: '+i+'\n'+str(e)
            finally:
                headers = {'Content-Type': 'application/json'}
                data={
                    "msgtype": "text",
                    "text": {
                        "content": error,
                    }
                }
                response=requests.post(url,data=json.dumps(data),headers=headers)
                sys.exit()
                
def send_alert(message,url):
    message='提示消息: '+str(message)
    headers = {'Content-Type': 'application/json'}
    data={
        "msgtype": "text",
        "text": {
            "content": message,
        }
    }
    response=requests.post(url,data=json.dumps(data),headers=headers)

def us_time_conversion(sdatestr):
    """
    冬令时、夏令时判断，将北京时间转换为美东时间的东夏令时 # 夏令时（3月11日至11月7日），冬令时（11月8日至次年3月11日）
    :param sdatestr: 日期，str，如19900101
    :return: sdatestr--当前日期-str,start_time--美东令时的当天开始时间-str,end_time--美东令时的当天结束时间-str
    """
    try:
        start_time = datetime.datetime.strptime(sdatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyy，如：19900101，error:{}".format(e))
    end_time = start_time + datetime.timedelta(days=1)
    sdatestr = start_time.strftime("%Y%m%d")
    start_mon = start_time.month
    start_day = start_time.day
    is_summer_day = 0
    if (start_mon > 3) and (start_mon < 11):
        is_summer_day = 1
    elif (start_mon == 3) and (start_day - 11 >= 0):
        is_summer_day = 1
    elif (start_mon == 11) and (start_day - 7 <= 0):
        is_summer_day = 1
    else:
        is_summer_day = 0
    if is_summer_day:
        start_time = start_time.strftime("%Y%m%d") + " 04:00:00"
        end_time = end_time.strftime("%Y%m%d") + " 04:00:00"
    else:
        start_time = start_time.strftime("%Y%m%d") + " 05:00:00"
        end_time = end_time.strftime("%Y%m%d") + " 05:00:00"

    return sdatestr,start_time,end_time


def get_first_last_day(year, month):
    """
    返回指定月份的第一天和最后一天
    :param year: 年份，字符串类型，如1990
    :param month: 月份，字符串类型，如1
    :return: firstDay-月初, lastDay-月末
    """
    try:
        datetime.datetime.strptime(str(year)+'0101', "%Y%m%d")
    except Exception as e:
        raise Exception("year 参数格式必须是yyyy，如：1990，error:{}".format(e))
    try:
        datetime.datetime.strptime('1990'+str(month)+'01', "%Y%m%d")
    except Exception as e:
        raise Exception("month 参数格式必须是yyyy，如：08，error:{}".format(e))
    # 获取当前月的第一天的星期和当月总天数
    weekDay, monthCountDay = calendar.monthrange(year, month)
    # 获取当前月份第一天
    firstDay = datetime.date(year, month, day=1)
    # 获取当前月份最后一天
    lastDay = datetime.date(year, month, day=monthCountDay)
    # 返回第一天和最后一天
    return firstDay, lastDay

def get_monday_firday(sdatestr):
    """
    返回星期一和星期五的日期
    :param sdatestr: 初始时间
    :return:  monday--周一,friday--周二
    """
    try:
        start_day = datetime.datetime.strptime(sdatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyy，如：1990，error:{}".format(e))
    weekday = start_day.weekday()
    monday = start_day - datetime.timedelta(days=weekday)
    friday = monday + datetime.timedelta(days=4)
    return monday,friday

def date_compare(sdatestr,edatestr):
    """
    start,end两个时间比较，返回bool值
    :param start: 日期，字符串格式20210101
    :param end: 日期，字符串格式20210102
    :return: bool值 true 表示start>end
    """
    try:
        start = datetime.datetime.strptime(sdatestr,"%Y%m%d")
        end = datetime.datetime.strptime(edatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyy，如：19900101，error:{}".format(e))
    return start > end


def get_month_early(sdatestr, n):
    """
    返回指定日期start前n个月的月初日期
    :param start: 开始日期 19900101
    :param n: 前n个月
    :return: 月初日期
    """
    try:
        sdate = datetime.datetime.strptime(sdatestr,"%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyy，如：19900101，error:{}".format(e))
    month = sdate.month
    year = sdate.year
    for i in range(n):
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
    return datetime.date(year, month, 1).strftime("%Y%m%d")


def get_date_by_times(sdatestr, edatestr):
    """
    根据开始日期、结束日期返回这段时间里所有天的集合
    :param sdatestr: 日期，字符串格式20210101
    :param edatestr: 日期，字符串格式20210101
    :return: 日期列表，list(str,)
    """
    try:
        datestart = datetime.datetime.strptime(sdatestr, "%Y%m%d")
        dateend = datetime.datetime.strptime(edatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyymmdd，如：19900101，error:{}".format(e))
    daylist = []
    daylist.append(datestart.strftime("%Y%m%d"))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        daylist.append(datestart.strftime("%Y%m%d"))
    return daylist



def get_date_by_offset(sdatestr,before_day):
    """
     获取前1天或N天的日期，before_day=1：前1天；before_day=N：前N天
    :param sdatestr: 日期，str,如20210101，开始日期
    :param before_day: 前before_day天，int，如5
    :return: re_date-日期，str,如20210101，结束日期
    """
    try:
        datestart = datetime.datetime.strptime(sdatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyymmdd，如：19900101，error:{}".format(e))
    # 计算偏移量
    offset = datetime.timedelta(days=-before_day)
    # 获取想要的日期的时间
    re_date = (datestart + offset).strftime("%Y%m%d")
    return re_date

def caltime(sdatestr, edatestr):
    """
    计算两个日期相差天数，自定义函数名，和两个日期的变量名
    #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    :param sdatestr: 日期，str,如20210101，开始日期
    :param edatestr: 日期，str,如20210101，结束日期
    :return:
    """
    try:
        # "%Y-%m-%d %H:%M:%S"  计算日期还是日期时间
        datestart = datetime.datetime.strptime(sdatestr, "%Y%m%d")
        dateend = datetime.datetime.strptime(edatestr, "%Y%m%d")
    except Exception as e:
        raise Exception("参数格式必须是yyyymmdd，如：19900101，error:{}".format(e))
    return (datestart-dateend).days



   
                
