from datetime import datetime
from .mt5_objects import MT5_dataframe, MT5_list 
import pandas as pd 

class Price(object):

    def __init__(self,client):
        
        self.mt5 = client

    def get_symbols(self):

        symbols = pd.DataFrame(self.mt5.symbols_get()).iloc[:,-1].str.split('\\').str[-1]
        category = pd.DataFrame(self.mt5.symbols_get()).iloc[:,-1].str.split('\\').str[0]

        symbols = pd.concat([category,symbols],axis=1,keys=['Category','Symbol'])

        return MT5_dataframe(symbols)

    def get_timeframes(self):
        
        m_dict = self.mt5.__dict__
        timeframes = dict(filter(lambda elem:'TIMEFRAME' in elem[0] , m_dict.items()))
        
        return timeframes

    def get_prices_range(self,symbol='EURUSD',timeframe='TIMEFRAME_H1',start=None,end=datetime.now()):

        if type(timeframe) == str:
            timeframe = self.get_timeframes()[timeframe]

        rates = self.mt5.copy_rates_range(symbol,
                                timeframe,
                            start,end)
        
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'],unit='s')
        df.insert(0,'symbol',symbol)
        return MT5_dataframe(df).to_datetime()

    def get_all_prices(self,symbol='EURUSD',timeframe='TIMEFRAME_D1'):
        df_list = []
        self.timeframe = timeframe
        year = datetime.today().year
        while True:

            start = datetime(year,1,1)
            end = datetime(year,12,31)

            df = self.get_prices_range(symbol,timeframe,start,end)
            df_list.append(df)


            year -= 1 

            if year == 2009:
                break

        return df_list
