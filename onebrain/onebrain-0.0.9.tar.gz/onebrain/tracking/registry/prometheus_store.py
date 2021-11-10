import requests
from prometheus_client import CollectorRegistry, Gauge, generate_latest

from onebrain.exceptions import OnebrainException
from onebrain.tracking.registry.abstract_store import AbstractStore
import onebrain.tools.env as env
import onebrain.tracking.utils as utils

API_PREFIX = "/metrics/job"
GAUGE_LABELS = ['run_id', 'node', 'pod', 'step', 'timestamp']


class PrometheusStore(AbstractStore):

    def __init__(self, get_host_creds):
        super().__init__()
        self.get_host_creds = get_host_creds
        self.registry = CollectorRegistry()
        self.customized_metrics = {}

    def _push_metric_to_gateway(self, job_name):
        host_creds = self.get_host_creds()
        url = host_creds.host + API_PREFIX + "/" + job_name
        r = requests.post(url, data=generate_latest(self.registry))
        if r.status_code != 200:
            print("can't post to prometheus pushgateway, please check your configuration")

    def log_metric(self, run_id, metric):
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: Metric instance to log
        """
        if metric.key in self.customized_metrics.keys():
            gauge = self.customized_metrics[metric.key]
        else:
            gauge = Gauge(metric.key, 'gauge metric by push-gateway', GAUGE_LABELS, registry=self.registry)

        gauge.labels(
            run_id,
            env.get_env(utils.TRACKING_NODE_ENV_VAR),
            env.get_env(utils.TRACKING_POD_ENV_VAR),
            metric.step,
            metric.timestamp,
        ).set(metric.value)

        self._push_metric_to_gateway(metric.key)