import os
import re
import datetime as dt

import pandas
import numpy as np


def most_frequent(List):
    return max(set(List), key = List.count)

def add_meta(item, created=False):
    item['updated_at'] = dt.datetime.now()
    item['updated_by'] = os.environ.get('ANALYST')
    if created:
        item['created_at'] = dt.datetime.now()
    return item


def loop_string_replace(replacedict, string, regex=True):
    for key, value in replacedict.items():
        string = re.sub(key, value, string) if regex == True\
                else string.replace(key, value)
    return string


def produce_allrows(df):
    """Make column containing string of row's concatenated values.
    Parameters
    ----------
    df : dataframe from which to combine row values in "allrows" column

    Returns
    -------
    dfcopy : dataframe
        Copy of original dataframe with "allrows" column
    """
    dfcopy = df.copy()
    l = lambda row: ''.join(str(x) for x in row.to_dict().values())\
    .replace("\n", "\\n")
    dfcopy['allrows'] = dfcopy.fillna("").apply(l, axis=1).copy()
    return dfcopy


def return_range(value, multiplier=.05):
    """Return tuple of values representing a range of the value given.
    """
    try:
        value = float(value)
    except ValueError:
        # unaddressed exception triggers: '4130/7140','43 g',
        if value == None:
            value = 0
    value_low = round(value - value*multiplier)
    value_high = round(value + value*multiplier)
    return (value_low, value_high)




### DataFrame Analysis Functions ###

def strip_col_from_col(df, col_a, col_b):
    """Returns col_a with col_b values stripped from corresponding rows.

    Parameters
    ----------
    df : dataframe
        Dataframe containing col_a and col_b
    col_a : str
        String corresponding to name of column a
    col_b : str
        String corresponding to name of column b
    """
    return [str(a).replace(str(b), '').strip() for a, b in zip(\
            df[col_a], df[col_b])]


def find_rows_with_val(df, value, rex=True, flags=False):
    """ Search across full dataframe rows for a specified value.

    Parameters
    ----------
    value : str
        The string which will be searched for across all rows.
    rex : boolean
        If True, use regex to search for value string.
    flags : boolean
        If not false, add designated flag or flags. Makes regex true by default.

    Returns
    -------
    rows : dataframe
        copied dataframe of rows containing the value among its columns.
    """
    params = {"regex":True, "flags":flags} if flags else\
            {"regex":rex}
    df_allrows = produce_allrows(df)
    rows = df_allrows.loc[df_allrows["allrows"].str.contains\
            (value, **params)].copy()
    rows.drop(columns="allrows", inplace=True)
    return rows

def remove_rows_with_val(df, value, rex=True, flags=False):
    """ Return dataframe with rows that don't contain the specified string value.

    Parameters
    ----------
    value : str
        The string which will be searched for across all rows.
    rex : boolean
        If True, use regex to search for value string.
    flags : boolean
        If not false, add designated flag or flags. Makes regex true by default.

    Returns
    -------
    rows : dataframe
        copied dataframe of rows containing the value among its columns.
    """
    params = {"regex":True, "flags":flags} if flags else\
            {"regex":rex}
    df_allrows = produce_allrows(df)
    df = df_allrows.loc[~df_allrows["allrows"].str.contains\
        (value, **params)].copy()
    df.drop(columns="allrows", inplace=True)
    return df


def one_value_in_df(df):
    a = df.to_numpy() # s.values (pandas<0.24)
    return (a[0] == a).all()


def return_rows_with_one_value(df):
    """ Return dataframe rows that contain only one col value.
    2. make boolean column reflecting whether the column value is equal
        to any other columns in the row.
    3. return copied dataframe slice of all rows with True boolean value
    """
    df_allrows = produce_allrows(df)
    df_allrows["allrows"] = df_allrows["allrows"].str.\
            replace("nan", "", regex=False)
    df_allrows["exists"] = df_allrows.drop(columns="allrows").\
            isin(df_allrows["allrows"]).any(1)
    one_val = df_allrows.loc[df_allrows['exists'] == True].copy()
    one_val.drop(columns=["allrows","exists"], inplace=True)
    return one_val

def count_occurrences_in_rows(df, substring):
    """ Count occurrence of a given substring in the rows of a dataframe.
    Parameters
    ----------
    df : dataframe
    substring : string
        partial or full string to count the occurrence of in dataframe rows
    """
    df_allrows = produce_allrows(df)
    df_allrows['count'] = df_allrows.allrows.str.count(substring)

    return df_allrows.drop(columns="allrows")



### DataFrame Alteration Functions ###

def loop_replace_on_col(replacedict, df, col, reg=True):
    for key, value in replacedict.items():
        df[col] = df[col].str.replace(key, value, regex=True)
    return df

def recombine_rows(df, row1, row2):#recombine_dict):
    """combine the cells of two dataframe rows by column.
    Parameters
    ----------
    df : dataframe
        The dataframe on which row recombination is to be performed
    row1 : integer
    row2 : integer
    """
    for index, row in df.iloc[[row2]].iterrows():
        for k, v in row.items():
            df.loc[row1, k] += " {}".format(v)
    return df



# def recombine_rows(df, row_one_idx_list):#recombine_dict):
#     """combines two rows' cells.
#     Parameters
#     ----------
#     df : dataframe
#         The dataframe on which row recombination is to be performed
#     recombine_dict : dict
#         Dict of start and end indices for row recombination.
#     """
#     # s = ' '.join(df['text'])
#     # df.loc[]
#     idx_list = [i + 1 for i in row_one_idx_list]
#     for index, row in df.iloc[[1]].iterrows():
#         for k, v in row.items():
#             df.loc[index - 1, k] += " {}".format(v)
#     df.drop(1, inplace=True)
#     df.reset_index(drop=True, inplace=True)
#     print("post-recombine_rows:\n", df)
#     return df

def recombine_header_rows(df, header_idx_list):
    """Merge header row that is split into multiple rows back into one row.

    Parameters
    ----------
    df : DataFrame
    header_idx_list : list
        list of lists in which each list begins with the index of the first
        row to be combined and ends with the index of the last.
    """
    droprows = []
    for l in header_idx_list:
        if isinstance(l, list):
            diff = l[-1]-l[0]
            for i in range(1, 1+diff):
                df = recombine_rows(df, l[0], l[0]+i)
                droprows.append(l[0]+i)
    df = df.drop(df.index[droprows]).reset_index(drop=True)
    return df

def rename_cols_by_index(df, keep=True):
    """rename dataframe columns by column order in the dataframe, starting with 0

    Parameters
    ----------
    df : DataFrame
    keep : bool, optional (default True)
        If True, keep the header column that is being overwritten.
    """
    if keep == True:
        df = df.columns.to_frame().T.append(df, ignore_index=True)
    rename_dict = dict(zip(df.columns.values.tolist(), range(len(df.columns))))
    df = df.rename(columns=rename_dict)
    return df

def set_first_row_as_header(df, corrections=True, droprow=True):
    firstrow_list = df.loc[0].tolist()
    if corrections == True:
        firstrow_list = [i.lower().strip("_ ") for i in firstrow_list]
    rename_dict = dict(zip(df.columns.values.tolist(), firstrow_list))
    df = df.rename(columns=rename_dict)
    df = df.drop(0).reset_index(drop=True) if droprow == True else df
    return df


def align_vals(df, subset, cols=None, col=0, neg_cols=["rowtype", "serving_size_unit", "menu_section"]):
    """
    put all values for one-column rows into same column, then delete
    values in that row outside the alignment column.

    Parameters
    ----------
    df : dataframe from which to combine row values in "allrows" column
    cols: list, optional

    Returns
    -------
    df : dataframe
    """
    in_subset = df.index.isin(subset.index)
    alignment_col = str(df.columns.values[col])
    if cols == None:
        l = lambda row: ''.join(str(v) for k,v in row.to_dict().\
                items() if k not in neg_cols)
    else:
        l = lambda row: ''.join(str(v) for k, v in row.to_dict().\
                items() if k in cols)
    df.loc[in_subset, alignment_col] = df.fillna("").apply(l, axis=1)
    df = df.fillna("")
    # print([str(column) for column in df])
    for column in df:
        if cols == None:
            if str(column) != alignment_col and str(column) not in neg_cols:
                df.loc[in_subset, column] = ""
        else:
            if str(column) in cols:
                df.loc[in_subset, column] = ""

    return df


def delete_all_na(df, subset=None, fill=True):
    """Delete empty rows/cols and return df with nulls as empty strings.

    Parameters
    ----------
    df : dataframe
        Dataframe from which to delete null rows/columns.
    subset : str {"rows", "cols", or None}, default None
        Limit to only rows or columns.
    fill : bool, default False
        If true, don't replace NaNs with empty strings before returning.

    Returns
    -------
    df : dataframe
        Dataframe with deleted null rows/columns.
    """
    df = df.replace('', np.nan)

    if subset == "rows":
        df.dropna(how='all', inplace=True)
    elif subset == "cols":
        df.dropna(axis=1, how='all', inplace=True)
    elif subset == None:
        df.dropna(how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)
    else:
        raise ValueError('Unrecognized subset value')

    if fill == True:
        df.fillna("", inplace=True)
    elif fill == False:
        pass
    else:
        raise ValueError('Unrecognized fillna value')
    return df
