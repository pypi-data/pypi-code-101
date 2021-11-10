import json
from enum import Enum

import requests

from onebrain.tracking import utils
from onebrain.tracking.registry.abstract_store import AbstractStore
from onebrain.tools import env

API_PREFIX = "/metric/collect"


class RestStoreApi(Enum):
    LOG_METRIC = "log_metric"


class RestStore(AbstractStore):

    def __init__(self, get_host_creds):
        super().__init__()
        self.get_host_creds = get_host_creds

    def _call_endpoint(self, api, json_body):
        host_creds = self.get_host_creds()
        url = host_creds.host + API_PREFIX + "/" + api.value
        payload = json_body
        headers = {
            'X-Token': host_creds.token
        }
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code == 200:
            resp_msg = json.loads(r.content)
            if resp_msg and 'status' in resp_msg and resp_msg['status'] == 200:
                return
            else:
                if 'httpCode' in resp_msg:
                    err_code = resp_msg['httpCode']
                else:
                    err_code = resp_msg['status']
                print("server response: %s, please check it" % err_code)
        else:
            if r.status_code == 500:
                print("exception has happened on server")
            elif r.status_code == 404:
                print("server can not be connected")

    def log_metric(self, run_id, metric):
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: Metric instance to log
        """
        req_body = {
            'run_id': run_id,
            'node': env.get_env(utils.TRACKING_NODE_ENV_VAR),
            'pod': env.get_env(utils.ONEBRAIN_TRACKING_POD),
            'key': metric.key,
            'value': metric.value,
            'timestamp': metric.timestamp,
            'step': metric.step,
        }
        self._call_endpoint(RestStoreApi.LOG_METRIC, req_body)