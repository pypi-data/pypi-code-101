# ====================================================================================================
# hyperopt for xgb
# ====================================================================================================
import pandas as pd
import numpy as np
import xgboost as xgb
def get_params_dft_list_xgb(objective = 'binary', metric = 'auc'):
    params_dft_list = []
    params = {
        'random_state': 777,
        'objective': 'reg:squarederror',
        'eval_metric': metric,
        'nthread': 16,
        'verbosity': 0,
        'learning_rate': 0.1,
        'max_depth': 8,
        'subsample':0.5,
        'colsample_bytree': 0.5,
        # 'alpha' : 0.07,
        # 'lambda' : 0.07,
        # 'min_child_weight':7,
    }
    params['objective'] = 'binary:logistic' if objective == 'binary' else params['objective']
    params_dft_list.append(params)
    
    params = {
        'objective': 'reg:linear',
        'eval_metric': metric,
        'eta': 0.01,
        'min_child_weight': 6,
        'subsample': 0.7,
        'colsample_bytree': 0.6,
        'scale_pos_weight': 0.8,
        'silent': 1,
        'max_depth': 8,
        'max_delta_step': 2,
        'nthread': 16,
        'random_state': 777
    }
    params['objective'] = 'binary:logistic' if objective == 'binary' else params['objective']
    params_dft_list.append(params)
    return params_dft_list

def get_score_xgb(X, y, params):
    score_list = []
    # from sklearn.model_selection import StratifiedKFold
    # skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=777).split(X, y)
    from sklearn.model_selection import KFold
    skf = KFold(n_splits = 5, shuffle = False, random_state = 777).split(X)
    for i, (train_idx, valid_idx) in enumerate(skf):
        if i != 4:
            continue
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_valid, y_valid = X.iloc[valid_idx], y.iloc[valid_idx]
        dtrain, dvalid = xgb.DMatrix(X_train, label = y_train), xgb.DMatrix(X_valid, label = y_valid)
        model = xgb.train(params, dtrain, num_boost_round = 10000,
                          evals = [(dvalid, 'valid')], early_stopping_rounds = 100, verbose_eval = 0)
        score_list.append(model.best_score)
        gc.collect();
    return np.mean(score_list)

def opt_adapter_xgb(objective, metric):
    # params_basic
    params_basic = {
        'objective': 'reg:linear' if objective == 'regression' else 'binary:logistic',
        'eval_metric': metric,
        'silent': 1,
        'nthread': 16,
        'random_state': 777
    }
    # space
    import math
    math_log_num_leaves = np.logspace(math.log(2, 2), math.log(128, 2), 1000, endpoint=True, base=2, dtype=int)
    space = {
        "eta": hp.choice("eta", [0.01]),
        "max_depth": hp.choice("max_depth", [2, 3,4,5,6,7,8,9,10,11]),
        "scale_pos_weight": hp.quniform('scale_pos_weight', 0.0, 1.0, 0.1),
        "colsample_bytree": hp.quniform("colsample_bytree", 0.2, 1.0, 0.05),
        "subsample": hp.quniform("subsample", 0.2, 1.0, 0.05),
        "max_delta_step": hp.choice("max_delta_step", np.linspace(0, 10, 1, dtype=int)),
        "min_child_weight": hp.uniform('min_child_weight', 1, 20),
    }
    # get_score function
    get_score_func = get_score_xgb
    # init params
    params_dft_list = get_params_dft_list_xgb(objective, metric)
    return params_basic, space, get_score_func, params_dft_list

# ====================================================================================================
# hyperopt for lgb
# ====================================================================================================
import lightgbm as lgb
def get_params_dft_list_lgb(objective = 'binary', metric = 'auc'):
    params_dft_list = []
    params = {
        'objective': 'binary' if objective == 'binary' else 'regression',
        'metric': 'auc' if objective == 'binary' else 'rmse',
        'boosting_type': 'gbdt',
        'learning_rate': 0.01,
        'num_leaves': 255,
        'max_depth': -1,
        'bagging_fraction': 0.5,
        'feature_fraction': 0.5,
        # 'max_bin': 255,
        # 'bagging_freq': 1,
        # 'lambda_l1': 0.01,
        # 'lambda_l2': 0.01,
        # 'min_data_in_leaf': 10,
        'verbosity': -1,
        'seed': 42,
        'n_jobs': 16,
    }
    params_dft_list.append(params)

    params = {
        'objective': 'binary' if objective == 'binary' else 'regression',
        'metric': 'auc' if objective == 'binary' else 'rmse',
        'boosting_type': 'gbdt',
        'learning_rate': 0.01,
        'num_leaves': 2,
        'max_depth': 1,
        'bagging_fraction': 0.4,
        'feature_fraction': 0.05,
        'bagging_freq': 5,
        # 'lambda_l1': 0.01,
        # 'lambda_l2': 0.01,
        'min_data_in_leaf': 80,
        # 'max_bin': 255,
        'verbosity': -1,
        'seed': 42,
        'n_jobs': 16,
    } 
    params_dft_list.append(params)
    
    params = {
        'objective': 'binary' if objective == 'binary' else 'regression',
        'metric': 'auc' if objective == 'binary' else 'rmse',
        'boosting_type': 'gbdt',
        'learning_rate': 0.01,
        'num_leaves': 13,
        'max_depth': -1,
        'bagging_fraction': 0.4,
        'feature_fraction': 0.05,
        'bagging_freq': 5,
        # 'lambda_l1': 0.01,
        # 'lambda_l2': 0.01,
        'min_data_in_leaf': 80,
        # 'max_bin': 255,
        'verbosity': -1,
        'seed': 42,
        'n_jobs': 16,
    } 
    params_dft_list.append(params)
    
    params = {
        'seed': 777,
        'objective': 'binary' if objective == 'binary' else 'regression',
        'metric': 'auc' if objective == 'binary' else 'rmse',
        "n_jobs": 16,
        'verbosity':-1,
        'learning_rate': 0.01,
        'num_leaves': 31,
        'max_depth': -1,
        'lambda_l1': 0.07,
        'lambda_l2': 7,
        'min_data_in_leaf':7,
        'feature_fraction': 0.7,
        'bagging_fraction': 0.7,
        'bagging_freq': 7,
    }
    params_dft_list.append(params)
    return params_dft_list

def get_score_lgb(X, y, params):
    score_list = []
    # from sklearn.model_selection import StratifiedKFold
    # skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=777).split(X, y)
    from sklearn.model_selection import KFold
    skf = KFold(n_splits = 5, shuffle = False, random_state = 777).split(X)
    for i, (train_idx, valid_idx) in enumerate(skf):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_valid, y_valid = X.iloc[valid_idx], y.iloc[valid_idx]
        dtrain, dvalid = lgb.Dataset(X_train, y_train), lgb.Dataset(X_valid, y_valid)
        model = lgb.train(params, dtrain, 10000, dvalid, early_stopping_rounds = 100, verbose_eval = 0)
        score_list.append(model.best_score["valid_0"][params["metric"]])
        gc.collect();
    return np.mean(score_list)

def opt_adapter_lgb(objective, metric):
    # params_basic
    params_basic = {
        'objective': objective,
        'metric': metric,
        'boosting_type': 'gbdt',
        'verbosity': -1,
        'seed': 777,
        'n_jobs': 16,
    }
    # space
    import math
    math_log_num_leaves = np.logspace(math.log(2, 2), math.log(1000, 2), 1000, endpoint=True, base=2, dtype=int)
    space = {
        "learning_rate": hp.choice("learning_rate", [0.01]),
        "max_depth": hp.choice("max_depth", [-1,3,4,5,6,7,8,9,10,11]),
        "num_leaves": hp.choice("num_leaves", math_log_num_leaves),
        "feature_fraction": hp.quniform("feature_fraction", 0.2, 1.0, 0.05),
        "bagging_fraction": hp.quniform("bagging_fraction", 0.2, 1.0, 0.05),
        "bagging_freq": hp.choice("bagging_freq", np.linspace(0, 50, 5, dtype=int)),
        # "reg_alpha": hp.uniform("reg_alpha", 0, 30), # it will cause auc = 0.5 some times
        # "reg_lambda": hp.uniform("reg_lambda", 0, 30), # it will cause auc = 0.5 some times
        "min_child_weight": hp.quniform('min_child_weight', 0.0, 20, 0.5),
    }
    # get_score function
    get_score_func = get_score_lgb
    # init params
    params_dft_list = get_params_dft_list_lgb(objective, metric)
    return params_basic, space, get_score_func, params_dft_list

# ====================================================================================================
# hyperopt go
# ====================================================================================================
import hyperopt
from hyperopt import hp, tpe, STATUS_OK, space_eval, Trials, partial
import datetime, time, gc, os, sys
def hyperopt_go(X, y, n_search, opt_config, 
                params_basic, space, get_score_func, params_dft_list):
    # util 
    def merge_dict(d1, d2):
        tmp = d1.copy()
        tmp.update(d2)
        return tmp
    def dowmsample(X, y):
        max_shape = 100000 * 200
        max_row = int(max_shape / X.shape[1])
        max_row = np.clip(max_row, 10000, 100000)
        if X.shape[0] > max_row:
            print('[+] dowmsample .... max_row = {}'.format(max_row))
            y = y.sample(max_row, random_state = 0)
            X = X.loc[y.index]
            X.reset_index(drop = True, inplace = True)
            y.reset_index(drop = True, inplace = True)
            print('[+] X.shape = {}, y.shape = {}\n[+] vc = \n{}'.\
                  format(X.shape, y.shape, y.value_counts().iloc[:5].to_string()))
        return X, y

    # dowmsample
    print('[+] X.shape = {}, y.shape = {}\n[+] vc = \n{}'.\
          format(X.shape, y.shape, y.value_counts().iloc[:5].to_string()))
    X, y = dowmsample(X, y)

    # obj for hyperopt
    a_min_max = -1 if opt_config['metric'] in ['auc'] else 1
    params_score_list = []
    def objective(params):
        # params to try
        params = merge_dict(params_basic, params)
        
        # params_dft
        if opt_config['cnt_search'] < len(params_dft_list):
            params = params_dft_list[opt_config['cnt_search']]
            
        # score
        score = get_score_func(X, y, params)
        params_score_list.append([params, score])
        print('\n[+] {} i = {} / {} + {}, score = {:.6f}'.\
              format('+' * 70, opt_config['cnt_search'], len(params_dft_list), n_search, score))
        print('[+] {}'.format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
        print(params)
        opt_config['cnt_search'] += 1
        return {'loss': a_min_max * score, 'status': STATUS_OK}
    
    # hyperopt.fmin
    trials = Trials()
    best = hyperopt.fmin(fn=objective, space=space, trials=trials, 
                         max_evals=n_search+len(params_dft_list), verbose=0,
                         algo=partial(tpe.suggest, n_startup_jobs = 30 + len(params_dft_list)),
                         rstate=np.random.RandomState(0))
    hyperopt_result = pd.DataFrame(params_score_list, columns = ['params', 'score'])
    return hyperopt_result.sort_values(by='score', ascending=a_min_max==1).reset_index(drop=False)

# ====================================================================================================
# hyperopt master
# ====================================================================================================
def hyperopt_master(X, y, n_search = 10, model_name = 'lgb'):
    print('\n====================================================================================================')
    print('hyperopt_master begin', datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print('====================================================================================================')
    # opt_config
    np.random.seed(777)
    opt_config = {
        'objective': 'binary' if len(set(y)) == 2 else 'regression',
        'metric': 'auc' if len(set(y)) == 2 else 'rmse',
        'cnt_search': 0,
    }  
    print('[+] opt_config = {}'.format(opt_config))

    # adapter
    if model_name == 'lgb':
        params_basic, space, get_score_func, params_dft_list = \
            opt_adapter_lgb(opt_config['objective'], opt_config['metric'])
    elif model_name == 'xgb':
        params_basic, space, get_score_func, params_dft_list = \
            opt_adapter_xgb(opt_config['objective'], opt_config['metric'])
    else:
        return pd.DataFrame([], columns = ['params', 'score'])
    
    # search
    hyperopt_result = hyperopt_go(X, y, n_search, opt_config, 
                                  params_basic, space, get_score_func, params_dft_list)
    print('\n====================================================================================================')
    print('hyperopt_master finised', datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print('====================================================================================================')
    return hyperopt_result    


# ====================================================================================================
# test data
# ====================================================================================================
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings("ignore")

np.random.seed(777)
n, m = 20000, 20
# ======================================== randint ==================================================
train = pd.DataFrame(np.random.randint(0, 100, (n, m)))
test = pd.DataFrame(np.random.randint(0, 100, (n, m)))
train_label = np.random.randint(0, 2, (len(train)))
test_label = np.random.randint(0, 2, (len(test)))

# ======================================== randn ==================================================
train = pd.DataFrame(np.random.randn(n, m))
test = pd.DataFrame(np.random.randn(n, m))
train_label = np.random.randint(0, 2, (len(train)))
test_label = np.random.randint(0, 2, (len(test)))

# ======================================== sklearn ==================================================
from sklearn.datasets import make_classification
train, train_label = make_classification(n_samples = n * 2,
                           n_features = m,
                           n_redundant = 0,
                           n_clusters_per_class = 1,
                           n_classes = 2,
                           random_state = 777)

# from sklearn.datasets import make_regression
# train, train_label = make_regression(n_samples = n * 2,
#                                      n_features = m,
#                                      random_state = 777)

train, test = train[:n], train[n:]
train_label, test_label = train_label[:n], train_label[n:]

# ======================================== foramt ==================================================
train = pd.DataFrame(train)
test = pd.DataFrame(test)
train.columns = ['c_' + str(i) for i in range(train.shape[1])]
test.columns = ['c_' + str(i) for i in range(test.shape[1])]
train_label = pd.Series(train_label)
test_label = pd.Series(test_label)
cols_cat = train.columns.tolist()[:m // 2]
cols_num = train.columns.tolist()[m // 2:]
train[cols_cat] = (train[cols_cat] * 100).astype(int) % 300
test[cols_cat] = (test[cols_cat] * 100).astype(int) % 300
train_fea, test_fea = train, test

hyperopt_result_xgb = hyperopt_master(train_fea, train_label, n_search = 10, model_name = 'xgb')

hyperopt_result_lgb = hyperopt_master(train_fea, train_label, n_search = 10, model_name = 'lgb')
