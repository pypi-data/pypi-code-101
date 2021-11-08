import pandas as pd
import os.path

def parser(excel_file):
    """
    Parses the excel file to extract the dataframes

    :param excel_file: .xlsx file with multiple sheets
    :return: the individual dataframes, w and Sb
    """

    xlsx = pd.ExcelFile(excel_file)
    ids = xlsx.sheet_names
    d = {}
    for sheet in ids:
            d[f'{sheet}'] = pd.read_excel(xlsx, sheet_name=sheet)

    df_global = pd.read_excel(xlsx, sheet_name='Global')
    w = df_global['w (rad/s)'].values[0]
    Sb = df_global['S base (MVA)'].values[0]

    return d, w, Sb
