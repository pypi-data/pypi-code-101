import pandas as pd
import numpy as np


# une data classe ?
class Dataset:
    def __init__(self, X: pd.DataFrame,
                 y: np.array = None,
                 weight: np.array = None,
                 y_pred: np.array = None,
                 y_pred_with_threshold: np.array = None,
                 y_pred_proba: np.array = None,
                 X_preprocessed: pd.DataFrame = None,
                 X_p: pd.DataFrame = None, # after preprocessing (e.g. data with no target is filtered)
                 y_p: np.array = None,
                 weight_p: np.array = None,
                 metrics: dict = None,
                 confusion_matrices: dict = None,
                 bootstrap_proba: np.array = None,
                 proba_confidence_intervals: np.array = None,
                 # shap_values = None #np.array pd.DataFrame ?
                 ):
        self.X = X
        self.y = y
        self.weight = weight
        self.y_pred = y_pred
        self.y_pred_with_threshold = y_pred_with_threshold
        self.y_pred_proba = y_pred_proba
        self.X_preprocessed = X_preprocessed
        self.X_p = X_p
        self.y_p = y_p
        self.weight_p = weight_p
        self.metrics = metrics
        self.confusion_matrices = confusion_matrices
        self.bootstrap_proba = bootstrap_proba
        self.proba_confidence_intervals = proba_confidence_intervals
