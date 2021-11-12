"""
市场结构的测试代码部分
"""
import pandas as pd
import numpy as np
import os
import datetime
import statsmodels.api as sm
from hbshare.rm_associated.util.data_loader import get_trading_day_list
from hbshare.quant_research.MarketStructure import MarketHist, MarketStructure, AlphaSeries
from tqdm import tqdm


data_path = "D:\\研究基地\\Analysis"


def run_daily_plot(start_date, end_date):
    date_list = get_trading_day_list(start_date, end_date)
    for date in tqdm(date_list):
        MarketHist(date, '000905').daily_plot()


def run_market_structure(start_date, end_date):
    date_list = get_trading_day_list(start_date, end_date)
    all_res = []
    for date in tqdm(date_list):
        res = MarketStructure(date, '000905').get_construct_result()
        all_res.append(res)

    structure_all = pd.concat(all_res)
    structure_all.to_csv(os.path.join(data_path, "market_structure.csv"))


def run_turnover_rate(start_date, end_date):
    from WindPy import w
    w.start()

    res = w.wsd("000001.SH,399001.SZ", "amt", start_date, end_date, "")
    if res.ErrorCode != 0:
        data = pd.DataFrame()
        print("fetch amt data error: start_date = {}, end_date = {}".format(
            start_date, end_date))
    else:
        if len(res.Data) == 1:
            data = pd.DataFrame(res.Data[0], index=res.Codes, columns=res.Times).T
        else:
            data = pd.DataFrame(res.Data, index=res.Codes, columns=res.Times).T
        data.index.name = 'trade_date'
        data.reset_index(inplace=True)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
        data.rename(columns={"000001.SH": "amt_sh", "399001.SZ": "amt_sz"}, inplace=True)
        data = (data.set_index('trade_date') / 1e+8).reset_index()
    amt = data.copy()
    amt['market_A'] = amt['amt_sh'] + amt['amt_sz']
    amt.to_csv(os.path.join(data_path, 'market_turnover.csv'), index=False)


def run_analysis(start_date, end_date):
    structure_df = pd.read_csv(os.path.join(data_path, 'market_structure.csv'), index_col=0)
    structure_df['trade_date'] = structure_df.index
    structure_df['trade_date'] = structure_df['trade_date'].map(str)
    structure_df = structure_df.set_index('trade_date')
    turn_over = pd.read_csv(os.path.join(data_path, 'market_turnover.csv'), dtype={"trade_date": str})
    turn_over['market_A'] /= 1e+4
    turn_over.rename(columns={"market_A": "turn_value"}, inplace=True)
    structure_df = pd.merge(
        turn_over.set_index('trade_date')['turn_value'], structure_df, left_index=True, right_index=True)

    alpha_excess = AlphaSeries(start_date, end_date).calculate()
    idx = structure_df.index.intersection(alpha_excess.index)
    structure_df = structure_df.reindex(idx)
    alpha_excess = alpha_excess.reindex(idx)
    structure_df['alpha_excess'] = alpha_excess

    structure_df.corr()

    # 先尝试一下线性回归
    y = np.array(alpha_excess)
    x = sm.add_constant(np.array(structure_df[['skew', 'lose_med', 'size_return', 'ind_cr']]))
    model = sm.OLS(y, x).fit()
    y_predict = model.predict(x)
    y_predict = pd.Series(index=alpha_excess.index, data=y_predict)
    compare_df = pd.merge(
        alpha_excess.to_frame('true'), y_predict.to_frame('predict'), left_index=True, right_index=True)

    return compare_df


if __name__ == '__main__':
    # run_daily_plot('20211111', '20211111')
    # run_market_structure('20200101', '20211108')
    run_analysis('20200101', '20211108')