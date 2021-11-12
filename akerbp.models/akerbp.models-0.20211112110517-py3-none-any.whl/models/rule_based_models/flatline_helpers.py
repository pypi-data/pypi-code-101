import numpy as np

### Flatline anomalies
def get_constant_derivatives(df, logname, th=0.0005):
    """
    Returns indices of anomalous samples based on derivatives lower than a threshold

    Args:
        df (pd.DataFrame): dataframe with data to analyse
        logname (str): curve to be flagged, if any
        th (float, optional): threshold to which lower values will be considered constant. Defaults to 0.0005.

    Returns:
        list: indices of constant derivatives
    """
    df['d1']              = np.gradient(df[logname], df['DEPTH'])
    df['d2']              = np.gradient(df['d1'], df['DEPTH'])
    df['cnst_derivative'] = np.abs(df['d1']-df['d2'])<th
    return df[df['cnst_derivative']==True].index

def get_constant_windows(df, logname, window_size=10, min_periods=5, th=0.0005):
    """
    Returns indices of anomalous samples based on derivatives lower than a threshold within a window

    Args:
        df (pd.DataFrame): dataframe with data to analyse
        logname (str): curve to be flagged, if any
        window_size (int): size of window
        min_periods (int): min_periods of rolling window
        th (float, optional): threshold to which lower values will be considered constant. Defaults to 0.0005.

    Returns:
        list: indices of constant derivatives
    """
    df['minw']        = df[logname].rolling(window_size, min_periods=min_periods, center=True).min()
    df['maxw']        = df[logname].rolling(window_size, min_periods=min_periods, center=True).max()
    df['cnst_window'] = np.abs(df['maxw']-df['minw'])<th
    return df[df['cnst_window']==True].index

def get_den_flatlines(df, th=0.002):
    """
    Returns flatlines specifically for density, where threshold was decided empirically

    Args:
        df (pd.DataFrame): dataframe with data to analyse
        th (float, optional): threshold to which lower values will be considered constant. Defaults to 0.002.

    Returns:
        list: indices of anomalous density samples
    """
    df['DEN_flat'] = np.gradient(df['DEN'])
    idx = df[
        (np.abs(df['DEN_flat'].diff())<th) &\
        (np.abs(df['DEN_flat'].diff(-1))<th)
    ].index
    return idx

def get_flatlines(df, logname, cols, window=5, n_cols=2):
    """
    Returns indices of anomalous values indicating flatline badlog

    Args:
        df (pd.DataFrame): data to analyze
        logname (str): logname to find anomalies
        cols (list): list of curves to analyse logname against
        window (int, optional): window size for window constant derivatives. Defaults to 10.

    Returns:
        list: indices of flatlines anomlies
    """
    # get gradients and see if one gradient is not as small as at least three other curves
    cols_grad     = [c+'_gradient' for c in cols]
    gradient_flag = (df[f'{logname}_gradient']<df[f'{logname}_gradient'].rolling(10, center=True).std()) &\
                    (np.sum(df[cols_grad]>df[cols_grad].rolling(10, center=True).std(), axis=1)>n_cols)
    # get variance
    variance      = df[[logname]+cols].rolling(window).var()
    variance_flag = (variance[logname]<variance[logname].rolling(10, center=True).std()) &\
                    (np.sum(variance[cols]>variance[cols].rolling(10, center=True).std(), axis=1)>n_cols)
    # flatlines
    flatlines = gradient_flag | variance_flag
    return flatlines[flatlines==True].index

def flag_flatline(df_well, y_pred=None, **kwargs):
    """
    Returns flatlines indices for AC, ACS and DEN

    Args:
        df_well (pd.DataFrame): data from one well

    Returns:
        tuple: lists of gradient anomalies for AC, ACS and DEN
    """
    print('Method: flatline...')
    if y_pred is None:
        y_pred = df_well.copy()

    expected_curves = kwargs.get('expected_curves', set(['DEN', 'AC', 'ACS', 'GR', 'NEU', 'RDEP', 'RMED']))
    cols        = kwargs.get('cols', expected_curves)
    window_size = kwargs.get('window', 5)
    ncols       = kwargs.get('ncols', 2)

    y_pred.loc[:, ['flag_flatline_gen', 'flag_flatline_ac', 'flag_flatline_acs', 'flag_flatline_den']] =\
        0, 0, 0, 0

    for col in cols:
        df_well.loc[:, col+'_gradient'] = np.abs(np.gradient(df_well[col]))

    ac_grad_anomalies = get_flatlines(
        df=df_well, 
        logname='AC', 
        cols=list(set(cols) - set(['AC'])), 
        window=window_size,
        n_cols=ncols
    )
    acs_grad_anomalies = get_flatlines(
        df=df_well, 
        logname='ACS',
        cols=list(set(cols) - set(['ACS'])), 
        window=window_size,
        n_cols=ncols
    )
    den_grad_anomalies = get_flatlines(
        df=df_well, 
        logname='DEN', 
        cols=list(set(cols) - set(['DEN'])), 
        window=window_size,
        n_cols=ncols
    )

    ac_grad_anomalies  = ac_grad_anomalies.append(get_constant_derivatives(df_well, 'AC'))
    acs_grad_anomalies = acs_grad_anomalies.append(get_constant_derivatives(df_well, 'ACS'))
    den_grad_anomalies = den_grad_anomalies.append(get_constant_derivatives(df_well, 'DEN'))

    ac_grad_anomalies  = ac_grad_anomalies.append(get_constant_windows(df_well, 'AC'))
    acs_grad_anomalies = acs_grad_anomalies.append(get_constant_windows(df_well, 'ACS'))
    den_grad_anomalies = den_grad_anomalies.append(get_constant_windows(df_well, 'DEN'))

    den_grad_anomalies = den_grad_anomalies.append(get_den_flatlines(df_well))

    y_pred.loc[ac_grad_anomalies, ['flag_flatline_gen', 'flag_flatline_ac']]    = 1
    y_pred.loc[acs_grad_anomalies, ['flag_flatline_gen', 'flag_flatline_acs']]  = 1
    y_pred.loc[den_grad_anomalies, ['flag_flatline_gen', 'flag_flatline_den']]  = 1

    return y_pred