import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold

from sklearn.linear_model import LogisticRegression

class BasicOOF:
    def __init__(self, clf, kf_type='kf', nfolds=5, shuffle=True, seed=1995, predict_proba=False):
        
        self.clf = clf
        
        self.nfolds = nfolds
        self.shuffle = shuffle
        self.seed = seed
        self.kf_type = kf_type
        self.predict_proba=predict_proba
        
        if kf_type == 'kf':
            self.kf = KFold(n_splits = self.nfolds, shuffle=True, random_state=self.seed)
        else:
            self.kf = StratifiedKFold(n_splits = self.nfolds, shuffle=True, random_state=self.seed)
    
    def get_oof(self, X_train, y_train, X_test):
        oof_train = np.zeros((len(X_train),))
        oof_test = np.zeros((len(X_test),))
        oof_test_kf = np.empty((self.nfolds, len(X_test)))
        
        for i, (train_index, val_index) in enumerate(self.kf.split(X_train, y_train)):
            print('------Fold:', i)
            X_tr, X_val = X_train.loc[train_index], X_train.loc[val_index]
            y_tr, y_val = y_train.loc[train_index], y_train.loc[val_index]
            
            self.clf.train(X_tr, y_tr, X_val, y_val, **kwargs)
            if self.predict_proba:
                oof_train[val_index] = self.clf.predict_proba(X_val)
                oof_test_kf[i, :] = self.clf.predict_proba(X_test)
            else:
                oof_train[val_index] = self.clf.predict(X_val)
                oof_test_kf[i, :] = self.clf.predict(X_test)
            
        oof_test[:] = oof_test_kf.mean(axis=0)
        
        self.oof_train = oof_train.reshape(-1, 1)
        self.oof_test = oof_test.reshape(-1, 1)
        
        return oof_train.reshape(-1, 1), oof_test.reshape(-1, 1)

class StackingLogisticRegressionModel:
    
    def __init__(self):
        self.clf = LogisticRegression()
        
    def fit(self, oof_X_trains, y_train):
        stacking_X_train = np.concatenate(oof_X_trains, axis=1)
        self.clf.fit(stacking_X_train, y_train)
        
    def predict(self, oof_tests):
        stacking_X_test = np.concatenate(oof_tests, axis=1)
        pred = self.clf.predict(stacking_X_test)
        return pred
    def predict_proba(self, oof_tests):
        stacking_X_test = np.concatenate(oof_tests, axis=1)
        pred = self.clf.predict_proba(stacking_X_test)
        
        return pred[:, 1]