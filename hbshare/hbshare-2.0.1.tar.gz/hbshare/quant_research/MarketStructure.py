"""
指增策略 - 市场结构
"""
import pandas as pd
import hbshare as hbs
import numpy as np
from scipy import stats
import datetime
import plotly.graph_objs as go
from plotly.offline import plot as plot_ly
from statsmodels.stats.weightstats import DescrStatsW
from hbshare.rm_associated.util.data_loader import get_trading_day_list


class MarketHist:
    """
    市场收益率Histogram
    """
    def __init__(self, trade_date, benchmark_id):
        self.trade_date = trade_date
        self.benchmark_id = benchmark_id
        self._load_data()

    def _load_data(self):
        # A股行情
        sql_script = "SELECT SYMBOL, SNAME, VOTURNOVER, PCHG, MCAP, TCAP FROM finchina.CHDQUOTE WHERE" \
                     " TDATE = {}".format(self.trade_date)
        data = pd.DataFrame(hbs.db_data_query('readonly', sql_script, page_size=5000)['data'])
        data = data[data['SYMBOL'].str[0].isin(['0', '3', '6'])]
        data = data[data['VOTURNOVER'] > 1e-8]
        data = data[~data['SNAME'].str.contains('ST')]
        data = data[~data['SNAME'].str.contains('N')]
        data = data[~data['SNAME'].str.contains('C')]
        market_df = data.rename(
            columns={"SYMBOL": "ticker", 'PCHG': "return", "TCAP": "marketValue"})[
            ['ticker', 'return', 'marketValue']].dropna()
        # 指数收益率
        start_dt = datetime.datetime.strptime(self.trade_date, '%Y%m%d')
        pre_date = (start_dt - datetime.timedelta(days=30)).strftime('%Y%m%d')
        sql_script = "SELECT JYRQ as TRADEDATE, ZQMC as INDEXNAME, SPJG as TCLOSE from funddb.ZSJY WHERE ZQDM = '{}' " \
                     "and JYRQ >= {} and JYRQ <= {}".format(self.benchmark_id, pre_date, self.trade_date)
        data = pd.DataFrame(hbs.db_data_query('readonly', sql_script)['data'])
        data['index_return'] = data['TCLOSE'].pct_change()
        index_return = data.set_index('TRADEDATE').loc[self.trade_date, 'index_return']

        self.market_df = market_df
        self.index_return = index_return

    def daily_plot(self):
        market_df = self.market_df.copy()
        market_df = market_df[market_df['return'].abs() <= 10]
        # locate the index return
        index_return = self.index_return * 100.
        lower = round(np.floor(index_return / 0.2) * 0.2, 2)
        cut_set = [round(x, 2) for x in np.linspace(-10, 10, 101)]
        color_list = ['#55CBF2'] * 100
        color_list[cut_set.index(lower)] = '#ff2d51'
        # quantile
        win_ratio = round(100 - stats.percentileofscore(np.array(market_df['return']), index_return), 1)
        win_med = market_df[market_df['return'] >= index_return]['return'].median()
        lose_med = market_df[market_df['return'] < index_return]['return'].median()
        # locate the lower med
        lower = round(np.floor(lose_med / 0.2) * 0.2, 2)
        cut_set = [round(x, 2) for x in np.linspace(-10, 10, 101)]
        color_list[cut_set.index(lower)] = '#ffa400'
        # locate the upper med
        lower = round(np.floor(win_med / 0.2) * 0.2, 2)
        cut_set = [round(x, 2) for x in np.linspace(-10, 10, 101)]
        color_list[cut_set.index(lower)] = '#ffa400'
        # text
        map_dict = {"000905": "中证500", "000852": "中证1000", "000300": "沪深300"}
        title_text = "【{}】市场个股收益率结构, {}收益率{}%, 跑赢指数的个股比例为{}%, 跑赢的中位数为{}%, 跑输的中位数为{}%".format(
            self.trade_date, map_dict[self.benchmark_id], round(index_return, 2),
            win_ratio, round(win_med, 2), round(lose_med, 2))

        L = go.Layout(xaxis=dict(range=[-10, 10]), title=title_text, width=1440, height=800)
        D = go.Histogram(x=np.array(market_df['return']), xbins=dict(start=-10, end=10, size=0.2),
                         histfunc='count', histnorm='probability density',
                         marker=dict(color=color_list, line=dict(color='white', width=1)))
        F = go.Figure(data=[D], layout=L)
        plot_ly(F, filename='D:\\市场微观结构图\\个股收益率结构\\{}.html'.format(self.trade_date), auto_open=False)


class MarketStructure:
    def __init__(self, trade_date, benchmark_id):
        self.trade_date = trade_date
        self.benchmark_id = benchmark_id
        self._load_data()

    def _load_market_info(self):
        # A股行情
        sql_script = "SELECT SYMBOL, SNAME, VOTURNOVER, PCHG, MCAP, TCAP FROM finchina.CHDQUOTE WHERE" \
                     " TDATE = {}".format(self.trade_date)
        data = pd.DataFrame(hbs.db_data_query('readonly', sql_script, page_size=5000)['data'])
        data = data[data['SYMBOL'].str[0].isin(['0', '3', '6'])]
        data = data[data['VOTURNOVER'] > 1e-8]
        data = data[~data['SNAME'].str.contains('ST')]
        data = data[~data['SNAME'].str.contains('N')]
        data = data[~data['SNAME'].str.contains('C')]
        # 剔除新股
        list_status = pd.read_csv('D:\\kevin\\risk_model_jy\\RiskModel\\data\\common_data\\list_status.csv',
                                  index_col=0, dtype={"listDate": str})
        list_status['ticker'] = list_status['ticker'].apply(lambda x: str(x).zfill(6))
        trade_dt = datetime.datetime.strptime(self.trade_date, '%Y%m%d')
        pre_date = (trade_dt - datetime.timedelta(days=90)).strftime('%Y%m%d')
        list_status = list_status[list_status['listDate'] <= pre_date]
        data = data[data['SYMBOL'].isin(list_status['ticker'].tolist())]

        data = data[data['PCHG'].abs() <= 10.1]

        market_df = data.rename(
            columns={"SYMBOL": "ticker", 'PCHG': "return", "TCAP": "marketValue", "MCAP": "floatM"})[
            ['ticker', 'return', 'marketValue', 'floatM']].dropna()
        # 指数收益率
        sql_script = "SELECT JYRQ as TRADEDATE, ZQMC as INDEXNAME, SPJG as TCLOSE from funddb.ZSJY WHERE ZQDM = '{}' " \
                     "and JYRQ >= {} and JYRQ <= {}".format(self.benchmark_id, pre_date, self.trade_date)
        data = pd.DataFrame(hbs.db_data_query('readonly', sql_script)['data'])
        data['index_return'] = data['TCLOSE'].pct_change()
        index_return = data.set_index('TRADEDATE').loc[self.trade_date, 'index_return']

        return market_df, index_return

    def _load_style_factor_return(self):
        sql_script = "SELECT * FROM st_ashare.r_st_barra_factor_return where TRADE_DATE = '{}'".format(self.trade_date)
        data = pd.DataFrame(hbs.db_data_query('alluser', sql_script)['data'])
        size_return = data.set_index('factor_name').loc['size', 'factor_ret']

        return size_return

    def _load_industry_data(self):
        start_dt = datetime.datetime.strptime(self.trade_date, '%Y%m%d')
        pre_date = (start_dt - datetime.timedelta(days=50)).strftime('%Y%m%d')

        sql_script = "SELECT * FROM st_market.t_st_zs_hyzsdmdyb where fljb = {} and hyhfbz = 2".format('1')
        res = hbs.db_data_query('alluser', sql_script, page_size=5000)
        data = pd.DataFrame(res['data']).rename(columns={"zsdm": "SYMBOL", "flmc": "INDEXSNAME"})
        map_dict = data.set_index('SYMBOL')['INDEXSNAME'].to_dict()
        industry_index = []
        for key, value in map_dict.items():
            sql_script = "SELECT JYRQ as TRADEDATE, ZQMC as INDEXNAME, SPJG as TCLOSE, LTSZ as NEG_MKV " \
                         "FROM funddb.ZSJY WHERE " \
                         "ZQDM = '{}' and JYRQ >= {} and " \
                         "JYRQ <= {}".format(key, pre_date, self.trade_date)
            res = hbs.db_data_query('readonly', sql_script, page_size=5000)
            df = pd.DataFrame(res['data'])
            df['INDEXNAME'] = value
            industry_index.append(df)
        industry_index = pd.concat(industry_index)

        return industry_index

    def _load_data(self):
        market_df, index_return = self._load_market_info()
        size_return = self._load_style_factor_return()
        industry_index = self._load_industry_data()

        self.data_param = {
            "market_df": market_df,
            "index_return": index_return,
            "size_return": size_return,
            "industry_index": industry_index
        }

    def get_construct_result(self):
        data_param = self.data_param.copy()

        structure_df = pd.DataFrame(index=[self.trade_date], columns=[
            'cs_vol', 'cs_vol_w', 'skew', 'kurt', 'win_ratio', 'win_med', 'lose_med', 'size_return', 'ind_cr'])

        market_df = data_param['market_df']
        index_return = data_param['index_return'] * 100.
        structure_df.loc[self.trade_date, 'cs_vol'] = market_df['return'].std() / 100.
        structure_df.loc[self.trade_date, 'cs_vol_w'] = \
            DescrStatsW(np.array(market_df['return']), weights=np.array(market_df['floatM']), ddof=1).std / 100.
        structure_df.loc[self.trade_date, 'skew'] = market_df['return'].skew()
        structure_df.loc[self.trade_date, 'kurt'] = market_df['return'].kurt()
        win_ratio = round(100 - stats.percentileofscore(np.array(market_df['return']), index_return), 1)
        win_med = market_df[market_df['return'] >= index_return]['return'].median() - index_return
        lose_med = market_df[market_df['return'] < index_return]['return'].median() - index_return
        structure_df.loc[self.trade_date, 'win_ratio'] = win_ratio
        structure_df.loc[self.trade_date, 'win_med'] = win_med
        structure_df.loc[self.trade_date, 'lose_med'] = lose_med
        size_return = data_param['size_return']
        structure_df.loc[self.trade_date, 'size_return'] = size_return

        industry_index = data_param['industry_index']
        tmp = pd.pivot_table(
            industry_index, index='TRADEDATE', columns='INDEXNAME', values='TCLOSE').sort_index()
        industry_return = tmp.pct_change().dropna().loc[self.trade_date]
        structure_df.loc[self.trade_date, 'ind_cr'] = industry_return.gt(0).sum() / len(industry_return)

        return structure_df


alpha_dict = {
    "衍复指增三号": "SJH866",
    "九坤日享中证500指数增强1号": "ST9804",
    "因诺聚配中证500指数增强": "SGX346",
    "启林中证500指数增强1号": "SGY379"
}


class AlphaSeries:
    def __init__(self, start_date, end_date, benchmark_id='000905'):
        self.start_date = start_date
        self.end_date = end_date
        self.benchmark_id = benchmark_id

    def calculate(self):
        nav_series_list = []
        for name, fund_id in alpha_dict.items():
            sql_script = "SELECT a.jjdm fund_id, b.jzrq TRADEDATE, b.fqdwjz as ADJ_NAV from " \
                         "st_hedge.t_st_jjxx a, st_hedge.t_st_rhb b where a.cpfl = '4' and a.jjdm = b.jjdm " \
                         "and a.jjzt not in ('3') " \
                         "and a.jjdm = '{}' and b.jzrq >= {} and b.jzrq <= {} " \
                         "order by b.jzrq".format(fund_id, self.start_date, self.end_date)
            res = hbs.db_data_query("highuser", sql_script, page_size=5000)
            data = pd.DataFrame(res['data']).set_index('TRADEDATE')['ADJ_NAV']
            data.name = name
            nav_series_list.append(data)
        nav_df = pd.concat(nav_series_list, axis=1).sort_index()
        # 衍复前期的剔除掉
        nav_df.loc[:"20200219", "衍复指增三号"] = np.NaN
        # 处理: 单独只有衍复有的去掉
        nav_df = nav_df.dropna(subset=nav_df.columns[1:], how='all', axis=0)

        trading_day_list = get_trading_day_list(nav_df.index[0], nav_df.index[-1])
        nav_df = nav_df.reindex(trading_day_list).dropna(how='all', axis=0)

        for col in nav_df.columns:
            nav_df[col] = nav_df[col] / nav_df[col].shift(1) - 1
        nav_df.dropna(axis=0, how='all', inplace=True)
        mean_alpha = nav_df.mean(axis=1)  # 策略日度平均收益

        sql_script = "SELECT JYRQ as TRADEDATE, ZQMC as INDEXNAME, SPJG as TCLOSE from funddb.ZSJY WHERE ZQDM = '{}' " \
                     "and JYRQ >= {} and JYRQ <= {}".format(self.benchmark_id, self.start_date, self.end_date)
        data = pd.DataFrame(hbs.db_data_query('readonly', sql_script)['data'])
        data['index_return'] = data['TCLOSE'].pct_change()
        index_return = data.set_index('TRADEDATE')['index_return'].dropna()

        idx = mean_alpha.index.intersection(index_return.index)
        excess_return = mean_alpha.reindex(idx) - index_return.reindex(idx)
        # excess_return = mean_alpha.reindex(idx)

        return excess_return
