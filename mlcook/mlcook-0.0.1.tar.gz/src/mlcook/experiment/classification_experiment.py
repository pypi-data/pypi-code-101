import pandas as pd
import numpy as np
import logging

from .stat_utils import get_stat_by_group


from .i_experiment import IExperiment
from ..model.classifier import IClassifier
from .utils import Dataset

from .preprocessor import Preprocessor
from .trainer import Trainer
from .predictor import Predictor
from .post_processor import PostProcessor
from .evaluator import Evaluator
from .explainer import Explainer

# from .drift_analyzer import DriftAnalyzer


class ClassificationExperiment(IExperiment):

    def __init__(self,
                 clf: IClassifier, # vraiment bien de mettre la parent class here ?
                 train_data: pd.DataFrame,
                 valid_data: pd.DataFrame,
                 target: str,
                 num_features: list,
                 cat_features: list,
                 #text_features: list = None, # not supported for the moment
                 test_data: pd.DataFrame = None,
                 thresholds: dict = None,
                 precision_target: float = None,
                 random_seed: int = None,
                 labels=None,
                 sample_weight_train: np.array = None,
                 sample_weight_valid: np.array = None,
                 sample_weight_test: np.array = None,
                 verbose=None,
                 fillna_value_cat='NULL',
                 fillna_value_num=-10,
                 ):

        self.clf = clf
        self.train = Dataset(X=train_data[[col for col in train_data.columns if col != target]],
                             y=train_data[target].values,
                             weight=sample_weight_train)
        self.valid = Dataset(X=valid_data[[col for col in valid_data.columns if col != target]],
                             y=valid_data[target].values,
                             weight=sample_weight_valid)
        if test_data is None:
            self.test = None
        else:
            self.test = Dataset(X=test_data[[col for col in test_data.columns if col != target]],
                                y=test_data[target].values if target in test_data.columns else None,
                                weight=sample_weight_test)
        self.target = target
        self.num_features = num_features
        self.cat_features = cat_features
        self.random_seed = random_seed
        self.thresholds = thresholds
        self.precision_target = precision_target
        self.labels = labels if labels is not None else train_data[target].dropna().unique().tolist()
        self.verbose = verbose
        self.fillna_value_cat = fillna_value_cat
        self.fillna_value_num = fillna_value_num
        self.below_threshold_label = 'NSP'

        self.metrics = None
        self.confusion_matrices = None
        self.confusion_matrices_with_threshold = None

    def make(self):
        preprocessor = Preprocessor(self)
        preprocessor.preprocess()
        self.clf.build(random_seed=self.random_seed,
                       labels=self.labels,
                       verbose=self.verbose,
                       cat_features=self.cat_features)
        trainer = Trainer(self)
        trainer.train()
        predictor = Predictor(self)
        predictor.predict()
        post_processor = PostProcessor(self)
        post_processor.post_process()
        self.evaluator = Evaluator(self)
        self.evaluator.evaluate()
        explainer = Explainer(self)
        explainer.explain() # TODO

        #self._get_proba_distributions()
        #self._get_variable_importance()

    def save(self, filename):
        pass

    def load(self, filename):
        pass

    def get_metrics_by(self, by: str, dataset_name: str):
        return self.evaluator.get_metrics_by(by, self.__dict__[dataset_name])

    def get_ground_truth_distribution_by(self, by, dataset_name):
        dataset = self.__dict__[dataset_name]
        by_values = dataset.X[by].fillna(self.fillna_value_cat).values
        if pd.isnull(dataset.y).sum() > 0:
            logging.info('Warning: presence of missing values in the target. They are excluded from this computations')
        return get_stat_by_group(by_values=by_values[pd.notnull(dataset.y)],
                                       feature_values=dataset.y[pd.notnull(dataset.y)],
                                       feature_labels=self.labels)

    def get_prediction_distribution_by(self, by, dataset_name):
        dataset = self.__dict__[dataset_name]
        return get_stat_by_group(by_values=dataset.X[by].fillna(self.fillna_value_cat),
                                       feature_values=dataset.y_pred,
                                       feature_labels=self.labels
                                       )

    def get_bootstrap_intervals(self, n_iter, inf = 0.025, sup = 0.975):
        bootstrap_proba_train = np.zeros((self.train.X_preprocessed.shape[0], len(self.labels), n_iter))
        bootstrap_proba_valid = np.zeros((self.valid.X_preprocessed.shape[0], len(self.labels), n_iter))
        if self.test is not None:
            bootstrap_proba_test = np.zeros((self.test.X_preprocessed.shape[0], len(self.labels), n_iter))
        for i in range(n_iter):
            print(i)
            bootstrap_ix = np.random.randint(self.train.X_p.shape[0], size=self.train.X_p.shape[0])
            clf = self.clf.build_copy(random_seed=self.random_seed, labels=self.labels,
                                      verbose=0, cat_features=self.cat_features)
            X_train_bootstrap = self.train.X_p.iloc[bootstrap_ix].copy()
            y_train_bootstrap = self.train.y_p[bootstrap_ix].copy()
            sample_weight_train_bootstrap = self.train.weight_p[bootstrap_ix] if self.train.weight_p is not None else None
            clf.fit(X_train=X_train_bootstrap,
                    y_train=y_train_bootstrap,
                    X_valid=self.valid.X_p,
                    y_valid=self.valid.y_p,
                    sample_weight_train=sample_weight_train_bootstrap,
                    sample_weight_valid=self.valid.weight_p,)
            bootstrap_proba_train[:, :, i] = clf.predict_proba(self.train.X_preprocessed)
            bootstrap_proba_valid[:, :, i] = clf.predict_proba(self.valid.X_preprocessed)
            if self.test is not None:
                bootstrap_proba_test[:, :, i] = clf.predict_proba(self.test.X_preprocessed)
        # for the moment save this just for the test
        self.train.bootstrap_proba = bootstrap_proba_train
        self.valid.bootstrap_proba = bootstrap_proba_valid
        if self.test is not None:
            self.test.bootstrap_proba = bootstrap_proba_test
        self.train.proba_confidence_intervals = np.quantile(bootstrap_proba_train, q=[inf, sup], axis=2).transpose(1, 2, 0)
        self.valid.proba_confidence_intervals = np.quantile(bootstrap_proba_valid, q=[inf, sup], axis=2).transpose(1, 2, 0)
        if self.test is not None:
            self.test.proba_confidence_intervals = np.quantile(bootstrap_proba_test, q=[inf, sup], axis=2).transpose(1, 2, 0)


    def _get_proba_distributions(self):
        pass

    def _get_variable_importance(self):
        pass

    def generate_report(self):
        "idea is to generate of report with all interesting things automatically"
        pass
