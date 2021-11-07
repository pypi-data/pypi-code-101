import pandas as pd

from .i_experiment import IExperiment
from .utils import Dataset

class Preprocessor:

    def __init__(self, exp: IExperiment):
        self.exp = exp # vraiment besoin ? on pourrait mettre en paramètre de preprocess ce serait suffisant ?

    def preprocess(self):
        # train
        self.preprocess_dataset(self.exp.train)
        self.preprocess_dataset(self.exp.valid)
        if self.exp.test is not None:
            self.preprocess_dataset(self.exp.test)

    def preprocess_dataset(self, dataset: Dataset):
        X_preprocessed = dataset.X[self.exp.cat_features + self.exp.num_features].copy()
        X_preprocessed[self.exp.cat_features] = X_preprocessed[self.exp.cat_features].fillna(self.exp.fillna_value_cat)
        X_preprocessed[self.exp.num_features] = X_preprocessed[self.exp.num_features].fillna(self.exp.fillna_value_num)
        dataset.X_preprocessed = X_preprocessed
