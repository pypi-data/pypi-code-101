import logging
import time

from onebrain.entities import Metric
from onebrain.tracking import utils
from onebrain.tracking.validation import _validate_metric

_logger = logging.getLogger(__name__)


class TrackingServiceClient(object):

    def __init__(self, tracking_uri, store_type=None):
        self.tracking_uri = tracking_uri
        self.store_type = utils._resolve_store_type(store_type=store_type)
        self.store = utils._get_store(store_uri=self.tracking_uri, store_type=self.store_type)

    def log_metric(self, run_id, key, value, timestamp, step):
        timestamp = timestamp if timestamp is not None else int(time.time() * 1000)
        step = step if step is not None else 0
        valid = _validate_metric(key, value, timestamp, step)
        if not valid:
            return
        metric = Metric(key, value, timestamp, step)
        self.store.log_metric(run_id, metric)