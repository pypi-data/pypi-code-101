#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 15:21
# @Author : 心蓝
"""Test case implementation"""
import random
import re
import json
from unittest import TestCase

import requests
from jsonpath import jsonpath
from faker import Faker

# from .common.log_handler import logger


class BaseCase(TestCase):
    name = None   # 功能名称
    # logger = logger  # 日志器

    @classmethod
    def setUpClass(cls) -> None:
        # 类前置
        cls.logger.info('=========={}测试开始============'.format(cls.name))
        # print('==========注册接口测试开始============')

    @classmethod
    def tearDownClass(cls) -> None:
        # 类后置
        cls.logger.info('=========={}测试结束============'.format(cls.name))
        # print('==========注册接口测试结束============')

    @classmethod
    def send_http_request(cls, url, method='get', **kwargs) -> requests.Response:
        """
        sent http request
        :param url: 
        :param method: 
        :param kwargs: 
        :return: 
        """
        if getattr(cls, 'session', None) is None:
            cls.session = requests.session()
        method = method.lower()
        return getattr(cls.session, method)(url, **kwargs)

    @classmethod
    def get_unused_phone_num(cls, sql_template=None):
        """
        生成一个没用使用的手机号码
        :sql_template: sql模板，用来查询数据库中是否存在指定的电话号码，format风格
        例如：select id from member where mobile_phone='{}'
        :return: 手机号码
        """
        if cls.db is None:
            raise RuntimeError('没有数据库链接信息，要根据数据库结果生成手机号码请设置数据库链接信息')
        if not sql_template:
            sql_template = "select id from member where mobile_phone='{}'"
        for i in range(100):
            phone_num = cls.generate_phone_num()
            if not cls.db.exist(sql_template.format(phone_num)):
                return phone_num

    @staticmethod
    def generate_phone_num():
        """
        随机生成手机号码
        :return:
        """
        # 1开头，11位，第二数3456789，后面9位
        # 1开头，11位，第二个数358
        # 写死，避免后面出问题，如果要测手机号码单独测试
        phone = ['158']
        # 剩下的9位
        for i in range(8):
            phone.append(random.choice('0123456789'))
        phone = ''.join(phone)

        return phone

    def test(self, testcase):
        self.case = testcase
        self.logger.debug('用例【{}】开始测试>>>>>>>>'.format(self.case['title']))
        try:
            self.__process_test_data()

            self.send_request()

            self.__assert_res()

            self.__extract_data_from_response()
            self.logger.info('用例【{}】测试成功<<<<<<<<<'.format(self.case['title']))
        except Exception as e:
            self.logger.warning('用例【{}】测试失败<<<<<<<<<'.format(self.case['title']))
            raise e
        finally:
            self.logger.debug('用例【{}】测试结束<<<<<<<<<'.format(self.case['title']))

    def __process_test_data(self):
        """
        处理测试数据
        :return:
        """
        self.generate_test_data()
        self.__check_case()
        self.__process_url()
        self.__replace_args()
        self.__handle_request_data()

    def generate_test_data(self):
        """
        动态生成测试数据 phone
        :return:
        """
        fake = Faker('zh-cn')
        fake_keys = dir(fake)
        # 子类可以复写实现自定义的生成测试数据
        # 1 生成动态数据并替换
        temp = json.dumps(self.case)
        keys = re.findall(r'\$(\w*?)\$', temp)
        for key in keys:
            if key not in fake_keys:
                self.logger.error('${}$这个动态数据关键字不支持'.format(key))
                raise ValueError('${}$这个动态数据关键字不支持'.format(key))
            value = str(getattr(fake, key)())
            temp = temp.replace('${}$'.format(key), value)
        self.case = json.loads(temp)

    def __check_case(self):
        """
        检查用例数据格式
        :return:
        """
        keys = ['title', 'method', 'url', 'status_code', 'res_type']
        for key in keys:
            if key not in self.case:
                raise ValueError('用例数据错误！必须包含【{}】字段'.format(key))

    def __process_url(self):
        """
        处理url
        :return:
        """

        if self.case['url'].startswith('http'):
            pass
        elif self.case['url'].startswith('/'):
            self.case['url'] = self.project.get('host') + self.case['url']
        else:
            if self.case['url'] not in self.project.get('interfaces'):
                self.logger.warning('用例【{}】处理url错误：接口名字 \'{}\'不正确'.format(self.case['title'], self.case['url']))
                raise ValueError('用例【{}】处理url错误：接口名字 \'{}\'不正确'.format(self.case['title'], self.case['url']))
            self.case['url'] = self.project.get('host') + self.project.get('interfaces')[self.case['url']]

    def __replace_args(self):
        """
        替换参数
        """
        temp = json.dumps(self.case)
        temp = self.replace_args_by_re(temp)
        self.case = json.loads(temp)

    def __handle_request_data(self):
        """
        处理请求数据
        :return:
        """
        if self.case.get('request'):
            self.case['request'] = self.__loads_by_json_or_eval(self.case['request'])
        else:
            self.case['request'] = {}

    def send_request(self):
        """
        发送请求，当有特殊处理时可以复写
        """
        try:
            self.response = self.send_http_request(url=self.case['url'], method=self.case['method'],
                                                   **self.case['request'])
        except Exception as e:
            self.logger.warning('用例【{}】发送http请求错误: {}'.format(self.case['title'], e))
            self.logger.warning('url:{}'.format(self.case['url']))
            self.logger.warning('method:{}'.format(self.case['method']))
            self.logger.warning('args:{}'.format(self.case['request']))
            raise RuntimeError('用例【{}】发送http请求错误:{}'.format(self.case['title'], e))

    def __assert_res(self):
        """
        断言
        """
        self.__assert_status_code()
        self.__assert_response()
        self.__assert_db()

    def __assert_status_code(self):
        """
        响应状态码断言
        :return:
        """
        try:
            self.assertEqual(self.case['status_code'], self.response.status_code)
        except AssertionError as e:
            self.logger.warning('用例【{}】状态码断言失败！'.format(self.case['title']))
            raise e
        else:
            self.logger.debug('用例【{}】状态码断言成功！'.format(self.case['title']))

    def __assert_response(self):
        if self.case.get('assertion'):
            self.__check_assertion_field()

            if self.case['res_type'].lower() == 'json':
                self.__assert_json_response()
            elif self.case['res_type'].lower() == 'xml':
                self.__assert_xml_response()
            else:
                self.logger.warning('用例【{}】响应数据断言错误：请指定合适的响应类型'.format(self.case['title']))
                raise ValueError('用例【{}】响应数据断言错误：请指定合适的响应类型'.format(self.case['title']))

    def __loads_by_json_or_eval(self, s):
        """
        将json字符串load为python字典，支持简单的算术表达式，通过eval实现
        :param s:
        :return:
        """
        try:
            if not isinstance(s, str):
                s = json.dumps(s)
            res = json.loads(s)
        except Exception as e:
            try:
                from decimal import Decimal
                res = eval(s)
            except Exception as e:
                self.logger.warning('用例【{}】转换json参数失败：{}'.format(self.case['title'], e))
                raise ValueError('用例【{}】转换json参数失败：{}'.format(self.case['title'], e))
            else:
                return res

        else:
            return res

    def __create_single_data(self, s):
        """
        造单个的测试数据，例如电话号码
        :param s:
        :return:
        """
        names = re.findall('#(.*?)#', s)
        for name in names:
            if name == 'phone':
                phone = self.get_unused_phone_num()
                setattr(self, name, phone)

    def replace_args_by_re(self, s):
        """
        通过正则表达式动态替换参数
        :param s: 需要被替换的json字符串
        :return:
        """
        args = re.findall('#(.*?)#', s)
        for arg in set(args):
            value = getattr(self, arg, None)
            if value:
                s = s.replace('#{}#'.format(arg), str(value))
        return s

    def __assert_json_response(self):
        """
        断言json响应
        :return:
        """
        self.response_data = self.response.json()
        for item in self.case['assertion']:

            actual_res = self.__extract_data_from_json(self.response_data, item[1])

            expect_res = item[2]

            try:
                if item[0] == 'eq':
                    self.assertEqual(expect_res, actual_res)
            except Exception as e:
                self.logger.warning('用例【{}】响应数据断言失败'.format(self.case['title']))
                self.logger.warning('请求数据是: {}'.format(self.case['request']))
                self.logger.warning('期望结果是：{}'.format(expect_res))
                self.logger.warning('实际结果是：{}'.format(actual_res))
                self.logger.warning('校验条件是: {}'.format(item))
                self.logger.warning('响应回的数据是：{}'.format(self.response_data))
                raise e
        else:
            self.logger.debug('用例【{}】响应数据断言成功'.format(self.case['title']))

    def __assert_xml_response(self):
        """
        断言xml
        :return:
        """
        pass

    def __assert_db(self):
        """
        数据库断言
        :return:
        """
        if not self.case.get('db_assertion'):
            return
        if self.db is None:
            raise RuntimeError('没有数据库链接信息，要数据库断言请填写数据库信息')
        self.case['db_assertion'] = self.replace_args_by_re(self.case['db_assertion'])
        self.case['db_assertion'] = self.__loads_by_json_or_eval(self.case['db_assertion'])
        self.__check_db_assertion_field()

        for item in self.case['db_assertion']:
            actual_res = self.__get_value_from_db(item[0], item[1])
            expect_res = item[2]
            try:

                self.assertEqual(expect_res, actual_res)
            except Exception as e:
                self.logger.warning('用例【{}】::数据库断言失败'.format(self.case['title']))
                self.logger.warning('执行sql是: {}'.format(item[1]))
                self.logger.warning('期望结果是：{}'.format(expect_res))
                self.logger.warning('实际结果是：{}'.format(actual_res))
                self.logger.warning('校验条件时: {}'.format(item))
                raise e
        else:
            self.logger.debug('用例【{}】数据库断言成功'.format(self.case['title']))

    def __get_value_from_db(self, condition, sql):
        """
        获取sql对应的值
        :param item:
        :return:
        """
        if condition == 'exist':
            res = self.db.exist(sql)
        elif condition == 'eq':
            res = self.db.get_one_value(sql)
        else:
            raise ValueError('用例【{}】数据库断言条件不支持，当前支持：exist,eq'.format(self.case['title']))
        return res

    def __extract_data_by_jsonpath(self, obj, extract_exp):
        """
        jsonpath提取数据
        :param obj:
        :param extract_exp:
        :return:
        """
        res = jsonpath(obj, extract_exp)
        if res:
            if len(res) == 1:
                return res[0]
            return res
        else:
            raise ValueError('用例【{}】jsonpath表达式:{}错误'.format(self.case['title'], extract_exp))

    def __extract_data_from_json(self, obj, extract_exp):
        """
        从json数据里提取数据
        """
        res = jsonpath(obj, extract_exp)
        if not res:
            res = re.findall(extract_exp, json.dumps(obj, ensure_ascii=False))
            if not res:
                return '没有匹配到值'
                # raise ValueError('用例【{}】断言提取表达式:{} 错误'.format(self.case['title'], extract_exp))

        return res[0]

    def __extract_actual_res(self, extract_exp):
        if self.case['res_type'].lower() == 'json':
            res = self.response.json()

        if extract_exp[0] == '.':
            keys = extract_exp[1:].split('.')
            for key in keys:
                res = res.get(key)
        return res

    def __extract_data_from_response(self):
        """
        从响应中提取数据
        :return:
        """
        if self.case.get('extract'):

            self.__check_extract_field()
            if self.case['res_type'].lower() == 'json':
                for item in self.case['extract']:
                    value = self.__extract_data_by_jsonpath(self.response_data, item[1])

                    setattr(self.__class__, item[0], value)
            elif self.case['res_type'].lower() == 'xml':
                pass

    def __check_extract_field(self):
        """
        检查extract字段格式
        :return:
        """
        self.__check_field('extract', 2)

    def __check_assertion_field(self):
        """
        检查assertion字段格式
        :return:
        """
        self.__check_field('assertion', 3)

    def __check_db_assertion_field(self):
        """
        检查db_assertion字段格式
        :return:
        """
        if isinstance(self.case['db_assertion'], list):
            for item in self.case['db_assertion']:
                if not len(item) == 3:
                    raise ValueError(
                        '用例【{}】{}字段格式错误: {} 不是一个{}元列表'.format(self.case['title'], 'db_assertion', 3, item))

        else:
            raise ValueError('用例【{0}】{1}字段格式错误:{1}字段应该是一个列表'.format(self.case['title'], 'db_assertion'))

    def __check_field(self, field_name, length):
        """
        检查field_name字段格式
        :param field_name:
        :param length
        :return:
        """
        try:
            self.case[field_name] = self.__loads_by_json_or_eval(self.case[field_name])
        except Exception as e:
            self.logger.error('用例【{}】{}字段json格式错误: {}'.format(self.case['title'], field_name, e))
            raise ValueError('用例【{}】{}字段json格式错误: {}'.format(self.case['title'], field_name, e))

        if isinstance(self.case[field_name], list):
            for item in self.case[field_name]:
                if not len(item) == length:
                    raise ValueError('用例【{}】{}字段格式错误: {} 不是一个{}元列表'.format(self.case['title'], field_name, item, length))

        else:
            raise ValueError('用例【{0}】{1}字段格式错误:{1}字段应该是一个列表'.format(self.case['title'], field_name))




