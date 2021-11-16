from dataclasses import dataclass

import pandas as pd
from pandas import DataFrame
from scipy.stats import loguniform

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from tqdm.auto import tqdm
from xgboost import XGBRegressor, XGBClassifier

DEFAULT_REGRESSION_MODELS = [
    ('KNN', KNeighborsRegressor(), dict(n_neighbors=[2, 4, 8, 16, 32, 64, 128, 256])),
    ('SVR', SVR(), dict(
        C=loguniform(1e-4, 1e4),
        gamma=loguniform(1e-4, 1e4))),
    ('XGB', XGBRegressor(), dict(n_estimators=[100, 1000]))
]

DEFAULT_CLASSIFICATION_MODELS = [
    ('LogReg', LogisticRegression(), dict(C=loguniform(1e-4, 1e4))),
    ('RF', RandomForestClassifier(), dict(n_estimators=[100, 1000])),
    ('KNN', KNeighborsClassifier(), dict(leaf_size=[15, 30])),
    ('SVM', SVC(), dict(
        C=loguniform(1e-4, 1e4),
        gamma=loguniform(1e-4, 1e4))),
    ('GNB', GaussianNB(), dict(var_smoothing=[1e-9])),
    ('XGB', XGBClassifier(), dict(n_estimators=[100, 1000]))
]


@dataclass
class RCVOutput():
    best_models: dict
    cv_by_model: DataFrame
    preds: list


def RandomizedCV(X_train: pd.DataFrame, y_train: pd.DataFrame, models=DEFAULT_REGRESSION_MODELS, return_preds=False,
                 **kwargs):
    cv_by_model = []
    preds = []
    best_models = dict()
    for name, model, distributions in tqdm(models):
        random_search = RandomizedSearchCV(model,
                                           distributions,
                                           random_state=666,
                                           **kwargs)
        random_search.fit(X_train, y_train)

        cv_df = pd.DataFrame(random_search.cv_results_)
        cv_df['model'] = name
        if return_preds:
            preds.append(random_search.best_estimator_.predict(X_train))
        best_models[name] = random_search.best_estimator_
        cv_by_model.append(cv_df)
    return RCVOutput(best_models, pd.concat(cv_by_model,ignore_index=True), preds)


def get_best_model(out:RCVOutput, metric="score"):
    idx = out.cv_by_model[f'mean_test_{metric}'].idxmax()
    best_entry = out.cv_by_model.loc[idx].dropna()
    best_model = out.best_models[best_entry.model]

    return best_model
