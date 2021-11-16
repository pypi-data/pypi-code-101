import logging

from mlflow_utils.mlflow_utils import MlflowUtils

DEFAULT_LEVEL = "DEBUG"
format_ = "%(levelname)s %(asctime)s - %(message)s"


def setup_logger(level):
    if not MlflowUtils().has_active_run():
        return base_logger(level)

    # Create new logger
    formatter = logging.Formatter(format_)

    log = logging.getLogger()
    file_handler = logging.FileHandler(MlflowUtils().get_artifact_path() / "debug.log", "w+")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # remove all old handlers
    for hdlr in log.handlers[:]:
        log.removeHandler(hdlr)

    log.addHandler(file_handler)
    log.addHandler(stream_handler)
    log.setLevel(level)

    return log


def base_logger(level=DEFAULT_LEVEL):
    logging.basicConfig(format=format_)
    log = logging.getLogger("root")
    log.setLevel(level)
    return log
