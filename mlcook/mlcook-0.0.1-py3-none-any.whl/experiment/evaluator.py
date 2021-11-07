import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix

from .stat_utils import chi2_test

from .i_experiment import IExperiment
from .utils import Dataset


def compute_metrics(y_true: np.array, y_pred: np.array, y_pred_with_threshold: np.array):
    # TODO : there are some specific notations here
    metrics = {}
    if pd.notnull(y_true).sum() > 0:
        metrics['accuracy'] = accuracy_score(y_true[pd.notnull(y_true)], y_pred[pd.notnull(y_true)])
    else:
        metrics['accuracy'] = None

    if y_pred_with_threshold is not None:
        mask_thresholds = y_pred_with_threshold != 'NSP'
        metrics['below_threshold_rate'] = 1 - np.mean(mask_thresholds)
        metrics['above_threshold_rate'] = np.mean(mask_thresholds)
        metrics['automation_rate'] = np.mean((y_pred_with_threshold == 'acceptation_manuelle') |
                                             (y_pred_with_threshold == 'refus_GM'))
        if np.sum(mask_thresholds & pd.notnull(y_true)) > 0:
            metrics['accuracy_above_threshold'] = accuracy_score(y_pred[mask_thresholds & pd.notnull(y_true)],
                                                                 y_true[mask_thresholds & pd.notnull(y_true)])
        else:
            metrics['accuracy_above_threshold'] = None

    return metrics


def compute_confusion_matrix(y_true: np.array, y_pred: np.array, labels: list, percentage: bool):
    # temporary fix : keep only labels that appear only once in y_true or y_pred
    labels = [label for label in labels if label in np.concatenate([y_true, y_pred])]
    conf_mat = pd.DataFrame(confusion_matrix(y_pred, y_true), index=labels, columns=labels, )
    total_pred = conf_mat.sum(axis=1)
    total_ground_truth = conf_mat.sum(axis=0)
    total_ground_truth.loc['total'] = total_pred.sum()
    if percentage:
        conf_mat = (conf_mat.T / total_pred).T.round(2)
    conf_mat["total"] = total_pred
    conf_mat.loc["total"] = total_ground_truth
    return conf_mat


class Evaluator:
    def __init__(self, exp: IExperiment):
        self.exp = exp

    def evaluate(self):
        # default is to evaluate metrics by dataset
        self._get_metrics()
        self._get_confusion_matrices()

    def _get_metrics(self):
        self._get_metrics_on(self.exp.train)
        self._get_metrics_on(self.exp.valid)
        if self.exp.test is not None:
            self._get_metrics_on(self.exp.test)

    @staticmethod
    def _get_metrics_on(dataset: Dataset):
        dataset.metrics = compute_metrics(dataset.y, dataset.y_pred, dataset.y_pred_with_threshold)

    def get_metrics_by(self, by, dataset: Dataset):
        # TODO : handle case where by is not categorical
        # be careful to missing values here
        metrics_by = {}
        by_values = dataset.X[by].fillna(self.exp.fillna_value_cat)
        for value in by_values.unique():
            metrics_by[value] = {}
            metrics_by[value]['count'] = (by_values == value).sum()
            y_pred_with_threshold = dataset.y_pred_with_threshold[by_values == value] \
                if dataset.y_pred_with_threshold is not None else None
            metrics_by[value]['metrics'] = compute_metrics(
                y_true=dataset.y[by_values == value],
                y_pred=dataset.y_pred[by_values == value],
                y_pred_with_threshold=y_pred_with_threshold, )

        chi2 = chi2_test(by_values[pd.notnull(dataset.y)],
                         dataset.y[pd.notnull(dataset.y)] == dataset.y_pred[pd.notnull(dataset.y)])
        return {'metrics_by': metrics_by,
                'chi2_test_based_on_accuracy': chi2}

    def _get_confusion_matrices(self):
        self._get_confusion_matrices_on(self.exp.train)
        self._get_confusion_matrices_on(self.exp.valid)
        if self.exp.test is not None:
            self._get_confusion_matrices_on(self.exp.test)

    def _get_confusion_matrices_on(self, dataset: Dataset):
        confusion_matrices = {}
        confusion_matrices['count'] = compute_confusion_matrix(dataset.y[pd.notnull(dataset.y)],
                                                               dataset.y_pred[pd.notnull(dataset.y)],
                                                               labels=self.exp.labels,
                                                               percentage=False)
        confusion_matrices['percentage'] = compute_confusion_matrix(dataset.y[pd.notnull(dataset.y)],
                                                                    dataset.y_pred[pd.notnull(dataset.y)],
                                                                    labels=self.exp.labels,
                                                                    percentage=True)

        if dataset.y_pred_with_threshold is not None:
            confusion_matrices['count_with_threshold'] = \
                compute_confusion_matrix(dataset.y[pd.notnull(dataset.y) & (dataset.y_pred_with_threshold !=
                                                                            self.exp.below_threshold_label)],
                                         dataset.y_pred[pd.notnull(dataset.y) & (dataset.y_pred_with_threshold !=
                                                                                 self.exp.below_threshold_label)],
                                         labels=self.exp.labels,
                                         percentage=False)
            confusion_matrices['percentage_with_threshold'] = \
                compute_confusion_matrix(dataset.y[pd.notnull(dataset.y) & (dataset.y_pred_with_threshold !=
                                                                            self.exp.below_threshold_label)],
                                         dataset.y_pred[pd.notnull(dataset.y) & (dataset.y_pred_with_threshold !=
                                                                                 self.exp.below_threshold_label)],
                                         labels=self.exp.labels,
                                         percentage=True)

        dataset.confusion_matrices = confusion_matrices
