import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

from mlpet.Datasets import lithology

## Crossplot
def find_crossplot_scores(df, x, y, algo='comb'):
    """
    Find anomalies based on the crossplots of x vs. y

    Args:
        df_well (pd.DataFrame): dataframe with data from one well
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list with indices of anomalous samples
    """
    df = df[(df[x]!=0) & (df[y]!=0)].copy()

    anomal_idx = []
    tmp = df[[x, y]].dropna().copy()
    scores = dict()
    if len(tmp)>10:
        if algo=='DBSCAN':
            cls = DBSCAN(eps=0.05).fit(tmp)
            preds = cls.predict(tmp)
        elif algo=='EliEnv':
            cls = EllipticEnvelope(contamination=0.05, random_state=0).fit(tmp)
            preds = cls.predict(tmp)
            scores['EliEnv'] = cls.score_samples(tmp)
        elif algo=='SVM':
            cls = OneClassSVM(gamma='scale', nu=0.01).fit(tmp)
            preds = cls.predict(tmp)
            scores['SVM'] = cls.score_samples(tmp)         
        elif algo=='IsoFor':
            preds = isofor_res(tmp, RUNS, n_estimators=50, contamination=0.01)
        elif algo=='comb':
            preds1 = DBSCAN(eps=0.05).fit_predict(tmp)
            try:
                ee = EllipticEnvelope(contamination=0.05, random_state=0).fit(tmp)
                preds2 = ee.predict(tmp)
                scores['EliEnv'] = ee.score_samples(tmp)
            except:
                preds2 = np.zeros(len(tmp))
            svm = OneClassSVM(gamma='scale', nu=0.01).fit(tmp)
            preds3 = svm.predict(tmp)
            scores['SVM'] = svm.score_samples(tmp)
            ifo = IsolationForest(
                n_estimators=50,
                contamination=0.01, 
                random_state=0
                ).fit(tmp)
            preds4 = ifo.predict(tmp)
            scores['IsoFor'] = ifo.score_samples(tmp)
            preds  = np.where(preds1==-1, 1, 0) +\
                    np.where(preds2==-1, 1, 0) +\
                    np.where(preds3==-1, 1, 0) +\
                    np.where(preds4==-1, 1, 0)

        if algo=='comb':
            tmp['pred'] = np.where(preds>1, 1, 0)
        else:
            tmp['pred'] = np.where(preds==-1, 1, 0)

        anomal_idx.append(list(tmp[tmp.pred==1].index))

    return sum(anomal_idx, []), scores, tmp.index

def cross_vp_den(df_well, algo='comb'):
    """
    Finds anomalies based on the crossplots of VP vs DEN

    Args:
        df_well (pd.DataFrame): dataframe with data from one well
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list with indices of anomalous samples
    """
    preds, scores, idx = find_crossplot_scores(
        df_well, x='VP', y='DEN', algo=algo
    )
    return preds, scores, idx

def cross_ai_vpvs(df_well, algo='comb'):
    """
    Finds anomalies based on the crossplots of AI vs VPVS

    Args:
        df_well (pd.DataFrame): dataframe with data from one well
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list with indices of anomalous samples
    """
    preds, scores, idx = find_crossplot_scores(
        df_well, x='AI', y='VPVS', algo=algo
    )
    return preds, scores, idx
    
def cross_vp_vs(df_well, algo='comb'):
    """
    Finds anomalies based on the crossplots of VP vs VS

    Args:
        df_well (pd.DataFrame): dataframe with data from one well
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list with indices of anomalous samples
    """
    preds, scores, idx = find_crossplot_scores(
        df_well, x='VP', y='VS', algo=algo
    )
    return preds, scores, idx

def flag_crossplots(df_well, **kwargs):
    """
    Returns anomalous indices of three crossplots

    Args:
        df_well (pd.DataFrame): data of one well

    Returns:
        tuple: lists of anomalous indices for each crossplot
    """
    vp_den_anomalies, vp_den_scores, vp_den_idx = cross_vp_den(df_well, algo='comb')
    ai_vpvs_anomalies, ai_vpvs_scores, ai_vpvs_idx = cross_ai_vpvs(df_well, algo='comb')
    vp_vs_anomalies, vp_vs_scores, vp_vs_idx = cross_vp_vs(df_well, algo='comb')

    vp_den_res = dict()
    vp_den_res['anomalies'] = vp_den_anomalies
    vp_den_res['scores'] = vp_den_scores
    vp_den_res['idx'] = vp_den_idx

    ai_vpvs_res = dict()
    ai_vpvs_res['anomalies'] = ai_vpvs_anomalies
    ai_vpvs_res['scores'] = ai_vpvs_scores
    ai_vpvs_res['idx'] = ai_vpvs_idx

    vp_vs_res = dict()
    vp_vs_res['anomalies'] = vp_vs_anomalies
    vp_vs_res['scores'] = vp_vs_scores
    vp_vs_res['idx'] = vp_vs_idx

    return vp_den_res, ai_vpvs_res, vp_vs_res

#FIXME! Too long.
def prep_crossplot(**kwargs):
    cp_names = kwargs.get('cp_names', ['vp_den', 'vp_vs', 'ai_vpvs'])
    #Make sure both dataset- and model- settings are provided
    settings = kwargs.get('settings', None)
    folder_path = kwargs.get('folder_path', None)

    if (settings is None) or (folder_path is None) or (mappings is None):
        raise ValueError("Method 'crossplot' cannot be used without 'settings', 'mappings, and 'folder_path'")

    if ('datasets' not in settings.keys()) or ('models' not in settings.keys()):
        raise ValueError("Both 'datasets' and 'models' settings are required.")
    #Make sure folder_path is provided
    if not os.path.isdir(folder_path):
        raise ValueError("Provided folder_path ({}) does not exist.".format(folder_path))

    #Assuming all cp_names use the same model- and data-settings
    model_settings = settings['models']
    data_settings = settings['datasets']['lithology']

    #Instantiate datasets and models for each of the crossplots
    datasets = dict()
    models = dict()
    key_wells = dict()
    folder_paths = dict()

    for cp_name in cp_names:
        print('init ds and model - BadlogModel - {}'.format(cp_name))
        folder_paths[cp_name] = os.path.join(folder_path, cp_name)
        datasets[cp_name] = lithology.Lithologydata(
            settings=data_settings, 
            mappings=mappings,
            folder_path=folder_paths[cp_name]
            ) #but don't load any data into the dataset, because we need to get that from running the find_crossplot_scores
        
        models[cp_name] = classification_models.XGBoostClassificationModel(
            model_settings, 
            folder_paths[cp_name]
            )

        key_wells[cp_name] = joblib.load(os.path.join(folder_paths[cp_name], 'key_wells.joblib'))
    return datasets, models, key_wells, folder_paths

def train_crossplot(**kwargs):
    pass

#FIXME! Too long!
def flag_crossplot(X_pred, cp_names, datasets, models, key_wells, **kwargs):
    print('Method: crossplot - general...')
    y = X_pred.copy()

    #Set the default outlier scores to 0
    for cp_name in cp_names:
        outlier_methods = ['EliEnv', 'SVM', 'IsoFor']
        for method in outlier_methods:
            X_pred['{}_{}'.format(method, cp_name)] = 0.

    vp_den_anomalies, ai_vpvs_anomalies, vp_vs_anomalies = [], [], []
    for lsu in X_pred['GROUP'].unique():
        lsu_data = X_pred[X_pred['GROUP']==lsu]
        vp_den_res, ai_vpvs_res, vp_vs_res =\
            flag_crossplots(
                lsu_data, 
                **kwargs.get('crossplot', {}))

        vp_den_anom = vp_den_res['anomalies']
        ai_vpvs_anom = ai_vpvs_res['anomalies']
        vp_vs_anom = vp_vs_res['anomalies']

        vp_den_anomalies.append(vp_den_anom)
        ai_vpvs_anomalies.append(ai_vpvs_anom)
        vp_vs_anomalies.append(vp_vs_anom)

        #Add scores to X_pred for further use (in cp_supervised)
        for dic, cp_name in zip([vp_den_res, vp_vs_res, ai_vpvs_res], cp_names):
            for outlier_method in dic['scores'].keys():
                X_pred.loc[dic['idx'], '{}_{}'.format(outlier_method, cp_name)] = dic['scores'][outlier_method]
    
    vp_den_anomalies  = sum(vp_den_anomalies, [])
    ai_vpvs_anomalies = sum(ai_vpvs_anomalies, [])
    vp_vs_anomalies   = sum(vp_vs_anomalies, [])

    #Set everything to "good"
    y.loc[:, [
        'flag_vpden_ac', 'flag_vpvs_ac', 'flag_aivpvs_ac',
        'flag_vpvs_acs', 'flag_aivpvs_acs',
        'flag_vpden_den', 'flag_aivpvs_den']] =\
        0, 0, 0, 0, 0, 0, 0

    pred_gen_cols = ['flag_crossplot_gen', 'flag_vpden_gen', 'flag_aivpvs_gen', 'flag_vpvs_gen']
    y.loc[:, ['flag_crossplot_gen', 'flag_vpden_gen', 'flag_aivpvs_gen', 'flag_vpvs_gen']] =\
        0, 0, 0, 0        
    y.loc[vp_den_anomalies, ['flag_crossplot_gen', 'flag_vpden_gen']]   = 1
    y.loc[ai_vpvs_anomalies, ['flag_crossplot_gen', 'flag_aivpvs_gen']] = 1
    y.loc[vp_vs_anomalies, ['flag_crossplot_gen', 'flag_vpvs_gen']]     = 1

    #Add the general crossplot flags to X_pred(to use as features in the model)
    for col in pred_gen_cols:
        X_pred[col] = y[col]

    #Run the anomalous samples through the relevant trained model and get predictions
    #Preprocessing using key_wells will need the well_name column, but the value is unimportant
    X_pred['well_name'] = 'dummy'

    cp_preds = dict()
    for cp_name in cp_names:

        flag_name = 'flag_{}_gen'.format(cp_name.replace('_', ''))
        datasets[cp_name].load_from_df(X_pred)
        bad_logs = datasets[cp_name].df_original[datasets[cp_name].df_original['flag_crossplot_gen']!=0]

        
        if len(bad_logs) > 0:
           
            df_preprocessed, _, feats = datasets[cp_name].preprocess(
                datasets[cp_name].df_original.loc[bad_logs.index],
                _normalize_curves={'key_wells':key_wells[cp_name]}
                )
            cp_preds[cp_name] = models[cp_name].predict(df_preprocessed[feats])

            y['{}_tmp'.format(cp_name)] = 0
            y.loc[bad_logs.index, '{}_tmp'.format(cp_name)] = cp_preds[cp_name]

            #Map predictions depending on which crossplot they come from
            if cp_name == 'vp_den':
                y.loc[((y['{}_tmp'.format(cp_name)]==1)| (y['{}_tmp'.format(cp_name)]==3)), 'flag_vpden_ac'] = 1
                y.loc[((y['{}_tmp'.format(cp_name)]==2) | (y['{}_tmp'.format(cp_name)]==3)), 'flag_vpden_den'] = 1
                
            elif cp_name == 'vp_vs':
                y.loc[((y['{}_tmp'.format(cp_name)]==1) | (y['{}_tmp'.format(cp_name)]==3)), 'flag_vpvs_ac'] = 1
                y.loc[((y['{}_tmp'.format(cp_name)]==2) | (y['{}_tmp'.format(cp_name)]==3)), 'flag_vpvs_acs'] = 1
                
            elif cp_name == 'ai_vpvs':
                y.loc[((y['{}_tmp'.format(cp_name)]==4) | (y['{}_tmp'.format(cp_name)]==5) | (y['{}_tmp'.format(cp_name)]==6) | (y['{}_tmp'.format(cp_name)]==7)), 'flag_aivpvs_den'] = 1
                y.loc[((y['{}_tmp'.format(cp_name)]==1) | (y['{}_tmp'.format(cp_name)]==3) | (y['{}_tmp'.format(cp_name)]==5) | (y['{}_tmp'.format(cp_name)]==7)), 'flag_aivpvs_ac'] = 1
                y.loc[((y['{}_tmp'.format(cp_name)]==2) | (y['{}_tmp'.format(cp_name)]==4) | (y['{}_tmp'.format(cp_name)]==6) | (y['{}_tmp'.format(cp_name)]==7)), 'flag_aivpvs_acs'] = 1

    return y
