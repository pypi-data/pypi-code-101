import tempfile
from pathlib import Path

import mlflow

from mlflow_utils.file_handler import HANDLER_MAPPING


def convert_to_valid_tracking_uri(mlflow_dir):
    """
    Converts from a windows path like 'C:/example/mlflow' to a valid mlflow tracking uri.
    """
    mlflow_dir = Path(mlflow_dir)
    tracking_uri = f"file:///{(mlflow_dir / 'mlruns').as_posix()}"
    return tracking_uri


def init_mlflow(tracking_uri_path, experiment):
    mlflow.set_tracking_uri(convert_to_valid_tracking_uri(tracking_uri_path))
    mlflow.set_experiment(experiment)


class MlflowUtils:
    DRIVE = "C"

    def __init__(self, run_id=None, experiment=None):
        self.experiment = experiment
        self.run_id = run_id

        self._active_run = self._get_active_run()
        self._active_exp = self._get_active_experiment()

        self._relevant_run_id = None
        self._relevant_run_obj = None
        self._relevant_exp = None

        self._get_relevant_run()
        self._get_relevant_exp()

    def has_active_run(self):
        if self._get_active_run() is None:
            return False
        return True

    def _get_active_run(self):
        return mlflow.active_run()

    def _get_active_experiment(self):
        if self.has_active_run():
            return mlflow.get_experiment(self._active_run.info.experiment_id).name
        return None

    def _set_experiment(self, experiment):
        if experiment is not None:
            mlflow.set_experiment(experiment)

    def _get_relevant_run(self):
        self._relevant_run_id = self.run_id if self.run_id is not None else self._active_run
        self._relevant_run_obj = mlflow.get_run(self.run_id) if self.run_id is not None else mlflow.active_run()

    def _get_relevant_exp(self):
        self._relevant_exp = self.experiment if self.experiment is not None else self._active_exp

    def get_artifact_path(self):
        r = Path(f"{self.DRIVE}:/" + self._relevant_run_obj.info.artifact_uri.split(":")[2])
        self._exit()
        return r

    @staticmethod
    def _get_file_kind(fn):
        kind = fn.split(".")[1]
        return kind

    @staticmethod
    def _check_file_kind(kind):
        if kind not in HANDLER_MAPPING.keys():
            raise NotImplementedError(f"File handler for kind '{kind}' not implemented.")

    def _exit(self):
        self._set_experiment(self._active_exp)

    def log_file(self, file, fn):
        kind = self._get_file_kind(fn)
        self._check_file_kind(kind)

        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdirname_path = Path(tmpdirname)
            fp = tmpdirname_path / fn

            handler = HANDLER_MAPPING[kind]()
            handler.save(data=file, fp=fp)

            mlflow.log_artifact((tmpdirname_path / fn).as_posix())

        self._exit()

    def load_file(self, fn):
        self._set_experiment(self._relevant_exp)
        artifact_path = self.get_artifact_path()
        fp = artifact_path / fn

        kind = self._get_file_kind(fn)
        self._check_file_kind(kind)

        handler = HANDLER_MAPPING[kind]()
        file = handler.load(fp=fp)

        self._exit()

        return file


def log_file(file, fn):
    MlflowUtils().log_file(file, fn)


def load_file(fn, run_id=None, experiment=None):
    return MlflowUtils(run_id=run_id, experiment=experiment).load_file(fn)


def artifact_path(run_id=None, experiment=None):
    return MlflowUtils(run_id=run_id, experiment=experiment).get_artifact_path()
