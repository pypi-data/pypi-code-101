import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

from akerbp.models.rule_based_models import BS_helpers

def find_anomaly_scores(df_):
    """
    Find anomalies and their scores in 'CALI-BS' data for washout method 

    Args:
        df_ (pd.DataFrame): dataframe with CALI and BS columns

    Returns:
        tuple: anomalies indices, scores and full indices list
    """
    if 'CALI' in df_.columns and 'BS' in df_.columns:
        df_.loc[:, 'CALI_BS'] = np.abs(df_['CALI'] - df_['BS'])
        df = df_[(df_['CALI_BS']!=0)].copy()

        anomal_idx = []
        tmp    = df[df['CALI_BS'].notna()].copy()
        tmpre  = tmp.CALI_BS.values.reshape(-1,1)
        scores = dict()
        if len(tmp)>10:
            # dbscan
            preds1 = DBSCAN(eps=0.02).fit_predict(tmpre)
            # svm
            svm = OneClassSVM(gamma='scale', nu=0.01).fit(tmpre)
            preds2 = svm.predict(tmpre)
            scores['SVM'] = svm.score_samples(tmpre)
            # isolation forest
            ifo = IsolationForest(
                n_estimators=20,
                contamination=0.05,
                random_state=0
                ).fit(tmpre)
            preds3 = ifo.predict(tmpre)
            scores['IsoFor'] = ifo.score_samples(tmpre)
            # combine predictions
            preds  = np.where(preds1==-1, 1, 0) +\
                    np.where(preds2==-1, 1, 0) +\
                    np.where(preds3==-1, 1, 0)
            tmp.loc[:, 'pred'] = np.where(preds>1, 1, 0)
            anomal_idx.append(list(tmp[tmp.pred==1].index))
        return sum(anomal_idx, []), scores, tmp.index    
    else:
        raise ValueError ('Washout method error: CALI and/or BS are not present in dataframe')

def flag_washout(df_well, y_pred=None, **kwargs):
    """
    Returns anomalous CALI-BS

    Args:
        df_well (pd.DataFrame): [description]

    Returns:
        [type]: [description]
    """
    print('Method: washout...')
    if y_pred is None:
        y_pred = df_well.copy()

    y_pred.loc[:, ['flag_washout_gen', 'flag_washout_den']] = 0, 0

    x = 'CALI'
    y = 'BS'
    df_well = BS_helpers.find_BS_jumps(df_well)
    den_washout_anomalies = []
    if df_well['BS_region'].nunique() < 10:
        for i, bsr in enumerate(df_well['BS_region'].unique()):
            df_gr = df_well[df_well['BS_region']==bsr].copy()
            if (df_gr[x].dropna().shape[0] != 0) and (df_gr[y].dropna().shape[0] != 0):
                preds, _, _ = find_anomaly_scores(df_gr)
                den_washout_anomalies.extend(preds)

    y_pred.loc[den_washout_anomalies, ['flag_washout_gen', 'flag_washout_den']] = 1
    return y_pred
