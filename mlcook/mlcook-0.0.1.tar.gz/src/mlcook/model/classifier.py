from catboost import CatBoostClassifier, Pool
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import numpy as np
import pandas as pd
import pickle as pkl


class IClassifier:
    def build(self, random_seed, labels, verbose,
              cat_features, # only used by catboost...
              ):
        # here I can either pass exp as argument, or the details of the arguments
        pass

    def build_copy(self, random_seed, labels, verbose, cat_features,):
        pass

    def fit(self,
            X_train: pd.DataFrame, y_train: np.array,
            X_valid: pd.DataFrame, y_valid: np.array,
            sample_weight_train: np.array,
            sample_weight_valid: np.array,):
        pass

    def predict(self, X: pd.DataFrame) -> np.array:
        pass

    def predict_proba(self, X: pd.DataFrame) -> np.array:
        pass

    def save(self, file_name):
        pass

    def load(self, file_name):
        pass


class CatboostClassifier(IClassifier):
    def __init__(self, loss_function=None, learning_rate=None, iterations=None,
                 max_depth=None, one_hot_max_size=None,
                 early_stopping_rounds=None):
        """
        - faire comme ça permet d'éviter à l'utilisateur de pouvoir entrer des arguments de catboost comme
        random_seed, ou scale_pos_weight (que je dois gérer ailleurs...)
        - je pourrais aussi standardiser les différents arguments en fonction des diff modèles scikit, xgbooost,
        catboost, etc.. à voir à l'avenir si c'est pertinent
        - pas de **kwargs car l'idée est justement de restreindre les arguments possibles
        - reste à savoir comment je pourrais gérer l'optim des hyper-paramètres...

        -> l'idée serait de mettre seulement les paramètres spécifiques à l'algo dans ces classes "intermédiaire",
        ne pas oublier que potentiellement on pourrait avoir des algos non arbre...
        """
        self.loss_function = loss_function
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.max_depth = max_depth
        self.one_hot_max_size = one_hot_max_size
        self.early_stopping_rounds = early_stopping_rounds
        self.clf = None

        # je pourrais stocker les arguments du modèle dans l'objet ici,
        # mais pas forcément besoin avec get_param...

    def build(self, random_seed, labels, verbose, cat_features, ):
        self.clf = CatBoostClassifier(loss_function=self.loss_function,
                                      learning_rate=self.learning_rate,
                                      iterations=self.iterations,
                                      max_depth=self.max_depth,
                                      one_hot_max_size=self.one_hot_max_size,
                                      early_stopping_rounds=self.early_stopping_rounds, # maybe put in trainer..
                                      verbose=verbose,
                                      cat_features=cat_features, #maye in trainer too
                                      class_names=labels,
                                      random_seed=random_seed,
                                      )

    def build_copy(self, random_seed, labels, verbose, cat_features,):
        clf = CatboostClassifier(loss_function=self.loss_function,
                                 learning_rate=self.learning_rate,
                                 iterations=self.iterations,
                                 max_depth=self.max_depth,
                                 one_hot_max_size=self.one_hot_max_size,
                                 early_stopping_rounds=self.early_stopping_rounds)
        clf.build(random_seed=random_seed, labels=labels, verbose=verbose, cat_features=cat_features,)
        return clf

    def fit(self, X_train, y_train, X_valid, y_valid,
            sample_weight_train=None,
            sample_weight_valid=None):
        self.clf.fit(X=Pool(X_train, y_train, weight=sample_weight_train,
                            cat_features=self.clf.get_param('cat_features')),
                     eval_set=Pool(X_valid, y_valid, weight=sample_weight_valid,
                                   cat_features=self.clf.get_param('cat_features')))

    def predict(self, X):
        X_pool = Pool(X, cat_features=self.clf.get_param('cat_features'))
        if self.loss_function == 'MultiClass':
            return self.clf.predict(X_pool)[:, 0]
        else:
            return self.clf.predict(X_pool)

    def predict_proba(self, X: pd.DataFrame) -> np.array:
        X_pool = Pool(X, cat_features=self.clf.get_param('cat_features'))
        return self.clf.predict_proba(X_pool)

    def save(self, file_name):
        self.clf.save_model(file_name)

    def load(self, file_name):
        self.clf = CatBoostClassifier()
        self.clf.load_model(file_name)


class SklearnRandomForestClassifier(IClassifier):
    def __init__(self, n_estimators: int = 100, criterion: str = 'gini', max_depth: int = None,
                 min_samples_leaf: int = 1, max_features: str = 'auto'):
        self.n_estimators = n_estimators
        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.clf = None

    def build(self, random_seed, labels, verbose,
              cat_features,):
        self.clf = RandomForestClassifier(n_estimators=self.n_estimators,
                                          criterion=self.criterion,
                                          max_depth=self.max_depth,
                                          min_samples_leaf=self.min_samples_leaf,
                                          max_features=self.max_features,
                                          random_state=random_seed,
                                          verbose=verbose)
        """
        TODO : verbose may have different meanings depending on algo
        cat_features not needed here..
        labels not accepted.. mais je dois pouvoir avec class_weight
        (à voir: mais comment on reconnaît la colonne du predict_proba dans sklearn dans ce cas...)
        """

    def fit(self,
            X_train: pd.DataFrame, y_train: np.array,
            X_valid: pd.DataFrame, y_valid: np.array,
            sample_weight_train: np.array,
            sample_weight_valid: np.array,):
        self.clf.fit(X=X_train, y=y_train, sample_weight=sample_weight_train) # no valid or early stopping here

    def predict(self, X: pd.DataFrame) -> np.array:
        return self.clf.predict(X)

    def predict_proba(self, X: pd.DataFrame) -> np.array:
        return self.clf.predict_proba(X)

    def save(self, filename):
        # TODO : need to see for need of serialize rather than save/load
        with open(filename, 'wb') as f:
            pkl.dump(self.clf, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.clf = pkl.load(f)


class XGboostClassifier(IClassifier):

    def __init__(self, n_estimators: int, booster: str, objective: str,
                 learning_rate: float, max_depth: int,
                 early_stopping_rounds: int, verbose: int):
        self.n_estimators = n_estimators
        self.booster = booster
        self.objective = objective
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.early_stopping_rounds = early_stopping_rounds
        self.verbose = verbose
        self.clf = None

    def build(self, random_seed, labels, verbose,
              cat_features,):
        self.clf = xgb.XGBClassifier(n_estimators=self.n_estimators,
                                 booster=self.booster,
                                 objective=self.objective,
                                 learning_rate=self.learning_rate,
                                 max_depth=self.max_depth,
                                 seed=random_seed,
                                     use_label_encoder=False)
        """
        TODO : verbose may have different meanings depending on algo
        cat_features not needed here..
        labels not accepted.. mais je dois pouvoir avec class_weight
        (à voir: mais comment on reconnaît la colonne du predict_proba dans sklearn dans ce cas...)
        """

    def fit(self,
            X_train: pd.DataFrame, y_train: np.array,
            X_valid: pd.DataFrame, y_valid: np.array,
            sample_weight_train: np.array,
            sample_weight_valid: np.array,):
        self.clf.fit(X=X_train, y=y_train, sample_weight=sample_weight_train,
                     eval_set=[(X_valid, y_valid)], sample_weight_eval_set=sample_weight_valid,
                     early_stopping_rounds=self.early_stopping_rounds, verbose=self.verbose)

    def predict(self, X: pd.DataFrame) -> np.array:
        return self.clf.predict(X)

    def predict_proba(self, X: pd.DataFrame) -> np.array:
        return self.clf.predict_proba(X)

    def save(self, filename):
        self.clf.save_model(filename)

    def load(self, filename):
        self.clf.load_model(filename)


class LightGBMClassifier(IClassifier):
    pass

