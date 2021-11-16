#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/21 9:32 下午
# @Author  : xinlan
import os
import sys
from argparse import ArgumentParser
from configparser import ConfigParser

from .producer import TestProducer
from .runner import Runner
from .common.test_data_handler import load_data_from_excel, load_data_from_yaml
from .common.log_handler import get_logger
from .utils import DjangoJSONEncoder


class TestProgram:
    def __init__(self, args=None, test_data=None, url=None):
        self.test_data = test_data
        self.result = None
        self.args = None
        self.parse_args(args)
        self.test_base_dir = None
        self.settings = {}
        self.get_settings()
        self.logger = get_logger(file=self.settings.get('logfile'), debug=self.settings.get('debug', False))
        if self.test_data is None:
            self.get_test_data_from_file()
        self.TestProducer = TestProducer
        self.TestProducer.logger = self.logger
        self.Runner = Runner
        self.Runner.logger = self.logger
        self.Runner.settings = self.settings
        self.TestProducer.settings = self.settings
        if self.args['auto'] == 1:

            self.run()

    def parse_args(self, args):
        if sys.version < '3.9':
            parser = ArgumentParser(description='easytest 命令行参数帮助')
        else:
            parser = ArgumentParser(description='easytest 命令行参数帮助', exit_on_error=False)
        parser.add_argument('file_or_dir', nargs='?', type=str, help='项目路径，或者需要执行的用例文件')
        parser.add_argument('--debug', action="store_true", help='开启日志调试模式，默认为False')
        parser.add_argument('--logfile', type=str, help='日志文件路径')
        parser.add_argument('--marks', type=str, default='', help='运行标记')
        parser.add_argument('--thread_num', type=int, default=0, help='运行启动线程的数量')
        parser.add_argument('--report', type=str, help='测试报告文件路径，按文件后缀生成对应格式的报告')
        parser.add_argument('--auto', type=int, default=1, help='是否自动执行用例，还是要主动运行方法运行，默认为1表示自动运行')
        if args:
            self.args = vars(parser.parse_args(args))
        else:
            self.args = vars(parser.parse_args())

    def get_settings(self):
        ini_file = os.path.join(os.getcwd(), 'easytest.ini')
        if os.path.exists(ini_file):
            self.settings = self.get_ini_config(ini_file)

        for key, value in self.args.items():
            if value:
                self.settings[key] = value
        self.settings['file_or_dir'] = self.args['file_or_dir']

    @staticmethod
    def get_ini_config(ini_file):
        config = ConfigParser()
        config.read(ini_file)
        res = {
        }
        for section in config.sections():
            if section in ['project', 'run']:
                res.update(dict(config[section]))
            else:
                res[section] = dict(config[section])
        if 'run' in config:
            if 'debug' in config['run']:
                res['debug'] = config['run'].getboolean('debug')
            if 'thread_num' in config['run']:
                res['thread_num'] = config['run'].getint('thread_num')
            if 'retry' in config['run']:
                res['retry'] = config['run'].getint('retry')
        if 'db_config' in config and 'port' in config['db_config']:
            res['db_config']['port'] = config['db_config'].getint('port')
        return res

    def get_test_data_file_name(self):
        files = []
        file = self.args['file_or_dir']
        if file is None:
            file = os.getcwd()
            self.test_base_dir = file
        file = os.path.abspath(file)

        if os.path.isfile(file):
            files.append(file)
            self.test_base_dir = os.path.dirname(file)
        elif os.path.isdir(file):
            self.test_base_dir = file
            for root, _, fs in os.walk(file):
                for f in fs:
                    if f.split('.')[-1] in ['xlsx', 'yaml', 'yml']:
                        files.append(os.path.join(root, f))
        else:
            self.logger.warning('目录/文件：{}不存在'.format(file))
            raise RuntimeError('目录/文件：{}不存在'.format(file))

        return files

    def get_test_data_from_file(self):
        files = self.get_test_data_file_name()
        self.test_data = {
            'name': self.settings.get('name', 'easytest'),
            'host': self.settings.get('host'),
            'db_config': self.settings.get('db_config'),
            'interfaces': self.settings.get('interfaces'),
            'test_suits': []
        }
        for file in files:
            if file.split('.')[-1] == 'xlsx':
                data = load_data_from_excel(file)
            else:
                data = load_data_from_yaml(file)
            if os.path.dirname(file) == self.test_base_dir:
                for opt in ['name', 'host', 'db_config', 'interfaces']:
                    if opt in data:
                        self.test_data[opt] = data[opt]
            if 'test_suits' in self.test_data:
                self.test_data['test_suits'].extend(data['test_suits'])

    def generate_report(self):
        if self.settings['report'].split('.')[-1] == 'json':
            with open(self.settings['report'], 'w', encoding='utf-8') as f:
                import json
                json.dump(self.result, f, ensure_ascii=False, cls=DjangoJSONEncoder)
        else:
            print('正在开发中，敬请期待')

    def run(self):
        ts = self.TestProducer(self.test_data).produce()
        self.result = self.Runner().run(ts)
        print('用例总数:{},成功:{}个,跳过:{},失败:{}个,错误:{}个'.format(
            self.result['total_test_case'],
            self.result['success_test_case'],
            self.result['skip_test_case'],
            self.result['fail_test_case'],
            self.result['error_test_case'],
        ))
        if self.settings.get('report'):
            self.generate_report()
        exit(self.result['status'])

    def return_result(self):
        ts = self.TestProducer(self.test_data).produce()
        return self.Runner().run(ts)


main = TestProgram
