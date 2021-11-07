import pandas as pd
from .i_experiment import IExperiment


class Trainer:
    """
    hyperparameter optim, multiple models.., bootstrap
    """

    def __init__(self, exp: IExperiment):
        self.exp = exp  # vraiment besoin ? on pourrait mettre en paramètre de train ce serait suffisant..

    def train(self):
        self.exp.train.X_p, self.exp.train.y_p, self.exp.train.weight_p = \
            self._filter_missing_target(self.exp.train.X_preprocessed, self.exp.train.y, self.exp.train.weight)

        self.exp.valid.X_p, self.exp.valid.y_p, self.exp.valid.weight_p = \
            self._filter_missing_target(self.exp.valid.X_preprocessed, self.exp.valid.y, self.exp.valid.weight)

        self.exp.clf.fit(X_train=self.exp.train.X_p,
                         y_train=self.exp.train.y_p,
                         X_valid=self.exp.valid.X_p,
                         y_valid=self.exp.valid.y_p,
                         sample_weight_train=self.exp.train.weight_p,
                         sample_weight_valid=self.exp.valid.weight_p,
                         )

    def _filter_missing_target(self, X, y, weight):
        weight_p = weight[pd.notnull(y)] if weight is not None else None
        return X.loc[pd.notnull(y)], y[pd.notnull(y)], weight_p
