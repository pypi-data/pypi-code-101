# encoding: utf-8
'''
@author: zyl
@file: utils.py
@time: 2021/11/11 9:35
@desc:
'''

import pandas as pd


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def to_excel(dataframe, excel_path, sheet_name='default'):
        try:
            from openpyxl import load_workbook
            book = load_workbook(excel_path)
            writer = pd.ExcelWriter(excel_path, engine='openpyxl')
            writer.book = book
        except:
            writer = pd.ExcelWriter(excel_path, engine='openpyxl')

        dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()
