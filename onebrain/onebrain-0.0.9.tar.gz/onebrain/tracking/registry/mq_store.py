import json

from rocketmq.client import Producer, Message, SendStatus

from onebrain.exceptions import OnebrainException
from onebrain.tracking import utils
from onebrain.tracking.registry.abstract_store import AbstractStore
from onebrain.tools import env

METRIC_MQ_PRODUCER = "onebrain-metric-producer"
METRIC_MQ_TOPIC = "onebrain-metric"
METRIC_MQ_TAG = "by-sdk"


class MqStore(AbstractStore):

    def __init__(self, get_host_creds):
        super().__init__()
        self.get_host_creds = get_host_creds
        host_creds = self.get_host_creds()

        producer = Producer(METRIC_MQ_PRODUCER)
        producer.set_name_server_address(host_creds.host)
        self.producer = producer
        self.producer.start()

    def __del__(self):
        if self.producer:
            self.producer.shutdown()

    def _publish_to_mq(self, msg_body):
        msg = Message(METRIC_MQ_TOPIC)
        msg.set_tags(METRIC_MQ_TAG)
        msg.set_body(json.dumps(msg_body))
        ret = self.producer.send_sync(msg)
        if ret and ret.status == SendStatus.OK:
            return
        else:
            print("failed to pushlish metic message to rocketmq")

    def log_metric(self, run_id, metric):
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: Metric instance to log
        """
        msg = {
            'run_id': run_id,
            'node': env.get_env(utils.TRACKING_NODE_ENV_VAR),
            'pod': env.get_env(utils.TRACKING_POD_ENV_VAR),
            'key': metric.key,
            'value': metric.value,
            'timestamp': metric.timestamp,
            'step': metric.step,
        }
        self._publish_to_mq(msg)