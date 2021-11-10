import numpy as np
import pandas as pd

import xgboost as xgb
import lightgbm as lgb
import catboost as cb

from sklearn.model_selection import KFold, StratifiedKFold

# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression

class XgbWrapper(object):
    def __init__(self, seed=0, params={}):
        self.params = params
        self.params['seed'] = seed
        
    def train(self, X_train, y_train, X_val, y_val, num_boost_round=100000, early_stopping_rounds=100, verbose_eval=100):
        
        xgb_train = xgb.DMatrix(X_train, label=y_train)  
        xgb_valid = xgb.DMatrix(X_val, label=y_val)
        
        num_boost_round = self.params['num_boost_round'] if 'num_boost_round' in self.params.keys() else num_boost_round
        early_stopping_rounds = self.params['early_stopping_rounds'] if 'early_stopping_rounds' in self.params.keys() else early_stopping_rounds
        verbose_eval = self.params['verbose_eval'] if 'verbose_eval' in self.params.keys() else verbose_eval
        try:
            del self.params['num_boost_round']
            del self.params['early_stopping_rounds']
            del self.params['verbose_eval']
        except:
            pass
        self.clf = xgb.train(params=self.params, 
                      dtrain=xgb_train,
                      evals=[(xgb_train, 'train'), (xgb_valid, 'valid')],
                      num_boost_round=num_boost_round,   
                      verbose_eval=verbose_eval,
                      early_stopping_rounds=early_stopping_rounds,
                   )

    def predict(self, x):
        return self.clf.predict(xgb.DMatrix(x))
    
    def predict_proba(self, x):
        return self.clf.predict_proba(x)
    @staticmethod
    def cv(X, y, params, num_boost_round=100000, early_stopping_rounds=100, verbose_eval=1000, nfolds=5, kf_type='kf', show_stdv=False, seed=1995, get_best=False, direction='maximize'):
        
        data_train = xgb.DMatrix(X, label=y)  
        
        num_boost_round = params['num_boost_round'] if 'num_boost_round' in params.keys() else num_boost_round
        early_stopping_rounds = params['early_stopping_rounds'] if 'early_stopping_rounds' in params.keys() else early_stopping_rounds
        verbose_eval = params['verbose_eval'] if 'verbose_eval' in params.keys() else verbose_eval
        
        if kf_type == 'kf':
            kf = KFold(n_splits = nfolds, shuffle=True, random_state=seed)
        else:
            kf = StratifiedKFold(n_splits = nfolds, shuffle=True, random_state=seed)
        
        
        try:
            del params['num_boost_round']
            del params['early_stopping_rounds']
            del params['verbose_eval']
        except:
            pass
        
        history = xgb.cv(params, data_train, 
             num_boost_round=num_boost_round, 
             folds=kf, 
             early_stopping_rounds=early_stopping_rounds, 
             verbose_eval=verbose_eval, 
             show_stdv=show_stdv,  # 显示metric的标准差
             seed=seed)
        if get_best:
            
            col = [col for col in history.columns if 'mean' in col and 'test' in col][0]
            
            if direction == 'maximize':
                return np.max(history[col])
            
            else:
                return np.min(history[col])
        
        return history
    
class LightGBMWrapper(object):
    def __init__(self, seed=0, params={}):
        params['feature_fraction_seed'] = seed
        params['bagging_seed'] = seed
        self.params = params
        
    def train(self, X_train, y_train, X_val, y_val, num_boost_round=100000, early_stopping_rounds=100, verbose_eval=100):
        
        lgb_train = lgb.Dataset(X_train,y_train)  
        lgb_valid = lgb.Dataset(X_val,y_val)
        
        num_boost_round = self.params['num_boost_round'] if 'num_boost_round' in self.params.keys() else num_boost_round
        early_stopping_rounds = self.params['early_stopping_rounds'] if 'early_stopping_rounds' in self.params.keys() else early_stopping_rounds
        verbose_eval = self.params['verbose_eval'] if 'verbose_eval' in self.params.keys() else verbose_eval

        try:
            del self.params['num_boost_round']
            del self.params['early_stopping_rounds']
            del self.params['verbose_eval']
        except:
            pass
        
        self.clf = lgb.train(params=self.params, 
                         train_set=lgb_train,
                         valid_sets=[lgb_train, lgb_valid],
                         num_boost_round=num_boost_round,
                         verbose_eval=verbose_eval,
                         early_stopping_rounds=early_stopping_rounds,
                        )
        
    def predict(self, x):
        return self.clf.predict(x)
    
    def predict_proba(self, x):
        return self.clf.predict_proba(x)
    
    @staticmethod
    def cv(X, y, params, num_boost_round=100000, early_stopping_rounds=100, verbose_eval=-1, nfolds=5, kf_type='kf', show_stdv=False, seed=1995, get_best=False, direction='maximize'):
        
        data_train = lgb.Dataset(X, y)  
        
        num_boost_round = params['num_boost_round'] if 'num_boost_round' in params.keys() else num_boost_round
        early_stopping_rounds = params['early_stopping_rounds'] if 'early_stopping_rounds' in params.keys() else early_stopping_rounds
        verbose_eval = params['verbose_eval'] if 'verbose_eval' in params.keys() else verbose_eval
        
        
        if kf_type == 'kf':
            kf = KFold(n_splits = nfolds, shuffle=True, random_state=seed)
        else:
            kf = StratifiedKFold(n_splits = nfolds, shuffle=True, random_state=seed)
        
        try:
            del params['num_boost_round']
            del params['early_stopping_rounds']
            del params['verbose_eval']
        except:
            pass
        
        history = lgb.cv(params, data_train, 
             num_boost_round=num_boost_round, 
             folds=kf, 
             early_stopping_rounds=early_stopping_rounds, 
             verbose_eval=verbose_eval, 
             show_stdv=show_stdv,  # 显示metric的标准差
             seed=seed)
        
        if get_best:
            
            col = [col for col in history.keys() if 'mean' in col][0]
            
            if direction == 'maximize':
                return np.max(history[col])
            
            else:
                return np.min(history[col])
        
        return history

class CatboostWrapper(object):
    def __init__(self, seed=0, params={}):
        params['random_seed'] = seed
        self.params = params
    def train(self, X_train, y_train, X_val, y_val, num_boost_round=100000, early_stopping_rounds=100, verbose=100):
        cb_train = cb.Pool(X_train,y_train)  
        cb_valid = cb.Pool(X_val,y_val)
        
        num_boost_round = self.params['num_boost_round'] if 'num_boost_round' in self.params.keys() else num_boost_round
        early_stopping_rounds = self.params['early_stopping_rounds'] if 'early_stopping_rounds' in self.params.keys() else early_stopping_rounds
        verbose_eval = self.params['verbose_eval'] if 'verbose_eval' in self.params.keys() else verbose_eval
        try:
            del self.params['num_boost_round']
            del self.params['early_stopping_rounds']
            del self.params['verbose_eval']
        except:
            pass
        
        self.clf = cb.train(dtrain=cb_train, 
                            params=self.params, 
                            evals=[cb_train, cb_valid],
                            num_boost_round=num_boost_round,
                            early_stopping_rounds=early_stopping_rounds,
                            verbose=verbose
                           )
    
    def predict(self, x):
        return self.clf.predict(x)
    
    def predict_proba(self, x):
        return self.clf.predict_proba(x)

class SklearnWrapper(object):
    def __init__(self, clf, seed=0, params={}):
        params['random_state'] = seed
        self.clf = clf(**params)

    def train(self, X_train, y_train, X_val, y_val):
        self.clf.fit(X_train, y_train)
    
    def predict(self, x, proba=True):
        if proba:
            return self.clf.predict_proba(x)[:,1]
        else:
            return self.clf.predict(x)

    def predict_proba(self, x):
        return self.clf.predict_proba(x)