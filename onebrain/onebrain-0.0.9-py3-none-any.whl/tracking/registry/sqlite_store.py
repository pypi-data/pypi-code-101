import json
import os

from onebrain.tracking import utils
from onebrain.tracking.registry.abstract_store import AbstractStore
from onebrain.tools import env
from onebrain.tools.sqlite_utils import Database, Model

HOSTFILE_PATH = "/home/hostfile.json"
DB_PATH = "/workspace/metrics"


class SqliteStore(AbstractStore):

    def __init__(self, get_host_creds):
        super().__init__()
        self.get_host_creds = get_host_creds
        self._init_db()

    def _init_db(self):
        self._check_folder()
        pod_name = self._load_from_hostfile()
        if pod_name:
            self.pod_name = pod_name
            database = f'{DB_PATH}/{pod_name}.metric'
            self.db = Database(database=database, check_same_thread=False, timeout=600)
            LOG_METRIC.db = self.db

    def _load_from_hostfile(self):
        if not os.path.exists(HOSTFILE_PATH):
            print("can't find hostfile.json")
        own_ip = env.get_env(utils.TRACKING_OWN_IP_ADDRESS)
        with open(HOSTFILE_PATH, 'r') as f:
            load_dict = json.load(f)
            for item in load_dict:
                if own_ip == item['ip']:
                    if "master" == item['role']:
                        return item['group']
                    else:
                        return item['group'] + '_' + str(item['index'])

    def _check_folder(self):
        if not os.path.exists(DB_PATH):
            parent_file = os.path.abspath(DB_PATH)
            os.makedirs(parent_file, exist_ok=True)

    def log_metric(self, run_id, metric):
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: Metric instance to log
        """
        if not self.db:
            return

        self._check_folder()

        run_id = run_id if run_id is not None else env.get_env(utils.ONEBRAIN_RUN_ID)
        logMetric = LOG_METRIC(run_id=run_id,
                               node_name=env.get_env(utils.TRACKING_NODE_ENV_VAR),
                               pod_name=self.pod_name,
                               metric_key=metric.key,
                               metric_value=float(metric.value),
                               ts=metric.timestamp,
                               step=metric.step)
        logMetric.save()
        self.db.commit()


class LOG_METRIC(Model):
    run_id = str
    node_name = str
    pod_name = str
    metric_key = str
    metric_value = float
    ts = int
    step = int

    def __init__(self, run_id=None, node_name=None, pod_name=None, metric_key=None, metric_value=None, ts=None,
                 step=None) -> None:
        self.run_id = run_id
        self.node_name = node_name
        self.pod_name = pod_name
        self.metric_key = metric_key
        self.metric_value = metric_value
        self.ts = ts
        self.step = step
