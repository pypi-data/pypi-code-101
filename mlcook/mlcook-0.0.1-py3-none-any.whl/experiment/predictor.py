from .i_experiment import IExperiment
from .utils import Dataset


class Predictor:
    def __init__(self, exp: IExperiment):
        self.exp = exp

    def predict(self):
        self._predict_on(self.exp.train)
        self._predict_on(self.exp.valid)
        if self.exp.test is not None:
            self._predict_on(self.exp.test)

    def _predict_on(self, dataset: Dataset):
        dataset.y_pred = self.exp.clf.predict(dataset.X_preprocessed)
        dataset.y_pred_proba = self.exp.clf.predict_proba(dataset.X_preprocessed)
