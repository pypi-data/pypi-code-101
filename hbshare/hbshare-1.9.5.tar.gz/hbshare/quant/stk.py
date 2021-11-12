import pandas as pd
import numpy as np
from db_cons import sql_write_path_work, sql_user_work
from datetime import datetime, timedelta
from hbshare.quant.cons import sql_write_path_hb, properties_stk_k, db, db_tables
from table_gen import generate_table
from hbshare.quant.sql_l import sql_quote
from hbshare.quant.load_data import load_calendar_extra
import hbshare as hbs
import pymysql

pymysql.install_as_MySQLdb()

page_size_con = 49999


def ch_stk_quote_to_local(table='ch_stk_quote', db_path=None, sql_info=None, page_size=None):
    if page_size is None:
        page_size = page_size_con

    if db_path is None:
        db_path = sql_write_path_work['daily']

    if sql_info is None:
        sql_info = sql_user_work

    from_table = db_tables['ch_stocks_daily_quote']

    try:
        generate_table(
            database='daily_data',
            table=table,
            generate_sql=sql_quote,
            sql_ip=sql_info['ip'],
            sql_user=sql_info['user'],
            sql_pass=sql_info['pass'],
            table_comment='from ' + from_table
        )
        print(table + ' generated')
    except pymysql.err.InternalError:
        print(table + ' exists')

    latest_date_in_db = pd.read_sql_query(
        'select distinct `TDATE` from ' + table + ' order by `TDATE` desc limit 1', db_path
    )
    if len(latest_date_in_db) > 0:
        latest_date = latest_date_in_db['TDATE'][0]
    else:
        latest_date = datetime(2000, 12, 31).date()

    print('\tLatest date in db: ' + str(latest_date))
    while 1:
        latest_date += timedelta(days=1)
        if latest_date > datetime.now().date():
            print('\t\t' + 'No more new quote data')
            return
        sql = (
                'select '
                'TDATE, '
                'SYMBOL, '
                'EXCHANGE, '
                'LCLOSE, '
                'TOPEN, '
                'TCLOSE, '
                'HIGH, '
                'LOW, '
                'VOTURNOVER, '
                'VATURNOVER, '
                'AVGPRICE, '
                'CHG, '
                'PCHG, '
                'PRANGE, '
                'MCAP, '
                'TCAP '
                'from ' + from_table
                + ' where  TDATE=' + latest_date.strftime('%Y%m%d')
        )

        data = hbs.db_data_query(db=db, sql=sql, page_size=page_size)
        df = pd.DataFrame(data['data'])
        if len(df) == 0:
            continue
        df['TDATE'] = pd.to_datetime(df['TDATE'].astype(str)).dt.date
        df = df.drop(columns=['ROW_ID']).rename(
            columns={
                'TOPEN': 'OPEN',
                'TCLOSE': 'CLOSE',
                'VOTURNOVER': 'VOLUME',
                'VATURNOVER': 'AMOUNT'
            }
        )
        df.to_sql(table, db_path, if_exists='append', index=False)
        print('\tNew data: ' + str(len(df)) + ', date: ' + latest_date.strftime('%Y-%m-%d'))


def trade_calendar(start_date=None, end_date=None, page_size=None):
    if start_date is None:
        start_date = datetime(2010, 1, 1).date()
    if end_date is None:
        end_date = datetime.now().date()
    if page_size is None:
        page_size = page_size_con

    sql = 'select distinct TDATE from ' + db_tables['ch_stocks_daily_quote'] \
          + ' where TDATE<=' + end_date.strftime('%Y%m%d') \
          + ' and TDATE>=' + start_date.strftime('%Y%m%d') \
          + ' order by TDATE'
    data = hbs.db_data_query(db=db, sql=sql, page_size=page_size)
    if data['pages'] > 1:
        for p in range(2, data['pages'] + 1):
            data['data'] = data['data'] + hbs.db_data_query(db=db, sql=sql, page_size=page_size, page_num=p)['data']

    return pd.to_datetime(pd.DataFrame(data['data'])['TDATE'], format='%Y%m%d').dt.date.tolist()


def daily_ret_by_vol(start_date=None, end_date=None, min_vol=10000, page_size=None):
    if start_date is None:
        start_date = datetime(2010, 1, 1).date()
    if end_date is None:
        end_date = datetime.now().date()
    if page_size is None:
        page_size = page_size_con

    sql = 'select ' + ', '.join(properties_stk_k) + ' from ' + db_tables['ch_stocks_daily_quote'] \
          + ' where TDATE<=' + end_date.strftime('%Y%m%d') \
          + ' and TDATE>=' + start_date.strftime('%Y%m%d') \
          + '  and VOTURNOVER>=' + str(min_vol) + ' order by TDATE, SYMBOL'

    data = hbs.db_data_query(db=db, sql=sql, page_size=page_size)
    if data['pages'] > 1:
        for p in range(2, data['pages'] + 1):
            data['data'] = data['data'] + hbs.db_data_query(db=db, sql=sql, page_size=page_size, page_num=p)['data']

    return data


def load_index(index_list, start_date=None, end_date=None, table=db_tables['index_daily_quote'], page_size=None):
    if start_date is None:
        start_date = datetime(2010, 1, 1).date()
    if end_date is None:
        end_date = datetime.now().date()
    if page_size is None:
        page_size = page_size_con

    if len(index_list) == 1:
        index_sql = '=\'' + index_list[0] + '\''
    elif len(index_list) > 1:
        index_sql = ' in ' + str(tuple(index_list))
    else:
        index_sql = '=\'000905\''

    sql = 'select ' \
          'JYRQ as tdate, ' \
          'ZQDM as code, ' \
          'QSPJ as pre_close, ' \
          'KPJG as open, ' \
          'SPJG as close, ' \
          'ZGJG as high, ' \
          'ZDJG as low, ' \
          'CJJS as amount,' \
          'ZDFD as PCHG from ' + table \
          + ' where JYRQ<=' + end_date.strftime('%Y%m%d') \
          + ' and JYRQ>=' + start_date.strftime('%Y%m%d') \
          + ' and ZQDM' + index_sql

    data = hbs.db_data_query(db=db, sql=sql, page_size=page_size)
    if data['pages'] > 1:
        for p in range(2, data['pages'] + 1):
            data['data'] = data['data'] + hbs.db_data_query(db=db, sql=sql, page_size=page_size, page_num=p)['data']

    return pd.DataFrame(data['data'])


def load_stk(start_date=None, end_date=None, table=db_tables['stocks_daily_quote'], page_size=None):
    if start_date is None:
        start_date = datetime(2010, 1, 1).date()
    if end_date is None:
        end_date = datetime.now().date()
    if page_size is None:
        page_size = page_size_con

    sql = 'select ' \
          'JYRQ, ' \
          'ZQDM as code, ' \
          'QSPJ as pre_close, ' \
          'KPJG as open, ' \
          'SPJG as close, ' \
          'ZGJG as high, ' \
          'ZDJG as low, ' \
          'HSBL as TURNOVER, ZDFD as PCHG from ' + table \
          + ' where JYRQ<=' + end_date.strftime('%Y%m%d') \
          + ' and JYRQ>=' + start_date.strftime('%Y%m%d') \
          + ' and (ZQDM like \'6%\' or ZQDM like \'3%\' or ZQDM like \'0%\') ' \
          + ' order by JYRQ, ZQDM'

    data = hbs.db_data_query(db=db, sql=sql, page_size=page_size)
    if data['pages'] > 1:
        for p in range(2, data['pages'] + 1):
            data['data'] = data['data'] + hbs.db_data_query(db=db, sql=sql, page_size=page_size, page_num=p)['data']

    return pd.DataFrame(data['data'])


def index_win(index_list, start_date=None, end_date=None, freq='D'):
    index_data = load_index(index_list=index_list, start_date=start_date, end_date=end_date)
    stk_data = load_stk(start_date=start_date, end_date=end_date)

    index_data = pd.DataFrame(index_data['data'])
    index_data['TDATE'] = pd.to_datetime(index_data['TDATE']).dt.date

    stk_data = pd.DataFrame(stk_data['data'])
    stk_data['TDATE'] = pd.to_datetime(stk_data['TDATE'].astype(str)).dt.date
    win_data = pd.DataFrame()
    for i in index_list:
        index_data_i = index_data[index_data['CODE'] == i]
        stk_data_i = stk_data[['TDATE', 'CODE', 'PCHG']].merge(
            index_data_i[['TDATE', 'PCHG']].rename(columns={'PCHG': 'IPCHG'}),
            on='TDATE',
            how='left'
        )
        if freq != 'D':
            stk_pool = stk_data_i.groupby('TDATE').count()[['CODE']].reset_index()

            cal = pd.DataFrame(pd.to_datetime(stk_data_i['TDATE'].drop_duplicates().sort_values()))
            cal = cal.set_index('TDATE', drop=False).resample(freq).last()

            stk_pool = pd.DataFrame(cal['TDATE'].dt.date).reset_index(drop=True).merge(stk_pool, on='TDATE', how='left')

            stk_data_i_p = stk_data_i.pivot(index='TDATE', columns='CODE', values='PCHG')
            stk_data_i_p = stk_data_i_p.set_index(pd.to_datetime(stk_data_i_p.index))
            stk_data_i_p = (stk_data_i_p + 100) / 100
            stk_data_i_p_r = stk_data_i_p.resample(freq).prod() - 1
            stk_data_i_p_r.index = cal['TDATE'].dt.date

            index_data_i = (index_data_i.set_index(pd.to_datetime(index_data_i['TDATE']))[['PCHG']] + 100) / 100
            index_data_r = index_data_i.resample(freq).prod() - 1
            index_data_r.index = cal['TDATE'].dt.date

            win_data_i = pd.DataFrame(
                ((stk_data_i_p_r.values - index_data_r.values) > 0).sum(axis=1) / stk_pool['CODE'] * 100
            ).rename(columns={'CODE': 'WIN'})
            win_data_i['TDATE'] = cal['TDATE'].dt.date.tolist()
            win_data_i['CODE'] = i
        else:
            stk_data_i['WIN'] = (stk_data_i['PCHG'] > stk_data_i['IPCHG'])
            stk_data_i_group = stk_data_i.groupby(['TDATE']).sum()['WIN'] \
                               / stk_data_i.groupby(['TDATE']).count()['WIN'] * 100

            win_data_i = pd.DataFrame(stk_data_i_group).reset_index()
            win_data_i['CODE'] = i
        win_data = win_data.append(win_data_i, sort=True)

    return win_data


if __name__ == '__main__':
    # main = load_index(index_list='000905', start_date=datetime(2021, 10, 1))
    # main2 = load_stk(start_date=datetime(2021, 10, 1))

    # aa = index_win(
    #     index_list=[
    #         # '000300',
    #         '000905'
    #     ],
    #     start_date=datetime(2021, 1, 1),
    #     freq='W'
    # )
    ch_stk_quote_to_local()
    print()


