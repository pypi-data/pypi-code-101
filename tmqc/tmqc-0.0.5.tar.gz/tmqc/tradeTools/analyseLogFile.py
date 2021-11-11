# -*- coding: utf-8 -*-
# 对策略的回测日志分析
import pandas as pd
import json
import os
import re
import sys
import requests
import datetime
from  tmqc.common import basefunc
from tmqc.frame import data_center
CON_NET_VALUE_FILENAME = "stock_day_net_value.log" # 要读取的日志文件名
STRATEGY_PATH_CONF = [os.path.dirname(os.path.dirname(__file__)),"reversal","log_500等权"]
# STRATEGY_PATH_CONF = [os.path.dirname(os.path.dirname(__file__)),"reversal","log_500市值加权"]
# pathCnf = [STRATEGY_PATH, f"{CON_NET_VALUE_FILENAME}.log"]
path = os.sep.join(STRATEGY_PATH_CONF)
full_path = path + os.sep + CON_NET_VALUE_FILENAME
print(full_path)


class Mgr():
    def __init__(self):
        self.oldDc = data_center.use()
        self.df = self.load()

    def genIDXData(self,symbol="SH.000905"):
        # 获取指数月度收益率数据
        if not hasattr(self, "oldDc"):
            self.oldDc = data_center.use()
        sql = "SELECT "
        sql += f" code,time,close from `index_day_data` WHERE code = '{symbol}'"
        df = pd.read_sql(sql, self.oldDc.database.conn)
        df['date'] = pd.to_datetime(df['time'], format='%Y%m%d')
        df.set_index('date', inplace=True)
        df[f"{symbol}收益率"] = df.close / df.close.shift(1) - 1
        return df

    def load(self):
        df = pd.read_csv(full_path,engine='python', encoding='gb2312', sep='\t')
        df['date'] = pd.to_datetime(df['日期'], format='%Y%m%d')
        df.set_index('date', inplace=True)
        return df

    def concat(self):
        indexSymbol = "SH.000905"
        df = pd.concat([self.df,self.genIDXData()],axis = 1,join="inner")
        dateIdx = df[df['净值']!= 1].iloc[0].name # 首次开仓日期
        df = df[df.index>=dateIdx].copy()
        df["中证500"] = (1 + df[f"{indexSymbol}收益率"]).cumprod()
        name = path+os.sep+f"{STRATEGY_PATH_CONF[-1]}.xlsx"
        df.to_excel(name, sheet_name="数据源")
# def genYearReport():
#
#     df = df.resample('Y').last()
#     # Index(['日期', '净值', '回撤', '上证指数', '上证回撤', '沪深300', '沪深300回撤', '上证50', '上证50回撤',
#     #        '资产', '利润', '保证金', '手续费', '滑点损失'],
#     #       dtype='object')
#     df.to_excel("年度净值报告 .xlsx", sheet_name="数据源")

if __name__ == '__main__':
    mgr = Mgr()
    mgr.concat()
