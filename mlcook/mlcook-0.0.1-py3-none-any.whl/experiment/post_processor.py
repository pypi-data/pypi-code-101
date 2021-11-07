import numpy as np
import pandas as pd

from .i_experiment import IExperiment
from .utils import Dataset


def optimize_threshold(yy_true: np.array, yy_pred_proba: np.array, precision_target: float) -> float:
    thresholds = np.linspace(0.01, 0.99, 99)
    precisions = {threshold: np.sum(yy_true[yy_pred_proba > threshold]) / np.sum(yy_pred_proba > threshold)
                  for threshold in thresholds if np.sum(yy_pred_proba > threshold) > 0}
    good_thresholds = [threshold for threshold, p in precisions.items() if p >= precision_target]
    optim_threshold = min(good_thresholds) if len(good_thresholds) > 0 else 1.0
    return optim_threshold


class PostProcessor:
    """
    compute thresholds
    """
    def __init__(self, exp: IExperiment):
        self.exp = exp

    def post_process(self):
        if self.exp.thresholds is not None:
            self._get_predictions_with_threshold()
        elif self.exp.precision_target is None:
            pass
        else:
            self._estimate_thresholds(self.exp.valid)
            self._get_predictions_with_threshold()

    def _get_predictions_with_threshold(self):
        self._get_predictions_with_threshold_on(self.exp.train)
        self._get_predictions_with_threshold_on(self.exp.valid)
        if self.exp.test is not None:
            self._get_predictions_with_threshold_on(self.exp.test)

    def _get_predictions_with_threshold_on(self, dataset: Dataset):
        mask_thresholds = np.array(list(map(lambda x: any([x[i] > threshold for i, threshold in
                                                           enumerate(self.exp.thresholds.values())]),
                                            dataset.y_pred_proba)))
        y_pred_with_threshold = dataset.y_pred.copy()
        y_pred_with_threshold[~mask_thresholds] = self.exp.below_threshold_label
        dataset.y_pred_with_threshold = y_pred_with_threshold

    def _estimate_thresholds(self, dataset: Dataset):
        self.exp.thresholds = {}
        for i, label in enumerate(self.exp.labels):
            self.exp.thresholds[label] = optimize_threshold(dataset.y[pd.notnull(dataset.y)] == label,
                                                            dataset.y_pred_proba[pd.notnull(dataset.y), i],
                                                            self.exp.precision_target)
