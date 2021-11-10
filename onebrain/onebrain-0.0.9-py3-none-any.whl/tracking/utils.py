import os
import platform
import sys

from onebrain.exceptions import OnebrainException
from onebrain.tools import *

# 有几种方法可以获得tracking_uri
# 1.可以在这里写死
_tracking_uri = None

# 2.通过环境变量设置
TRACKING_URI_ENV_VAR = "ONEBRAIN_TRACKING_URI"
TRACKING_ROCKETMQ_ENV_VAR = "ONEBRAIN_ROCKETMQ_URI"

# 3.通过挂载文件
DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH = "./onebrain_runs"

TRACKING_USERNAME_ENV_VAR = "ONEBRAIN_TRACKING_USERNAME"
TRACKING_PASSWORD_ENV_VAR = "ONEBRAIN_TRACKING_PASSWORD"
TRACKING_TOKEN_ENV_VAR = "ONEBRAIN_TRACKING_TOKEN"
TRACKING_INSECURE_TLS_ENV_VAR = "ONEBRAIN_TRACKING_INSECURE_TLS"

TRACKING_NODE_ENV_VAR = "ONEBRAIN_TRACKING_NODE"
ONEBRAIN_TRACKING_POD = "ONEBRAIN_TRACKING_POD"
TRACKING_OWN_IP_ADDRESS = "OWN_IP_ADDRESS"

ONEBRAIN_RUN_ID = "RUN_ID"


def _resolve_tracking_uri(tracking_uri=None):
    return tracking_uri or get_tracking_uri()


def get_tracking_uri():
    global _tracking_uri
    if _tracking_uri is not None:
        return _tracking_uri
    elif env.get_env(TRACKING_ROCKETMQ_ENV_VAR) is not None:
        return env.get_env(TRACKING_ROCKETMQ_ENV_VAR)
    elif env.get_env(TRACKING_URI_ENV_VAR) is not None:
        return env.get_env(TRACKING_URI_ENV_VAR)
    else:
        return file_utils.path_to_local_file_uri(os.path.abspath(DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH))


def _resolve_store_type(store_type):
    return store_type or get_store_type()


def get_store_type():
    # rocketmq client only support linux so far
    if is_on_linux() and env.get_env(TRACKING_ROCKETMQ_ENV_VAR) is not None:
        return "mq"
    elif env.get_env(TRACKING_URI_ENV_VAR) is not None:
        return "rest"
    else:
        return "embedded"


def _get_store(store_uri=None, store_type=None):
    store_uri = _resolve_tracking_uri(store_uri)

    def get_default_host_creds():
        return rest_utils.OneflowHostCreds(
            host=store_uri,
            username=os.environ.get(TRACKING_USERNAME_ENV_VAR),
            password=os.environ.get(TRACKING_PASSWORD_ENV_VAR),
            token=os.environ.get(TRACKING_TOKEN_ENV_VAR),
            ignore_tls_verification=os.environ.get(TRACKING_INSECURE_TLS_ENV_VAR) == "true",
        )
    if store_type == "mq":
        from onebrain.tracking.registry.mq_store import MqStore
        return MqStore(get_host_creds=get_default_host_creds)
    elif store_type == "rest":
        from onebrain.tracking.registry.rest_store import RestStore
        return RestStore(get_host_creds=get_default_host_creds)
    elif store_type == "embedded":
        from onebrain.tracking.registry.sqlite_store import SqliteStore
        return SqliteStore(get_host_creds=get_default_host_creds)
    else:
        raise OnebrainException("no store can use")


def is_on_linux():
    return platform.system() == "Linux"