import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

from models.rule_based_models import helpers

### Log outliers
def log_outliers(logname, df_well, curves, algo='comb'):
    """
    Finds anomalies based on the crossplots of values of two logs 

    Args:
        logname (string): which log name is being analysed
        df_well (pd.DataFrame): data from one well
        curves (list): which curves to get crossplots with
        algo (str, optional): which algorithm to use. Defaults to 'comb'.

    Returns:
        list: list of anomalous indices
    """
    df_well = df_well[(df_well[logname]!=0) & (df_well[logname].notna())].copy()
    if logname not in curves:
        curves = curves + [logname]
    
    anomal_idx = []
    for i, j in enumerate(curves):
        tmp = df_well[
            (df_well[j]!=0) &\
            (df_well[j].notna())
        ].copy()
        if len(tmp)>10 and curves!=logname:
            tmp_X = tmp[[logname, j]].dropna().copy()
            if len(tmp_X) > 0:
                if algo=='DBSCAN':
                    preds = DBSCAN(eps=0.1).fit_predict(tmp_X)
                elif algo=='EliEnv':
                    preds = EllipticEnvelope(contamination=0.01, random_state=0).fit_predict(tmp_X)
                elif algo=='SVM':
                    preds = OneClassSVM(gamma='scale', nu=0.01).fit_predict(tmp_X)
                elif algo=='IsoFor':
                    preds = IsolationForest(n_estimators=50, contamination=0.01, random_state=0).fit_predict(tmpX)
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

def flag_outliers(df_well, y_pred=None, **kwargs):
    """
    Returns anomalous indices for AC, ACS and DEN based on outliers of crossplots between AC, ACS and DEN
    and other curves

    Args:
        df_well (pd.DataFrame): data from one well

    Returns:
        tuple: lists of anomalous indices of AC, ACS and DEN
    """
    print('Method: outliers...')
    if y_pred is None:
        y_pred = df_well.copy()

    y_pred.loc[:, ['flag_outliers_gen', 'flag_outliers_ac', 'flag_outliers_acs', 'flag_outliers_den']] =\
        0, 0, 0, 0

    if 'CALI_BS' not in df_well.columns:
        df_well['CALI_BS'] = np.abs(df_well['CALI'] - df_well['BS'])
    if 'RDEP_log' not in df_well.columns and 'RDEP' in df_well.columns:
        df_well['RDEP_log'] = np.log10(df_well.RDEP)
    default_curves = ['AC', 'CALI', 'GR', 'NEU', 'PEF', 'RDEP_log', 'CALI_BS']
    curves = kwargs.get('curves', default_curves)

    if 'GROUP' in curves:
        curves.remove('GROUP')
    ac_outliers_anomalies   = log_outliers('AC', df_well, [c for c in curves if c!='VP'])
    acs_outliers_anomalies  = log_outliers('ACS', df_well, [c for c in curves if c!='VS'])
    den_outliers_anomalies  = log_outliers('DEN', df_well, curves)

    y_pred.loc[ac_outliers_anomalies, 'flag_outliers_ac']    = 1
    y_pred.loc[acs_outliers_anomalies, 'flag_outliers_acs']  = 1
    y_pred.loc[den_outliers_anomalies, 'flag_outliers_den']  = 1

    y_pred['flag_outliers_ac']  = helpers.fill_holes(y_pred, 'flag_outliers_ac')
    y_pred['flag_outliers_acs'] = helpers.fill_holes(y_pred, 'flag_outliers_acs')
    y_pred['flag_outliers_den'] = helpers.fill_holes(y_pred, 'flag_outliers_den')

    y_pred.loc[y_pred.flag_outliers_ac==1, 'flag_outliers_gen']  = 1
    y_pred.loc[y_pred.flag_outliers_acs==1, 'flag_outliers_gen'] = 1
    y_pred.loc[y_pred.flag_outliers_den==1, 'flag_outliers_gen'] = 1

    return y_pred
