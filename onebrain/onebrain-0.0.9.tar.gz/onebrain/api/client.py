import traceback

from onebrain.tracking import utils
from onebrain.tracking.client import TrackingServiceClient

# _DEFAULT_STORE_TYPE = "rest"


class OnebrainClient(object):

    def __init__(self):
        final_tracking_uri = utils._resolve_tracking_uri()
        self._tracking_client = TrackingServiceClient(final_tracking_uri)

    def log_metric(self, key, value, run_id=None, timestamp=None, step=None):
        try:
            self._tracking_client.log_metric(run_id, key, value, timestamp, step)
        except Exception:
            print("Error: failed to report metric to platform")
            traceback.print_exc()