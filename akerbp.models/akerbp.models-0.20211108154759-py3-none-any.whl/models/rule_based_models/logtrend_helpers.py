import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

from akerbp.models.rule_based_models import helpers

### Log trends
def log_trends(logname, df_well, curves_to_diff, algo='comb'):
    """
    Finds anomalies based on the crossplots of differences between consecutive samples of two logs 

    Args:
        logname (string): which log name is being analysed
        df_well (pd.DataFrame): data from one well
        curves_to_diff (list): which curves to get crossplots with
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list of anomalous indices
    """
    df_well = df_well[df_well[logname]!=0].copy()
    if logname not in curves_to_diff:
        curves_to_diff = curves_to_diff + [logname]
    diff_curves = [f'{c}_diff' for c in curves_to_diff]
    df_well[diff_curves] = df_well[curves_to_diff].diff()
    anomal_idx = []
    for i, j in enumerate(curves_to_diff):
        tmp = df_well[
            (df_well[j]!=0) &\
            (df_well[j].notna()) &\
            (df_well[diff_curves[i]]!=0) &\
            (df_well[diff_curves[i]].notna())
        ].copy()
        if len(tmp)>10 and curves_to_diff!=logname:
            tmp_X = tmp[[f'{logname}_diff', diff_curves[i]]].dropna().copy()
            if len(tmp_X) > 0:
                if algo=='DBSCAN':
                    preds = DBSCAN(eps=0.1).fit_predict(tmp_X)
                elif algo=='EliEnv':
                    preds = EllipticEnvelope(contamination=0.01, random_state=0).fit_predict(tmp_X)
                elif algo=='SVM':
                    preds = OneClassSVM(gamma='scale', nu=0.01).fit_predict(tmp_X)
                elif algo=='IsoFor':
                    preds = IsolationForest(n_estimators=50, contamination=0.01, random_state=0).fit_predict(tmp)
                elif algo=='comb':
                    preds1 = DBSCAN(eps=0.4).fit_predict(tmp_X)
                    try:
                        preds2 = EllipticEnvelope(contamination=0.01, random_state=0).fit_predict(tmp_X)
                    except:
                        preds2 = np.zeros(len(tmp_X))
                    preds3 = OneClassSVM(gamma='scale', nu=0.005).fit_predict(tmp_X)
                    preds4 = IsolationForest(n_estimators=50, contamination=0.005, random_state=0).fit_predict(tmp_X)
                    preds  = np.where(preds1==-1, 1, 0) +\
                            np.where(preds2==-1, 1, 0) +\
                            np.where(preds3==-1, 1, 0) +\
                            np.where(preds4==-1, 1, 0)
                if algo=='comb':
                    tmp_X['pred'] = np.where(preds>1, 1, 0)
                else:
                    tmp_X['pred'] = np.where(preds==-1, 1, 0)
    
                anomal_idx.append(list(tmp_X[tmp_X.pred==1].index))

    return sum(anomal_idx, [])

def flag_logtrend(df_well, y_pred=None, **kwargs):
    """
    Returns anomalous indices for AC, ACS and DEN based on log trends

    Args:
        df_well (pd.DataFrame): data from one well

    Returns:
        tuple: lists of anomalous indices of AC, ACS and DEN
    """
    print('Method: logtrend...')
    if y_pred is None:
        y_pred = df_well.copy()

    y_pred.loc[:, ['flag_logtrend_gen', 'flag_logtrend_ac', 'flag_logtrend_acs', 'flag_logtrend_den']] =\
        0, 0, 0, 0

    if 'CALI_BS' not in df_well.columns:
        df_well['CALI_BS'] = np.abs(df_well['CALI'] - df_well['BS'])
    default_curves = ['CALI', 'GR', 'NEU', 'CALI_BS']
    curves_to_diff = kwargs.get('curves_to_diff', default_curves)

    if 'GROUP' in curves_to_diff:
        curves_to_diff.remove('GROUP')
    ac_trends_anomalies   = log_trends('AC', df_well, [c for c in curves_to_diff if c!='VP'])
    acs_trends_anomalies  = log_trends('ACS', df_well, [c for c in curves_to_diff if c!='VS'])
    den_trends_anomalies  = log_trends('DEN', df_well, curves_to_diff)

    y_pred.loc[ac_trends_anomalies, 'flag_logtrend_ac']    = 1
    y_pred.loc[acs_trends_anomalies, 'flag_logtrend_acs']  = 1
    y_pred.loc[den_trends_anomalies, 'flag_logtrend_den']  = 1

    y_pred['flag_logtrend_ac']  = helpers.fill_holes(y_pred, 'flag_logtrend_ac')
    y_pred['flag_logtrend_acs'] = helpers.fill_holes(y_pred, 'flag_logtrend_acs')
    y_pred['flag_logtrend_den'] = helpers.fill_holes(y_pred, 'flag_logtrend_den')

    y_pred.loc[y_pred.flag_logtrend_ac==1, 'flag_logtrend_gen']  = 1
    y_pred.loc[y_pred.flag_logtrend_acs==1, 'flag_logtrend_gen'] = 1
    y_pred.loc[y_pred.flag_logtrend_den==1, 'flag_logtrend_gen'] = 1

    return y_pred
