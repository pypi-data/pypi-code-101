import pandas as pd
import numpy as np

from catboost import Pool, cv, CatBoostClassifier

from sklearn.metrics import accuracy_score, confusion_matrix
from scipy.stats import ttest_ind_from_stats, chi2_contingency


class ClassificationExperiment:

    def __init__(self, train_data: pd.DataFrame,
                 valid_data: pd.DataFrame,
                 target: str,
                 num_features: list,
                 cat_features: list,
                 max_depth: int,
                 one_hot_max_size: int,
                 test_data: pd.DataFrame = None,
                 thresholds: dict = None,
                 random_seed: int = None,
                 precision_target: float = None,
                 labels=None):
        self.dataset = {'train': train_data,
                        'valid': valid_data,
                        'test': test_data}
        self.target = target
        self.num_features = num_features
        self.cat_features = cat_features
        self.max_depth = max_depth
        self.one_hot_max_size = one_hot_max_size
        self.thresholds = thresholds
        self.random_seed = random_seed
        self.precision_target = precision_target
        self.labels = labels if labels is not None else train_data[target].dropna().unique().tolist()
        self.clf = None
        self.y_pred = None
        self.y_pred_with_threshold = None
        self.y_pred_proba = None
        self.metrics = None
        self.confusion_matrices = None
        self.confusion_matrices_with_threshold = None

        assert self.thresholds is not None or self.precision_target is not None

    def make(self):
        self._train()
        self._get_all_predictions()
        self._get_thresholds()
        self._get_all_predictions_with_threshold()
        self._get_all_metrics()

        # possible to remove this from make and add it as a method
        self._get_all_confusion_matrices()
        self._get_proba_distributions()
        self._get_variable_importance()

    def _train(self):
        X_train, y_train = self._prepare_data(self.dataset['train'])
        X_valid, y_valid = self._prepare_data(self.dataset['valid'])

        self.clf = CatBoostClassifier(learning_rate=0.1,
                                      loss_function='MultiClass',
                                      max_depth=self.max_depth,
                                      iterations=1000,
                                      random_seed=self.random_seed,
                                      one_hot_max_size=self.one_hot_max_size,
                                      class_names=self.labels,
                                      verbose=10,
                                      early_stopping_rounds=20,
                                      cat_features=self.cat_features,
                                      )
        self.clf.fit(X_train,
                     y_train,
                     eval_set=(X_valid, y_valid),
                     )

    def _prepare_data(self, data):
        X = data.loc[pd.notnull(data[self.target]), self.cat_features + self.num_features].copy()
        X[self.cat_features] = X[self.cat_features].fillna("NULL")
        X[self.num_features] = X[self.num_features].fillna(-10)
        y = data.loc[pd.notnull(data[self.target]), self.target].values
        return X, y

    def _get_all_predictions(self):
        self.y_pred = {}
        self.y_pred_proba = {}
        self.y_pred['train'], self.y_pred_proba['train'] = self._predict(self.dataset['train'])
        self.y_pred['valid'], self.y_pred_proba['valid'] = self._predict(self.dataset['valid'])
        if self.dataset['test'] is not None:
            self.y_pred['test'], self.y_pred_proba['test'] = self._predict(self.dataset['test'])

    def _predict(self, data):
        # repetition with _prepare_data
        X = data[self.cat_features + self.num_features].copy()
        X[self.cat_features] = X[self.cat_features].fillna("NULL")
        X[self.num_features] = X[self.num_features].fillna(-10)

        X_pool = Pool(X, cat_features=self.cat_features)
        y_pred = self.clf.predict(X_pool)[:, 0]
        y_pred_proba = self.clf.predict_proba(X_pool)
        return y_pred, y_pred_proba

    def _get_all_predictions_with_threshold(self):
        self.y_pred_with_threshold = {}
        self._get_predictions_with_threshold('train')
        self._get_predictions_with_threshold('valid')
        if self.dataset['test'] is not None:
            self._get_predictions_with_threshold('test')

    def _get_predictions_with_threshold(self, dataset_name):
        mask_thresholds = np.array(list(map(lambda x: any([x[i] > threshold for i, threshold in
                                                           enumerate(self.thresholds.values())]),
                                            self.y_pred_proba[dataset_name])))
        y_pred_with_threshold = self.y_pred[dataset_name].copy()
        y_pred_with_threshold[~mask_thresholds] = 'NSP'
        self.y_pred_with_threshold[dataset_name] = y_pred_with_threshold

    def _get_all_metrics(self):
        self.metrics = {}
        self._get_metrics('train')
        self._get_metrics('valid')
        if self.dataset['test'] is not None:
            self._get_metrics('test')

    def _get_metrics(self, dataset_name):
        y_true = self.dataset[dataset_name][self.target].values
        y_pred = self.y_pred[dataset_name]
        y_pred_with_threshold = self.y_pred_with_threshold[dataset_name]
        self.metrics[dataset_name] = self._compute_metrics(y_true, y_pred, y_pred_with_threshold)

    @staticmethod
    def _compute_metrics(y_true, y_pred, y_pred_with_threshold):
        """ y_true may be None at some position """
        mask_thresholds = y_pred_with_threshold != 'NSP'

        metrics = {}
        if pd.notnull(y_true).sum() > 0:
            metrics['accuracy'] = accuracy_score(y_true[pd.notnull(y_true)], y_pred[pd.notnull(y_true)])
        else:
            metrics['accuracy'] = None
        metrics['NSP'] = 1 - np.mean(mask_thresholds)
        metrics['proportion_above_threshold'] = np.mean(mask_thresholds)
        metrics['automation_rate'] = np.mean((y_pred_with_threshold == 'acceptation_manuelle') |
                                             (y_pred_with_threshold == 'refus_GM'))
        if np.sum(mask_thresholds & pd.notnull(y_true)) > 0:
            metrics['accuracy_above_threshold'] = accuracy_score(y_pred[mask_thresholds & pd.notnull(y_true)],
                                                                 y_true[mask_thresholds & pd.notnull(y_true)])
        else:
            metrics['accuracy_above_threshold'] = None

        return metrics

    def get_metrics_by(self, by, dataset_name):
        # be careful to missing values here
        prediction_df = self.dataset[dataset_name]
        prediction_df['prediction'] = self.y_pred[dataset_name]
        # no need for pred_proba yet
        #for i, label in enumerate(self.y_pred_proba.shape[1]):
        #    prediction_df['proba_' + label] = self.y_pred_proba[dataset_name][:, i]
        prediction_df['prediction_with_threshold'] = self.y_pred_with_threshold[dataset_name]
        metrics_by = {}
        for value in prediction_df[by].unique():
            metrics_by[value] = {}
            metrics_by[value]['count'] = (prediction_df[by] == value).sum()
            metrics_by[value]['metrics'] = self._compute_metrics(
                y_true=prediction_df.loc[prediction_df[by] == value, self.target],
                y_pred=prediction_df.loc[prediction_df[by] == value, 'prediction'],
                y_pred_with_threshold=prediction_df.loc[prediction_df[by] == value, 'prediction_with_threshold'])
        return metrics_by

    def get_contingency_table_by(self, by: str, dataset_name: str):
        return pd.crosstab(self.dataset[dataset_name][by].fillna("NULL"),
                           self.y_pred[dataset_name])

    def get_chi2_test_by(self, by, dataset_name):
        contingency_table = self.get_contingency_table_by(by, dataset_name)
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        return (chi2, p_value, dof)

    def get_2_sample_test_by(self, by, dataset_name):
        metrics_by = self.get_metrics_by(by, dataset_name)
        counts = [v['count'] for v in metrics_by.values()]
        accuracies = [v['metrics']['accuracy'] for v in metrics_by.values()]
        return self._compute_2_sample_test_for_probabilities(accuracies, counts)

    @staticmethod
    def _compute_2_sample_test_for_probabilities(probas, counts):
        #mean_proba = (counts[0] * probas[0] + counts[1] * probas[1]) / (counts[0] + counts[1])
        #z_stat = (probas[0] - probas[1]) / np.sqrt(mean_proba * (1-mean_proba)) / np.sqrt(1/counts[0] + 1/counts[1])
        stds = [np.sqrt(proba * (1-proba)) for proba in probas]
        result_test = ttest_ind_from_stats(mean1=probas[0], std1=stds[0], nobs1=counts[0],
                                           mean2=probas[1], std2=stds[1], nobs2=counts[1])
        return {'t_stat': result_test[0],
                'p_value': result_test[1]}

    def get_prediction_repartition_by(self, by, dataset_name):
        prediction_df = self.dataset[dataset_name]
        prediction_df['prediction'] = self.y_pred[dataset_name]
        prediction_repartition_by = {}
        for value in prediction_df[by].unique():
            prediction_repartition_by[value] = \
                prediction_df.loc[prediction_df[by] == value, 'prediction'].value_counts(normalize=True)
        return prediction_repartition_by

    def _get_thresholds(self):
        if self.thresholds is None:
            self.thresholds = {}
            y_true = self.dataset['valid'][self.target].copy().values
            y_pred_proba = self.y_pred_proba['valid']
            for i, label in enumerate(self.labels):
                self.thresholds[label] = self.optimize_threshold(y_true[pd.notnull(y_true)] == label,
                                                                 y_pred_proba[pd.notnull(y_true), i],
                                                                 self.precision_target)

    @staticmethod
    def optimize_threshold(yy_true: np.array, yy_pred_proba: np.array, precision_target: float) -> float:
        thresholds = np.linspace(0.01, 0.99, 99)
        precisions = {threshold: np.sum(yy_true[yy_pred_proba > threshold]) / np.sum(yy_pred_proba > threshold)
                      for threshold in thresholds if np.sum(yy_pred_proba > threshold) > 0}
        good_thresholds = [threshold for threshold, p in precisions.items() if p >= precision_target]
        optim_threshold = min(good_thresholds) if len(good_thresholds) > 0 else 1.0
        return optim_threshold

    def _get_all_confusion_matrices(self):
        self.confusion_matrices = {}
        self.confusion_matrices_with_threshold = {}
        for dataset_name in ['train', 'valid', 'test']:
            if self.dataset[dataset_name] is not None:
                self._get_confusion_matrices(dataset_name)

    def _get_confusion_matrices(self, dataset_name):
        y_true = self.dataset[dataset_name][self.target].values
        y_pred = self.y_pred[dataset_name]
        y_pred_with_threshold = self.y_pred_with_threshold[dataset_name]

        self.confusion_matrices[dataset_name] = {}
        print(dataset_name)
        self.confusion_matrices[dataset_name]['count'] = self.compute_confusion_matrix(y_true[pd.notnull(y_true)],
                                                                                       y_pred[pd.notnull(y_true)],
                                                                                       labels=self.labels,
                                                                                       percentage=False)
        self.confusion_matrices[dataset_name]['percentage'] = self.compute_confusion_matrix(y_true[pd.notnull(y_true)],
                                                                                            y_pred[pd.notnull(y_true)],
                                                                                            labels=self.labels,
                                                                                            percentage=True)
        self.confusion_matrices_with_threshold[dataset_name] = {}
        self.confusion_matrices_with_threshold[dataset_name]['count'] = \
            self.compute_confusion_matrix(y_true[pd.notnull(y_true) & (y_pred_with_threshold != 'NSP')],
                                          y_pred[pd.notnull(y_true) & (y_pred_with_threshold != 'NSP')],
                                          labels=self.labels,
                                          percentage=False)
        self.confusion_matrices_with_threshold[dataset_name]['percentage'] = \
            self.compute_confusion_matrix(y_true[pd.notnull(y_true) & (y_pred_with_threshold != 'NSP')],
                                          y_pred[pd.notnull(y_true) & (y_pred_with_threshold != 'NSP')],
                                          labels=self.labels,
                                          percentage=True)

    @staticmethod
    def compute_confusion_matrix(y_true, y_pred, labels, percentage):
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

    def predict_with_switch_sex(self):
        # repetition with _prepare_data
        data = self.dataset['valid']
        X = data[self.cat_features + self.num_features].copy()
        X[self.cat_features] = X[self.cat_features].fillna("NULL")
        X[self.num_features] = X[self.num_features].fillna(-10)
        X['caseData_life_GENDER'] = X['caseData_life_GENDER'].map({'H': 'F', 'F': 'H'})
        X['caseData_life_TITLE'] = X['caseData_life_TITLE'].map({'MR': 'MME', 'MME': 'MR', 'MLE': 'MR'})

        X_pool = Pool(X, cat_features=self.cat_features)
        y_pred = self.clf.predict(X_pool)[:, 0]
        y_pred_proba = self.clf.predict_proba(X_pool)
        return y_pred, y_pred_proba

    def _get_proba_distributions(self):
        pass

    def _get_variable_importance(self):
        pass

    def generate_report(self):
        "idea is to generate of report with all interesting things automatically"
        pass

