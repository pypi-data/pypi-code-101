import pandas as pd
import logging
from pathlib import Path
from proai.constants import DATA_DIR

log = logging.getLogger(__name__)


def clean_df_columns(df=None, columns=None, drop_unknown_columns=True):
    r""" Return DataFrame with normalized column names: lower() strip() " "->"_"
    """
    columns = df.columns if columns is None else columns
    if isinstance(columns, str):
        columns = [columns]
    else:
        # df = df if isinstance(df, pd.DataFrame) else None
        columns = list(columns)
    new_column_names = [c.lower().strip().replace(' ', '_') for c in columns]
    column_name_map = dict(zip(columns, new_column_names))
    df = df.rename(columns=column_name_map)
    if drop_unknown_columns:
        unknown_columns = [
            c for c in new_column_names if c.lower().lstrip().startswith('unknown')]
        for c in unknown_columns:
            df.drop(c, inplace=True)
    return df


def make_filepath(filepath,
                  data_dirs=('', DATA_DIR),
                  suffixes='.csv .tsv'.split()):
    """ TODO: strip leading / to try abs and rel path """
    filepath = Path(filepath)
    names = (filepath, filepath.name, filepath.with_suffix(''))
    for pref in data_dirs:  # , SHARED_DATA_DIR)
        for suf in suffixes:
            for name in names:
                for suf2 in [''] + '.gz .zip .bz2'.split():
                    p = Path(pref) / Path(name)
                    # separate branch for if p.suffix p.suffix + suf + suf2
                    if suf:
                        if suf2:
                            p = p.with_suffix(suf + suf2)
                        else:
                            p = p.with_suffix(suf)
                    else:
                        if suf2:
                            p = p.with_suffix(suf2)
                    if p.is_file():
                        return p


def make_df(df_or_filepath,
            column_name_cleaner=clean_df_columns,
            drop_unknown_columns=True,
            low_memory=False,
            index_col=0,
            **kwargs):
    """ Construct DataFrame from filepath or array-like object

    >>> df =  make_df([
    ...     dict(hi='world', bye='planet'),
    ...     dict(hi=1, low=-1),
    ...     ])
    >>> df.shape
    (2, 3)
    >>> df
          hi     bye  low
    0  world  planet  NaN
    1      1     NaN -1.0
    """
    try:
        df_or_filepath = pd.DataFrame(
            data=df_or_filepath.copy(),
            columns=list(df_or_filepath.columns.values),
            index=list(df_or_filepath.index.values))
    except AttributeError:
        pass
    if isinstance(df_or_filepath, (Path, str)):
        p = make_filepath(df_or_filepath)
        df_or_filepath = pd.read_csv(str(p), low_memory=low_memory, index_col=index_col, **kwargs)
    if not isinstance(df_or_filepath, pd.DataFrame):
        try:
            return pd.DataFrame(df_or_filepath,
                                index_col=index_col,
                                low_memory=low_memory, **kwargs)
        except Exception:
            pass
            # look for files [with_suffix('.csv') '.gz', '.csv.gz']
    if column_name_cleaner:
        return column_name_cleaner(df_or_filepath,
                                   drop_unknown_columns=drop_unknown_columns)
    return df_or_filepath


def make_series(series_or_filepath, colnum=-1):
    """ Construct a Series from filepath or array-like object

    >>> series = make_series(DATA_DIR / )
    >>> series.shape
    (200,)
    >>> series.name
    'changed_college_Y2'
    >>> series2 = load_series(series)
    >>> series2.shape == series.shape
    True
    >>> series.name == series2.name
    True
    >>> series.values.sum() == series.values.sum()
    True
    """
    try:
        return pd.Series(
            data=series_or_filepath.copy(),
            index=list(series_or_filepath.index.values))
    except AttributeError:
        if isinstance(series_or_filepath, (Path, str)):
            series_or_filepath = pd.read_csv(series_or_filepath)
    if len(series_or_filepath.shape) == 1:
        return pd.Series(series_or_filepath)
    elif series_or_filepath.shape[1] == 1:
        return pd.Series(series_or_filepath)
    elif series_or_filepath.shape[0] == 1:
        return pd.Series(series_or_filepath.iloc[0])
    else:
        return series_or_filepath[list(series_or_filepath.columns)[colnum]]
    return pd.Series(series_or_filepath)
