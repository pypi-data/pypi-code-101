from hbshare.quant.stk import index_win
import pandas as pd
from db_cons import sql_write_path_work
from datetime import datetime, timedelta

index_list = [
    '000300',
    '000905',
    '000852'
]

freq_list = [
    'D',
    'W',
    'M',
]

end_date = datetime(2021, 1, 1).date()
for i in freq_list:
    table_index_win = 'index_win'
    last_date = pd.read_sql_query(
        'select TDATE from ' + table_index_win
        + ' where FREQ=\'' + i
        + '\' order by TDATE desc limit 1',
        sql_write_path_work['daily']
    )

    if len(last_date) == 0:
        last_date = datetime(2010, 1, 1).date()
    else:
        last_date = last_date['TDATE'][0] + timedelta(days=1)

    index_win_data = index_win(
        index_list=index_list,
        start_date=last_date,
        end_date=end_date,
        freq=i
    )
    index_win_data['FREQ'] = i
    index_win_data.to_sql(table_index_win, sql_write_path_work['daily'], if_exists='append', index=False)
    print(i + ' ' + end_date.strftime('%Y/%m/%d') + ' done')
