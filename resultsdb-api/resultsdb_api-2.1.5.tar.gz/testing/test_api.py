# Copyright 2014, Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors:
#   Martin Krizek <mkrizek@redhat.com>

import resultsdb_api

import json

import pytest
import requests
from unittest.mock import patch


class TestAPI():
    def setup_method(self, method):
        self.rdb_url = "http://0.0.0.0:5000/api/v1.0"
        self.ref_url = "http://example.com/someref"
        self.ref_status = "SCHEDULED"
        self.ref_testcase_name = "testcase"
        self.ref_testcase_url = "http://fedoraqa.fedoraproject.org/testcase"
        self.ref_outcome = "PASSED"
        self.ref_content_type = "application/json"
        self.ref_accept = "text/plain"
        self.ref_job_id = 1
        self.ref_result_id = 1

        self.helper = resultsdb_api.ResultsDBapi(self.rdb_url)

    @patch('requests.Session.send')
    def test_create_testcase(self, mocksend):
        auth = resultsdb_api.ResultsDBAuth.basic_auth("user", "pass")
        authhelper = resultsdb_api.ResultsDBapi(self.rdb_url, request_auth=auth)

        # test twice to test authentication, once without, once with
        for (helper, authed) in ((self.helper, False), (authhelper, True)):
            mocksend.reset_mock()
            helper.create_testcase(self.ref_testcase_name, self.ref_testcase_url)
            mocksend.assert_called_once()
            request = mocksend.mock_calls[0][1][0]
            data = json.loads(request.body)

            assert request.url == "%s/testcases" % self.rdb_url
            assert request.headers['Content-type'] == self.ref_content_type
            assert request.headers['Accept'] == self.ref_accept
            if authed:
                assert request.headers['Authorization'] == "Basic dXNlcjpwYXNz"
            else:
                assert 'Authorization' not in request.headers
            assert data['ref_url'] == self.ref_testcase_url
            assert data['name'] == self.ref_testcase_name

    @patch('requests.Session.send')
    def test_update_testcase(self, mocksend):
        self.helper.update_testcase(self.ref_testcase_name, self.ref_testcase_url)

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]
        data = json.loads(request.body)

        assert request.url == "%s/testcases" % (self.rdb_url)
        assert request.headers['Content-type'] == self.ref_content_type
        assert request.headers['Accept'] == self.ref_accept
        assert data['ref_url'] == self.ref_testcase_url
        assert data['name'] == self.ref_testcase_name

    @patch('requests.Session.send')
    def test_get_testcase(self, mocksend):
        self.helper.get_testcase(self.ref_testcase_name)

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]

        assert request.url == "%s/testcases/%s" % (self.rdb_url, self.ref_testcase_name)

    @patch('requests.Session.send')
    def test_get_testcases(self, mocksend):
        self.helper.get_testcases()

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]

        assert request.url == "%s/testcases" % self.rdb_url

    @patch('requests.Session.send')
    def test_create_result(self, mocksend):
        self.helper.create_result(self.ref_outcome, self.ref_testcase_name)

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]
        data = json.loads(request.body)

        assert request.url == "%s/results" % self.rdb_url
        assert request.headers['Content-type'] == self.ref_content_type
        assert request.headers['Accept'] == self.ref_accept
        assert data['testcase'] == self.ref_testcase_name
        assert data['outcome'] == self.ref_outcome

    @patch('requests.Session.send')
    def test_get_result(self, mocksend):
        self.helper.get_result(self.ref_result_id)

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]

        assert request.url == "%s/results/%s" % (self.rdb_url, self.ref_job_id)

    def test_get_result_invalid(self):
        with pytest.raises(TypeError):
            self.helper.get_result()

    @patch('requests.Session.send')
    def test_get_results(self, mocksend):
        self.helper.get_results()

        mocksend.assert_called_once()
        request = mocksend.mock_calls[0][1][0]

        assert request.url == "%s/results" % self.rdb_url

    @patch('requests.Session.request')
    def test_get_results_params(self, mockreq):
        self.helper.get_results(testcase_name=self.ref_testcase_name, job_id=self.ref_job_id)

        mockreq.assert_called_once()
        rdb_url = mockreq.mock_calls[0][1][1]
        params = mockreq.mock_calls[0][2]['params']

        assert rdb_url == "%s/results" % self.rdb_url
        assert params['testcase_name'] == self.ref_testcase_name
        assert params['job_id'] == str(self.ref_job_id)
