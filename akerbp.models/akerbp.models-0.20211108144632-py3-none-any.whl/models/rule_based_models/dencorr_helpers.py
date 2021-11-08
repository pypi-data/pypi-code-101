import numpy as np

from models.rule_based_models import BS_helpers
from models.rule_based_models import crossplot_helpers

def flag_dencorr(df_well, y_pred=None, **kwargs):
    """
    Returns anomalous density corrections

    Args:
        df_well (pd.DataFrame): [description]

    Returns:
        [type]: [description]
    """
    print('Method: Density correction...')
    if y_pred is None:
        y_pred = df_well.copy()

    x = 'DEN'
    y = 'DENC'
    df_well = BS_helpers.find_BS_jumps(df_well).copy()
    y_pred.loc[:, ['flag_dencorr_gen', 'flag_dencorr_den']] =\
        0, 0
    dencorr_anomalies = []
    if df_well['BS_region'].nunique() < 10:
        for i, bsr in enumerate(df_well['BS_region'].unique()):
            df_gr = df_well[df_well['BS_region']==bsr].copy()
            if (df_gr[x].dropna().shape[0] != 0) and (df_gr[y].dropna().shape[0] != 0):
                anomalies, _, _ = crossplot_helpers.find_crossplot_scores(df_gr, x=x, y=y, **kwargs)
                unacceptable_denc = set(df_gr.loc[np.abs(df_gr['DENC']>0.1)].index.tolist())
                dencorr_anomalies.extend(list(set(anomalies).intersection(unacceptable_denc)))
    y_pred.loc[dencorr_anomalies, ['flag_dencorr_gen', 'flag_dencorr_den']] = 1
    return y_pred