#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import unittest
import mock
from gwc import gwc_scripts
import sys
from tempfile import TemporaryFile
import platform
import argparse
import os
import requests_mock
import os
from gdpy.yml_utils import yaml_loader
from collections import namedtuple
from gwc.runners.wdl import WDLRunner
from gwc.runners.gwl import GWLRunner


class TestGWCScripts(unittest.TestCase):

    @mock.patch("gdpy.api.Tasks.create_task")
    @mock.patch("gwc.gwc_scripts.read_configuration")
    @mock.patch("builtins.open" if platform.python_version_tuple()[0] == "3" else "__builtin__.open")
    @mock.patch("gwc.gwc_scripts.WorkflowApp._find_workflow")
    def test_run_workflow(self, mock_find_workflow, mock_open, mock_read_configuration, mock_create_task):
        mock_open.return_value = get_mock_file("{}")
        file_name = "input.json"
        mock_read_configuration.return_value = "endpoint", "access_id", "access_key", "account_name", "user_name"

        mock_find_workflow.return_value = {"workflow": "workflow", "version": "1"}, gwc_scripts.WDLWorkflow()
        testargs = ["", "workflow", "run", "-n", "many_layer_part_file", "-k", "true",
                    "-v", "1", "-a", "test", "-d", "run_dir", "-p", file_name]
        with mock.patch.object(sys, 'argv', testargs):
            gwc_scripts.main()
        self.assertEqual(mock_create_task.call_args[1]["parameters"]["keep_output_structure"], True)

        # test default --keep_output_structure
        testargs = ["", "workflow", "run", "-n", "many_layer_part_file",
                    "-v", "1", "-a", "test", "-d", "run_dir", "-p", file_name]

        mock_open.return_value = get_mock_file("{}")
        with mock.patch.object(sys, 'argv', testargs):
            gwc_scripts.main()
        self.assertEqual(mock_create_task.call_args[1]["parameters"]["keep_output_structure"], True)

        # test  --keep_output_structure false
        testargs = ["", "workflow", "run", "-n", "many_layer_part_file", "-k", "false",
                    "-v", "1", "-a", "test", "-d", "run_dir", "-p", file_name]

        mock_open.return_value = get_mock_file("{}")
        with mock.patch.object(sys, 'argv', testargs):
            gwc_scripts.main()
        self.assertEqual(mock_create_task.call_args[1]["parameters"]["keep_output_structure"], False)

    def test_str2bool(self):
        self.assertEqual(gwc_scripts.str2bool("yes"), True)
        self.assertEqual(gwc_scripts.str2bool("true"), True)
        self.assertEqual(gwc_scripts.str2bool("t"), True)
        self.assertEqual(gwc_scripts.str2bool("y"), True)
        self.assertEqual(gwc_scripts.str2bool("1"), True)
        self.assertEqual(gwc_scripts.str2bool("no"), False)
        self.assertEqual(gwc_scripts.str2bool("false"), False)
        self.assertEqual(gwc_scripts.str2bool("f"), False)
        self.assertEqual(gwc_scripts.str2bool("n"), False)
        self.assertEqual(gwc_scripts.str2bool("0"), False)
        with self.assertRaises(argparse.ArgumentTypeError):
            gwc_scripts.str2bool("error")
        with self.assertRaises(argparse.ArgumentTypeError):
            gwc_scripts.str2bool("==")

    @mock.patch("gwc.gwc_scripts.read_configuration")
    def test_get_gwl_workflow(self, mock_read_configuration):
        mock_read_configuration.return_value = "endpoint", "access_id", "access_key", "account_name", "user_name"
        temp_dir = tempfile.mkdtemp()
        value = {'workflows': [{'status': 'checked', 'description': '详见公共工具Fastqc（v2）', 'tags': [], 'fileset': False,
                                'modified_time': 1593340882.598991, 'version': 3, 'created_time': 1593340882.256582,
                                'configs': {'nodelist': [{'inputs': None, 'name': 'loaddata', 'parameters': None,
                                                          'outputs': {'data': {'enid': 'loaddata_reads'}},
                                                          'app_id': '55128c58f6f4067d63b956b5', 'alias': '输入序列文件',
                                                          'node_id': 'loaddata_reads'},
                                                         {'inputs': {'reads': [{'enid': 'loaddata_reads'}]},
                                                          'name': 'Fastqc',
                                                          'parameters': {'threads': {'variable': True, 'value': 2}},
                                                          'outputs': {'tgz': [{'enid': 'Fastqc_output_tgz'}]},
                                                          'app_id': '5b39fbaa671856001e0e13d5',
                                                          'alias': 'fastqc 0.11.3', 'node_id': 'Fastqc_node1'},
                                                         {'inputs': {'data': {'enid': 'Fastqc_output_tgz'}},
                                                          'name': 'storedata', 'parameters': {
                                                             'description': {'variable': False, 'value': ' '},
                                                             'name': {'variable': False, 'value': ' '}},
                                                          'outputs': None, 'app_id': '55128c94f6f4067d63b956b6',
                                                          'alias': 'store Fastqc_output_tgz',
                                                          'node_id': 'store_data_node_fastqc'}]}}]}
        with requests_mock.Mocker() as mock_server:
            mock_server.get("https://endpoint/accounts/account_name/projects/default/workflows/Fastqc_gwl/", json=value)
            gwc_scripts._get_gwl_workflow("Fastqc_gwl", 3, os.path.join(temp_dir, "test.yml"), out_type="file")
        data = yaml_loader(os.path.join(temp_dir, "test.yml"))

        value['workflow'] = value['workflows'][0]
        del value['workflows']
        value['workflow']['nodelist'] = value['workflow']['configs']['nodelist']
        del value['workflow']['configs']
        value['workflow']['name'] = "Fastqc_gwl"

        self.assertEqual(data, value)

    @mock.patch("gwc.gwc_scripts.read_configuration")
    def test_get_job_runner(self, mock_read_configuration):
        mock_read_configuration.return_value = "endpoint", "access_id", "access_key", "account_name", "user_name"
        Args = namedtuple("Args", "quiet taskid")
        args = Args(False, "task_id")
        value = {'type': 'wdl'}
        with requests_mock.Mocker() as mock_server:
            mock_server.get("https://endpoint/accounts/account_name/projects/default/wdl/tasks/task_id/", json=value)
            runner = gwc_scripts.TasksApp._get_job_runner(args)
            self.assertIsInstance(runner, WDLRunner)

        value = {'type': 'gwl'}
        with requests_mock.Mocker() as mock_server:
            mock_server.get("https://endpoint/accounts/account_name/projects/default/wdl/tasks/task_id/", json=value)
            runner = gwc_scripts.TasksApp._get_job_runner(args)
            self.assertIsInstance(runner, GWLRunner)

    @mock.patch("gdpy.api.Tasks.restart_task")
    @mock.patch("gwc.gwc_scripts.read_configuration")
    @mock.patch("gwc.gwc_scripts.WorkflowApp._find_workflow")
    def test_restart_task(self, mock_find_workflow, mock_read_configuration, mock_restart_task):
        mock_read_configuration.return_value = "endpoint", "access_id", "access_key", "account_name", "user_name"

        mock_find_workflow.return_value = {"workflow": "workflow", "version": "1"}, gwc_scripts.WDLWorkflow()
        testargs = ["", "task", "restart", "-i", "task_id"]
        with mock.patch.object(sys, 'argv', testargs):
            gwc_scripts.main()
        self.assertEqual(mock_restart_task.call_args[0][0], "task_id")
        self.assertEqual(mock_restart_task.call_args[1], {"debug_params": []})

        testargs = ["", "task", "restart", "-i", "task_id", "-r", "test/file/restart_config.yaml"]
        with mock.patch.object(sys, 'argv', testargs):
            gwc_scripts.main()
        self.assertEqual(mock_restart_task.call_args[0][0], "task_id")
        self.assertEqual(mock_restart_task.call_args[1], {"debug_params": [{
            "job_name": "test_job",
            "runtime": {
                "cpu": 4,
                "memory": 5
            },
            "command": "test command"
        }]})

    @mock.patch("builtins.print" if platform.python_version_tuple()[0] == "3" else "__builtin__.print")
    @mock.patch("gwc.runners._base.api.Tasks.get_jobs")
    @mock.patch("gwc.runners._base.api.Tasks.list_tasks")
    @mock.patch("gwc.gwc_scripts.read_configuration")
    def test_get_jobs(self, mock_read_configuration, mock_list_tasks, mock_get_jobs, mock_print):
        mock_read_configuration.return_value = "endpoint", "access_id", "access_key", "account_name", "user_name"

        mock_list_tasks.side_effect = [mock.MagicMock(task_list=[{'status': 'success', 'account': 'multitest',
                                                                  'task_name': '6142ac31d272fbeabd817466-call-sub_sample',
                                                                  'task_id': '6142ac32810cbfa96114a645',
                                                                  'process': None,
                                                                  'workflow_name': 'subtest',
                                                                  'workflow_id': '5f1a9e3a4090eab68b1da86c',
                                                                  'user': 'admin', 'startTime': 1631759410.2506895,
                                                                  'endTime': 1631759594.1862488, 'type': 'wdl',
                                                                  'workflow_version': 1}]),
                                       mock.MagicMock(task_list=[
                                           {'status': 'success', 'account': 'multitest',
                                            'task_name': '6142ac32810cbfa96114a645-call-sub_sample',
                                            'task_id': '6142ac32f41d86b35814a645', 'process': None,
                                            'workflow_name': 'subtest', 'workflow_id': '5f1a9e3a4090eab68b1da86c',
                                            'user': 'admin', 'startTime': 1631759410.5368168,
                                            'endTime': 1631759591.167847, 'type': 'wdl', 'workflow_version': 1}]),
                                       mock.MagicMock(task_list=[])
                                       ]
        mock_get_jobs.side_effect = [mock.MagicMock(jobs=[
            {'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
             'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2b%2F6142ac6ef042b7001ed6df2b',
             'job_id': '6142ac6ef042b7001ed6df2b', 'task_id': '6142ac32f41d86b35814a645',
             'job_name': '6142ac32f41d86b35814a645-call-work-0', 'startTime': 1631759470.697, 'endTime': 1631759591.114,
             'id': '6142ac6e740522bc8814a645', 'name': 'call-work-0'}]),
            mock.MagicMock(jobs=[{'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
                                  'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2b%2F6142ac6ef042b7001ed6df2b.1631759470.'
                                              '6142ac6e4b72510001327e3b%2Fstdout.log?OSSAccessKeyId=LTAI4GKcuQgcEmF921qrULUf&Expires=1947119584&Signature=sq1UWKme35c%2F1YyPmQxryUhGDUk%3D',
                                  'job_id': '6142ac6e740522bc8814a645', 'task_id': '6142ac32f41d86b35814a645',
                                  'job_name': 'call-work-0',
                                  'full_job_name': '6142ac32f41d86b35814a645-call-work-0',
                                  'startTime': '2021-09-16 10:31:10',
                                  'endTime': '2021-09-16 10:33:11', 'id': '6142ac6e740522bc8814a645',
                                  'name': 'call-work-0'}]),
            mock.MagicMock(jobs=[{'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
                                  'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2a%2F6142ac6ef042b7001ed6df2a.1631759470.'
                                              '6142ac6e4b72510001327e36%2Fstdout.log?OSSAccessKeyId=LTAI4GKcuQgcEmF921qrULUf&Expires=1947119586&Signature=CegnB3ud%2Bk2u33OTZrHQlh2%2Be4I%3D',
                                  'job_id': '6142ac6ef042b7001ed6df2a', 'task_id': '6142ac32810cbfa96114a645',
                                  'job_name': '6142ac32810cbfa96114a645-call-work-0', 'startTime': 1631759470.53,
                                  'endTime': 1631759594.17, 'id': '6142ac6ef41d86b35814a648', 'name': 'call-work-0'}])
        ]

        testargs = ["", "task", "getjobs", "-i", "6142ac31d272fbeabd817466", "-s"]
        with mock.patch.object(sys, 'argv', testargs):
            value = {'type': 'wdl'}
            with requests_mock.Mocker() as mock_server:
                mock_server.get(
                    "https://endpoint/accounts/account_name/projects/default/wdl/tasks/6142ac31d272fbeabd817466/",
                    json=value)
                gwc_scripts.main()
        self.assertEqual(mock_print.call_count, 9)
        self.assertEqual(mock_print.call_args[0][0],
                         "                       |--    6142ac6e740522bc8814a645   call-work-0   success   2021-09-16 10:31:10   2021-09-16 10:33:11  ")

        mock_list_tasks.side_effect = [mock.MagicMock(task_list=[{'status': 'success', 'account': 'multitest',
                                                                  'task_name': '6142ac31d272fbeabd817466-call-sub_sample',
                                                                  'task_id': '6142ac32810cbfa96114a645',
                                                                  'process': None,
                                                                  'workflow_name': 'subtest',
                                                                  'workflow_id': '5f1a9e3a4090eab68b1da86c',
                                                                  'user': 'admin', 'startTime': 1631759410.2506895,
                                                                  'endTime': 1631759594.1862488, 'type': 'wdl',
                                                                  'workflow_version': 1}]),
                                       mock.MagicMock(task_list=[
                                           {'status': 'success', 'account': 'multitest',
                                            'task_name': '6142ac32810cbfa96114a645-call-sub_sample',
                                            'task_id': '6142ac32f41d86b35814a645', 'process': None,
                                            'workflow_name': 'subtest', 'workflow_id': '5f1a9e3a4090eab68b1da86c',
                                            'user': 'admin', 'startTime': 1631759410.5368168,
                                            'endTime': 1631759591.167847, 'type': 'wdl', 'workflow_version': 1}]),
                                       mock.MagicMock(task_list=[])
                                       ]
        mock_get_jobs.side_effect = [mock.MagicMock(jobs=[
            {'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
             'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2b%2F6142ac6ef042b7001ed6df2b',
             'job_id': '6142ac6ef042b7001ed6df2b', 'task_id': '6142ac32f41d86b35814a645',
             'job_name': '6142ac32f41d86b35814a645-call-work-0', 'startTime': 1631759470.697, 'endTime': 1631759591.114,
             'id': '6142ac6e740522bc8814a645', 'name': 'call-work-0'}]),
            mock.MagicMock(jobs=[{'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
                                  'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2b%2F6142ac6ef042b7001ed6df2b.1631759470.'
                                              '6142ac6e4b72510001327e3b%2Fstdout.log?OSSAccessKeyId=LTAI4GKcuQgcEmF921qrULUf&Expires=1947119584&Signature=sq1UWKme35c%2F1YyPmQxryUhGDUk%3D',
                                  'job_id': '6142ac6e740522bc8814a645', 'task_id': '6142ac32f41d86b35814a645',
                                  'job_name': 'call-work-0',
                                  'full_job_name': '6142ac32f41d86b35814a645-call-work-0',
                                  'startTime': '2021-09-16 10:31:10',
                                  'endTime': '2021-09-16 10:33:11', 'id': '6142ac6e740522bc8814a645',
                                  'name': 'call-work-0'}]),
            mock.MagicMock(jobs=[{'status': 'success', 'job_outputs': [{'name': 'value', 'value': 'i'}],
                                  'log_file': 'http://computer-system-staging-bj.oss-cn-beijing.aliyuncs.com/6142ac6ef042b7001ed6df2a%2F6142ac6ef042b7001ed6df2a.1631759470.'
                                              '6142ac6e4b72510001327e36%2Fstdout.log?OSSAccessKeyId=LTAI4GKcuQgcEmF921qrULUf&Expires=1947119586&Signature=CegnB3ud%2Bk2u33OTZrHQlh2%2Be4I%3D',
                                  'job_id': '6142ac6ef042b7001ed6df2a', 'task_id': '6142ac32810cbfa96114a645',
                                  'job_name': '6142ac32810cbfa96114a645-call-work-0', 'startTime': 1631759470.53,
                                  'endTime': 1631759594.17, 'id': '6142ac6ef41d86b35814a648', 'name': 'call-work-0'}])
        ]

        testargs = ["", "task", "getjobs", "-i", "6142ac31d272fbeabd817466"]
        with mock.patch.object(sys, 'argv', testargs):
            value = {'type': 'wdl'}
            with requests_mock.Mocker() as mock_server:
                mock_server.get(
                    "https://endpoint/accounts/account_name/projects/default/wdl/tasks/6142ac31d272fbeabd817466/",
                    json=value)
                gwc_scripts.main()
        a = str(mock_print.call_args[0][0])
        a = str(mock_print.call_args[0][0])
        self.assertEqual(str(mock_print.call_args[0][0]),
                         "                                                                                                \n"
                         "  job_id                     job_name      status    startTime             endTime              \n"
                         "                                                                                                \n"
                         "  6142ac6ef41d86b35814a648   call-work-0   success   2021-09-16 10:31:10   2021-09-16 10:33:14  \n"
                         "  6142ac6e740522bc8814a645   call-work-0   success   2021-09-16 10:31:10   2021-09-16 10:33:11  \n"
                         "  6142ac6e740522bc8814a645   call-work-0   success   2021-09-16 10:31:10   2021-09-16 10:33:11  \n"
                         "                                                                                                ")


def get_mock_file(content):
    f = TemporaryFile(mode="w+")
    f.write(content)
    f.seek(0)
    return f


if __name__ == '__main__':
    unittest.main()
